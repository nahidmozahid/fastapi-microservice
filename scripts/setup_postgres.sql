CREATE DATABASE microdb;

\c microdb;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100)
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50),
    item VARCHAR(100)
);
