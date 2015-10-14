from datetime import datetime


def give_time(msg):
    msg.Chat.SendMessage("The time is {}".format(datetime.now())
