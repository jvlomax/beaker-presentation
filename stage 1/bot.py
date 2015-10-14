import Skype4Py

class SkypeBot(object):
    def __init__(self):

        self.client = Skype4Py.Skype(Events=self)


if __name__ == "__main__":
    bot = SkypeBot()
    bot.client.Attach()
    while 1:
        pass
        

    
