import time
import os
from turtle import clear 

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def countdown(t):
    while t:
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Let's Begin!")

print("""
Welcome to the Pomodoro Timer! 
The Pomodoro Technique was developed in the late 1980s by Francesco Cirillo.
The name was inspired by the kitchen alarm that Francesco used to time himself that was shaped like a Pomodoro, which is Italian for Tomato.

This technique breaks down complex projects, allowing you to devote a set length of time to focused study time and taking incremental breaks inbetween.
More information about the Pomodoro Technique is available on https://francescocirillo.com/products/the-pomodoro-technique
""")

time.sleep(5)

print("""
In this program, you are able to set a custom time for your pomodoro and break sessions in minutes. 
A typical Pomodoro session will last 25 minutes, with a 5 minute break inbetween.
""")

t = input("To begin, please enter a time in seconds to count down to before beginning your Pomodoro: ")

countdown(int(t))

def pomodoro():
    clearScreen()
    pom = int(input("Enter the pomodoro session length in minutes (default is 25): "))
    breakTime = int(input("Enter the break length in minutes (default is 5): "))
    sessions = int(input("Enter the amount of pomodoro sessions you'd like to do today (default is 4): "))
    if pom <= 0:
        pom = 25
    elif breakTime <= 0:
        breakTime = 5
    elif sessions <= 0:
        sessions = 4
    elif pom <= 0 & breakTime <= 0 & sessions <= 0:
        pom = 25
        breakTime = 5
        sessions = 4

    print("The pomodoro timer has started, start working!")
    for i in range(sessions):
        t = pom*60
        while t:
            mins = t // 60
            secs = t % 60
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        i += 1
        clearScreen()
        print(f"""Well done on getting through Pomodoro {i}. Your break has now started. 
Take a walk, stretch, drink some water or refill before the start of the next session""")

        t = breakTime*60
        while t:
            mins = t // 60
            secs = t % 60
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        if i == sessions:
            print("You have reached the end of your pomodoro sessions. How did you do? Thank you for using the program!")
        else:
            clearScreen()
            print("You have completed " + str(i) + " pomodoros so far! There are " + str(sessions - i) + " remaining.")
            time.sleep(5)
            print("Your break has ended. Pomodoro number " + str(i + 1) + " is about to begin!")
            time.sleep(5)
            print("Starting now!")
    
pomodoro()