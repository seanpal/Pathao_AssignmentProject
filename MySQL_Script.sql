drop database if exists book_application;
create database book_application;
use book_application;

drop table if exists author;
drop table if exists publisher;
drop table if exists  reviews;
drop table if exists  checkouts;
drop table if exists addresses;
drop table if exists users;
drop table if exists books;
show tables;

CREATE TABLE users (
  user_id INT NOT NULL AUTO_INCREMENT,
  name varchar(30) NOT NULL,
  enabled BOOLEAN,
  last_login timestamp DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (user_id)
);
CREATE TABLE addresses (
  id integer NOT NULL AUTO_INCREMENT,
  user_id integer, 
  street varchar(30),
  city varchar(30),
  country varchar(30) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id)
      REFERENCES users (user_id)
      ON DELETE CASCADE
);
CREATE TABLE author (
  author_id INT NOT NULL AUTO_INCREMENT,
  author_name varchar(255),
  author_dob DATE,
  author_details varchar(100),
  PRIMARY KEY (author_id)
);
CREATE TABLE publisher (
  publisher_id INT NOT NULL AUTO_INCREMENT,
  publisher_name varchar(255),
  publisher_address varchar(255),
  publisher_phone varchar(255),
  PRIMARY KEY (publisher_id)
);
CREATE TABLE books (
  id INT NOT NULL AUTO_INCREMENT,
  title varchar(100) NOT NULL,
  author_id INT NOT NULL,
  publisher_id INT NOT NULL,
  published_date DATE,
  isbn char(12),
  PRIMARY KEY (id),
  UNIQUE (isbn),
  FOREIGN KEY (author_id)
      REFERENCES books(id)
      ON DELETE CASCADE
);
CREATE TABLE reviews (
  id INT NOT NULL AUTO_INCREMENT,
  book_id integer NOT NULL,
  reviewer_name varchar(255),
  content varchar(255),
  rating integer,
  published_date timestamp DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (book_id)
      REFERENCES books(id)
      ON DELETE CASCADE
);
CREATE TABLE checkouts (
  id INT NOT NULL AUTO_INCREMENT,
  user_id int NOT NULL,
  book_id int NOT NULL,
  checkout_date timestamp,
  return_date timestamp,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(user_id)
                        ON DELETE CASCADE,
  FOREIGN KEY (book_id) REFERENCES books(id)
                        ON DELETE CASCADE
);

show tables;

INSERT INTO users(name,enabled, last_login) VALUES ("ok",TRUE,CURRENT_TIMESTAMP);
INSERT INTO addresses(user_id, street, city, country) VALUES (1,"ok","ok","ok");
INSERT INTO author(author_name, author_dob, author_details) VALUES ("ok","1990-12-12","okok");
INSERT INTO publisher(publisher_name, publisher_address, publisher_phone) VALUES ("publisher_name","publisher_address","93458394584");
INSERT INTO books(title, author_id,publisher_id,published_date, isbn) VALUES ("Python Programming",1,1,"2020-12-12","283485883458");
INSERT INTO reviews(book_id, reviewer_name, content, rating,published_date) VALUES (1,"sanjoy","ok",4,CURRENT_TIMESTAMP);
INSERT INTO checkouts (user_id, book_id, checkout_date, return_date) VALUES (1,1,"2020-12-12","2020-12-30");
