"""
check the duplicates docs , create a .txt to save md5 code to match when upload docs
ommit docs if same
"""

import os
import hashlib
import back.config as config


def check_md5(md5_str: str):
    """recieve a md5 str to match in md5.txt"""
    if not os.path.exists(config.MD5_PATH):
        open(config.MD5_PATH, "w", encoding="utf-8").close()
        return False

    with open(config.MD5_PATH, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip() == md5_str:
                return True

    return False


def save_md5(md5_str: str):
    """recieve a md5 str to save in md5.txt"""
    with open(config.MD5_PATH, "a", encoding="utf-8") as f:
        f.write(md5_str + "\n")


def get_string_md5(input_str):
    """recieve a input str and transfer to md5 str"""
    str_byte = input_str
    md5_obj = hashlib.md5()
    md5_obj.update(str_byte)
    md5_hex = md5_obj.hexdigest()

    return md5_hex
