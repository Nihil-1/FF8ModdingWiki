import os
import frontmatter


def generate_slug(title):
    # Convert title to lowercase and replace spaces with hyphens
    return title.lower().replace(" ", "-")


def process_markdown_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                with open(filepath, "r", encoding="utf-8") as f:
                    post = frontmatter.load(f)

                # Skip if slug is already defined
                if "slug" in post.metadata:
                    continue

                # Generate slug from title
                if "title" in post.metadata:
                    title = post.metadata["title"]
                    slug = generate_slug(title)
                    post.metadata["slug"] = slug

                # Save the updated file
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(frontmatter.dumps(post))


if __name__ == "__main__":
    process_markdown_files(".")  # Process all Markdown files in the current directory