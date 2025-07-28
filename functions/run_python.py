import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    working_path = os.path.abspath(working_directory)
    file_to_run_path = os.path.abspath(os.path.join(working_directory, file_path))
    check_for_self = file_to_run_path.startswith(working_path)
    check_for_common_path = os.path.commonpath([working_path, file_to_run_path])
    if check_for_common_path != working_path:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if os.path.exists(file_to_run_path) is False:
        return f'Error: File "{file_path}" not found.'
    if not file_to_run_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        result = subprocess.run(
            args,
            executable=file_to_run_path,
            cwd=working_directory,
            check=True,
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.stderr != 0:
            return f"Error: Process exited with code {result.returncode}.\nSTDOUT:{result.stdout}\nSTDERR:{result.stderr}"
            if result.stdout == '':
                return f"No output produced."
        if result.stdout == '':
            return f"No output produced."
        return f"STDOUT:{result.stdout}\nSTDERR:{result.stderr}"
    
    except Exception as exc:
        return f"Error: executing Python file: {exc}"
    
    