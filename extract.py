import re


def match(text):
    pattern = r".*\.(jpg|png|gif|bmp)"
    return re.search(pattern, text)
