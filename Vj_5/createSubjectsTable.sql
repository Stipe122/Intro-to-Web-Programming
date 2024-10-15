CREATE TABLE IF NOT EXISTS subjects(
	id INT NOT NULL AUTO_INCREMENT,
	kod VARCHAR(100) NOT NULL,
	ime VARCHAR(100) NOT NULL,
	bodovi INT NOT NULL,
	godina INT NOT NULL,
	PRIMARY KEY(id)
);

INSERT INTO subjects (kod,ime,godina,bodovi) VALUES ("ip", "Introduction to programming", 1, 6);

INSERT INTO subjects (kod,ime,godina,bodovi) VALUES ("c1", "Calculus 1", 1, 7);

INSERT INTO subjects (kod,ime,godina,bodovi) VALUES ("cu", "Computer usage", 1, 5);

INSERT INTO subjects (kod,ime,godina,bodovi) VALUES ("dmt", "Digital and microprocessor technology", 1, 6);

INSERT INTO subjects (kod,ime,godina,bodovi) VALUES ("db", "Databases", 2, 6);

INSERT INTO subjects (kod,ime,godina,bodovi) VALUES ("c2", "Calculus 2", 2, 7);

INSERT INTO subjects (kod,ime,godina,bodovi) VALUES ("dsa", "Data structures and alghoritms", 2, 5);

INSERT INTO subjects (kod,ime,godina,bodovi) VALUES ("ca", "Computer architecture", 2, 6);

INSERT INTO subjects (kod,ime,godina,bodovi) VALUES ("isd", "Information systems design", 3, 5);

INSERT INTO subjects (kod,ime,godina,bodovi) VALUES ("c3", "Calculus 3", 3, 7);

INSERT INTO subjects (kod,ime,godina,bodovi) VALUES ("sa", "Server Architecture", 3, 6);

INSERT INTO subjects (kod,ime,godina,bodovi) VALUES ("cds", "Computer and data security", 3, 6);
