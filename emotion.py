class emotion:
    emotion_names = 'anger anticipation disgust fear joy negative positive sadness surprise trust'.split()
    emotions = {}

    def __init__(self):
        for emotion in self.emotion_names:
            self.emotions[emotion] = 0

        print(self.emotions)


x = emotion()