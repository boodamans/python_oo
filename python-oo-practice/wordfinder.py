"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Machine for finding random words from dictionary.
    
    >>> wf = WordFinder(words.txt)
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """

    def __init__(self, filepath):
        self.filepath = filepath
        file = open(self.filepath)
        self.wordlist = file.readlines()
        self.res = []
        for word in self.wordlist:
            self.res.append(word.replace('\n', ''))
        print(f'{len(self.res)} words read')
        self.word = (self.res[random.randint(0,len(self.res))])

    def random(self):
        return (self.res[random.randint(0,len(self.res))])

class SpecializedWordFiner(WordFinder):
    
    def parse(self, dictfile):
        return [word.strip() for word in dictfile if word.strip() and not word.startswith('#')]