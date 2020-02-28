from colorama import Fore
import os
import importlib.util
from helpers import print


print(f"[{Fore.MAGENTA}{'System':20}{Fore.RESET}] Reloading actions")

actions = []
command_actions = {}

dir_path = os.path.dirname(os.path.realpath(__file__))
for itm in sorted(os.listdir(dir_path)):
    if itm.startswith("__"):
        continue

    spec = importlib.util.spec_from_file_location(itm, dir_path + "/" + itm)
    loaded_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded_module)
    actions.append(loaded_module)
    for command in loaded_module.commands:
        command_actions[command] = loaded_module
