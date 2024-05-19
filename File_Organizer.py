import os
import readline  # Import readline module for auto-completion
import shutil

def get_directory():
    while True:
        dir_path = input("Enter the full or relative directory of the files to be sorted (or type 'exit' to quit): ").strip()
        if dir_path.lower() == 'exit':
            print("Exiting the program.")
            exit(0)
        dir_path = os.path.expanduser(dir_path)  # Expand ~ to the full path
        dir_path = os.path.abspath(dir_path)  # Get absolute path
        if os.path.isdir(dir_path):
            return dir_path
        else:
            print(f"The directory '{dir_path}' does not exist. Please try again.")

def main():
    # Enable auto-completion for paths
    readline.set_completer_delims(' \t\n;')
    readline.parse_and_bind("tab: complete")

    # Get the directory from the user
    source_folder = get_directory()

    # Get the filename of the current script dynamically
    current_script = os.path.basename(__file__)

    # Create a dictionary to map file extensions to folder names
    file_types = {
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.odt', '.rtf'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.tif'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv'],
        'Music': ['.mp3', '.wav', '.aac', '.flac', '.m4a', '.ogg'],
        'Archives': ['.zip', '.tar', '.gz', '.7z', '.rar', '.iso'],
        'Scripts': ['.py', '.sh', '.bat', '.ps1', '.php', '.js']
    }

    # Organize files
    for filename in os.listdir(source_folder):
        # Skip the current script file dynamically
        if filename == current_script:
            continue

        # Get the file extension
        file_extension = os.path.splitext(filename)[1]

        # Skip directories
        if os.path.isdir(os.path.join(source_folder, filename)):
            continue

        # Move files to the corresponding folder
        moved = False
        for folder, extensions in file_types.items():
            if file_extension in extensions:
                # Create the directory if it doesn't exist
                os.makedirs(os.path.join(source_folder, folder), exist_ok=True)
                shutil.move(os.path.join(source_folder, filename), os.path.join(source_folder, folder, filename))
                moved = True
                break

        # If file type is unknown, leave the file alone
        if not moved:
            pass

    print("Files have been organized.")

if __name__ == "__main__":
    main()
