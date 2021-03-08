class colors: # You may need to change color settings depending on OS
    BOLD    = "\033[;1m"
    UNDERLINE = "\033[;4m"
    REVERSE = "\033[;7m"
    RESET = "\033[0;0m"
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN  = '\033[36m'
    WHITE = '\033[37m'

# Return text with colors
def color_text(color, string):
    return(color+string+colors.RESET)
