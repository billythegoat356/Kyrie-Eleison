from random import choice, randint

strings = "abcdefghijklmnopqrstuvwxyz0123456789"




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

    def _encrypt(text: str):
        t = [chr(ord(t)+5)if t != "\n" else "\n" for t in text]
        return "".join(
            "".join(choice(strings) for _ in range(4)) + i
            for i in t)



    def _decrypt(text: str):
        n = 4
        t = r = ""
        while True:
            if len(text) <= n:
                break
            t = text[n]
            text = text[n+1:]
            r += chr(ord(t)-5) if t != "\n" else "\n"
        return r



class Key:

    def encrypt(e: str, key: str):
        e1 = Kyrie._ekyrie(e)
        return Key._encrypt(e1, key=key)

    def decrypt(e: str, key: str):
        text = Key._decrypt(e, key=key)
        return Kyrie._dkyrie(text)


    def _encrypt(text: str, key: str):
        n = sum(ord(i) for i in key)
        while True:
            if n % 4 == 0:
                break
            n += 1
        d = 3
        t = [chr(ord(t)+d) if t != "\n" else "\n" for t in text]
        return "".join(
            "".join(choice(strings) for _ in range(n)) + i
            for i, _ in zip(t, range(len(t)))
        )

    def _decrypt(text: str, key: str):

        n = sum(ord(i) for i in key)
        while True:
            if n % 4 == 0:
                break
            n += 1
        d = 3
        t = ""
        r = ""
        while True:
            if len(text) <= n:
                break
            t = text[n]
            text = text[n+1:]
            r += chr(ord(t)-d) if t != "\n" else "\n"
        return r
