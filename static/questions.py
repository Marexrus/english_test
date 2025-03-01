class Question:
    def __init__(self, english:str, russian:str, answer:str):
        self.english = english
        self.russian = russian
        self.answer = answer

Questions_mixed = [
    # Present Simple
    Question("I ___ to school every day.", "Я хожу в школу каждый день.", "go"),
    Question("She ___ a book every evening.", "Она читает книгу каждый вечер.", "reads"),
    Question("They ___ football on weekends.", "Они играют в футбол по выходным.", "play"),
    Question("He ___ his homework after school.", "Он делает домашнюю работу после школы.", "does"),
    Question("We ___ to the park on Sundays.", "Мы ходим в парк по воскресеньям.", "go"),
    Question("You ___ coffee in the morning.", "Ты пьешь кофе утром.", "drink"),
    Question("It ___ a lot in this region.", "Здесь часто идет дождь.", "rains"),
    Question("She ___ to music every day.", "Она слушает музыку каждый день.", "listens"),
    Question("They ___ English at school.", "Они учат английский в школе.", "study"),
    Question("He ___ his bike to work.", "Он ездит на работу на велосипеде.", "rides"),

    # Past Simple
    Question("I ___ to the store yesterday.", "Я ходил в магазин вчера.", "went"),
    Question("She ___ a cake last night.", "Она испекла торт прошлой ночью.", "made"),
    Question("They ___ to the cinema last weekend.", "Они ходили в кино на прошлых выходных.", "went"),
    Question("He ___ his keys at home.", "Он забыл свои ключи дома.", "left"),
    Question("We ___ a great time at the party.", "Мы отлично провели время на вечеринке.", "had"),
    Question("You ___ the door open.", "Ты оставил дверь открытой.", "left"),
    Question("It ___ a lot last week.", "На прошлой неделе часто шел дождь.", "rained"),
    Question("She ___ her phone at home.", "Она забыла свой телефон дома.", "left"),
    Question("They ___ the movie last night.", "Они смотрели фильм прошлой ночью.", "saw"),
    Question("He ___ his homework yesterday.", "Он сделал домашнюю работу вчера.", "did"),

    # Present Perfect
    Question("I ___ already ___ my homework.", "Я уже сделал домашнюю работу.", "have done"),
    Question("She ___ just ___ a new book.", "Она только что прочитала новую книгу.", "has read"),
    Question("They ___ already ___ the movie.", "Они уже посмотрели фильм.", "have seen"),
    Question("He ___ never ___ to Paris.", "Он никогда не был в Париже.", "has been"),
    Question("We ___ just ___ the dishes.", "Мы только что помыли посуду.", "have washed"),
    Question("You ___ already ___ the letter.", "Ты уже написал письмо.", "have written"),
    Question("It ___ just ___ raining.", "Дождь только что закончился.", "has stopped"),
    Question("She ___ already ___ her breakfast.", "Она уже позавтракала.", "has eaten"),
    Question("They ___ never ___ sushi.", "Они никогда не ели суши.", "have eaten"),
    Question("He ___ just ___ the door.", "Он только что закрыл дверь.", "has closed")
]        