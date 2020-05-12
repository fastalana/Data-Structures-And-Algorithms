import os

def find_files(suffix, path, list_of_paths):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    all_paths = os.listdir(path)
    
    if len(all_paths) == 0:
        return []
    
    list_of_paths += [os.path.join(path, item) for item in all_paths if suffix in os.path.join(path, item)]
    list_of_directories = [os.path.join(path, item) for item in all_paths if os.path.isdir(os.path.join(path, item)) is True]
    
    for item in list_of_directories:
        find_files(suffix, item, list_of_paths)
    
    return list_of_paths

## TESTS ##
path_base = './testdir'

print(find_files(suffix='c', path=path_base, list_of_paths=[]))
# ['./testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c']

print(find_files(suffix='h', path=path_base, list_of_paths=[]))
# ['./testdir/t1.h', './testdir/subdir5/a.h', './testdir/subdir1/a.h', './testdir/subdir3/subsubdir1/b.h']

print(find_files(suffix='z', path=path_base, list_of_paths=[]))
# []
