import winreg
import vdf
import random
import os

aReg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)

print(aReg)

game_list = []

steam_key = winreg.OpenKeyEx(aReg, r"SOFTWARE\WOW6432Node\Valve\Steam")
install_path = winreg.QueryValueEx(steam_key, "InstallPath")
if install_path:
    winreg.CloseKey(steam_key)
    print(install_path)
    spath = install_path[0] + '\\steamapps\\libraryfolders.vdf'
    with open(spath, 'r') as file:
        data = vdf.loads(file.read())
        print(data)

    libfolders = data["libraryfolders"]
    print(libfolders)
    del libfolders["contentstatsid"]
    print(libfolders)
    for loc in libfolders:
        print(loc)
        loc_data = libfolders[loc]
        print(loc_data)
        for app in loc_data["apps"].items():
            game_list.append(app)

    print(game_list)

    rand_num = random.randint(0, (len(game_list) - 1))
    print(rand_num)

    print(game_list[rand_num][0])
    os.system(f'cmd /k ""{install_path[0]}\\steam.exe" steam://rungameid/'
              f'{game_list[rand_num][0]}"')
