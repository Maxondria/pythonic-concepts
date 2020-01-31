try:
    # Try something()
    pass
except Exception as e:
    '''Exception:
        For any caught exception, it will be caught!
        If the Exception was specified eg FileNotFoundError, it will be caught, else,
        it will be pushed to the 'else' block below

        This block can be repeated for 'n' number of specifications to be caught,
        Remember to put specific ones on top and Exception as last except block
    '''
    # print(e)
    pass
else:
    '''Else:
        Excecuted if no exceptions were caught
    '''
    pass
finally:
    '''finally:
        Happens regardlessly  
    '''
    pass
