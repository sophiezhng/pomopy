#!/usr/bin/env python

# Built-in modules
import os
import json
import readline
import threading 
import time

# Require install
from playsound import playsound

# Custom Python Modules
from colors import *
from pomohelp import *
from file_management import *
from pomotimer import *

# Global Variables
timer = None
data = None
work_interval = None

# Main Function
def main():
    global timer
    global data
    global work_interval
    
    print("\n"+colors.BOLD + "Hello, welcome to..." + colors.RESET)
    print_file("banner.txt", colors.RED)
    print(color_text(colors.GREEN,"POM-OH-PIE")+": The Terminal Pomodoro Timer")
    print("❤")
    print(colors.RESET+"Enter `"+color_text(colors.CYAN,"help")+"` for a list of commands.")
    

    readline.parse_and_bind('tab: complete')
    readline.parse_and_bind('set editing-mode vi')

    # while loop repeats looking for commands as input
    while True:
        cmd = input().strip().lower()
        # Start Timer from "beginning" 
        if cmd.startswith("start"):
            if timer == None:
                args = cmd.split(' ')
                data = json.load(open("preferences.json", "r"))
                print("Starting Pomodoro for a...")
                print(color_text(colors.BLUE,str(data['work'])+" minute work period and a "+str(data['break'])+" minute break"))
                if len(args) == 1 and data['auto']:
                    work_interval = False
                elif len(args) == 1 and not data['auto']:
                    print("Auto has been turned off. Please specify `"+color_text(colors.CYAN,"start work")+"` or `"+color_text(colors.CYAN,"start break")+"`.", end='')
                    print(" Or turn auto back on with `"+color_text(colors.CYAN, "auto on")+"`.")
                    continue
                elif args[1] == "work":
                    work_interval = False
                elif args[1] == "break":
                    work_interval = True
                else:
                    print("Did you mean `"+color_text(colors.CYAN, "start")+"`, `"+color_text(colors.CYAN, "start work")+"` or `"+color_text(colors.CYAN, "start break")+"`?")
                    continue
                next_interval()
            else:
                print("Did you mean `"+color_text(colors.CYAN, "resume")+"`?")

        elif cmd == "end" or cmd == "stop":
            if timer != None:
                timer.cancel()
                timer = None
                print(color_text(colors.BLUE, "Timer has been ended."))
            else:
                print(color_text(colors.BOLD, "Start a timer first!"))
            
        # Quit entire program
        elif cmd == "quit":
            print(color_text(colors.BOLD,"See you later!"))
            if timer != None:
                timer.cancel()
            return

        # Pause timer
        elif cmd == "pause":
            if timer != None:
                print("Timer has been "+color_text(colors.RED, "paused")+". There are "+str(round(timer.pause()/60, 1))+" minutes left.")
            else:
                print(color_text(colors.BOLD, "Start a timer first!"))
        # Resume timer
        elif cmd == "resume":
            if timer != None:
                print("Timer has been "+color_text(colors.GREEN, "resumed")+". There are "+str(round(timer.resume()/60, 1))+" minutes left.")
            else:
                print(color_text(colors.BOLD, "Start a timer first!"))
        # Remaining time until next interval switch
        elif cmd == "remaining":
            if timer != None:
                print("There are "+color_text(colors.MAGENTA, str(round(timer.remaining()/60, 1)))+" minutes of ", end='')
                if work_interval:
                    print("your work period remaining.")
                else:
                    print("your break period left.")
            else:
                print(color_text(colors.BOLD,"Start a timer first!"))
            
        # Use OS module to clear terminal
        elif cmd == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')

        #TODO: Switch intervals automatically vs manualling `start work` and `start break`
        elif cmd.startswith("auto"):
            if cmd == "auto on":
                set_pref("auto", True)
                print("Now automatically looping working time and breaks.")
            elif cmd == "auto off":
                set_pref("auto", False)
                print("Now working time and breaks must now be started manually.")
            else:
                print("Did you mean `"+color_text(colors.CYAN, "auto on")+"` or `"+color_text(colors.CYAN, "auto off"+"`?")+"`.")

        # set work or break period
        elif cmd.startswith("set ") and len(cmd.split(" ")) <= 3:
            arg = cmd.split(" ")
            if arg[1] == "work" and len(cmd.split(" ")) == 3:
                set_pref(arg[1], float(arg[2]))
                print("Work period updated to "+color_text(colors.MAGENTA, str(float(arg[2])))+" minutes.")
            elif arg[1] == "break" and len(cmd.split(" ")) == 3:
                set_pref(arg[1], float(arg[2]))
                print("Break period updated to "+color_text(colors.MAGENTA, str(float(arg[2])))+" minutes.")
            else:
                print("Did you mean `"+color_text(colors.CYAN, "set work [number of mins]")+"` or `"+color_text(colors.CYAN, "set work [number of mins]")+"`?")

        # Print help    
        elif cmd == "help":
            print_help()
        # Print about text file
        elif cmd == "about":
            print(colors.UNDERLINE+"About:"+colors.RESET)
            print_file("about.txt", "")

        # Fun features
        elif cmd == "tomato":
            print_file("tomato.txt", colors.RED)
        elif cmd.startswith("hack"):
            args = cmd.split(' ')
            if len(args)>1 and args[1] == "save":
                new_txt = input("Input your troll text here: ")
                set_pref("troll", new_txt)
                print("Troll text saved.")
            else:
                print_troll()
                
        # Edgecase       
        else:
            print("Sorry we don't recognize that command :(")

def next_interval():
    global timer
    global data
    global work_interval
    
    work_interval = not work_interval
    data = json.load(open("preferences.json", "r"))

    if data['auto'] == True:
        if work_interval:
            timer = pomotimer(data['work']*60, next_interval)
            print(color_text('\033[1;31m',">> Work for "+str(data['work'])+" minutes!"))
        else:
            timer = pomotimer(data['break']*60, next_interval)
            print(color_text('\033[1;32m',">> Take a break for "+str(data['break'])+" minutes!"))
        threading.Thread(target=playsound, args=('digital_watch_alarm.mp3',), daemon=True).start()
        timer.start()
    else:
        if work_interval:
            timer = pomotimer(data['work']*60, finished_interval)
            print(color_text('\033[1;31m',">> Work for "+str(data['work'])+" minutes!"))
        else:
            timer = pomotimer(data['break']*60, finished_interval)
            print(color_text('\033[1;32m',">> Take a break for "+str(data['break'])+" minutes!"))
        threading.Thread(target=playsound, args=('digital_watch_alarm.mp3',), daemon=True).start()
        timer.start()

def finished_interval():
    global timer
    
    print(color_text(colors.BLUE, "Timer has been ended."))
    threading.Thread(target=playsound, args=('digital_watch_alarm.mp3',), daemon=True).start()
    timer.cancel()
    timer = None
    
if __name__ == "__main__":
    main()
