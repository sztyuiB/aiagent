import os

def get_files_info(working_directory, directory="."):
    try:
        full_path = os.path.join(working_directory, directory)
    
        if os.path.abspath(full_path).startswith(os.path.abspath(working_directory)) == False:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if os.path.isdir(full_path) == False:
            return f'Error: "{directory}" is not a directory'

        content_list = []
        content_list = os.listdir(full_path)
        output = ""   

        for item in content_list:
            item_path = os.path.join(full_path, item)
            output += f"- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}\n"
    
        return output[:-1]
    except Exception as E:
        return f"Error: str({E})"
