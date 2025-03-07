import os
import re


def generate_permalink(file_path):
    # Remove the base directory (FF8) and file extension
    relative_path = file_path.replace('FF8/', '').replace('.md', '')

    # Convert to lowercase and replace spaces/underscores with hyphens
    clean_path = relative_path.lower().replace(' ', '-').replace('_', '-')

    # Remove numbers and special characters (optional)
    clean_path = re.sub(r'[^a-z0-9\-]', '', clean_path)

    return f'/{clean_path}/'


def update_front_matter(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()

    # Check if the file already has a permalink
    has_permalink = any(line.strip().startswith('permalink:') for line in content)
    if has_permalink:
        return

    # Generate the permalink
    permalink = generate_permalink(file_path)

    # Inject the permalink into the front matter
    front_matter_end = content.index('---\n', 1) if '---\n' in content[1:] else 1
    content.insert(front_matter_end, f'permalink: {permalink}\n')

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