from client import Client

temp = Client("192.168.122.89", 41990)

temp.connect()

while True:
    print("*"*10, "Notes", "*"*10)
    print("1 - Create a note")
    print("2 - View notes")
    print("3 - Delete a note")
    print("4 - Quit")

    c = input("--> Choose an option: ")

    if c == '1':
        temp.newNote()
    if c == '2':
        temp.allNotes()
    if c == '3':
        temp.delNote()
    if c == '4':
        temp.disconnect()
        exit(0)
