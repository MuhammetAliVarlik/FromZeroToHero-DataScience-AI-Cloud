-- 1) Paragraphs that start with an emphasised "Insight:" become index-card notes:
--    HTML  -> <div class="insight"><span class="insight-label">Insight</span> ...</div>
--    Typst -> #insight[...]            (defined in site/book.typ)
-- 2) Typst only: the page footer shows "M07 · Chapter 07" (module id and lesson number from the file name).

local is_typst = quarto and quarto.doc and quarto.doc.is_format("typst")

local function insight_parts(inlines)
  local first = inlines[1]
  if not first or first.t ~= "Emph" then return nil end
  if not pandoc.utils.stringify(first):match("^Insight:") then return nil end
  local body = pandoc.List(first.content)
  -- drop the "Insight:" word and the following space
  if body[1] and body[1].t == "Str" then
    local rest = body[1].text:gsub("^Insight:", "")
    if rest == "" then body:remove(1) else body[1] = pandoc.Str(rest) end
    if body[1] and body[1].t == "Space" then body:remove(1) end
  end
  local out = pandoc.List({ pandoc.Emph(body) })
  for i = 2, #inlines do out:insert(inlines[i]) end
  return out
end

function Para(el)
  local parts = insight_parts(el.content)
  if not parts then return nil end
  if is_typst then
    local blocks = pandoc.List({ pandoc.RawBlock("typst", "#insight[") })
    blocks:insert(pandoc.Para(parts))
    blocks:insert(pandoc.RawBlock("typst", "]"))
    return blocks
  end
  local label = pandoc.Span({ pandoc.Str("Insight") }, pandoc.Attr("", { "insight-label" }))
  local content = pandoc.List({ label, pandoc.Space() })
  content:extend(parts)
  return pandoc.Div({ pandoc.Para(content) }, pandoc.Attr("", { "insight" }))
end

function Pandoc(doc)
  if not is_typst then return nil end
  local input = (quarto.doc.input_file or ""):gsub("\\", "/")
  local module = input:match("/(M%d%d)%-[^/]+/") or ""
  local fname = input:match("([^/]+)$") or ""
  local num = fname:match("^(%d%d)%-")
  local label = module
  if input:match("/assignments/") and num then
    label = module .. " · Mission " .. num .. (fname:match("%-solution%.") and " · Solution" or "")
  elseif num then
    label = module .. " · Chapter " .. num
  end
  doc.blocks:insert(1, pandoc.RawBlock("typst", '#lesson-label.update("' .. label .. '")'))
  doc.blocks:insert(2, pandoc.RawBlock("typst", '#lesson-num.update("' .. (num or "") .. '")'))
  return doc
end
