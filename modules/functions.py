import re

def preg_match(needle, haystack):
    parts = re.search(needle, haystack)

    if parts:
        return(parts)

    return False