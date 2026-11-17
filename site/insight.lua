-- Turn paragraphs that start with an emphasised "Insight:" into a styled note: <div class="insight">
local function starts_with_insight(inlines)
  local first = inlines[1]
  if not first or first.t ~= "Emph" then return false end
  local text = pandoc.utils.stringify(first)
  return text:match("^Insight:") ~= nil
end

function Para(el)
  if starts_with_insight(el.content) then
    return pandoc.Div({el}, pandoc.Attr("", {"insight"}))
  end
end
