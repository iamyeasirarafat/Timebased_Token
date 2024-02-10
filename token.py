from datetime import datetime, timedelta
import time

class Token:
    def __init__(self, secret):
        self.secret = secret
        self.dict, self.sum = self.count()

    def count(self):
        _dict = {}
        i = 0
        for c in self.secret:
            _dict[c] = i
            i += 1
        return _dict, sum(_dict.values())

    def timeToken(self, i):
        now = datetime.utcnow()
        if i < 0:
            i = abs(i)
            now -= timedelta(minutes=i)
        else:
            now += timedelta(minutes=i)
        month = now.month
        day = now.day
        hour = now.hour
        min = now.minute
        sec = now.second
        total = month+day+hour+min+sec
        return total

    def generate(self):
        return self.timeToken(0)*self.sum

    def generate_for_check(self, distance=3):
        tokens = []
        for i in range(-distance, 1):
            tokens.append(self.timeToken(i)*self.sum)
        return tokens

    def verify(self, token):
        tokens = self.generate_for_check(distance=3)
        print(tokens)
        return token in tokens

tk = Token("87ADB446E4B5727AD6F47B8DFB7C6")
print(_token:=tk.generate())
time.sleep(1)
print(tk.verify(token=_token))