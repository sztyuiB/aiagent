import os
import subprocess
import sys
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    try:
        full_path = os.path.join(working_directory, file_path)
        abs_wdir = os.path.abspath(working_directory)

        if os.path.abspath(full_path).startswith(os.path.abspath(working_directory)) == False:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if os.path.exists(full_path) == False:
            return f'Error: File "{file_path}" not found.'

        if full_path.endswith(".py") == False:
            return f'Error: "{file_path}" is not a Python file.'

    except Exception as E:
        return f"Error: str({E})"
    
    try:
        completed_process = subprocess.run([sys.executable, os.path.abspath(full_path), *args], cwd=abs_wdir, text=True, capture_output=True, check=True, timeout=30)
        if completed_process.stdout == "" and completed_process.stderr == "":
            return "No output produced."
        if completed_process.returncode != 0:
            return f'STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}\nProcess exited with code {completed_process.returncode}'
        else:
            return f'STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}'
    except Exception as F:
        return f"Error: executing Python file: {F}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python file constrained to the working directory, with optional arguments.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the python file we want to run, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="A list of the optional arguments to run the files with."
            )
        },
    ),
)