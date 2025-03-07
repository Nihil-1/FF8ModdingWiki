import os
import re


def generate_permalink(title):
    # Convert the title to lowercase and replace spaces/underscores with hyphens
    clean_title = title.lower().replace(' ', '-').replace('_', '-')

    # Remove special characters (except hyphens)
    clean_title = re.sub(r'[^a-z0-9\-]', '', clean_title)

    return clean_title


def update_front_matter(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()

    # Extract the title from the front matter
    title = None
    for line in content:
        if line.strip().startswith('title:'):
            title = line.strip().replace('title:', '').strip().strip('"').strip("'")
            break

    if not title:
        print(f"Skipping {file_path}: No title found in front matter.")
        return

    # Generate the new permalink using the title
    new_permalink = generate_permalink(title)

    # Check if the file already has a permalink
    has_permalink = False
    for i, line in enumerate(content):
        if line.strip().startswith('permalink:'):
            has_permalink = True
            # Replace the existing permalink with the new one
            content[i] = f'permalink: /{new_permalink}/\n'
            break

    # If no permalink exists, inject it into the front matter
    if not has_permalink:
        front_matter_end = content.index('---\n', 1) if '---\n' in content[1:] else 1
        content.insert(front_matter_end, f'permalink: /{new_permalink}/\n')

    # Write the updated content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(content)


def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                update_front_matter(os.path.join(root, file))


if __name__ == '__main__':
    docs_directory = 'FF8'  # Change this to your FF8 directory
    process_directory(docs_directory)