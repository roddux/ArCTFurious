PRAGMA foreign_keys = 1;
BEGIN TRANSACTION;
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
COMMIT;

-- Dummy data
BEGIN TRANSACTION;
INSERT INTO users VALUES(1,'fred@google.com','Fred Durden','FredDaMan');
INSERT INTO users VALUES(2,'ssmith@google.com','Steve Smith','st3v3');
INSERT INTO users VALUES(3,'skr4t@google.ru','Xerxes','xyl0ph');
INSERT INTO users VALUES(4,'john@google.com','john smith','johnthebest');
INSERT INTO scores VALUES(1,50);
INSERT INTO scores VALUES(2,35);
INSERT INTO scores VALUES(3,95);
INSERT INTO scores VALUES(4,50);
COMMIT;
