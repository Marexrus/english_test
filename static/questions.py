class Question:
    def __init__(self, english:str, russian:str, answer:str):
        self.english = english
        self.russian = russian
        self.answer = answer

Questions_inf = [
    Question("I ___ to school every day.", "Я хожу в школу каждый день.", "go"),
    Question("She ___ a book right now.", "Она читает книгу прямо сейчас.", "is reading"),
    Question("They ___ pizza for dinner yesterday.", "Они заказали пиццу на ужин вчера.", "ordered"),
    Question("We ___ to the beach last weekend.", "Мы ездили на пляж на прошлых выходных.", "went"),
    Question("He ___ his homework every evening.", "Он делает домашнее задание каждый вечер.", "does"),
    Question("I ___ never ___ to Paris.", "Я никогда не был в Париже.", "have been"),
    Question("The sun ___ in the east.", "Солнце встает на востоке.", "rises"),
    Question("She ___ to the gym three times a week.", "Она ходит в спортзал три раза в неделю.", "goes"),
    Question("They ___ a new car next month.", "Они купят новую машину в следующем месяце.", "will buy"),
    Question("I ___ my keys at home this morning.", "Я забыл свои ключи дома сегодня утром.", "left"),
    Question("He ___ his phone while he was running.", "Он уронил свой телефон, когда бежал.", "dropped"),
    Question("We ___ the movie last night.", "Мы смотрели фильм прошлой ночью.", "watched"),
    Question("She ___ to the party if she has time.", "Она пойдет на вечеринку, если у нее будет время.", "will go"),
    Question("I ___ already ___ my breakfast.", "Я уже позавтракал.", "have eaten"),
    Question("They ___ playing football in the park.", "Они играют в футбол в парке.", "are")
]

Questions_past_simple = [
    Question("I ___ to the park yesterday.", "Я ходил в парк вчера.", "went"),
    Question("She ___ a cake for her birthday.", "Она испекла торт на свой день рождения.", "baked"),
    Question("They ___ football last weekend.", "Они играли в футбол на прошлых выходных.", "played"),
    Question("We ___ a movie last night.", "Мы смотрели фильм прошлой ночью.", "watched"),
    Question("He ___ his homework after school.", "Он сделал домашнее задание после школы.", "did"),
    Question("I ___ my keys on the table this morning.", "Я оставил свои ключи на столе сегодня утром.", "left"),
    Question("She ___ to the store to buy some milk.", "Она пошла в магазин купить молока.", "went"),
    Question("They ___ their grandparents last summer.", "Они навещали своих бабушку и дедушку прошлым летом.", "visited"),
    Question("We ___ a lot of photos during our trip.", "Мы сделали много фотографий во время нашей поездки.", "took"),
    Question("He ___ his bike to school yesterday.", "Он ехал на велосипеде в школу вчера.", "rode"),
    Question("I ___ a letter to my friend last week.", "Я написал письмо своему другу на прошлой неделе.", "wrote"),
    Question("She ___ her phone at home this morning.", "Она забыла свой телефон дома сегодня утром.", "forgot"),
    Question("They ___ the bus to get to the city center.", "Они сели на автобус, чтобы добраться до центра города.", "took"),
    Question("We ___ dinner at a nice restaurant last night.", "Мы ужинали в хорошем ресторане прошлой ночью.", "had"),
    Question("He ___ his room before the guests arrived.", "Он убрал свою комнату до прихода гостей.", "cleaned")
]

Questions_past_participle = [
    Question("I have ___ the book.", "Я прочитал книгу.", "read"),
    Question("She has ___ her homework.", "Она сделала домашнее задание.", "done"),
    Question("They have ___ to Paris.", "Они ездили в Париж.", "been"),
    Question("We have ___ the movie.", "Мы посмотрели фильм.", "watched"),
    Question("He has ___ his keys.", "Он потерял свои ключи.", "lost"),
    Question("I have never ___ sushi.", "Я никогда не пробовал суши.", "tried"),
    Question("She has ___ a new car.", "Она купила новую машину.", "bought"),
    Question("They have ___ the project.", "Они завершили проект.", "completed"),
    Question("We have ___ the cake.", "Мы испекли торт.", "baked"),
    Question("He has ___ his room.", "Он убрал свою комнату.", "cleaned"),
    Question("I have ___ the letter.", "Я написал письмо.", "written"),
    Question("She has ___ the flowers.", "Она сорвала цветы.", "picked"),
    Question("They have ___ the game.", "Они выиграли игру.", "won"),
    Question("We have ___ the news.", "Мы услышали новости.", "heard"),
    Question("He has ___ his phone.", "Он сломал свой телефон.", "broken")
]
        