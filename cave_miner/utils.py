def parse_int(st: str) -> int:
    if "x" in st:
        return int(st, 16)
    elif "X" in st:
        return int(st, 16)
    else:
        return int(st)


class Bcolors:
    GREEN = "\033[92m"
    YELLOW = "\033[33m"
    ENDC = "\033[0m"
    GREY = "\033[37m"
    BOLD = "\033[1m"
    RED = "\033[31m"


def color(tpl: str) -> str:
    return tpl.format(
        green=Bcolors.GREEN,
        yellow=Bcolors.YELLOW,
        endc=Bcolors.ENDC,
        grey=Bcolors.GREY,
        bold=Bcolors.BOLD,
        red=Bcolors.RED,
    )
