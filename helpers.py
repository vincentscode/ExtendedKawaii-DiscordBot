from datetime import datetime
import builtins
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
log_file = open(dir_path + "/log.txt", "w", encoding="utf8")


# noinspection PyShadowingBuiltins
def print(*args, log_level=0, end="\n"):
    if log_level == 0:
        log_prefix = "[INFO ] "
    elif log_level == 1:
        log_prefix = "[WARN ] "
    elif log_level == 2:
        log_prefix = "[ERROR] "
    else:
        log_prefix = "[     ] "

    print_string = "[" + datetime.now().strftime('%H:%M:%S.%f') + "] " + log_prefix + " ".join(map(str, args)).replace("\n", "")

    builtins.print(print_string, end=end)
    log_file.write(print_string + end)
    log_file.flush()
