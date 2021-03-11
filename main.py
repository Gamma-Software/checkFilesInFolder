import sys
import os


def get_files_from_folder(path_to_folder):
    """ Get the list of files in folder recursively and sort them """
    print("Get the list of files from ", path_to_folder)
    onlyfiles = []
    for root, dirs, files in os.walk(path_to_folder, topdown=False):
        for file in files:
            onlyfiles.append(file)
    onlyfiles.sort()
    return onlyfiles


def compare_files(list_a, list_b):
    """ Compare the list A and B of files and return the files not found in one another"""
    list_concat = list_a + list_b
    duplicates = [list_concat[i] for i in range(len(list_concat)) if not i == list_concat.index(list_concat[i])]
    for file_duplicate in duplicates:
        list_concat.remove(file_duplicate)
        list_concat.remove(file_duplicate)
    return list_concat


if __name__ == '__main__':
    print(os.getcwd()+"/folderA/")
    list_of_files_A = get_files_from_folder(sys.argv[1])
    list_of_files_B = get_files_from_folder(sys.argv[2])
    print(list_of_files_A, list_of_files_B)

    files_intruded = compare_files(list_of_files_A, list_of_files_B)

    if len(files_intruded) == 0:
        print("The list are identical")
    else:
        print("The list is not identical, here are the intruder")
        print(files_intruded)
