import spacy
import nltk
import re
# nltk.download('punkt')

from string import punctuation
from nltk.corpus import stopwords
from autocorrect import spell
from spacy.lang.en import English

class DataProcessor:

    def _myprint(self, mylist):
        for item in mylist:
            print(item)

    def preProcess(self, text):
        tokens = self._tokenize(text)
        normalised = self._normalise(tokens)
        collected = self._spellCollect(normalised)
        self._myprint(collected)
        return collected

    # Tokenization
    def _tokenize(self, text):
        nlp = spacy.load('en_core_web_sm', disable=['ner'])
        return nlp(text)

    def _normalise(self, tokens):
        normalized = list()
        for token in tokens:
            if (token.lemma_ == "be" or token.text == "I"):
                normalized.append(token.text)
            elif (token.text == "n't"):
                normalized.append(token.lemma_)
            elif (token.is_alpha):
                lemma = token.lemma_.lower().strip() if token.lemma_ != "-PRON-" else token.lower_
                normalized.append(lemma)
            else:
                normalized.append(token.text)
        return normalized

    def _spellCollect(self, token):
        corrected = list()
        pattern = re.compile(r"(.)\1{2,}")

        for word in token:
            # Remove repeated alphabet that more than 2 characters
            _word = pattern.sub(r"\1\1", word)

            # Check spelling
            corrected.append(spell(_word))

        return corrected
