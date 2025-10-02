import os
from google.genai import types

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

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write to the given file, constrained to the working directory.  Creates file if it does not exist, and overwrites if it does.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write to, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
            ),
        },
        required=["file_path", "content"],
    ),
)