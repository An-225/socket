import sqlite3
from note import Note


class Database:
    def __init__(self, path) -> None:
        print(f"Connecting to database: {path}...",end='')
        self.__connection = sqlite3.connect(path)
        self.__cursor = self.__connection.cursor()
        print(f"OK!")

        
        print("Initializing table...",end='')
        notesTable = """CREATE TABLE IF NOT EXISTS notes(
                        note_id INTEGER PRIMARY KEY,
                        note_name TEXT NOT NULL,
                        note_text TEXT NOT NULL
                    );"""

        self.__cursor.execute(notesTable)
        self.__connection.commit()
        print("OK")
    
    def __del__(self) -> None:
        print(f"Closing connection...",end='')
        self.__cursor.close()
        self.__connection.close()
        print(f"OK!")

    def saveNote(self, note: Note) -> None:
        insert = f"INSERT INTO notes (note_name,note_text) VALUES ('{note.name}','{note.text}');"
        
        print("Saving note...",end='')
        self.__cursor.execute(insert)
        self.__connection.commit()
        print("OK")

    def querryAll(self) -> list:
        querry = "SELECT * FROM notes;"

        print("Querying notes...",end='')
        self.__cursor.execute(querry)
        data = self.__cursor.fetchall()
        print("OK")

        Notes = list()

        print("Creating list...",end='')
        for temp in data:
            tempNote = Note()
            tempNote.fromTuple(temp)
            Notes.append(tempNote)
        print("OK")
        
        return Notes

    def deleteNote(self, note: Note) -> None:
        delete = f"DELETE FROM notes WHERE note_id IS {note.id};"
        
        print("Deleting note...",end='')
        self.__cursor.execute(delete)
        self.__connection.commit()
        print("OK")
