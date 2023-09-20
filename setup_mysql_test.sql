-- Prepare the server for the project
-- Create a database hbnb_test_db and a new user hbnb_test (in localhost)
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

GRANT SELECT
	ON performance_schema.* to 'hbnb_test'@'localhost';

FLUSH PRIVILEGES;
