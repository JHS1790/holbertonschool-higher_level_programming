-- a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server
-- lists the table
SELECT score, name FROM second_table HAVING score >= 10 ORDER BY score DESC;