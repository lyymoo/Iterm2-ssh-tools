"""
homebrew bottle tool
"""
import os
import sys

# echo $(brew --prefix)
# RPL_STR = "@@HOMEBREW_PREFIX@@"
# PREFIX = "/usr/local"
# echo $(brew --cellar)
RPL_STR = "@@HOMEBREW_CELLAR@@"
PREFIX = "/Users/moz/opt"


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
    new_lst = []
    for rst in tool_rst:
        if RPL_STR in rst:
            tmp = rst.replace("\t", "").replace("\n", "")
            tmp = tmp.split(" (")[0]
            new_lst.append(tmp)
    return new_lst


def change_lib(lib1, bin_file):
    #install_name_tool -change @@HOMEBREW_PREFIX@@/opt/tidy-html5/lib/libtidy.58.dylib /usr/local/opt/tidy-html5/lib/libtidy.58.dylib php/8.1.6/bin/phpdbg
    lib2 = lib1.replace(RPL_STR, PREFIX)
    cmd = f"install_name_tool -change {lib1} {lib2} {bin_file}"
    o = os.popen(cmd)
    print(bin_file, lib1, o.read())


def main(path):
    file_lst = read_path(path)
    for file in file_lst:
        lib_lst = read_tool(file)
        for lib in lib_lst:
            change_lib(lib, file)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
