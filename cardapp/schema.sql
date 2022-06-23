DROP TABLE IF EXISTS card;
DROP TABLE IF EXISTS cardset;

CREATE TABLE cardset (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE card (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    prompt TEXT NOT NULL,
    answer TEXT NOT NULL,
    cardset_id INTEGER NOT NULL,
    box INTEGER NOT NULL DEFAULT 1,
    FOREIGN KEY (cardset_id) REFERENCES cardset (id)
);

-- Insert example cardset and cards
