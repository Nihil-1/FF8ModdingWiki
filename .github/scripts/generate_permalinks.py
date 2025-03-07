import os
import re


def generate_permalink(file_path, title):
    # Remove the base directory (FF8) and file extension
    relative_path = file_path.replace('FF8/', '').replace('.md', '')

    # Split the path into components (folders)
    path_components = relative_path.split('/')[:-1]  # Exclude the filename

    # Clean each folder component: lowercase, replace spaces/underscores with hyphens, remove special characters
    clean_components = []
    for component in path_components:
        clean_component = component.lower().replace(' ', '-').replace('_', '-')
        clean_component = re.sub(r'[^a-z0-9\-]', '', clean_component)
        clean_components.append(clean_component)

    # Clean the title for the last part of the permalink
    clean_title = title.lower().replace(' ', '-').replace('_', '-')
    clean_title = re.sub(r'[^a-z0-9\-]', '', clean_title)

    # Join the folder components and the cleaned title to form the permalink
    clean_path = '/'.join(clean_components + [clean_title])
    return f'/{clean_path}/'


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

    # Generate the new permalink using the folder structure and title
    new_permalink = generate_permalink(file_path, title)

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