from datetime import datetime
import builtins

log_file = open("log.txt", "w", encoding="utf8")


# noinspection PyShadowingBuiltins
def print(*args, log_level=0):
    if log_level == 0:
        log_prefix = "[INFO ] "
    elif log_level == 1:
        log_prefix = "[WARN ] "
    elif log_level == 2:
        log_prefix = "[ERROR] "
    else:
        log_prefix = "[     ] "

    print_string = "[" + datetime.now().strftime('%H:%M:%S.%f') + "] " + log_prefix + " ".join(map(str, args)).replace("\n", "")

    builtins.print(print_string)
    log_file.write(print_string + "\n")
    log_file.flush()
