import os
import sys
import stat

def process_directory(path):
    """
        This function recursively traverses through directories, retrieving all files and subdirectories.
    """
    try:
        items = os.listdir(path)
        print(items)
    except (PermissionError, FileNotFoundError, NotADirectoryError) as e:
        print(e)
        return
    
    for item in items:
        full_path = f"{path}/{item}"
        if os.path.isdir(full_path):
            process_directory(full_path + "/")
        elif os.path.isfile(full_path):
            process_file(full_path)

def process_file(path):
    """
        This function retrieves and prints all the required metadata for a given file.
        Input: The full file path must be provided as the input parameter.
    """
    stat_info = os.stat(path)

    file_mode = stat_info.st_mode

    is_readable = (file_mode & stat.S_IRUSR) != 0
    is_writable = (file_mode & stat.S_IWUSR) != 0
    is_executable = (file_mode & stat.S_IXUSR) != 0

    print(
        f"File name: {path}",
        f"File extension: {path[path.rfind('.')+1:]}",
        f"For user: {is_readable=}, {is_writable=}, {is_executable=}",
        f"File size: {stat_info.st_size} bytes.",
        f"File is large: {stat_info.st_size > LARGE_FILE_SIZE * 1024 * 1024}",
        sep="\n",
        end="\n\n"
        )

if __name__ == "__main__":
    args = sys.argv
    try:
        main_path = args[1]
        LARGE_FILE_SIZE = 5 if len(sys.argv) < 3 else float(sys.argv[2])    
    except Exception as e:
        print(
            f"Error: {e}",
            "Wrong input!!!",
            "Usage: python <script_name>.py <directory_path> [LARGE_FILE_SIZE]",
            sep="\n"
        )
    else:
        process_directory(main_path)
    

