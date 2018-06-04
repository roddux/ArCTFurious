PRAGMA foreign_keys = 1;

CREATE TABLE users (
	id INTEGER PRIMARY KEY NOT NULL,
	email TEXT UNIQUE NOT NULL,
	name TEXT NOT NULL,
	handle TEXT NOT NULL
);

CREATE TABLE scores (
	userid INTEGER NOT NULL PRIMARY KEY,
	score INTEGER NOT NULL,
	FOREIGN KEY(userid) REFERENCES users(id)
);

CREATE TABLE sessions (
	sessionid TEXT UNIQUE NOT NULL,
	userid INTEGER UNIQUE NOT NULL,
	FOREIGN KEY(userid) REFERENCES users(id)
);
CREATE UNIQUE INDEX sidindex on sessions(sessionid);
