import os
from functions.config import MAX_FILE_LENGTH

def get_file_content(working_directory, file_path):
    try:
        full_path = os.path.join(working_directory, file_path)

        if os.path.abspath(full_path).startswith(os.path.abspath(working_directory)) == False:
            return f'Error: Cannot read "{full_path}" as it is outside the permitted working directory'
        
        if os.path.isfile(full_path) == False:
            return f'Error: File not found or is not a regular file: "{full_path}"'
        
        with open(full_path, "r") as f:
            f.seek(0)
            file_full = f.read()
            f.seek(0)
            file_truncated = f.read(MAX_FILE_LENGTH)
            if len(file_full) > len(file_truncated):
                f.seek(0)
                file_content_string = f.read(MAX_FILE_LENGTH) + f'\n[...File "{full_path}" truncated at {MAX_FILE_LENGTH} characters]'
            else:
                f.seek(0)
                file_content_string = f.read()

        return file_content_string

    except Exception as E:
        return f"Error: str({E})"