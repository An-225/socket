//Criar
CREATE TABLE IF NOT EXISTS notes(
    note_id INTEGER PRIMARY KEY,
    note_name TEXT NOT NULL,
    note_text TEXT NOT NULL
);
//Ver
SELECT * FROM notes;

//Popular
INSERT INTO notes (note_name,note_text) VALUES ('teste1','testando1');
INSERT INTO notes (note_name,note_text) VALUES ('teste2','testando2');
INSERT INTO notes (note_name,note_text) VALUES ('teste3','testando3');
INSERT INTO notes (note_name,note_text) VALUES ('teste4','testando4');
INSERT INTO notes (note_name,note_text) VALUES ('teste5','testando5');

//
DELETE FROM notes WHERE note_id IS 5; 

//Limpar
DROP TABLE notes;