import json
import csv


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

    def treat_dataset(self):
        self.get_average_of_emotions()
        self.get_commitment_by_questions()
        self.clean_data()
        self.export_as_csv()
        return self.data_set

    def export_as_csv(self):
        data = self.data_set['dataset']
        keys = data[0].keys()

        with open('dataset.csv', 'w') as f:
            dict_writer = csv.DictWriter(f, keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)

    def clean_data(self):
        for person in self.data_set['dataset']:
            del person['classLink']
            del person['name']
            del person['grade']
            del person['__v']

    def get_commitment_by_questions(self):
        commitment_weight = 3
        subject_weight = 2
        didactics_weight = 1
        rythm_weight = 1
        qt_questions_used = 7

        total_sum = commitment_weight + subject_weight + didactics_weight + rythm_weight

        for person in self.data_set['dataset']:
            sum_commitment = person['continueVideosLikeThis'] + person['goodExperience'] + person['haveCommitment']
            sum_subject = person['interesting']
            sum_didactics = person['likeDidactics'] + person['goodExamples']
            sum_rythm = person['noPause']

            commitment_score = ((commitment_weight * sum_commitment) +
                                (subject_weight * sum_subject) +
                                (didactics_weight * sum_didactics) +
                                (rythm_weight * sum_rythm))

            person['commitment_score'] = (commitment_score / total_sum) * (1.0/qt_questions_used)

            del person['attention']
            del person['continueVideosLikeThis']
            del person['goodExamples']
            del person['goodExperience']
            del person['haveCommitment']
            del person['interesting']
            del person['likeDidactics']
            del person['longVideo']
            del person['moreDynamic']
            del person['noPause']
            del person['previousKnowledge']
            del person['recommendVideo']
            del person['tooMuchContent']

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

            person['average_anger'] = average_anger
            person['average_contempt'] = average_contempt
            person['average_fear'] = average_fear
            person['average_disgust'] = average_disgust
            person['average_happiness'] = average_happiness
            person['average_neutral'] = average_neutral
            person['average_sadness'] = average_sadness
            person['average_surprise'] = average_surprise

            del person['emotions']
        # print(self.data_set)


testing = Data()
testing.treat_dataset()
