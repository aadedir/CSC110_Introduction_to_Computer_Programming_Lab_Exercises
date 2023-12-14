def main():
    collectinputs()
    displaybanner()
    displaysectheaders()
def collectinputs():
    global name
    global date
    global program_name
    global program_description
    name = str(input("Enter your name: "))
    date = str(input("Enter the date: "))
    program_name = str(input("Enter the program name: "))
    program_description = str(input("Enter a short description: "))
def displaybanner():
    displaystarline()
    print("#    Name: " + name)
    print("#    Date: " + date)
    print("#    Program: " + program_name)
    print("#    About: " + program_description)
    displaystarline()
def displaystarline():
    print("#" + "*" * 70)
def displaysectheaders():
    print("")
    displaysectheader("Constants")
    displaysectheader("Variables")
    displaysectheader("Input")
    displaysectheader("Processing")
    displaysectheader("Output")
def displaysectheader(section_name):
    displaystarline()
    print("#    "+section_name)
    displaystarline()

main()