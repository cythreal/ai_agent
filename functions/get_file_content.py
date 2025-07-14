import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    working_path = os.path.abspath(working_directory)
    file_to_read_path = os.path.abspath(os.path.join(working_directory, file_path))
    check_for_self = file_to_read_path.startswith(working_path)
    if check_for_self is False:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    elif check_for_self is True:
        if os.path.isfile(file_to_read_path) is False:
            f'Error: File not found or is not a regular file: "{file_path}"'
        else:
            try:
                if os.path.isfile(file_to_read_path):
                    with open(file_to_read_path, "r") as f:
                        file_content_string = f.read(MAX_CHARS)
                        if os.path.getsize(file_to_read_path) > MAX_CHARS:
                            file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                    return f'{file_content_string}'        
            except Exception as exc:
                return f"Error listing file {file_path} contents: {exc}"