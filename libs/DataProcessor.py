import spacy
import nltk
import re
nltk.download('punkt')

from string import punctuation
from nltk.corpus import stopwords
from autocorrect import Speller
from spacy.lang.en import English

class DataProcessor:
    IS_DEBUG = False

    # TODO: remove stop word and stemming

    def _myprint(self, mylist):
        for item in mylist:
            print(item)

    def preProcess(self, text):
        tokens = self._tokenize(text)
        normalised = self._normalise(tokens)
        collected = self._spellCollect(normalised)
        if self.IS_DEBUG: self._myprint(collected)
        return collected

    # Tokenization
    def _tokenize(self, text):
        nlp = spacy.load('en_core_web_sm', disable=['ner'])
        return nlp(text)

    # Normalisation
    def _normalise(self, tokens):
        normalized = list()
        for token in tokens:
            # If word is "is, am, are" or "I", just leave it.
            if (token.lemma_ == "be" or token.text == "I"):
                normalized.append(token.text)

            # If word is shorten, turn the word in full word
            elif (token.text == "n't" or token.text == "'ll"):
                normalized.append(token.lemma_)

            # token is alphabetic characters
            elif (token.is_alpha):
                # If token is pronoun, lower token by token.lower_
                lemma = token.lemma_.lower().strip() if token.lemma_ != "-PRON-" else token.lower_
                normalized.append(lemma)

            # Special characters
            else:
                normalized.append(token.text)
        return normalized

    def _spellCollect(self, token):
        spell = Speller(lang='en')
        corrected = list()
        pattern = re.compile(r"(.)\1{2,}")

        for word in token:
            # Remove repeated alphabet that more than 2 characters
            _word = pattern.sub(r"\1\1", word)

            # Check spelling
            corrected.append(spell(_word))

        return corrected
