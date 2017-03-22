from .modules import init_config
from .modules import tag

def doTag(text=False, lexicon=False, tags=False):
    config = init_config()

    if text:
        config.text = text

    if lexicon:
        config.lexicon = lexicon

    if tags:
        if isinstance(tags, list):
            config.tags = tags

    return tag(config)