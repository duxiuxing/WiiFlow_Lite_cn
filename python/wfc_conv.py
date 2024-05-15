#-- coding: UTF-8 --

import os
import subprocess

from local_configs import LocalConfigs


def convert_boxcovers_png_to_wfc():
    if os.path.isfile(LocalConfigs.WFC_CONV_EXE) is False:
        print(f"ERROR: \"{LocalConfigs.WFC_CONV_EXE}\" is not found!")
        pc_tool_path = os.path.join(LocalConfigs.REPOSITORY_FOLDER, "pc-tool\\WFC_conv_0-1.zip")
        print(f"Tips: Install wfc_conv.exe first with \"{pc_tool_path}\"")
        return

    wiiflow_data_dir = os.path.join(LocalConfigs.REPOSITORY_FOLDER, "wiiflow")
    cmd_line = f"\"{LocalConfigs.WFC_CONV_EXE}\" \"{wiiflow_data_dir}\""
    print(cmd_line)
    subprocess.call(cmd_line)


convert_boxcovers_png_to_wfc()
