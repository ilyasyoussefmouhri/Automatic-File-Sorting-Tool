import pathlib
import shutil
from collections import defaultdict



def sort_by_extension(path, verbose=False):
    """
    Organizes files by extension.
    Creates folders like: path/jpg/, path/pdf/, etc.

    Args:
        path: Directory path to organize
        verbose: Print progress information

    Returns:
        tuple: (moved_files dict, errors list)
    """
    path = pathlib.Path(path)

    # Handling path related errors
    if not path.exists():
        raise ValueError(f"Path does not exist: {path}")
    if not path.is_dir():
        raise ValueError(f"Path is not a directory: {path}")

    moved_files = defaultdict(list)
    errors = []

    for file in path.iterdir():
        if not file.is_file():
            continue

        try:
            # Determine extension
            extension = file.suffix if file.suffix else 'no_extension'

            # Remove the leading dot from extension for cleaner folder names
            folder_name = extension.lstrip('.')
            if not folder_name:
                folder_name = 'no_extension'

            # Create target directory
            target_dir = path / folder_name
            target_dir.mkdir(exist_ok=True)

            # Move file
            target_path = target_dir / file.name

            # Handle duplicate filenames
            counter = 1
            original_target = target_path
            while target_path.exists():
                stem = original_target.stem
                suffix = original_target.suffix
                target_path = original_target.parent / f"{stem}_{counter}{suffix}"
                counter += 1

            shutil.move(str(file), str(target_path))
            moved_files[folder_name].append(file.name)

            if verbose:
                print(f"  Moved: {file.name} → {folder_name}/")

        except Exception as e:
            errors.append(f"Error moving {file.name}: {str(e)}")
            if verbose:
                print(f"  ❌ {errors[-1]}")

    # Print summary
    if verbose and moved_files:
        print("\n" + "-" * 50)
        for folder, files in moved_files.items():
            print(f"  {folder}/: {len(files)} files")
        if errors:
            print("\n  Errors:")
            for error in errors:
                print(f"    - {error}")

    return moved_files, errors


def sort_by_category(path, verbose=False):
    """
    Organizes files into categories (Images, Documents, etc.)
    Creates folders like: path/Images/, path/Documents/, etc.

    Args:
        path: Directory path to organize
        verbose: Print progress information

    Returns:
        tuple: (moved_files dict, errors list)
    """
    path = pathlib.Path(path)

    # Handling path related errors
    if not path.exists():
        raise ValueError(f"Path does not exist: {path}")
    if not path.is_dir():
        raise ValueError(f"Path is not a directory: {path}")

    # Define supported categories
    categories = {
        'Images': {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.ico', '.webp'},
        'Documents': {'.pdf', '.doc', '.docx', '.txt', '.xlsx', '.xls', '.pptx', '.odt'},
        'Videos': {'.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm'},
        'Audio': {'.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a'},
        'Archives': {'.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'},
        'Code': {'.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.h', '.json'},
        'Other': set()
    }

    moved_files = defaultdict(list)
    errors = []

    for file in path.iterdir():
        if not file.is_file():
            continue

        try:
            extension = file.suffix.lower()

            # Find which category this extension belongs to
            category = 'Other'
            for cat_name, extensions in categories.items():
                if extension in extensions:
                    category = cat_name
                    break

            # Create category folder
            category_folder = path / category
            category_folder.mkdir(exist_ok=True)

            # Move file
            target = category_folder / file.name

            # Handle duplicate filenames
            counter = 1
            original_target = target
            while target.exists():
                stem = original_target.stem
                suffix = original_target.suffix
                target = original_target.parent / f"{stem}_{counter}{suffix}"
                counter += 1

            shutil.move(str(file), str(target))
            moved_files[category].append(file.name)

            if verbose:
                print(f"  {file.name} → {category}/")

        except Exception as e:
            errors.append(f"Error moving {file.name}: {str(e)}")
            if verbose:
                print(f"  ❌ {errors[-1]}")

    # Print summary
    if verbose and moved_files:
        print("\n" + "-" * 50)
        for category, files in moved_files.items():
            print(f"  {category}/: {len(files)} files")
        if errors:
            print("\n  Errors:")
            for error in errors:
                print(f"    - {error}")

    return moved_files, errors