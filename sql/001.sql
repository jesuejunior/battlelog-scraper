CREATE TABLE profile (
	id INTEGER NOT NULL,
	username VARCHAR NOT NULL,
	url_stats VARCHAR NOT NULL,
	url_weapons VARCHAR NOT NULL,
	url_vehicles VARCHAR NOT NULL,
	PRIMARY KEY (id),
	UNIQUE (username)
)