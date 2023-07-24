-- CREATE TABLE `register` (
--   `ID` int(10) NOT NULL,
--   `First_Name` varchar(100) NOT NULL,
--   `Last_Name` varchar(100) NOT NULL,
--   `Email` varchar(100) NOT NULL,
--   `Password` int(100) NOT NULL,
--   `File` varchar(100) NOT NULL
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE users (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);