-- UNIQ ID
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT '0' NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (`id`)
);