import numpy as np
import pandas as pd

from .NrcProcess import NrcProcess
class TextClassifier(NrcProcess):

    def __init__(self):
        super().__init__()

    def classify(self, text):
        score = {}
        for word in text:
            # print("word: ", word)
            _score = self.getNrcScore(word)
            score = self.sumScore(_score, score)
            # print("score: ", score)
            # print("------------------------------------")

        return score