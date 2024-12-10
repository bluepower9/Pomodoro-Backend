DROP table users;
DROP table notes;

CREATE TABLE users (
    user_id  SERIAL,
    created_at timestamptz DEFAULT now(),
    username varchar NOT NULL UNIQUE,
    email varchar NOT NULL,
    password bytea NOT NULL,
    salt bytea NOT NULL,

    PRIMARY KEY (user_id)
);

CREATE TABLE notes (
    note_id SERIAL,
    created_at timestamptz DEFAULT now(),
    user_id INT NOT NULL,
    note VARCHAR
)