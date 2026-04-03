import os
import shutil

# We can change this path to the directory we want to organize. 
SOURCE_DIR = os.path.expanduser("~/Downloads")

# Defining the categories and the file extensions that belong in them.
# We can add or modify these based on your needs.
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".bmp", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".xls", ".xlsx", ".ppt", ".pptx", ".csv"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Executables": [".exe", ".msi", ".dmg", ".pkg"],
    "Code": [".py", ".html", ".css", ".js", ".json", ".cpp", ".c", ".java"]
}

def get_category(extension):      #Returns the category for a given file extension.
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Others"     # For files that don't match any listed extension

def organize_files(source_directory):
    """Scans the directory and moves files into their categorized folders."""
    
    # Check if the source directory exists
    if not os.path.exists(source_directory):
        print(f"Error: The directory '{source_directory}' does not exist.")
        return

    print(f"Organizing files in: {source_directory}...\n")
    moved_count = 0

    # Go through all items in the source directory
    for filename in os.listdir(source_directory):
        file_path = os.path.join(source_directory, filename)

        # Skip directories, we only want to move files
        if os.path.isdir(file_path):
            continue

        # Extract the file extension
        _, file_extension = os.path.splitext(filename)
        
        # If the file has no extension like hidden system files, it skips it
        if not file_extension:
            continue

        # Determine the target folder based on the extension
        category = get_category(file_extension)
        target_folder = os.path.join(source_directory, category)

        # Create the target folder if it doesn't already exist
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

        target_path = os.path.join(target_folder, filename)

        # Move the file
        try:
            # Check if a file with the same name already exists in the target folder
            if os.path.exists(target_path):
                print(f"Skipped: '{filename}' (File already exists in {category})")
            else:
                shutil.move(file_path, target_path)
                print(f"Moved: '{filename}' -> {category}/")
                moved_count += 1
        except Exception as e:
            print(f"Error moving '{filename}': {e}")

    print(f"\nOrganization complete! Successfully moved {moved_count} files.")

if __name__ == "__main__":
    organize_files(SOURCE_DIR)