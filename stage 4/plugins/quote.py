import random
quotes = [
    "something something",
    "something else",
    "Some important quote",
    "Some less important quote"
]

def give_quote(msg)
    msg.Chat.SendMessage(random.choice(quotes))
