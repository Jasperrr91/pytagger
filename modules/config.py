import argparse
import json
import os

def init_config(config_file):
    parser = argparse.ArgumentParser()

    load = {}

    if os.path.isfile(config_file):
        try:
            with open(config_file, 'rb') as data:
                load.update(json.load(data))
        except ValueError:
            print('Invalid configuration file')
            sys.exit(-1)
    else:
        print('Config file not found. Make sure config.json is in the config folder.')
        sys.exit(-1)

    # Read passed in Arguments
    required = lambda x: not x in load
    add_config(
        parser,
        load,
        short_flag="-t",
        long_flag="--text",
        help="Text to tag",
        default=None
    )
    add_config(
        parser,
        load,
        short_flag="-tg",
        long_flag="--tags",
        help="Tags to use",
        default=None
    )
    add_config(
        parser,
        load,
        short_flag="-l",
        long_flag="--lexicon",
        help="Text file with lexicon",
        default=False
    )

    config = parser.parse_args()
    if not config.text and 'text' not in load:
        config.text = input("Text to tag: ")

    fix_nested_config(config)
    return config

def add_config(parser, json_config, short_flag=None, long_flag=None, **kwargs):
    if not long_flag:
        raise Exception('add_config calls requires long_flag parameter!')

    full_attribute_path = long_flag.split('--')[1]
    attribute_name = full_attribute_path.split('.')[-1]

    if '.' in full_attribute_path:  # embedded config!
        embedded_in = full_attribute_path.split('.')[0: -1]
        for level in embedded_in:
            json_config = json_config.get(level, {})

    if 'default' in kwargs:
        kwargs['default'] = json_config.get(attribute_name, kwargs['default'])
    if short_flag:
        args = (short_flag, long_flag)
    else:
        args = (long_flag,)
    parser.add_argument(*args, **kwargs)


def fix_nested_config(config):
    config_dict = config.__dict__

    for key, value in config_dict.items():
        if '.' in key:
            new_key = key.replace('.', '_')
            config_dict[new_key] = value
            del config_dict[key]