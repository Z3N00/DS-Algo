def announce(f):
    def wrapper():
        print("Adding a new function")
        f()
        print("closing a function")
    return wrapper

@announce
def hello():
    print("Hello world")

hello()