-- creates the database btcp_0d_usa and the table states (in the database
-- btcp_0d_usa) on your MySQL server
CREATE DATABASE IF NOT EXISTS btcp_0d_usa;
USE btcp_0d_usa;
CREATE TABLE IF NOT EXISTS states
	   (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	   name VARCHAR(256) NOT NULL);
