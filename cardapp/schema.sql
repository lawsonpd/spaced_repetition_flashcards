DROP TABLE IF EXISTS card;
DROP TABLE IF EXISTS cardset;

CREATE TABLE cardset (
    cardsetid INTEGER PRIMARY KEY AUTOINCREMENT,
    cardsetname TEXT NOT NULL
);

CREATE TABLE card (
    cardid INTEGER PRIMARY KEY AUTOINCREMENT,
    prompt TEXT NOT NULL,
    answer TEXT NOT NULL,
    cardset_id INTEGER NOT NULL,
    box INTEGER NOT NULL DEFAULT 1,
    FOREIGN KEY(cardset_id) REFERENCES cardset(cardsetid)
);

-- Insert example cardset and cards
