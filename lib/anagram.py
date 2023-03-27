
# your code goes here!
class Anagram():

    def __init__(self, word):
        self.word = word
        self.listed_word = sorted(word)

    def match(self, words):
        anagram = []
        for word in words:
            if self.listed_word == sorted(list(word)):
                anagram.append(word)
            else:
                pass
        return anagram

listen = Anagram("listen")
listen.match(['enlists', 'google', 'inlets', 'banana'])
