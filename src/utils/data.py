

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

    def __init__(self, dataset):
        self.dataset = dataset

    def clean_dataset(self):
        return self.dataset

    @staticmethod
    def get_average_of_emotions(dataset):
        """
          [{
                "averageEmotions":  Number,
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
        for person in dataset:
            
        return 0
