import base

class Quote(base):
    def __init__(self, *args, **kwargs):
        self.quotes = [
            "something something",
            "something else",
            "Some important quote",
            "Some less important quote"
        ]
        self.command = "quote"
        super(Quote, self).__init__(*args, **kwargs)
  
    def message_received(self, status, msg):
        msg.Chat.SendMessage(random.choice(self.quotes))



