class Verb:
    def __init__(self, inf:str, PastSimple:str, PastPart:str, Translate:str):
        self.inf = inf
        self.PastSimple = PastSimple
        self.PastPart = PastPart
        self.Translate = Translate

Array = []

with open('verbs/verbs.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.replace('\n', '')
        temp = line.split(' ')
        verb = Verb(temp[0], temp[1], temp[2], temp[3])
        Array.append(verb)
        