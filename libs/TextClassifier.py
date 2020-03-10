import numpy as np
import pandas as pd

from .NrcProcess import NrcProcess
class TextClassifier(NrcProcess):
    IS_DEBUG = False

    def __init__(self):
        super().__init__()

    def classify(self, text):
        score = {}
        for word in text:
            if self.IS_DEBUG: print("word: ", word)
            _score = self.getNrcScore(word)
            score = self.sumScore(_score, score)
            if self.IS_DEBUG: print("score: ", score)
            if self.IS_DEBUG: print("------------------------------------")

        return score