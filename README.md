# Pomopy (pom-oh-pie): An old-school solution for a modern problem.

![Picture of terminal with pomopy](https://sophiezhng.github.io/pomopy/images/pomopy.png)

## 🍅 What is Pomopy?
Pomopy is a fun ASCII-art-filled, customizable, time-management solution to optimize productivity. The Pomodoro Technique was developed by Francesco Cirillo in the 1980s and emphasizes working and taking breaks in regular intervals. 

## Installation
```bash
pip install pomopy
```
OR
```bash
git clone https://github.com/sophiezhng/pomopy
cd pomopy
pip install -r requirements.txt
python setup.py install
```

## Usage
```bash
pomopy
```

Make sure your volume is unmuted to hear when the timer goes off!

Use the `help` command to see all of the available commands.

🍝 Read Wiki For More Info => [Full List of Commands](https://github.com/sophiezhng/pomopy/wiki/Commands)

## 🌱 How it's built
This Pomodoro timer was built in Python using the playsound library to play an alarm effect after each interval. It saves your preferences in a JSON file locally so that you can start and stop easily. 

## Credits
- [Pomodoro Technique](https://en.wikipedia.org/wiki/Pomodoro_Technique) - by: Francesco Cirillo
- [playsound](https://github.com/TaylorSMarks/playsound)
- [ASCII Text Generator](https://manytools.org/hacker-tools/ascii-banner/)
- [Tomato Art](https://textart.sh/topic/tomato)
- [Progress Bar](https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console)
