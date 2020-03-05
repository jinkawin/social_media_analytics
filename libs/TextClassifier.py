import numpy as np
import pandas as pd

from .NrcProcess import NrcProcess
class TextClassifier(NrcProcess):

    def __init__(self):
        super().__init__()

    def classify(self, text):
        score = {}
        for word in text:
            print("word: ", word)
            score = self._sumScore(word, score)
            print("score: ", score)
            print("------------------------------------")

        return score

    def _sumScore(self, target, score):
        _score = self.getNrcScore(target)

        # sum 2 dict up
        result = {key: score.get(key, 0) + _score.get(key, 0) for key in set(score) | set(_score)}
        print("result: ")
        self.printDict(result)

        return result