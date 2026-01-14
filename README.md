# File Organizer

A Python command-line tool to automatically organize files in a directory by category and/or file extension.

## Features

- 📁 **Sort by Extension**: Organize files into folders by extension (`.jpg`, `.pdf`, etc.)
- 🗂️ **Sort by Category**: Group files into categories (Images, Documents, Videos, etc.)
- 🔄 **Combined Sorting**: Sort by category first, then by extension within each category
- 🔍 **Duplicate Handling**: Automatically handles duplicate filenames
- ⚠️ **Error Reporting**: Comprehensive error handling and reporting
- 📊 **Verbose Mode**: Detailed progress information
- 🛡️ **Safe Operations**: Validates paths and provides clear error messages

## Installation

### Prerequisites

- Python 3.6 or higher

### Clone the Repository

```bash
git clone https://github.com/ilyasyoussefmouhri/Automatic-File-Sorting-Tool
cd Automatic-File-Sorting-Tool
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Basic Commands

**Sort by extension only:**
```bash
python file_organizer.py /path/to/folder -e
```
Creates: `path/jpg/`, `path/pdf/`, `path/mp3/`

**Sort by category only:**
```bash
python file_organizer.py /path/to/folder -c
```
Creates: `path/Images/`, `path/Documents/`, `path/Audio/`

**Sort by category then extension:**
```bash
python file_organizer.py /path/to/folder -c -e
```
Creates: `path/Images/jpg/`, `path/Documents/pdf/`, `path/Audio/mp3/`

**Enable verbose output:**
```bash
python file_organizer.py /path/to/folder -c -e -v
```

### Command-Line Options

```
positional arguments:
  path                  Directory to organize

optional arguments:
  -h, --help           Show help message and exit
  -v, --verbose        Print detailed progress information
  -e, --extension      Sort by file extension
  -c, --category       Sort by file category
```

**Note:** At least one of `-e` or `-c` is required.

## Supported File Categories

| Category   | Extensions |
|------------|------------|
| **Images** | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`, `.ico`, `.webp` |
| **Documents** | `.pdf`, `.doc`, `.docx`, `.txt`, `.xlsx`, `.xls`, `.pptx`, `.odt` |
| **Videos** | `.mp4`, `.avi`, `.mkv`, `.mov`, `.wmv`, `.flv`, `.webm` |
| **Audio** | `.mp3`, `.wav`, `.flac`, `.aac`, `.ogg`, `.m4a` |
| **Archives** | `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.bz2` |
| **Code** | `.py`, `.js`, `.html`, `.css`, `.java`, `.cpp`, `.c`, `.h`, `.json` |
| **Other** | All other file types |

## Examples

### Example 1: Organize Downloads Folder

```bash
python file_organizer.py ~/Downloads -c -e -v
```

**Before:**
```
Downloads/
├── photo.jpg
├── document.pdf
├── song.mp3
├── video.mp4
└── script.py
```

**After:**
```
Downloads/
├── Images/
│   └── jpg/
│       └── photo.jpg
├── Documents/
│   └── pdf/
│       └── document.pdf
├── Audio/
│   └── mp3/
│       └── song.mp3
├── Videos/
│   └── mp4/
│       └── video.mp4
└── Code/
    └── py/
        └── script.py
```

### Example 2: Quick Extension Sort

```bash
python file_organizer.py ~/Desktop -e
```

**Before:**
```
Desktop/
├── report.pdf
├── photo1.jpg
├── photo2.jpg
└── notes.txt
```

**After:**
```
Desktop/
├── pdf/
│   └── report.pdf
├── jpg/
│   ├── photo1.jpg
│   └── photo2.jpg
└── txt/
    └── notes.txt
```

## How It Works

### Duplicate Handling

If a file with the same name already exists in the target folder, the script automatically appends a number:

```
photo.jpg → photo_1.jpg
photo.jpg → photo_2.jpg
```

### Error Handling

- Invalid paths are caught and reported
- Individual file errors don't stop the entire process
- All errors are collected and reported at the end

### Safe Operations

- Only processes files (ignores subdirectories)
- Validates path existence before starting
- Uses `shutil.move()` for safe file operations
- Creates directories only when needed

## Project Structure

```
file-organizer/
├── file_organizer.py    # Main script (CLI entry point)
├── sorter.py            # Core sorting functions
├── README.md            # This file
├── requirements.txt     # Python dependencies
└── LICENSE              # License file
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Steps to Contribute:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Future Enhancements

- [ ] Add configuration file support for custom categories
- [ ] Support for recursive directory organization
- [ ] Undo functionality
- [ ] GUI version
- [ ] Dry-run mode to preview changes
- [ ] Custom naming patterns
- [ ] Support for organizing by date/size

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Troubleshooting

### Permission Errors

If you encounter permission errors:
```bash
# On Linux/Mac
sudo python file_organizer.py /path/to/folder -c -e

# Or change permissions
chmod +x file_organizer.py
```

### Path Not Found

Make sure to use absolute paths or verify relative paths:
```bash
# Absolute path (recommended)
python file_organizer.py /home/user/Downloads -c

# Relative path
python file_organizer.py ./my_folder -e
```

### Files Not Moving

- Check that you have write permissions in the directory
- Ensure the files aren't currently open in another program
- Run with `-v` flag to see detailed error messages

## FAQ

**Q: Will this delete any files?**  
A: No, the script only moves files, never deletes them.

**Q: What happens to files without extensions?**  
A: They are placed in a folder called `no_extension`.

**Q: Can I organize multiple folders at once?**  
A: Not directly, but you can run the script multiple times or use a shell loop:
```bash
for dir in ~/Downloads ~/Desktop ~/Documents; do
    python file_organizer.py "$dir" -c -e
done
```

**Q: Can I customize the categories?**  
A: Currently, you need to modify the `categories` dictionary in the `sort_by_category()` function. A configuration file feature is planned.

## Author

Ilyas Youssef Mouhri - [@ilyasyoussefmouhri](https://github.com/ilyasyoussefmouhri)

Project Link: [Automatic-File-Sorter](https://github.com/ilyasyoussefmouhri/Automatic-File-Sorting-Tool)

## Acknowledgments

- Built with Python's `pathlib` and `shutil` libraries
- Inspired by the need for automated file organization
- Thanks to all contributors

---

**Note:** Always backup important files before running organization scripts!