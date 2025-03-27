import os
import re
import shutil

# For backup purposes
import datetime

def rename_files_in_folder(folder_path, pattern, replacement, preview=False, backup=False):
    """
    Renames files in a specified folder based on a regular expression pattern.

    Parameters:
    - folder_path: str, the path to the folder containing files.
    - pattern: str, the regex pattern to search for in filenames.
    - replacement: str, the string to replace the matched pattern.
    - preview: bool, if True, just preview the renaming, no changes are made.
    - backup: bool, if True, create a backup before renaming the files.
    """
    try:
        # Check if folder exists
        if not os.path.exists(folder_path):
            print(f"The folder {folder_path} does not exist.")
            return
        
        # Create backup if needed
        if backup:
            backup_folder = f"backup_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
            shutil.copytree(folder_path, backup_folder)
            print(f"Backup created in {backup_folder}")

        # Preview the renaming process
        print("Previewing file renaming...")
        for filename in os.listdir(folder_path):
            if os.path.isfile(os.path.join(folder_path, filename)):
                new_filename = re.sub(pattern, replacement, filename)
                print(f"{filename} -> {new_filename}")

        # Rename files (only if preview is False)
        if not preview:
            print("\nRenaming files...")
            for filename in os.listdir(folder_path):
                if os.path.isfile(os.path.join(folder_path, filename)):
                    new_filename = re.sub(pattern, replacement, filename)
                    old_file_path = os.path.join(folder_path, filename)
                    new_file_path = os.path.join(folder_path, new_filename)
                    os.rename(old_file_path, new_file_path)
                    print(f"Renamed: {filename} -> {new_filename}")
        else:
            print("\nPreview complete. No files were renamed.")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("Welcome to the Bulk File Renamer!\n")

    folder_path = input("Enter the full path to the folder: ")
    pattern = input("Enter the pattern to match (e.g., 'old' to rename files containing 'old'): ")
    replacement = input("Enter the replacement string (e.g., 'new' to rename to 'new'): ")

    # Ask if user wants to preview the renaming
    preview_choice = input("Do you want to preview the renaming process? (y/n): ").lower()
    preview = preview_choice == 'y'

    # Ask if user wants to create a backup
    backup_choice = input("Do you want to create a backup of the folder before renaming? (y/n): ").lower()
    backup = backup_choice == 'y'

    # Run the renaming function
    rename_files_in_folder(folder_path, pattern, replacement, preview, backup)

if __name__ == "__main__":
    main()
