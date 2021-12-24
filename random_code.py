class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
    
    def encode(self, text):
        returnstring = ''
        key2 = self.key
        if len(self.key) < len(text):
            for i in range(len(text)- len(self.key)):
                key2 += key2[i]
        for i in range(len(text)):
            if text[i] in self.alphabet:
                if self.alphabet.index(text[i]) + self.alphabet.index(key2[i]) < (len(self.alphabet)-1):
                    returnstring += self.alphabet[self.alphabet.index(text[i]) + self.alphabet.index(key2[i])]
                else:
                    returnstring += self.alphabet[(self.alphabet.index(text[i]) + self.alphabet.index(key2[i]))-len(self.alphabet)]
            else:
                returnstring += text[i]
        return(returnstring)


    def decode(self, text):
        returnstring = ''
        key2 = self.key
        if len(self.key) < len(text):
            for i in range(len(text)- len(self.key)):
                key2 += (key2)
        for i in range(len(text)):
            if text[i] in self.alphabet:
                if self.alphabet.index(text[i]) - self.alphabet.index(key2[i]) > -1:
                    returnstring += self.alphabet[self.alphabet.index(text[i]) - self.alphabet.index(key2[i])]
                else:
                    returnstring += self.alphabet[(len(self.alphabet)) - (self.alphabet.index(key2[i]) - self.alphabet.index(text[i]))]
            else:
                returnstring += text[i]
        return(returnstring)


