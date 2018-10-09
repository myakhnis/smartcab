from distutils.dir_util import copy_tree

# copy subdirectory example
fromDirectory = "C:\\Users\\Mikhail -Yakhnis\\Documents\\machine_learning\\smartcab\\smartcab\\logs"
toDirectory = "C:\\Users\\Mikhail -Yakhnis\\Documents\\machine_learning\\smartcab\\logs"

copy_tree(fromDirectory, toDirectory)
