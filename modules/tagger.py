from modules.parser import parse_lexicon

def tag(config):
    counter = {}
    for tag in config.tags:
        counter[tag] = 0

    hashmap = parse_lexicon(config.lexicon)

    words = config.text.lower().split()
    for word in words:
        try:
            for tag in config.tags:
                try:
                    counter[tag] += hashmap[word][tag]
                except KeyError:
                    continue
        except KeyError:
            continue

    print(counter)