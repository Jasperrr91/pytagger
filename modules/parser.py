import os

from .functions import preg_match

def parse_lexicon(file):
    this_dir, this_filename = os.path.split(__file__)
    file = os.path.join(this_dir, "..", file)

    data = {}

    with open(file) as f:
        for line in f:
            pattern = '(.*?)\t(.*?)\t(.*)'
            match = preg_match(pattern, line)

            if match:
                word, emotion, score = match.group(1), match.group(2), int(match.group(3))
                if not word in data.keys():
                    data[word] = {}

                data[word][emotion] = score

    return data