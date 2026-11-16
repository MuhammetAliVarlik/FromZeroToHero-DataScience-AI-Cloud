"""Download, cache and load the public datasets used in the course.

Lessons import this module with:

    import sys; from pathlib import Path
    sys.path.insert(0, str(Path.cwd().parent / "tools"))
    import datasets

Files are cached in `data/cache/` (git-ignored). Every file has a pinned version and a SHA-256 checksum,
so all learners use exactly the same data.
"""
from __future__ import annotations

import hashlib
import shutil
import subprocess
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "data" / "cache"
COMPOSE = ROOT / "docker" / "compose.yml"

VEGA = "https://cdn.jsdelivr.net/npm/vega-datasets@2.8.0/data/"
TLC = "https://d37ci6vzurychx.cloudfront.net/"
CHINOOK = "https://github.com/lerocha/chinook-database/releases/download/v1.4.5/"
DATASETS = {
    # name: (url, sha256, licence / source note)
    "chinook_postgres.sql": (CHINOOK + "Chinook_PostgreSql.sql",
                             "e3fde5c1a5b51a2a91429a702c9ca6e69ba56e6c7f5e112724d70c3d03db695e",
                             "Chinook sample database v1.4.5, MIT licence, github.com/lerocha/chinook-database"),
    "chinook.sqlite": (CHINOOK + "Chinook_Sqlite.sqlite",
                       "bdf635be69850bd3be09c9a2dbeef7ddfb80036bd3ef3381383cd03b61e4a61a",
                       "Chinook sample database v1.4.5 (SQLite), MIT licence"),
    "chinook.json": (CHINOOK + "ChinookData.json",
                     "2998161de437518e3447e779c7ce7418f081895e388081bff315f3c258752d8c",
                     "Chinook sample data v1.4.5 (JSON), MIT licence"),
    # vega-datasets (BSD-3 package; each file keeps its original source licence), pinned to npm version 2.8.0
    "seattle-weather.csv": (VEGA + "seattle-weather.csv",
                            "0845078a290b48e3149ab8639966824110a251db4e06fc144c06ebb534af23be",
                            "Seattle daily weather 2012-2015 (NOAA), via vega-datasets 2.8.0"),
    "penguins.json": (VEGA + "penguins.json",
                      "0facf769609f1205b82cbceb8238c36af3e6147a0ca0e163902cc6281ce3e917",
                      "Palmer penguins (Gorman et al. 2014, CC0), via vega-datasets 2.8.0"),
    "gapminder.json": (VEGA + "gapminder.json",
                       "3966d16ec56bf416115672bc9b8bbb25b19f389d5a67ead59a82b9278475d5e1",
                       "Gapminder life expectancy, fertility and population (CC BY 4.0), via vega-datasets 2.8.0"),
    # NYC Taxi & Limousine Commission trip records (public data, NYC Open Data terms)
    "taxi_zone_lookup.csv": (TLC + "misc/taxi_zone_lookup.csv",
                             "1a99e105092230f8620f301edcca7f80d3080642ff404d28ed957d3fa222c8ed",
                             "NYC TLC taxi zone lookup table"),
    "taxi_zones.zip": (TLC + "misc/taxi_zones.zip",
                       "f6d711917bb4340f8f644d5366c51665489eb2d426dd1a4a55677721ae5adf17",
                       "NYC TLC taxi zone boundaries (shapefile, NAD83 / New York Long Island ftUS)"),
    "yellow_tripdata_2024-01.parquet": (TLC + "trip-data/yellow_tripdata_2024-01.parquet",
                                        "c4d59da7bbc8abaeeeb1727947ee93d9891a71acb42854bd80db1571b2030510",
                                        "NYC TLC yellow taxi trips, January 2024 (~3.0 million rows)"),
    "yellow_tripdata_2024-02.parquet": (TLC + "trip-data/yellow_tripdata_2024-02.parquet",
                                        "c76c43c18c6c6664080dd920baab4928988d5786a6b65980792ca7cd796f9f20",
                                        "NYC TLC yellow taxi trips, February 2024 (~3.0 million rows)"),
}


def fetch(name: str) -> Path:
    """Return the local path of a dataset file; download and verify it on first use."""
    url, sha, _ = DATASETS[name]
    path = CACHE / name
    if path.exists() and _sha256(path) == sha:
        return path
    CACHE.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".part")
    with urllib.request.urlopen(url, timeout=120) as r, open(tmp, "wb") as f:
        shutil.copyfileobj(r, f)
    if _sha256(tmp) != sha:
        tmp.unlink()
        raise RuntimeError(f"checksum mismatch for {name}: the download is corrupt or the source changed")
    tmp.replace(path)
    return path


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def taxi(month: str = "2024-01") -> Path:
    """Path of one month of NYC yellow taxi trips (Parquet)."""
    return fetch(f"yellow_tripdata_{month}.parquet")


# ------------------------------------------------------------------ docker helpers
def compose(*args: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(["docker", "compose", "-f", str(COMPOSE), *args], capture_output=True, text=True,
                          check=check)


HEALTHCHECKED = {"postgres", "superset"}       # services with a Docker health check: wait until "healthy"


def ensure_service(profile: str, service: str, timeout: int = 120) -> None:
    """Start a docker compose service (if needed) and wait until it is running/healthy."""
    if shutil.which("docker") is None:
        raise RuntimeError("Docker is not installed or not on PATH. See README 'Getting Started', step 4.")
    compose("--profile", profile, "up", "-d", service)
    deadline = time.time() + timeout
    while time.time() < deadline:
        state = compose("ps", "--format", "{{.Service}} {{.State}} {{.Health}}", check=False).stdout
        line = next((l for l in state.splitlines() if l.startswith(service + " ")), "")
        if "running" in line and ("healthy" in line or "starting" not in line and "unhealthy" not in line):
            if service not in HEALTHCHECKED or (" healthy" in line or line.endswith("healthy")) and "unhealthy" not in line:
                return
        time.sleep(2)
    raise RuntimeError(f"service {service} did not become ready within {timeout} s: {state}")


def load_chinook_postgres() -> None:
    """Create (or re-create) the `chinook` database in the course PostgreSQL container."""
    ensure_service("db", "postgres")
    sql = fetch("chinook_postgres.sql").read_text(encoding="utf-8")
    r = subprocess.run(["docker", "compose", "-f", str(COMPOSE), "exec", "-T", "postgres", "psql", "-q", "-U", "course",
                        "-d", "course", "-v", "ON_ERROR_STOP=1"], input=sql, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"loading Chinook failed:\n{r.stderr[-2000:]}")


POSTGRES_URL = "postgresql+psycopg://course:course@localhost:5432/{db}"


def ensure_chinook() -> str:
    """Make sure the Chinook database exists in PostgreSQL; load it only the first time. Returns the SQLAlchemy URL."""
    ensure_service("db", "postgres")
    r = subprocess.run(["docker", "compose", "-f", str(COMPOSE), "exec", "-T", "postgres", "psql", "-U", "course",
                        "-d", "course", "-tAc", "SELECT 1 FROM pg_database WHERE datname = 'chinook'"],
                       capture_output=True, text=True)
    if r.stdout.strip() != "1":
        load_chinook_postgres()
    return POSTGRES_URL.format(db="chinook")
