CREATE TABLE IF NOT EXISTS hardware (
id integer PRIMARY KEY AUTOINCREMENT,
who_issue text NOT NULL,
tech_type text NOT NULL,
tech_name text NOT NULL,
tech_sn text NOT NULL,
tech_in text NOT NULL,
for_whom text NOT NULL,
tech_locate text NOT NULL,
tech_buisnes text NOT NULL,
input_date text NOT NULL,
input_coment text NOT NULL
);