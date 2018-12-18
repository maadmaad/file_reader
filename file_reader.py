#!/usr/bin/python3
import sys
import glob
import os
import json
from pprint import pprint
import re

def usage():
    print("Usage:\t\t./fmt_reader.py directory file_extension ")
    print("example:\t./fm_reader.py /home/user/my_dir/ .fmt")

def check_arguments():
    if len(sys.argv) < 3 or sys.argv[2][0] != '.':
        usage()
        sys.exit(1)

def print_files(dir, file_ext):
    for file_path in glob.iglob(os.path.join(dir, '**', '*' + file_ext), recursive=True):
        json_file_name = os.path.splitext(os.path.basename(file_path))[0] + ".json"
        out_file_name = os.path.splitext(os.path.basename(file_path))[0] + ".txt"
        out_file_name = os.path.join(os.path.dirname(file_path), out_file_name)
        json_path = os.path.join(os.path.dirname(file_path), json_file_name)
        json_keys = set()
        try:
            with open(file_path, 'r') as file:
                if os.path.isfile(json_path):
                    with open(json_path, 'r') as json_file, open(out_file_name, 'w') as out_file:
                        json_data = json.load(json_file)
                        json_data_tmp = json_data
    
                        myre = re.compile(r'{([^{}]*)}')
                        for line in file:
                            match_set = set(myre.findall(line))
                            json_keys = set(json_data.keys())
                            diff = match_set.difference(json_keys)
                            for el in list(diff):
                                json_data_tmp[el] = "{{{}}}".format(el)
                            out_file.write(line.format(**json_data_tmp))                            
                            json_data_tmp = json_data
                else:
                    print("\n" + file_path + " :")
                    for line in file:
                        print(line, end='')
                    print()
        except IOError:
            print("Could not read a file " + file_path)

if __name__ == "__main__":
    check_arguments()
    print_files(sys.argv[1], sys.argv[2])
