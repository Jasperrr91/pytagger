import json
import os
import sys

from modules.config import init_config
from modules.tagger import tag

if __name__ == "__main__":
    config = init_config('config/config.json')
    from pprint import pprint
    pprint(config)

    tag(config)