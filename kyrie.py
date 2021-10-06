# by billythegoat356

strings = "abcdefghijklmnopqrstuvwxyz0123456789"  # ne pas changer svp
base = 356  # ne pas changer svp


class Kyrie():

    def encrypt(e: str):
        e = Kyrie._ekyrie(e)
        return Kyrie._encrypt(e)

    def decrypt(e: str):
        text = Kyrie._decrypt(e)
        return Kyrie._dkyrie(text)

    def _ekyrie(text: str):

        r = ""
        for a in text:
            if a in strings:
                a = strings[strings.index(a)-1]
            r += a
        return r

    def _dkyrie(text: str):
        r = ""
        for a in text:
            if a in strings:
                i = strings.index(a)+1
                if i >= len(strings):
                    i = 0
                a = strings[i]
            r += a
        return r

    def _encrypt(text: str, key: str = None):
        if key is None:
            key = base
        if type(key) == str:
            key = sum(ord(i) for i in key)
        t = [chr(ord(t)+key)if t != "\n" else "ζ" for t in text]
        return "".join(t)

    def _decrypt(text: str, key: str = None):
        if key is None:
            key = base
        if type(key) == str:
            key = sum(ord(i) for i in key)
        return "".join(chr(ord(t)-key) if t != "ζ" else "\n" for t in text)


class Key:

    def encrypt(e: str, key: str):
        e1 = Kyrie._ekyrie(e)
        return Kyrie._encrypt(e1, key=key)

    def decrypt(e: str, key: str):
        text = Kyrie._decrypt(e, key=key)
        return Kyrie._dkyrie(text)


# text = "Kyrie Eleison"
# key = strings

# print("CRYPTER: " + Kyrie.decrypt(Kyrie.encrypt(text)) + " -> " + Kyrie.encrypt(text))
# print("CHIFFRER: " + Key.decrypt(Key.encrypt(text, key=key), key=key) + " -> " + Key.encrypt(text, key=key))

"""
# CRYPTER: Kyrie Eleison -> ƯǜǕǌǈƄƩǏǈǌǖǒǑ
# CHIFFRER: Kyrie Eleison -> ൷ඤඝඔඐൌ൱඗ඐඔඞක඙
"""
