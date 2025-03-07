import os
import re


def generate_permalink(file_path):
    # Remove the base directory (FF8) and file extension
    relative_path = file_path.replace('FF8/', '').replace('.md', '')

    # Split the path into components (folders and filename)
    path_components = relative_path.split('/')

    # Clean each component: lowercase, replace spaces/underscores with hyphens, remove special characters
    clean_components = []
    for component in path_components:
        # Convert to lowercase and replace spaces/underscores with hyphens
        clean_component = component.lower().replace(' ', '-').replace('_', '-')
        # Remove special characters (except hyphens)
        clean_component = re.sub(r'[^a-z0-9\-]', '', clean_component)
        clean_components.append(clean_component)

    # Join the components with slashes to form the permalink
    clean_path = '/'.join(clean_components)
    return f'/{clean_path}/'


def update_front_matter(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()

    # Generate the new permalink
    new_permalink = generate_permalink(file_path)

    # Check if the file already has a permalink
    has_permalink = False
    for i, line in enumerate(content):
        if line.strip().startswith('permalink:'):
            has_permalink = True
            # Replace the existing permalink with the new one
            content[i] = f'permalink: {new_permalink}\n'
            break

    # If no permalink exists, inject it into the front matter
    if not has_permalink:
        front_matter_end = content.index('---\n', 1) if '---\n' in content[1:] else 1
        content.insert(front_matter_end, f'permalink: {new_permalink}\n')

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