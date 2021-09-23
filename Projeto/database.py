import sqlite3
from note import Note


class Database:
    def __init__(self,path) -> None:
        self.__connection = sqlite3.connect(path)
        self.__cursor = self.__connection.cursor()

        notesTable = """CREATE TABLE IF NOT EXISTS notes(
                        note_id INTEGER PRIMARY KEY,
                        note_name TEXT NOT NULL,
                        note_text TEXT NOT NULL
                    );"""
        
        self.__cursor.execute(notesTable)
        self.__connection.commit()

    def saveNote(self,note: Note) -> None:
        insert = f"INSERT INTO notes (note_name,note_text) VALUES ('{Note.name}','{note.text}');"
        self.__cursor.execute(insert);
        self.__connection.commit();

    def querryAll(self) -> list:
        querry = "SELECT * FROM notes;"

        self.__cursor.execute(querry)
        data = self.__cursor.fetchall()

        Notes = list()

        for temp in data:
            tempNote = Note()
            tempNote.fromTuple(temp)
            Notes.append(tempNote)
        return Notes


    