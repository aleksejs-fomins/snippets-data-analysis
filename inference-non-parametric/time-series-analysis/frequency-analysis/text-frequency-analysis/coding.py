

# Return frequencies of all characters in the text
def freq_dict(text):
    return {c: text.count(c) for c in set(text)}


class ShannonFanoCode:
    def __init__(self):
        self.buf = ""
        self.m = {}

    def encode(self, text):
        # Get frequency distribution
        self.distr = freq_dict(text)

        # Construct mapping
        # TODO: Shannon-fano code here
        self.m = {}
        self.mInv = {v:k for k, v in self.m.items()}

        # Map text
        return ''.join([self.m[c] for c in text])

    def _decode_char(self, c):
        # TODO: Raise error if buf will not match anything
        # TODO: Optimization: traverse tree, instead of comparing with all every char

        self.buf += c
        if self.buf in self.mInv.keys():
            rez = self.mInv[self.buf]
            self.buf = ""
            return rez
        else:
            return ""

    def decode(self, text):
        return ''.join([self._decode_char(c) for c in text])
        # TODO: Raise error if buffer non-empty at the end
