import os
import time

class FileBackup:
    def __init__(self, source_dir, dest_dir):
        self.source_dir = source_dir
        self.dest_dir = dest_dir

    def list_files(self):
        try:
            files = os.listdir(self.source_dir)
            return files
        except FileNotFoundError:
            print(f"Error: The directory '{self.source_dir}' does not exist.")
            return []

    def create_unique_filename(self, dest_file):
        if os.path.exists(dest_file):
            base, extension = os.path.splitext(dest_file)
            timestamp = time.strftime("%Y%m%d%H%M%S")
            unique_filename = base + "_" + timestamp + extension
            return unique_filename
        else:
            return dest_file

    def copy_file(self, source, destination):
        try:
            with open(source, 'rb') as src_file:
                content = src_file.read()
            with open(destination, 'wb') as dest_file:
                dest_file.write(content)
            print(f"Copied '{source}' to '{destination}'")
        except Exception as e:
            print(f"An error occurred while copying '{source}' to '{destination}': {e}")

    def backup_files(self):
        if not os.path.exists(self.dest_dir):
            print(f"Error: The directory '{self.dest_dir}' does not exist.")
            return

        files = self.list_files()
        for filename in files:
            source_file = os.path.join(self.source_dir, filename)
            dest_file = os.path.join(self.dest_dir, filename)

            unique_dest_file = self.create_unique_filename(dest_file)
            self.copy_file(source_file, unique_dest_file)

if __name__ == "__main__":
    source_directory = input("Enter the source directory: ")
    destination_directory = input("Enter the destination directory: ")

    backup = FileBackup(source_directory, destination_directory)
    backup.backup_files()
