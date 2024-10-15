seassion_id = id - primary key
data = text

CREATE TABLE IF NOT EXISTS sessions(
	session_id INT NOT NULL,
	data TEXT NOT NULL,
	PRIMARY KEY(session_id)
);

CREATE TABLE IF NOT EXISTS sessions(
	session_id INT NOT NULL AUTO_INCREMENT,
	data TEXT NOT NULL,
	PRIMARY KEY(session_id)
);