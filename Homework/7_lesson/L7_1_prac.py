import os


def project_starter(path: str, folders: list):
    """Creates project folders. The first word in the list is the folder name of the project ROOT"""
    for el in folders:
        if folders[0] == el and os.path.isdir(os.path.join(path, folders[0])) is False:
            os.mkdir(os.path.join(path, el))
        elif os.path.isdir(os.path.join(os.path.join(path + "\\" + folders[0], el))) is False and folders[0] != el:
            os.mkdir(os.path.join(path + "\\" + folders[0], el))


if __name__ == "__main__":
    import sys

    path = sys.argv[1]
    folders = sys.argv[2].split(",")
    project_starter(path, folders)
