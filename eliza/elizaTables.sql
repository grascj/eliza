CREATE DATABASE ElizaDB;

CREATE TABLE ElizaUser (
	username CHAR(30) NOT NULL,
	password CHAR(30) NOT NULL,
	email CHAR(50) NOT NULL,
	status BOOLEAN DEFAULT false,
	PRIMARY KEY (username)
);

CREATE TABLE Conversation (
	username CHAR(30) NOT NULL,
	convid INTEGER NOT NULL,
	startdate DATE NOT NULL,
	PRIMARY KEY (convid, username), 
	FOREIGN KEY (username) REFERENCES ElizaUser(username)
);

CREATE TABLE Statement (
	username CHAR(30) NOT NULL,
	convid INTEGER NOT NULL,	
	timestamp DATETIME NOT NULL DEFAULT NOW(),
	name CHAR(30) NOT NULL,
	text VARCHAR(20) NOT NULL,
	PRIMARY KEY (username, convid, timestamp)
	FOREIGN KEY (username) REFERENCES ElizaUser(username),
	FOREIGN KEY (convid) REFERENCES Conversation(convid)
);
