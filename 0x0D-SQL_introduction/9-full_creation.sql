-- a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows
-- creates the script
CREATE TABLE IF NOT EXISTS second_table (
    id INT(11),
    name VARCHAR(256),
    score INT(11)
);
-- add data
INSERT INTO second_table (`id`,`name`,`score`) VALUES (1,"John",10);
-- add data
INSERT INTO second_table (`id`,`name`,`score`) VALUES (2,"Alex",3);
-- add data
INSERT INTO second_table (`id`,`name`,`score`) VALUES (3,"Bob",14);
-- add data
INSERT INTO second_table (`id`,`name`,`score`) VALUES (4,"George",8);