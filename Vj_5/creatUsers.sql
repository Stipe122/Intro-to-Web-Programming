id = id - primary key
ime  = varchat(100)
email = varchar(100) i unique
password = binary64

CREATE TABLE IF NOT EXISTS users(
	id INT NOT NULL AUTO_INCREMENT,
	ime VARCHAR(100) NOT NULL,
	email VARCHAR(100) NOT NULL,
	password TEXT NOT NULL,
	PRIMARY KEY(id),
	UNIQUE(email)
);

CREATE TABLE IF NOT EXISTS users(
	id INT NOT NULL AUTO_INCREMENT,
	ime VARCHAR(100) NOT NULL,
	email VARCHAR(100) NOT NULL,
	password BINARY(64) NOT NULL,
	PRIMARY KEY(id),
	UNIQUE(email)
);

INSERT INTO users (ime, email,password) VALUES("petar","petar@gmail.com","12345");