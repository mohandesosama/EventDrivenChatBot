# Event Driven Programming - Chatbot
A chatbot is a perfect way to demonstrate event driven programming since we can't dictate in advance the "correct" sequence of statements a chatbot should make.

Instead, a chatbot should respond to "events" which come in the form of messages from the chatbot's conversation partner.

## Goals for this activity
* (re)familiarize yourself with how Python handles classes and object oriented programming.
* gain familiarity with what types of problems event driven programming is good for.
* write simple code that works within this event driven framework

### TODO 1 - Read through and understand the `EventDrivenChatBot` class
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
### TODO 2 - Run the Code
Run the code above, How does it compare to what you expected to see? What happens between calling the `handle_message` method and actually printing the chatbot's response?

### TODO 3 - Modify the Code
Once you feel like you understand how this code works, modify `EventDrivenChatBo`t so that the FIRST time it receives the message `"age?"` it calls `respond_to_age_request` but all subsequent `"age?"` messages should trigger a call to `respond_to_age_request_detailed`.

## Solution of This activity

The code below is my solution to the last TODO in the previous section. Below that you'll find a video walkthrough of the EventDrivenChatBot code.

### Solution Overview
There are many ways to solve this problem, but most solutions probably involve modeling the "state" of the chatbot as either

* has NOT yet seen the message "age?" OR
* HAS seen the message "age?"

I implemented this by making three modifications...

* In `__init__ I` added a state variable `has_been_asked_age` which is initially set to `False`

* I define a function called `handle_age_request` which in turn calls either `respond_to_age_request` or `respond_to_age_request_detailed` depending on the STATE of the bot.

* Register a callback that associated `handle_age_request` to the `"ask?"` message. Note that I also removed two calls to `register_callback` that were there previously.

```python
from datetime import datetime
import time

class EventDrivenChatBot:
    
    def __init__(self):
        self.accepted_messages = {}
        
        # 1. ADDED THIS "STATE" VARIABLE
        self.has_been_asked_age = False
        
        self.birth_time = datetime.now()
        
        # "registering" all callbacks
        self.register_callback("hi", 
                               self.respond_to_greeting)
        self.register_callback("bye", 
                               self.respond_to_departure)
        
        # 3. USING handle_age_request TO DISPATCH
        #    RESPONSES TO "age?"
        self.register_callback("age?",
                               self.handle_age_request)
    
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
    
    # 2. ADD DISPATCH POINT FOR PROCESSING "age?" MESSAGE
    def handle_age_request(self):
        if not self.has_been_asked_age:
            self.has_been_asked_age = True
            self.respond_to_age_request()
        else:
            self.respond_to_age_request_detailed()
            
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
time.sleep(1.3)
bot.handle_message("age?")
print("---No chatbot, let me ask you that again...")
bot.handle_message("age?")

```
[![event driven chatbot](https://img.youtube.com/vi/f_GPA9ULqJU/0.jpg)](https://www.youtube.com/watch?v=f_GPA9ULqJU)

## References:
This activity fully belongs to udacity
