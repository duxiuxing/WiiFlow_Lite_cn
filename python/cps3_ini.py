#-- coding: UTF-8 --

import os
import zlib

from configparser import ConfigParser
from local_configs import LocalConfigs


def compute_crc(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
        crc = zlib.crc32(data)
        return hex(crc & 0xFFFFFFFF)[2:].upper()


# 创建配置解析器
config_parser = ConfigParser()

cps3_section = "CPS3"
config_parser.add_section(cps3_section)

game_id = 800703

cps3_roms_dir = os.path.join(LocalConfigs.REPOSITORY_FOLDER, "roms\\cps3")
for item_name in os.listdir(cps3_roms_dir):
    item_path = os.path.join(cps3_roms_dir, item_name)

    if os.path.isfile(item_path):
        file_extension = item_path.split(".")[-1]
        if file_extension == "zip":
            option = str(item_name)[:-4]
            value = f"{str(game_id)}|{compute_crc(item_path)}"
            config_parser.set(cps3_section, option, value)
            game_id = game_id + 1

config_ini_path = os.path.join(LocalConfigs.REPOSITORY_FOLDER, "wiiflow\\plugins_data\\CPS3\\CPS3.ini")
if os.path.isfile(config_ini_path):
    os.remove(config_ini_path)

with open(config_ini_path, "w") as config_file:
    config_parser.write(config_file)
