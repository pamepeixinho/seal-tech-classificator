import json


class Data:
    """
        dataset = [
            {
                "emotions": [{
                    "anger": Number,
                    "contempt": Number,
                    "disgust": Number,
                    "fear": Number,
                    "happiness": Number,
                    "neutral": Number,
                    "sadness": Number,
                    "surprise": Number,
                }],
                "attention": Number,
                "continueVideosLikeThis":  Number,
                "goodExamples":  Number,
                "goodExperience":  Number,
                "haveCommitment":  Number,
                "interesting":  Number,
                "likeDidactics":  Number,
                "longVideo":  Number,
                "moreDynamic":  Number,
                "noPause":  Number,
                "previousKnowledge":  Number,
                "recommendVideo": Number,
                "tooMuchContent":  Number,
            }
        ]
    """

    def __init__(self):
        with open('videos-v2.json', encoding='utf-8') as data_json:
            self.data_set = json.load(data_json)

    def clean_dataset(self):
        return self.data_set

    def get_average_of_emotions(self):
        """
          [{
                "averageAnger":  Number,
                "averageContempt":  Number,
                "averageDisgust":  Number,
                "averageFear":  Number,
                "averageHappiness":  Number,
                "averageNeutral":  Number,
                "averageSadness":  Number,
                "averageSurprise":  Number,

                "attention": Number,
                "continueVideosLikeThis":  Number,
                "goodExamples":  Number,
                "goodExperience":  Number,
                "haveCommitment":  Number,
                "interesting":  Number,
                "likeDidactics":  Number,
                "longVideo":  Number,
                "moreDynamic":  Number,
                "noPause":  Number,
                "previousKnowledge":  Number,
                "recommendVideo": Number,
                "tooMuchContent":  Number,
            }]
        """

        for id, person in enumerate(self.data_set['dataset']):
            average_anger = 0
            average_contempt = 0
            average_disgust = 0
            average_fear = 0
            average_happiness = 0
            average_neutral = 0
            average_sadness = 0
            average_surprise = 0

            emotions = person['emotions']
            for idx, emotion in enumerate(emotions):

                if len(emotion.keys()) == 0:
                    continue

                average_anger += emotion['anger']
                average_contempt += emotion['contempt']
                average_disgust += emotion['disgust']
                average_happiness += emotion['happiness']
                average_neutral += emotion['neutral']
                average_sadness += emotion['sadness']
                average_surprise += emotion['surprise']

            emotions_size = len(emotions)

            average_anger /= emotions_size
            average_contempt /= emotions_size
            average_fear /= emotions_size
            average_disgust /= emotions_size
            average_happiness /= emotions_size
            average_neutral /= emotions_size
            average_sadness /= emotions_size
            average_surprise /= emotions_size

            person['averageAnger'] = average_anger
            person['averageContempt'] = average_contempt
            person['averageFear'] = average_fear
            person['averageDisgust'] = average_disgust
            person['averageHappiness'] = average_happiness
            person['averageNeutral'] = average_neutral
            person['averageSadness'] = average_sadness
            person['averageSurprise'] = average_surprise

            del person['emotions']
        print(self.data_set)

testing = Data()
# print(testing.data_set)
testing.get_average_of_emotions()
