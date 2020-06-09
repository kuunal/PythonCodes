from exceptions.mood_analyser_exceptions import  MoodAnalyserError

class MoodAnalyser:

    def __init__(self, *message):
        if(len(message)>0):
            MoodAnalyser.message=message[0]

    # returns mood based on message    
    def analyse_mood(self, *message):
        if(len(message)>0):
            self.message=message[0]
        self.check_empty(self.message)
        self.check_null(self.message)
        if "happy" in self.message.lower():
            return "Happy"
        elif "sad" in self.message.lower():
            return "Sad"
        
    
    def check_null(self, message):
        if self.message == None:
            raise MoodAnalyserError("Invalid message!","NULL_VALUE_EXCEPTION")            


    def check_empty(self, message):
        if self.message == "":
            raise MoodAnalyserError("Invalid message!","EMPTY_VALUE_EXCEPTION")

    def equals(self, object):
        if self==object or isinstance(object,MoodAnalyser):
            return True
        