from hide_frames import hide_frame

def shout(func):
    @hide_frame
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

def repeat(num):
    def decorator(func):
        @hide_frame
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) * num
        return wrapper
    return decorator

@shout
@repeat(3)
def greet(name):
    return "Hello " + name + "\n"

print(greet(1))
# oops... should be a string
# the traceback would be ugly with all these wrappers
# BUT! we have hide_frame
# it's like the wrappers don't even exist!
