import os
from config import MAX_CHARS
from google.genai import types


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
            
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read + list file contents, constrained to files in the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to read from, relative to the working directory. If not provided, reads files in the working directory itself.",
            ),
        },
        required=["file_path"],
    ),
)    