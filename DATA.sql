CREATE DATABASE placement;
USE placement;
CREATE TABLE students(
student_name varchar(50) NOT NULL,
student_id varchar(20) PRIMARY KEY,
Pass varchar(15) NOT NULL);

CREATE TABLE student_table (
  full_name VARCHAR(255),
  email VARCHAR(255),
  phone_number VARCHAR(255),
  gender CHAR(10),
  registration_number VARCHAR(255) PRIMARY KEY,
  branch VARCHAR(255),
  year varchar(50),
  CGPA DECIMAL(3,2),
  HSC DECIMAL(3,2),
  SSC DECIMAL(3,2),
  CP_Profile varchar(50)
);
CREATE TABLE company(
company_name varchar(50) NOT NULL,
company_id varchar(20) PRIMARY KEY,
Password varchar(15) NOT NULL);

CREATE TABLE company_table (
  company_name VARCHAR(255),
  company_ID VARCHAR(255) PRIMARY KEY,
  phone_number VARCHAR(255),
  email VARCHAR(255),
  branch VARCHAR(255),
  year varchar(50),
  number_of_recruits INT,
  HSC DECIMAL(3,2),
  SSC DECIMAL(3,2),
  CGPA DECIMAL(3,2)
);

CREATE TABLE selected (
  full_name VARCHAR(255),
  registration_number VARCHAR(255) PRIMARY KEY,
  company_name VARCHAR(255),
  CGPA DECIMAL(3,2),
  sector VARCHAR(255),
  year_of_joining INT
);



