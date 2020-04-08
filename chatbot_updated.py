from datetime import time
import time

class EventDrivenChatBot:
    def __init__(self):
        self.accepted_messages = {}
        self.register_callback('hi',self.respond_to_greeting)
        self.register_callback('bye',self.respond_to_goodbye)
        self.register_callback('really',self.respond_to_assure)

    def register_callback(self,message,callback):
        if message not in self.accepted_messages:
            self.accepted_messages[message]=[]
        self.accepted_messages[message].append(callback)

    def respond_to_greeting(self):
        print('Hello')

    def respond_to_assure(self):
        print("sure")

    def respond_to_goodbye(self):
        print("Good Bye")

    def handle_message(self,message):
        if message not in self.accepted_messages:
            print('sorry dont understand the message ', message)
        else:
            callbacks = self.accepted_messages[message]
            for callback in callbacks:
                callback()
if __name__=="__main__":
    evd=EventDrivenChatBot()
    evd.handle_message("Hlllldkfj")
    evd.handle_message('bye')
    evd.handle_message('really')