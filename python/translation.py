# -- coding: UTF-8 --

import os
import shutil
import subprocess

from local_configs import LocalConfigs

def compare_string_id(src_language_file, dest_language_file):
    languages_folder = os.path.join(LocalConfigs.REPOSITORY_FOLDER, "wiiflow\\languages")

    src_file_path = os.path.join(languages_folder, src_language_file)
    dest_file_path = os.path.join(languages_folder, dest_language_file)

    src_file = open(src_file_path, 'r', encoding="UTF-8")
    dest_file = open(dest_file_path, 'r', encoding="UTF-8")

    src_line = src_file.readline()
    dest_line = dest_file.readline()

    line_count = 0
    while src_line and dest_line:
        line_count = line_count + 1

        src_index = src_line.find('=')
        dest_index = dest_line.find('=')

        if src_index != dest_index:
            print(f"ERROR: ln {line_count} is not match!")
            break

        if src_index > 1:
            src_id = src_line[:src_index]
            dest_id = dest_line[:dest_index]
            if src_id != dest_id:
                print(f"ERROR: ln {line_count} ID is not match!")
                break

        src_line = src_file.readline()
        dest_line = dest_file.readline()

    src_file.close()
    dest_file.close()
    print(f"Total lines count: {line_count}")


compare_string_id("english.ini", "chinese_s.ini")
