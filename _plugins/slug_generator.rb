module Jekyll
  module PermalinkGenerator
    def generate_permalink(title)
      # Convert title to lowercase and replace spaces with hyphens
      title.downcase.gsub(/\s+/, '-')
    end
  end

  class Page
    include PermalinkGenerator

    def permalink
      # Generate permalink from title if not explicitly set
      return data['permalink'] if data['permalink']
      "/#{generate_permalink(data['title'])}/"
    end
  end
end