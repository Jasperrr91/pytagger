# PyTagger
Python Tagger based on the Java [EmotionTagger](https://github.com/cltl/EmotionTagger) by Piek Vossen that scores a tag for emotions and expressiveness.

Currently, the output is slightly differ. Intensifiers, Weakeners and Polarity Shifters are also to be added. On the other hand, you can customize with tags to use. This allows you to not only tag emotions but also others data, as long as you have a proper lexicon.

Output compared to the EmotionTagger:

PyTagger
```
{'anger': 0, 'anticipation': 1, 'disgust': 1, 'fear': 0, 'joy': 2, 'negative': 1, 'positive': 2, 'sadness': 0, 'surprise': 1, 'trust': 2}
```

EmotionTagger
```
{"emotion":[{"trust":2,"surprise":1,"negative":1,"joy":2,"anticipation":1,"sadness":0,"positive":2,"disgust":1,"anger":0,"fear":0}],"expression":[{"capitals":0,"intensifiers":0,"weakeners":0,"exclamation":0}]}
```

## Install
Copy `config.json.example` to `config.json` and make changes where necessary.

## Usage
There are multiple ways to run the tagger. You can specify a text to tag in the config file or use the `-t` flag. Alternatively, you can simply run the tagger and enter the text in the input.

## Config Options
Each options as a short flag and a long flag. JSON config keys are identical to long flag
* lexicon
  * --lexicon (long flag)
  * -l (short flag)
  * The lexicon file to be used

* tags
  * --tags (long flag)
  * -t (short flag)
  * The tags used

* text
  * --text (long flag)
  * -t (short flag)
  * The text to tag