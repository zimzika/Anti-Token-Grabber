# coding: utf-8

from os import system
import os
import random
import string
from time import sleep

if os.name != 'nt':
    print("[-] This protector is not maked for this operational system.")
    system("pause")
    exit(0)

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

APPDATA = os.getenv("APPDATA").replace("\\Roaming", "")
LOCAL_PATH = "\\Local\\Discord"
PATH_HASH = id_generator(15)
ROAMING_PATH = "\\Roaming\\discord"

print("\n\nAppdata: {}".format(APPDATA))
print("Local path: {}\n".format(LOCAL_PATH))

def get_folder(path, name):
    return [f for f in os.listdir(path) if os.path.isdir(path + "\\" + f) and f.find(name) != -1]

def get_discord_version():
    return get_folder(APPDATA+LOCAL_PATH, "app-")[0].split("-")[1]

discord_version = get_discord_version()

if not discord_version:
    print("Invalid discord version!")
    system("pause")
    exit(0)

RESOURCES_PATH = APPDATA+LOCAL_PATH+"\\app-" + discord_version + "\\resources"

print("Resources path: {}".format(RESOURCES_PATH))

def extract_files():
    print("Extracting app.asar")
    try:
        system("npm i -g asar")
        system("asar extract " + RESOURCES_PATH + "\\app.asar" + " " + RESOURCES_PATH + "\\tmp")
        return True
    except Exception as e:
        print("Extract error!")
        system("pause")
        exit(0)

print("Discord version: {}".format(discord_version))

if (extract_files()):
    patch = ""
    with open(RESOURCES_PATH+"\\tmp\\common\\paths.js", "r") as f:
        content = f.read()
        old_content = "return _path.default.join(userDataRoot, 'discord' + (buildInfo.releaseChannel == 'stable' ? '' : buildInfo.releaseChannel));"
        if (content.find(old_content) == -1):
            print("This file is not original")
            system("pause")
            exit(0)
        patch = content.replace(old_content, old_content.replace("'discord'", "'"+PATH_HASH+"'"))
    with open(RESOURCES_PATH+"\\tmp\\common\\paths.js", "w") as f:
        if f.write(patch):
            print("Patch applied!")
    system("asar pack " + RESOURCES_PATH+"\\tmp" + " " + RESOURCES_PATH+"\\app.asar")
    print("Done!")
    print("\nClose your Discord.")
    print("Delete Local Storage in {}".format(APPDATA+ROAMING_PATH))
    print("Open your Discord again!")