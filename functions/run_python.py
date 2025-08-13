import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    working_path = os.path.abspath(working_directory)
    file_to_run_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not (file_to_run_path == working_path or file_to_run_path.startswith(working_path + os.sep)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if os.path.exists(file_to_run_path) is False:
        return f'Error: File "{file_path}" not found.'
    if not file_to_run_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        result = subprocess.run(
            ["python3", file_path, *args],
            cwd=working_directory,
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.stdout == '' and result.stderr == "":
            return f"No output produced."
        if result.returncode != 0:
            return f"Error: Process exited with code {result.returncode}.\nSTDOUT:{result.stdout}\nSTDERR:{result.stderr}"
        return f"STDOUT:{result.stdout}\nSTDERR:{result.stderr}"
    
    except Exception as exc:
        return f"Error: executing Python file: {exc}"
    
    