from colorama import Fore
import os
import importlib.util
from helpers import print
import sys

print(f"[{Fore.MAGENTA}{'System':20}{Fore.RESET}] Reloading actions")

actions = []
command_actions = {}

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)
for itm in sorted(os.listdir(dir_path)):
    if itm.startswith("__"):
        continue
    try:
        module_name = itm.replace(".py", "")
        module_path = dir_path + "/" + itm

        spec = importlib.util.spec_from_file_location(module_name, module_path)
        assert spec is not None

        loaded_module = importlib.util.module_from_spec(spec)
        assert spec.loader is not None

        spec.loader.exec_module(loaded_module)
        sys.modules[module_name] = loaded_module

        actions.append(loaded_module)
        for command in loaded_module.commands:
            command_actions[command] = loaded_module

    except Exception as e:
        print("Exception on load of", itm, "->", e)
