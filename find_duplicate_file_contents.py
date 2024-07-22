import os
import hashlib

# read the contents of the file with the context manager to close file, then returns the readings of the file
def read_contents(file_path): 
    with open(file_path, 'rb') as file:
        return file.read()

# hashes the contents of the file, and will return the hexdigest of the contents (which we will use as the key)
def hash_the_contents(file_content):
    hasher = hashlib.sha256()
    hasher.update(file_content)
    return hasher.hexdigest()

def find_duplicate_files(directory):
    dictionary_of_contents = {}

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                contents_key = hash_the_contents(read_contents(file_path))
                if contents_key in dictionary_of_contents:
                    dictionary_of_contents[contents_key].append(file_path)
                else:
                    dictionary_of_contents[contents_key] = [file_path]
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")
    
    groups_of_file_paths = []

    for key, value in dictionary_of_contents.items():
        if len(value) > 1:
            groups_of_file_paths.append(value)

    return groups_of_file_paths

def main():
    directory = input("Enter the directory to search for duplicate files: ")
    duplicate_files = find_duplicate_files(directory)
    print(f"Here are the groups of file paths that have the same contents: {duplicate_files}")

if __name__ == "__main__":
    main()

                
                
