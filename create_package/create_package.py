import os
import secrets
import shutil

def create_package():
    temp_pack_dir=fr"{os.getcwd()}\\create_package\\temp\\"
    name="sigamepack"
    shutil.make_archive("sigamepack", 'zip', temp_pack_dir)
    try:
        os.rename(f"{name}.zip",f"{name}.siq")
    except FileExistsError:
        os.rename(f"{name}.zip", f"{name}_{secrets.token_hex(4)}.siq")

def clear_trash():
    shutil.rmtree(fr"{os.getcwd()}\\create_package\\temp\\")