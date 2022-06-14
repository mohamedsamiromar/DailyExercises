DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS dailyexercise;
CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  email Email NOT NULL ,
  password TEXT NOT NULL
);


CREATE TABLE dailyexercise (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  exercise_name TEXT NOT NULL ,
  exercise_start_date TIMESTAMP,
  exercise_end_date TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);
