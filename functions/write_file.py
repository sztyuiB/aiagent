import os
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        full_path = os.path.join(working_directory, file_path)

        if os.path.abspath(full_path).startswith(os.path.abspath(working_directory)) == False:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        path_dirs = os.path.join(working_directory, os.path.dirname(file_path))
        if os.path.exists(path_dirs) == False:
            os.mkdir(path_dirs)

    except Exception as E:
        return f"Error: str({E})"
    
    try:
        with open(full_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as F:
        return f"Error: str({F})"


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Updates the contents of the specified file with the given content, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the file we want to update, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The new content to update the old content of the specified file."
            )
        },
    ),
)