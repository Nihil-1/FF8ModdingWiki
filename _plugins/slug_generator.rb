Jekyll::Hooks.register :pages, :pre_render do |page|
  if page.data["title"]
    slug = page.data["title"].downcase.strip.gsub(" ", "-").gsub(/[^\w-]/, '')
    page.data["permalink"] = "/#{slug}/"
  end
end