# Event Driven Programming - Chatbot
A chatbot is a perfect way to demonstrate event driven programming since we can't dictate in advance the "correct" sequence of statements a chatbot should make.

Instead, a chatbot should respond to "events" which come in the form of messages from the chatbot's conversation partner.

## Goals for this activity
* (re)familiarize yourself with how Python handles classes and object oriented programming.
* gain familiarity with what types of problems event driven programming is good for.
* write simple code that works within this event driven framework

## TODO 1 - Read through and understand the `EventDrivenChatBot` class
Read through the code below until you have a prediction for what will happen when you execute this code by pressing the Test Run button.

***NOTE - the last few lines of the code below is where the EventDrivenChatBot class is instantiated and its methods are called.***

```python

from datetime import datetime
import time

class EventDrivenChatBot:
    
    def __init__(self):
        # accepted_messages maps incoming messages to 
        # list of callback functions
        self.accepted_messages = {}
        
        # time of instantiation
        self.birth_time = datetime.now()
        
        # "registering" all callbacks
        self.register_callback("hi", 
                               self.respond_to_greeting)
        self.register_callback("bye", 
                               self.respond_to_departure)
        self.register_callback("age?",
                               self.respond_to_age_request)
        self.register_callback("age?",
                               self.respond_to_age_request_detailed)
    
    def register_callback(self, message, callback):
        """
        Registers a callback to a message.
        """
        if message not in self.accepted_messages:
            self.accepted_messages[message] = []
        self.accepted_messages[message].append(callback)
        
    def respond_to_greeting(self):
        print("Hello!")
        
    def respond_to_departure(self):
        print("Nice chatting with you!")
            
    def respond_to_age_request(self):
        age = datetime.now() - self.birth_time
        print("I am", age.seconds, "seconds old.")
        
    def respond_to_age_request_detailed(self):
        age = datetime.now() - self.birth_time
        micros = age.microseconds
        print("Technically, I'm", age.seconds, "seconds and", 
              micros, "microseconds old")
        
    def handle_message(self, message):
        if message not in self.accepted_messages:
            print("sorry, I don't understand", message)
        else:
            callbacks = self.accepted_messages[message]
            for callback in callbacks:
                callback() 
                
bot = EventDrivenChatBot()
bot.handle_message("hi")
time.sleep(2.2)
bot.handle_message("age?")
bot.handle_message("bye")

```

## References:
Matrials fully belongs to udacity
