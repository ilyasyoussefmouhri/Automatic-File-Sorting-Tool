import argparse
from sorter import sort_by_extension
from sorter import sort_by_category

def main():

    # Creating user friendly CLI with example
    parser = argparse.ArgumentParser(
        description='Organize files in a directory by category and/or extension',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s /path/to/folder -e                 # Sort by extension: path/jpg/
  %(prog)s /path/to/folder -c                 # Sort by category: path/Images/
  %(prog)s /path/to/folder -c -e              # Sort by category then extension: path/Images/jpg/
  %(prog)s /path/to/folder -v -c -e           # Verbose output

Folder structures:
  -e:      path/jpg/photo.jpg, path/pdf/doc.pdf
  -c:      path/Images/photo.jpg, path/Documents/doc.pdf
  -c -e:   path/Images/jpg/photo.jpg, path/Documents/pdf/doc.pdf
        """
    )

    # Adding arguments

    parser.add_argument('path', type=pathlib.Path,
                        help='Directory to organize')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Print detailed progress')
    parser.add_argument('-e', '--extension', action='store_true',
                        help='Sort by file extension')
    parser.add_argument('-c', '--category', action='store_true',
                        help='Sort by file category')

    args = parser.parse_args()

    # Validate arguments
    if not args.extension and not args.category:
        parser.error("At least one of -e/--extension or -c/--category is required")

    try:
        all_errors = []

        # Sort by extension
        if args.extension and not args.category:
            print("Organizing by extension...")
            moved_files, errors = sort_by_extension(args.path, args.verbose)
            all_errors.extend(errors)

        # Sort by category
        elif args.category and not args.extension:
            print("Organizing by category...")
            moved_files, errors = sort_by_category(args.path, args.verbose)
            all_errors.extend(errors)

        # Sort by both, category first, then extension within each category
        elif args.category and args.extension:
            print("Step 1: Organizing by category...")
            cat_moved, cat_errors = sort_by_category(args.path, args.verbose)
            all_errors.extend(cat_errors)

            print("\nStep 2: Organizing by extension within each category...")
            # Sort each category folder by extension
            for subdir in args.path.iterdir():
                if subdir.is_dir():
                    if args.verbose:
                        print(f"\nProcessing {subdir.name}/...")
                    ext_moved, ext_errors = sort_by_extension(subdir, args.verbose)
                    all_errors.extend(ext_errors)

        # Final summary
        if not args.verbose or all_errors:
            print("\n" + "=" * 50)
            print("COMPLETE")
            print("=" * 50)
            if all_errors:
                print(f"⚠ {len(all_errors)} errors occurred:")
                for error in all_errors[:10]:  # Show first 10
                    print(f"  - {error}")
                if len(all_errors) > 10:
                    print(f"  ... and {len(all_errors) - 10} more")
            else:
                print("✓ All files organized successfully!")

    except Exception as e:
        print(f"Unexpected error: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())