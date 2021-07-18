/*
    Title: bacchus_init.sql
    Group: Bravo
    Author: Campbell, Hinkle, Luna, Orozco, Upadhyaya
    Date: 11 July 2020
    Description: Bacchus Winery database initialization script.
*/

-- drop test user if exists 
DROP USER IF EXISTS 'bacchus_user'@'localhost';

-- create bacchus_user and grant them all privileges to the bacchus database 
CREATE USER 'bacchus_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the bacchus database to user bacchus_user on localhost 
GRANT ALL PRIVILEGES ON bacchus.* TO'bacchus_user'@'localhost';