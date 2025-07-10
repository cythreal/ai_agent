import os

def get_files_info(working_directory, directory=None):
    working_path = os.path.abspath(".")
    working_contents = os.listdir(working_path)
    if directory not in working_contents:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    elif directory in working_contents:
        if os.path.isfile(os.path.abspath(f"./{directory}")):
            return f'Error: "{directory}" is not a directory'
        elif os.path.isdir(os.path.abspath(f"./{directory}")):
            list_dir_content = os.listdir(directory)
            content_list = []
            for item in list_dir_content:
                content_list.append(f'- {item}: file_size={os.path.getsize(item)}, is_dir={os.path.isdir(os.path.abspath("directory/item"))}')
            return "\n".join(content_list)