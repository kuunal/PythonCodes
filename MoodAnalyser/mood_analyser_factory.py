from exceptions.mood_analyser_exceptions import MoodAnalyserError

class MoodAnalyserFactory:

    # returns mood object of given package and class name  
    def return_mood_analyser_object(self, filename, classname, *parameters):
        try:
            mood_class = __import__(filename)
            mood_class = getattr(mood_class, classname)
        except (ModuleNotFoundError, AttributeError):
            raise MoodAnalyserError("Classname or package name is invalid!","INVALID_CLASS_OR_PACKAGE_EXCEPTION")
        else:
            if(len(parameters)==0):
                return mood_class()
            else:
                return mood_class(parameters[0])

    # call methods of given class 
    def invoke_methods(self, mood_object , methodname, *parameters):
        try:
            method = getattr(mood_object,methodname)
        except AttributeError:
            raise MoodAnalyserError("Invalid method name","INVALID_METHOD_EXCEPTION")
        else:
            return method()

    # changes attributes(variables) of given class 
    def change_fields_values(self, mood_object, methodname, fieldname, value):
        try:
            getattr(mood_object,fieldname)
        except AttributeError:
            raise MoodAnalyserError("No such field found","NO_SUCH_FIELD_EXCEPTION")
        else:
            setattr(mood_object,fieldname,value)
            return self.invoke_methods(mood_object,methodname)