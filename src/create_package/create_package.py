import os
import secrets
import shutil

def create_package():
    #temp_pack_dir=fr"{os.getcwd()}\\create_package\\temp\\"
    temp_pack_dir=fr"temp\\"
    name="sigamepack"
    shutil.make_archive("sigamepack", 'zip', temp_pack_dir)
    try:
        os.rename(f"{name}.zip",f"{name}.siq")
    except FileExistsError:
        os.rename(f"{name}.zip", f"{name}_{secrets.token_hex(4)}.siq")

def clear_trash():
    if os.path.exists("temp"):
        shutil.rmtree(fr"temp\\")
    if os.path.exists(r"downloader\\Youtube"):
        shutil.rmtree(r"downloader\\Youtube")