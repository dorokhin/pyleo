import os


def get_or_create_node(_file_name='cookies.txt', _path='.pyleo'):
    _file_path = os.path.join(os.path.expanduser("~"), _path)

    if not os.path.exists(os.path.join(_file_path, _file_name)):
        try:
            os.makedirs(_file_path)
        except FileExistsError as e:
            pass
        os.mknod(os.path.join(_file_path, _file_name))
    return os.path.join(_file_path, _file_name)
