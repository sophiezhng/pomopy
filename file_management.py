from colors import *
import json
import time

# Set preferences with pref type and value
def set_pref(pref_type, value):
    file = open("preferences.json", "r")
    prefs = json.load(file)
    prefs[pref_type] = value
    json.dump(prefs, open("preferences.json", "w"))

# Print file with colored text
def print_file(file_name, text_color):
    f = open(file_name, 'r')
    file_contents = f.read()
    print(text_color + file_contents + colors.RESET)
    f.close()

def print_troll():
    print(colors.GREEN, end = '')
    f = open("troll.txt", 'r')
    file_contents = f.read()
    f.close()
    for char in file_contents:
        print(char, end = '')
        time.sleep(0.0005)
    items = range(32)
    l = len(items)
    # Initial call to print 0% progress
    printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
    for i in items:
        # Do stuff...
        time.sleep(0.1)
        # Update Progress Bar
        printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
    data = json.load(open("preferences.json", "r"))
    print("HACKING COMPLETE")
    print(colors.RESET+data['troll'])

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()
