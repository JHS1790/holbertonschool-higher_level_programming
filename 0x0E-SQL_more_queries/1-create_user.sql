-- a script that creates the MySQL server user user_0d_1
-- Drop user if exists
DROP USER IF EXISTS 'user_0d_1'@'localhost';
-- creates the user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- grants privelages
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
-- Flush
FLUSH PRIVILEGES;