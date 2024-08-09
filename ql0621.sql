CREATE DATABASE IF NOT EXISTS PRJ301;
USE PRJ301;

CREATE TABLE Cart (
    id VARCHAR(50) NOT NULL,
    u_id INT NOT NULL,
    buyDate DATE NULL,
    PRIMARY KEY (id)
);

CREATE TABLE CartItem (
    id VARCHAR(50) NOT NULL,
    quantity INT NULL,
    unitPrice DOUBLE NULL,
    pro_id INT NOT NULL,
    cat_id VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE Category (
    id INT AUTO_INCREMENT NOT NULL,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE DateExp (
    id INT AUTO_INCREMENT NOT NULL,
    mfgDate DATE NOT NULL,
    expDate DATE NOT NULL,
    cid INT NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE `Order` (
    id INT AUTO_INCREMENT NOT NULL,
    `date` DATE NOT NULL,
    cid INT NOT NULL,
    totalmoney INT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE OrderLine (
    oid INT NOT NULL,
    pid INT NOT NULL,
    quantity DOUBLE NOT NULL,
    price DOUBLE NOT NULL,
    PRIMARY KEY (oid, pid)
);

CREATE TABLE Product (
    ID INT AUTO_INCREMENT NOT NULL,
    name VARCHAR(255) NOT NULL,
    price DOUBLE NULL,
    cid INT NOT NULL,
    image VARCHAR(50) NULL,
    `describe` TEXT NULL,
    PRIMARY KEY (ID)
);

CREATE TABLE `User` (
    id INT AUTO_INCREMENT NOT NULL,
    name VARCHAR(50) NOT NULL,
    fullname VARCHAR(50) NULL,
    email VARCHAR(50) NULL,
    phonenum VARCHAR(10) NULL,
    avatar VARCHAR(50) NULL,
    role INT NULL,
    password VARCHAR(36) NOT NULL,
    `address` VARCHAR(123) NULL,
    PRIMARY KEY (id)
);

CREATE TABLE emp (
    cdate DATETIME NULL
);
