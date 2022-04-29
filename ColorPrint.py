'''
--|~|--|~|--|~|--|~|--|~|--|~|--

██  ████        ██████        ██
████    ██     ██           ████
██      ██   ████████     ██  ██
████████       ██       ██    ██
██             ██       █████████
██             ██             ██
               ██
.codé en : UTF-8
.langage : python 3
--|~|--|~|--|~|--|~|--|~|--|~|--
'''

version = "v0.2.4"

def hex2rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    rgb = tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
    return rgb[0], rgb[1], rgb[2]

colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "cyan": (0, 255, 255),
    "magenta": (255, 0, 255),
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "gray": (127, 127, 127),
}

def setcolor(name, value):
    """
    add or edit a color

    --|~|--|~|--|~|--|~|--

    name:       str
    value:      tuple(int, int, int)
    """
    colors[name] = value

def decodecolor(color):
    r, g, b = 0, 0, 0
    if isinstance(color, tuple):
        r, g, b = color
    elif color.startswith("#"):
        r, g, b = hex2rgb(color)
    elif color in colors:
        r, g, b = colors[color]
    return r, g, b


def colorprint(text: str, color="", code = "") -> None:
    """
        colored print

    --|~|--|~|--|~|--|~|--

    text:       str
    color:      Colors.green
    code:
       "b" - bold
       "u" - underline
       "k" - do not go to the line
       (can be combined)
    """

    style = ""
    if "b" in code: style += "\033[01m"
    if "u" in code: style += "\033[04m"
    endl = "\n" if "k" not in code else ""
    r, g, b = decodecolor(color)
    print(f"{style}\033[38;2;{r};{g};{b}m{text}\033[38;2;255;255;255m\033[00m", end = endl, flush = True)


def colorinput(text: str, color="", code = "") -> None:
    """
        colored input

    --|~|--|~|--|~|--|~|--

    text:       str
    color:      Colors.green
    code:
       "b" - bold
       "u" - underline
       (can be combined)
    """

    style = ""
    if "b" in code: style += "\033[01m"
    if "u" in code: style += "\033[04m"
    r, g, b = decodecolor(color)
    return input(f"{style}\033[38;2;{r};{g};{b}m{text}\033[38;2;255;255;255m\033[00m")

if __name__ == "__main__":
    for s in ["","b","bu"]:
        for c in colors:
            colorprint(f"color: '{c}'  -  style: '{s}'", c, s)
        print()