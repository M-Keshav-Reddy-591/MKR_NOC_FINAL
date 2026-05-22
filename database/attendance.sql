CREATE DATABASE attendance_db;

USE attendance_db;

CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    emp_id VARCHAR(50) UNIQUE,
    name VARCHAR(100),
    department VARCHAR(100)
);

CREATE TABLE attendance (
    id INT PRIMARY KEY AUTO_INCREMENT,
    emp_id VARCHAR(50),
    date DATE,
    status VARCHAR(20)
);

CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    emp_id VARCHAR(50) UNIQUE,
    name VARCHAR(100),
    department VARCHAR(100),
    role VARCHAR(20),
    password VARCHAR(100)
);
CREATE TABLE shifts (
    id INT PRIMARY KEY AUTO_INCREMENT,
    shift_name VARCHAR(50),
    start_time TIME,
    end_time TIME,
    grace_minutes INT
);
CREATE TABLE roster (
    id INT PRIMARY KEY AUTO_INCREMENT,
    emp_id VARCHAR(50),
    shift_id INT,
    shift_date DATE
);
CREATE TABLE attendance (
    id INT PRIMARY KEY AUTO_INCREMENT,
    emp_id VARCHAR(50),
    shift_date DATE,
    login_time DATETIME,
    status VARCHAR(20)
);
CREATE TABLE leaves (
    id INT PRIMARY KEY AUTO_INCREMENT,
    emp_id VARCHAR(50),
    from_date DATE,
    to_date DATE,
    reason TEXT,
    status VARCHAR(20)
);
CREATE TABLE shift_swaps (
    id INT PRIMARY KEY AUTO_INCREMENT,
    requester_emp_id VARCHAR(50),
    target_emp_id VARCHAR(50),
    shift_date DATE,
    status VARCHAR(20)
);
