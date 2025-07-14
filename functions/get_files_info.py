import os

def get_files_info(working_directory, directory=None):
    working_path = os.path.abspath(working_directory)
    directory_path = os.path.abspath(os.path.join(working_directory, directory))
    check_for_self = directory_path.startswith(working_path)
    if check_for_self is False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    elif check_for_self is True:
        if os.path.isfile(directory_path):
            return f'Error: "{directory}" is not a directory'
        else:
            try:
                if os.path.isdir(directory_path):
                    list_dir_content = os.listdir(directory_path)
                    content_list = []
                    for item in list_dir_content:
                        content_list.append(f'- {item}: file_size={os.path.getsize(os.path.abspath(os.path.join(directory_path, item)))}, is_dir={os.path.isdir(os.path.abspath(os.path.join(directory_path, item)))}')
                    return "\n".join(content_list)
            except Exception as exc:
                return f"Error listing files: {exc}"