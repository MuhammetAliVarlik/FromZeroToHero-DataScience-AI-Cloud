// "Engineering pad" look for the PDF versions of lessons (Quarto typst format, included in the header).
// Fonts are in site/fonts (all SIL OFL): Atkinson Hyperlegible, Shantell Sans, Kalam, JetBrains Mono.

#let pad-ink = rgb("#2a2c2e")
#let pad-red = rgb("#c8453c")
#let pad-grid-minor = rgb(46, 125, 80, 22)
#let pad-grid-major = rgb(46, 125, 80, 46)
#let pad-paper = rgb("#fbfaf5")
#let pad-card = rgb("#fffbea")
#let pad-tape = rgb(214, 200, 150, 160)
#let pad-marker = rgb(255, 210, 0, 120)

// lesson label for the footer ("M07 · Chapter 07"), set by site/insight.lua at the start of the body
#let lesson-label = state("lesson-label", "")
#let lesson-num = state("lesson-num", "")      // "11" -> page numbers "11–4" (chapter–page)

// engineering grid: 5 mm minor, 25 mm major, plus the double red margin line
#let pad-grid = tiling(size: (5mm, 5mm))[
  #place(line(start: (0pt, 0pt), end: (5mm, 0pt), stroke: 0.35pt + pad-grid-minor))
  #place(line(start: (0pt, 0pt), end: (0pt, 5mm), stroke: 0.35pt + pad-grid-minor))
]
#let pad-grid-big = tiling(size: (25mm, 25mm))[
  #place(line(start: (0pt, 0pt), end: (25mm, 0pt), stroke: 0.5pt + pad-grid-major))
  #place(line(start: (0pt, 0pt), end: (0pt, 25mm), stroke: 0.5pt + pad-grid-major))
]

#let pad-background = {
  place(rect(width: 100%, height: 100%, fill: pad-grid))
  place(rect(width: 100%, height: 100%, fill: pad-grid-big))
  place(dx: 19mm, line(start: (0pt, 0pt), end: (0pt, 100%), stroke: 0.8pt + pad-red.transparentize(45%)))
  place(dx: 20mm, line(start: (0pt, 0pt), end: (0pt, 100%), stroke: 0.5pt + pad-red.transparentize(45%)))
}

#set page(
  fill: pad-paper,
  background: pad-background,
  footer: context {
    set text(font: "Kalam", size: 9.5pt, fill: pad-red)
    grid(columns: (1fr, auto),
      lesson-label.get(),
      { let n = lesson-num.get(); if n != "" [#n–#counter(page).display("1")] else [#counter(page).display("1")] })
  },
)

#set text(fill: pad-ink, hyphenate: false)
#set par(leading: 0.72em, spacing: 1.05em)

// handwritten headings with a pencil underline for level 1-2
#show heading: set text(font: "Shantell Sans", weight: 600, fill: pad-ink)
#show heading.where(level: 1): it => block(below: 0.9em, above: 1.6em)[
  #text(size: 17pt, it.body)
  #v(-0.5em)
  #curve(stroke: 0.9pt + rgb(128, 128, 128, 140),
    curve.move((0pt, 3pt)), curve.cubic((90pt, 0pt), (180pt, 6pt), (300pt, 2.5pt)), curve.line((440pt, 3pt)))
]
#show heading.where(level: 2): set text(size: 14pt)
#show heading.where(level: 3): set text(size: 12pt)

// marker highlights for bold text
#show strong: it => highlight(fill: pad-marker, top-edge: "x-height", bottom-edge: -0.18em, extent: 1.5pt, radius: 2pt, it)

// code: a white card with a hard shadow; outputs keep the stored text
#show raw: set text(font: "JetBrains Mono", size: 8.2pt, ligatures: false, features: (calt: 0))   // show "->" and "<=" as typed
#show raw.where(block: true): set par(justify: false)
#show raw.where(block: true): it => block(width: 100%, inset: 7pt, radius: 3pt, fill: white,
  stroke: 0.5pt + rgb(120, 120, 120, 90), breakable: true, it)

#show link: set text(fill: rgb("#0e6b66"))

// Insight notes: a taped index card, slightly tilted, written in pencil
#let insight(body) = block(above: 1.4em, below: 1.4em, breakable: false, width: 100%, inset: (x: 4pt))[
  #rotate(-0.6deg, reflow: true, block(width: 100%, fill: pad-card, inset: (x: 12pt, top: 13pt, bottom: 9pt),
    stroke: (bottom: 2.5pt + rgb(0, 0, 0, 14), right: 2.5pt + rgb(0, 0, 0, 14)))[
    #place(top + center, dy: -19pt, rotate(-2.5deg, rect(width: 70pt, height: 15pt, fill: pad-tape)))
    #set text(font: "Kalam", size: 11.5pt, fill: pad-ink)
    #text(fill: pad-red, weight: 700)[Insight] #body
  ])
]

// the title block uses the handwritten font too
#let _quarto-article = article
#let article(..args) = _quarto-article(..args, heading-family: ("Shantell Sans",), heading-weight: "bold")
