import os

def write_file(working_directory, file_path, content):
    working_path = os.path.abspath(working_directory)
    file_to_write_path = os.path.abspath(os.path.join(working_directory, file_path))
    check_for_common_path = os.path.commonpath([working_path, file_to_write_path])
    if check_for_common_path != working_path:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        os.makedirs(os.path.dirname(file_to_write_path), exist_ok=True)
        with open(file_to_write_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as exc:
        return f"Error writing to file {file_path}: {exc}"