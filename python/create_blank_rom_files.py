# -- coding: UTF-8 --

import os

from configparser import ConfigParser
from local_configs import LocalConfigs


def create_directory_if_not_exist(dir_path):
    if os.path.isdir(dir_path):
        return True
    else:
        os.mkdir(dir_path)
        return os.path.isdir(dir_path)


def create_blank_rom_files(roms_relative_dir, ini_relative_file_path, section_name, exclude_names=None):
    ini_file_path = os.path.join(
        LocalConfigs.REPOSITORY_FOLDER, ini_relative_file_path)
    print(f"Check ini Start: {ini_file_path}")

    config_parser = ConfigParser()
    config_parser.read(ini_file_path)

    file_count = 0
    roms_dir = os.path.join(LocalConfigs.REPOSITORY_FOLDER, roms_relative_dir)
    if create_directory_if_not_exist(roms_dir) is True:
        for key, value in config_parser[section_name].items():
            if exclude_names != None and str(key) in exclude_names:
                continue

            file_count = file_count + 1
            item_path = os.path.join(roms_dir, f"{key}.zip")
            if os.path.isfile(item_path) is True:
                continue

            open(item_path, "w").close()

    print(f"- {file_count} files done!")
    print(f"Check ini End: {ini_file_path}")


# 根据 CPS1.ini 中的文件名称，在 roms-blank\\cps1 文件夹里面创建空的 ROM 文件
create_blank_rom_files("roms-blank\\cps1", "wiiflow\\plugins_data\\CPS1\\CPS1.ini",
                       "CPS1", ("cps1frog", "ganbare", "pokonyan"))

# 根据 CPS2.ini 中的文件名称，在 roms-blank\\cps2 文件夹里面创建空的 ROM 文件
create_blank_rom_files(
    "roms-blank\\cps2", "wiiflow\\plugins_data\\CPS2\\CPS2.ini", "CPS2")

# 根据 CPS3.ini 中的文件名称，在 roms-blank\\cps3 文件夹里面创建空的 ROM 文件
create_blank_rom_files(
    "roms-blank\\cps3", "wiiflow\\plugins_data\\CPS3\\CPS3.ini", "CPS3")
