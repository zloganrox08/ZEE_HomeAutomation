# Replace all instances of the following:
# - "ClassTemplate"
# - "function1"



import os

class ClassTemplate() :
    # Toggle each logging type for this class
    # 0 - Do not log this type
    # 1 - Log this type

    # Typedefs
    ## Success - A message of a milestone hit or risky chunk of code completed successfully
    ## Error - There is something wrong and execution should stop on this area
    ## Debug - Information that would help if something is wrong
    ## Info - Information that a user would like to know
    ## ZEE_Stack - Stack trace to help with debug
    
    logging_toggles = {
        "Success": 1,
        "Error": 1,
        "Debug": 1,
        "Info": 1,
        "ZEE_Stack": 1
    }
    debugLogger = None

    # Variables

    def __init__(self) :
        #DEBUG
        from ..GlobalLibrary import DebugLogging
        self.debugLogger = DebugLogging.DebugLogging("ClassTemplate")
        if self.logging_toggles["ZEE_Stack"] :
            self.debugLogger.log_ZEE_Stack(text="__init__ start")
        if self.logging_toggles["Debug"] :
            self.debugLogger.log_debug(text="__init__ start") # Recommend to log input parameters
        try :
            # End of Header

            pass

            # Begin of Footer
        except BaseException as e :
            if self.logging_toggles["Error"] :
                logstring = str(e) + "," + str(e.__context__) + str(e.with_traceback)
                self.debugLogger.log_error(text=logstring)
        
        if self.logging_toggles["ZEE_Stack"] :
            self.debugLogger.log_ZEE_Stack(text="__init__ end")
    
    def function1(self):
        if self.logging_toggles["ZEE_Stack"] :
            self.debugLogger.log_ZEE_Stack(text="function1 start")
        if self.logging_toggles["Debug"] :
            self.debugLogger.log_debug(text="__init__ start") # Recommend to log input parameters
        try :
            # End of header

            pass

            # Begin of Footer
        except BaseException as e :
            if self.logging_toggles["Error"] :
                logstring = str(e) + "," + str(e.__context__) + str(e.with_traceback)
                self.debugLogger.log_error(text=logstring)
        
        if self.logging_toggles["ZEE_Stack"] :
            self.debugLogger.log_ZEE_Stack(text="function1 end")