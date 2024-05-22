#-- coding: UTF-8 --
# 检查 roms\\cps1 文件夹里面 ROM 文件的名称，是否和 wiiflow\\plugins_data\\CPS1\\CPS1.ini 中的文件名称一致
# 检查 roms\\cps2 文件夹里面 ROM 文件的名称，是否和 wiiflow\\plugins_data\\CPS2\\CPS2.ini 中的文件名称一致
# 检查 roms\\cps3 文件夹里面 ROM 文件的名称，是否和 wiiflow\\plugins_data\\CPS3\\CPS3.ini 中的文件名称一致

import os
import zlib

from configparser import ConfigParser
from local_configs import LocalConfigs


def compute_crc32(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
        crc = zlib.crc32(data)
        return hex(crc & 0xFFFFFFFF)[2:].upper()


def check_roms_is_in_ini_file(roms_relative_dir, ini_relative_file_path, section_name):
    config_parser = ConfigParser()
    ini_file_path = os.path.join(LocalConfigs.REPOSITORY_FOLDER, ini_relative_file_path)
    config_parser.read(ini_file_path)

    roms_dir = os.path.join(LocalConfigs.REPOSITORY_FOLDER, roms_relative_dir)
    print(f"List Directory Start: {roms_dir}")

    for item_name in os.listdir(roms_dir):
        item_path = os.path.join(roms_dir, item_name)

        if os.path.isfile(item_path):
            file_extension = item_path.split(".")[-1]
            if file_extension != "zip":
                continue
            option = str(item_name)[:-4]
            if config_parser.has_option(section_name, option) is True:
                continue
            
            crc32 = compute_crc32(item_path)
            option = str(item_name)[:-5]
            if config_parser.has_option(section_name, option) is True:
                value = config_parser.get(section_name, option)
                if value.find(crc32) > 0:
                    continue

            print("ERROR: file name not match")
            print(f"- path: {item_path}")
            print(f"- CRC32: {crc32}")

    print(f"List Directory End: {roms_dir}")


def check_roms_in_ini_file_is_exist(roms_relative_dir, ini_relative_file_path, section_name, exclude_names = None):
    ini_file_path = os.path.join(LocalConfigs.REPOSITORY_FOLDER, ini_relative_file_path)
    print(f"Check Ini Start: {ini_file_path}")

    config_parser = ConfigParser()
    config_parser.read(ini_file_path)

    roms_dir = os.path.join(LocalConfigs.REPOSITORY_FOLDER, roms_relative_dir)
    for key, value in config_parser[section_name].items():
        if exclude_names != None and str(key) in exclude_names:
            continue

        item_path = os.path.join(roms_dir, f"{key}.zip")
        if os.path.isfile(item_path) is True:
            continue

        item_path = os.path.join(roms_dir, f"{key}u.zip")
        if os.path.isfile(item_path) is True:
            continue

        print("ERROR: file name not match")
        print(f"- name: {key}")

    print(f"Check Ini End: {ini_file_path}")


check_roms_is_in_ini_file("roms\\cps1", "wiiflow\\plugins_data\\CPS1\\CPS1.ini", "CPS1")
check_roms_in_ini_file_is_exist("roms\\cps1", "wiiflow\\plugins_data\\CPS1\\CPS1.ini", "CPS1", ("cps1frog", "ganbare", "pokonyan"))

check_roms_is_in_ini_file("roms\\cps2", "wiiflow\\plugins_data\\CPS2\\CPS2.ini", "CPS2")
check_roms_in_ini_file_is_exist("roms\\cps2", "wiiflow\\plugins_data\\CPS2\\CPS2.ini", "CPS2")

check_roms_is_in_ini_file("roms\\cps3", "wiiflow\\plugins_data\\CPS3\\CPS3.ini", "CPS3")
check_roms_in_ini_file_is_exist("roms\\cps3", "wiiflow\\plugins_data\\CPS3\\CPS3.ini", "CPS3")
