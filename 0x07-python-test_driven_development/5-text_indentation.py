#!/usr/bin/python3
"""4. Text indentation"""
def text_indentation(text):
    """creates new lines in a string

    Args:
    text: a string

    Exceptions:
    TypeError: if text is not a string

    """
    parsed = []
    y = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for x in range(len(text)):
        if (
                text[x] == '.'
                or text[x] == '?'
                or text[x] == ':'
        ):
            parsed.append(text[y:x + 1])
            y = x + 1
        if y < len(text) and text[y] == ' ':
            y += 1
    for x in range(len(parsed)):
        print(parsed[x])
        print()
