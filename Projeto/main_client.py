from client import Client

temp = Client("192.168.0.105",41990,"data-test.db")

temp.connect()

print("*"*10,"Notes","*"*10)
print("1 - Create a note")
print("2 - View notes")
print("3 - Delete a note")

c = input("--> Choose an option: ")

if c == '1':
    temp.newNote()
if c == '2':
    temp.allNotes()
if c == '3':
    temp.delNote()
