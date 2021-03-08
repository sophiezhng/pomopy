from colors import colors, color_text

# Output for the help command
def print_help():
    print(colors.UNDERLINE+"Available Commands:"+colors.RESET)
    print("Make sure your volume is unmuted to hear when the timer goes off!\n")
    
    print(color_text(colors.GREEN, "Basic Commands:"))
    generate_cmd(colors.CYAN,"start","Begin the timer from start of work period")
    generate_cmd(colors.CYAN, "stop", "End Pomodoro timer")
    generate_cmd(colors.CYAN, "remaining", "Remaining time left until next interval")
    generate_cmd(colors.CYAN, "pause", "Pause the timer temporarily until resume")
    generate_cmd(colors.CYAN, "resume", "Continue from where you left off")
    generate_cmd(colors.CYAN, "clear", "Clear the terminal")
    generate_cmd(colors.CYAN, "quit", "Quit the program")

    print(color_text(colors.GREEN, "\nCustomize Settings:"))
    generate_cmd(colors.CYAN, "set work [number of mins]", "Change length of work period")
    generate_cmd(colors.CYAN, "set break [number of mins]", "Change length of break period")
    generate_cmd(colors.CYAN, "auto off", "Manually switch between working and breaks")
    print("➪ if enabled, must use `"+color_text(colors.CYAN, "start work")+"` or `"+color_text(colors.CYAN, "start break")+"`")
    generate_cmd(colors.CYAN, "auto on", "Default setting: automatically switchs between work and break periods in succession")
    
    print(color_text(colors.GREEN, "\nMore Info:"))
    generate_cmd(colors.CYAN, "about", "Purpose of the program, author, credits, and more")
    generate_cmd(colors.CYAN, "tomato", "Recieve a mysterious tomato")

# Generate the format for each command in the help output
def generate_cmd(color, cmd_name, desc):
    print("`"+color_text(color, cmd_name)+"` - "+desc)
