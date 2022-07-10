"""
homebrew bottle tool
"""
import os
import sys

RPL_STR = "@@HOMEBREW_PREFIX@@"


def read_path(path):
    dir_lst = os.listdir(path)
    file_lst = []
    for cur_file in dir_lst:
        path_abs = os.path.join(path, cur_file)
        if os.path.isfile(path_abs) and os.access(path_abs, os.X_OK):
            file_lst.append(path_abs)
    return file_lst

def read_tool(file):
    o = os.popen(f"otool -L {file}")
    tool_rst = o.readlines()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        _path = sys.argv[1]
        _file_lst = read_path(_path)
        read_tool(_file_lst[0])
