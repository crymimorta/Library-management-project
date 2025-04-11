-- Modernized SQL dump for `library` database
-- MySQL Server 8+ compatible

DROP DATABASE IF EXISTS library;
CREATE DATABASE library CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE library;

-- Table: authors
CREATE TABLE authors (
  id INT AUTO_INCREMENT PRIMARY KEY,
  author_name VARCHAR(100) NOT NULL
);
INSERT INTO authors (author_name) VALUES
  ('Mahmoud Ahmed'),
  ('sayed'),
  ('ali');

-- Table: category
CREATE TABLE category (
  id INT AUTO_INCREMENT PRIMARY KEY,
  category_name VARCHAR(100) NOT NULL
);
INSERT INTO category (category_name) VALUES
  ('Gaming'),
  ('Drama'),
  ('Sport'),
  ('Cooking');

-- Table: publisher
CREATE TABLE publisher (
  id INT AUTO_INCREMENT PRIMARY KEY,
  publisher_name VARCHAR(100) NOT NULL
);
INSERT INTO publisher (publisher_name) VALUES
  ('Ahmed Ali'),
  ('amal'),
  ('maati'),
  ('ahmed'),
  ('sayed');

-- Table: book
CREATE TABLE book (
  id INT AUTO_INCREMENT PRIMARY KEY,
  book_name VARCHAR(100) NOT NULL,
  book_description TEXT,
  book_code VARCHAR(50),
  book_category VARCHAR(100),
  book_author VARCHAR(100),
  book_publisher VARCHAR(100),
  book_price DECIMAL(10,2)
);
INSERT INTO book (book_name, book_description, book_code, book_category, book_author, book_publisher, book_price) VALUES
  ('space travel','space travel 3','002','Sport','Mahmoud Ahmed','Ahmed Ali',120),
  ('python coding','python tutorials','003','Gaming','sayed','maati',50),
  ('python programming','this is a book for python','004','Drama','Mahmoud Ahmed','Ahmed Ali',50),
  ('pyqt library system','a real project with pyqt5','005','Drama','sayed','ahmed',200),
  ('pyqt5 project','build a library system','006','Gaming','Mahmoud Ahmed','Ahmed Ali',40);

-- Table: clients
CREATE TABLE clients (
  id INT AUTO_INCREMENT PRIMARY KEY,
  client_name VARCHAR(100),
  client_email VARCHAR(100),
  client_nationalid VARCHAR(50)
);
INSERT INTO clients (client_name, client_email, client_nationalid) VALUES
  ('mahmoud','mahmoud@gmail.com','2123213124'),
  ('ahmed','ahmed@gmail.com','21232674676'),
  ('jack','jack22@gmail.com','123142423'),
  ('john33','john33@gmail.com','4534636346');

-- Table: dayoperations
CREATE TABLE dayoperations (
  id INT AUTO_INCREMENT PRIMARY KEY,
  book_name VARCHAR(100),
  client VARCHAR(100),
  type VARCHAR(50),
  days INT,
  date DATE,
  to_date DATE
);
INSERT INTO dayoperations (book_name, type, days, date, client, to_date) VALUES
  ('space', 'Retrieve', 4, '2019-01-08', NULL, NULL),
  ('python', 'Retrieve', 4, '2019-01-09', 'mahmoud', NULL);

-- Table: users
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_name VARCHAR(100) NOT NULL,
  user_email VARCHAR(100),
  user_password VARCHAR(100) NOT NULL
);
INSERT INTO users (user_name, user_email, user_password) VALUES
  ('mahmoud ahmed', 'pythondeveloper6@gmail.com', '12345'),
  ('ahmed2', 'ahmed10@gmail.com', '1234');
