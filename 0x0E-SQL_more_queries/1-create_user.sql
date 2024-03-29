-- creates the MySQL server user user_0d_1. by Okpako Michael
-- user_0d_1 should have all privileges on my MySQL server
-- The user_0d_1 password should be set to user_0d_1_pwd
-- To make a new user -> CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
-- To provide the user with all privileges -> GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
