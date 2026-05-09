CREATE DATABASE IF NOT EXISTS hotel_system;

USE hotel_system;

CREATE TABLE users(
    fname VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(100)
);

CREATE TABLE room(
    contact VARCHAR(20) PRIMARY KEY,
    checkin VARCHAR(30),
    checkout VARCHAR(30),
    roomtype VARCHAR(30),
    roomavailable VARCHAR(30),
    meal VARCHAR(30),
    noofdays VARCHAR(10)
);