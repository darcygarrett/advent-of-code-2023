import regex

def matcher(text):
    matches = regex.findall(r'(?:\d|one|two|three|four|five|six|seven|eight|nine)', text, overlapped=True)
    return matches