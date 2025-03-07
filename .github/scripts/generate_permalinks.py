import os
import re
import argparse


def get_title_from_index(folder_path):
    """Extract the title from the index.md file in the given folder."""
    index_path = os.path.join(folder_path, 'index.md')
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip().startswith('title:'):
                    return line.strip().replace('title:', '').strip().strip('"').strip("'")
    return None


def generate_permalink(file_path, title):
    """Generate the permalink using titles from index.md files in the folder structure and the file's title."""
    # Remove the base directory (FF8) and file extension
    relative_path = file_path.replace('FF8/', '').replace('.md', '')

    # Split the path into components (folders and filename)
    path_components = relative_path.split('/')

    # Traverse the folder structure and get titles from index.md files
    clean_components = []
    current_path = 'FF8'
    for component in path_components[:-1]:  # Exclude the filename
        current_path = os.path.join(current_path, component)
        index_title = get_title_from_index(current_path)
        if index_title:
            # Clean the title: lowercase, replace spaces/underscores with hyphens, remove special characters
            clean_title = index_title.lower().replace(' ', '-').replace('_', '-')
            clean_title = re.sub(r'[^a-z0-9\-]', '', clean_title)
            clean_components.append(clean_title)
        else:
            # If no index.md file is found, use the folder name (fallback)
            clean_component = component.lower().replace(' ', '-').replace('_', '-')
            clean_component = re.sub(r'[^a-z0-9\-]', '', clean_component)
            clean_components.append(clean_component)

    # If the file is an index.md, exclude the filename from the permalink
    if file_path.lower().endswith('index.md'):
        # Use the folder structure up to this point
        pass
    else:
        # Use the file's title for the last part of the permalink
        clean_title = title.lower().replace(' ', '-').replace('_', '-')
        clean_title = re.sub(r'[^a-z0-9\-]', '', clean_title)
        clean_components.append(clean_title)

    # Join the components with slashes to form the permalink
    clean_path = '/'.join(clean_components)
    return f'/{clean_path}/'


def update_front_matter(file_path, overwrite):
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

    # Generate the new permalink using the folder structure and titles
    new_permalink = generate_permalink(file_path, title)

    # Check if the file already has a permalink
    has_permalink = False
    for i, line in enumerate(content):
        if line.strip().startswith('permalink:'):
            has_permalink = True
            if overwrite:
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


def process_directory(directory, overwrite):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                update_front_matter(os.path.join(root, file), overwrite)


if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Generate permalinks for Markdown files.')
    parser.add_argument('--overwrite', action='store_true', help='Overwrite existing permalinks')
    args = parser.parse_args()

    docs_directory = 'FF8'  # Change this to your FF8 directory
    process_directory(docs_directory, args.overwrite)