import time

def countdown(t):
    while t:
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Let's Begin!")

print("""Welcome to the Pomodoro Timer! 
The Pomodoro Technique was developed in the late 1980s by Francesco Cirillo and is modelled after a typical cooking alarm.
The concept of this technique is to break down complex projects and devote a set length of time to focused study time, taking incremental breaks inbetween.
The name was inspired by the kitchen alarm that Francesco used to time himself that was shaped like a Pomodoro, which is Italian for Tomato.
More information about the Pomodoro Technique is available on https://francescocirillo.com/products/the-pomodoro-technique

In this program, you are able to set a custom time for your pomodoro and break sessions in minutes. A typical Pomodoro session will last 25 minutes, with a 5 minute break inbetween.
This program will time you through 4 pomodoro sessions.""")
t = input("To begin, please enter a time in seconds to count down to before beginning your Pomodoro: ")

countdown(int(t))

def pomodoro():
    pom = int(input("Enter the pomodoro session length in minutes (default is 25): "))
    breakTime = int(input("Enter the break length in minutes (default is 5): "))

    if pom <= 0:
        pom = 25
    elif breakTime <= 0:
        breakTime = 5
    elif pom <= 0 & breakTime <=0:
        pom = 25
        breakTime = 5

    print("The pomodoro timer has started, start working!")
    count = 0
    for i in range(4):
        t = pom*60
        while t:
            mins = t // 60
            secs = t % 60
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        i += 1

        print(f"""Well done on getting through Pomodoro {i}. Your break has now started. 
Take a walk, drink some water or refill your bottle before the start of the next session""")

        t = breakTime*60
        while t:
            mins = t // 60
            secs = t % 60
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        if i == 4:
            print("You have reached the end of your pomodoro sessions. How did you do? Thank you for using the program!")
        else:
            print("You have completed " + str(i) + " pomodoros so far! There are " + str(4 - i) + " remaining.")
            time.sleep(2)
            print("Your break has ended. Pomodoro number " + str(i + 1) + " is about to begin!")
            time.sleep(2)
            print("Starting now!")
    
pomodoro()