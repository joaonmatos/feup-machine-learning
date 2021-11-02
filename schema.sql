CREATE TABLE districts(
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    region TEXT NOT NULL,
    no_inhabitants INTEGER,
    no_small_places INTEGER,
    no_medium_places INTEGER,
    no_large_places INTEGER,
    no_cities INTEGER,
    ratio_urban_inhabitants REAL,
    avg_salary INTEGER,
    unemployment_95 REAL,
    unemployment_96 REAL,
    entrepreneur_ratio REAL,
    crimes_95 INTEGER,
    crimes_96 INTEGER
);

CREATE TABLE accounts(
    id INTEGER PRIMARY KEY,
    district_id INTEGER NOT NULL,
    frequency TEXT NOT NULL,
    "date" TEXT NOT NULL,

    FOREIGN KEY (district_id) REFERENCES districts (id)
);

CREATE TABLE loans(
    id INTEGER PRIMARY KEY,
    account_id INTEGER NOT NULL,
    "date" TEXT NOT NULL,
    amount INTEGER NOT NULL,
    duration INTEGER NOT NULL,
    payments INTEGER NOT NULL,
    status INTEGER,

    FOREIGN KEY (account_id) REFERENCES accounts(id)
);

CREATE TABLE transactions(
    id INTEGER PRIMARY KEY,
    account_id INTEGER NOT NULL,
    "date" TEXT NOT NULL,
    type TEXT NOT NULL,
    operation TEXT,
    amount REAL NOT NULL,
    balance REAL NOT NULL,
    k_symbol TEXT,
    bank TEXT,
    destination_account INTEGER,

    FOREIGN KEY (account_id) REFERENCES accounts(id)
);

CREATE TABLE clients (
    id INTEGER PRIMARY KEY,
    birthday TEXT NOT NULL,
    district_id INTEGER NOT NULL,
    gender TEXT NOT NULL,

    FOREIGN KEY (district_id) REFERENCES districts (id)
);

CREATE TABLE dispositions (
    id INTEGER PRIMARY KEY,
    client_id INTEGER NOT NULL,
    account_id INTEGER NOT NULL,
    type TEXT NOT NULL,

    FOREIGN KEY (account_id) REFERENCES accounts(id),
    FOREIGN KEY (client_id) REFERENCES clients(id)
);

CREATE TABLE cards (
    id INTEGER PRIMARY KEY,
    disposition_id INTEGER NOT NULL,
    type TEXT NOT NULL,
    issue_date TEXT NOT NULL,

    FOREIGN KEY (disposition_id) REFERENCES dispositions(id)
);
