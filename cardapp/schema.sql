DROP TABLE IF EXISTS card;
DROP TABLE IF EXISTS cardset;

CREATE TABLE cardset (
    cardsetid INTEGER PRIMARY KEY AUTOINCREMENT,
    cardsetname TEXT
);

CREATE TABLE card (
    cardid INTEGER PRIMARY KEY AUTOINCREMENT,
    prompt TEXT NOT NULL,
    answer TEXT NOT NULL,
    card_set INTEGER,
    FOREIGN KEY(card_set) REFERENCES cardset(cardsetid)
);
