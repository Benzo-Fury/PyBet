def blue(text):
    blue_text = ""
    for character in text:
        blue_text += f"\033[38;2;0;0;255m{character}\033[0m"
    return blue_text


def green(text):
    green_text = ""
    for character in text:
        green_text += f"\033[38;2;0;255;0m{character}\033[0m"
    return green_text


def orange(text):
    orange_text = ""
    for character in text:
        orange_text += f"\033[38;2;255;165;0m{character}\033[0m"
    return orange_text


def purple(text):
    purple_text = ""
    for character in text:
        purple_text += f"\033[38;2;221;160;221m{character}\033[0m"
    return purple_text


def yellow(text):
    yellow_text = ""
    for character in text:
        yellow_text += f"\033[38;2;255;255;0m{character}\033[0m"
    return yellow_text


def red(text):
    red_text = ""
    for character in text:
        red_text += f"\033[38;2;255;0;0m{character}\033[0m"
    return red_text


def pinkish_red(text):
    pinkish_red_text = ""
    for character in text:
        pinkish_red_text += f"\033[38;2;255;20;147m{character}\033[0m"
    return pinkish_red_text


def water(text):
    faded = ""
    colour_green = 10
    for line in text.splitlines():
        faded += f"\033[38;2;0;{colour_green};255m{line}\033[0m\n"
        if not colour_green == 255:
            colour_green += 15
            if colour_green > 255:
                colour_green = 255
    return faded