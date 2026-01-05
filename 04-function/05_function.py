# documenting a function

def display(name):
    '''
    this function will return the name with greeting message
    '''
    return f"Good morning, {name}"


name = display('Kc')
print(display.__doc__)
print(display.__name__)
print(name)
