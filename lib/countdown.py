import time

def countdown(arg):
    while arg >0:
        print(f'{arg} SECOND(S)!')
        arg=arg-1
    print("HAPPY NEW YEAR!")


def countdown_with_sleep(arg):
    while arg >0:
        print(f'{arg} SECOND(S)!')
        arg=arg-1
        time.sleep(1)
    print("HAPPY NEW YEAR!")