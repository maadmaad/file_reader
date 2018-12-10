#!/usr/bin/python3
import sys
import glob

def usage():
    print("Usage:\t./fmt_reader.py directory_name")
    print("or\tpython fm_reader.py directory_name")

def check_arguments():
    if len(sys.argv) < 3 or sys.argv[1][0] != '.':
        usage()
        sys.exit(1)

def print_files(file_extension, directory):
    if directory[-1] == '/':
        directory = directory[:-1]

    for file_path in glob.iglob(directory + '/**/*' + file_extension, recursive=True):
        try:
            with (open(file_path, 'r')) as file:
                print("\n" + file_path + " :")
                for line in file:
                    print(line, end='')
                print()
        except IOError:
            print("Could not read a file " + file_path)

if __name__ == "__main__":
    check_arguments()
    print_files(sys.argv[1], sys.argv[2])
