PRAGMA foreign_keys = 1;
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
