CREATE TABLE personal (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
rolle TEXT,
kontakt TEXT,
verfuegbarkeit TEXT,
veranstaltung_id INTEGER,
status TEXT CHECK(status IN ('angemeldet','abgemeldet')),
FOREIGN KEY (veranstaltung_id) REFERENCES veranstaltungen(id)
);

CREATE TABLE programmplan (
id INTEGER PRIMARY KEY AUTOINCREMENT,
veranstaltung_id INTEGER,
uhrzeit TEXT,
programmpunkt TEXT,
verantwortlich TEXT,
FOREIGN KEY (veranstaltung_id) REFERENCES veranstaltungen(id)
);
