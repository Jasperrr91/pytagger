from .modules import init_config
from .modules import tag

def doTag(text=False):
    config = init_config()

    if text:
        config.text = text

    return tag(config)