# -- coding: UTF-8 --

import os
import subprocess
import shutil

from local_configs import LocalConfigs


def verify_file_exist(file_path):
    if os.path.isfile(file_path):
        return True
    else:
        print("!!!!! Invalid file path: " + file_path)
        return False


def verify_directory_exist(dir_path):
    if os.path.isdir(dir_path):
        return True
    else:
        print("!!!!! Invalid directory path: " + dir_path)
        return False
    

def create_directory_if_not_exist(dir_path):
    if os.path.isdir(dir_path):
        return True
    else:
        os.mkdir(dir_path)
        return os.path.isdir(dir_path)
    

def copy_file_to(file_relpath, dir_relpath):
    file_path = os.path.join(LocalConfigs.REPOSITORY_FOLDER, file_relpath)
    if verify_file_exist(file_path) is False:
        return False
    
    dir_path = os.path.join(LocalConfigs.OUTPUT_FOLDER, dir_relpath)
    if create_directory_if_not_exist(dir_path) is False:
        return False

    dest_file_path = os.path.join(dir_path, os.path.basename(file_path))
    shutil.copyfile(file_path, dest_file_path)
    return verify_file_exist(dest_file_path)


def output_cps_game_app(cps_name, game_name, wad_file_name):
    src_root_dir = os.path.join(LocalConfigs.REPOSITORY_FOLDER, f"VC-Arcade\\{cps_name}\\{game_name}")
    if verify_directory_exist(src_root_dir) is False:
        return False

    dest_apps_dir = os.path.join(LocalConfigs.OUTPUT_FOLDER, "apps")
    if create_directory_if_not_exist(dest_apps_dir) is False:
        return False

    dest_app_dir = os.path.join(dest_apps_dir, f"{cps_name}-{game_name}")
    if create_directory_if_not_exist(dest_app_dir) is False:
        return False
    
    # boot.dol
    src_boot_dol_path = os.path.join(LocalConfigs.REPOSITORY_FOLDER, f"apps\\ra-{cps_name}\\boot.dol")
    dest_boot_dol_path = os.path.join(dest_app_dir, "boot.dol")
    shutil.copyfile(src_boot_dol_path, dest_boot_dol_path)

    # icon.png
    src_icon_png_path = os.path.join(src_root_dir, "icon.png")
    dest_icon_png_path = os.path.join(dest_app_dir, "icon.png")
    shutil.copyfile(src_icon_png_path, dest_icon_png_path)

    # meta.xml
    src_meta_xml_path = os.path.join(src_root_dir, "meta.xml")
    dest_meta_xml_path = os.path.join(dest_app_dir, "meta.xml")
    shutil.copyfile(src_meta_xml_path, dest_meta_xml_path)

    # .wad
    src_wad_file_path = os.path.join(src_root_dir, wad_file_name)
    dest_wad_dir = os.path.join(LocalConfigs.OUTPUT_FOLDER, "wad")
    if create_directory_if_not_exist(dest_wad_dir) is False:
        return False
    dest_wad_dir = os.path.join(dest_wad_dir, "VC-Arcade")
    if create_directory_if_not_exist(dest_wad_dir) is False:
        return False
    
    dest_wad_file_path = os.path.join(dest_wad_dir, wad_file_name)
    shutil.copyfile(src_wad_file_path, dest_wad_file_path)


output_cps_game_app("cps1", "sf2", "Street Fighter II [SF21].wad")
output_cps_game_app("cps1", "sf2ce", "Street Fighter II CE [SF22].wad")
output_cps_game_app("cps3", "sf33", "Street Fighter III 3rd [SF33].wad")
