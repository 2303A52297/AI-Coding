-- SQLite
DROP TABLE IF EXISTS students;


CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name TEXT,
    subject_name TEXT,
    marks INT,
    grades TEXT,
    semester TEXT
);

INSERT INTO students VALUES
(2297,'Chowdary','Devops',85,'A','3-2'),
(2216,'Ashwitha','Python',78,'B+','3-2'),
(2382,'Veda','Data Science',92,'A+','3-2'),
(2438,'Rishitha','Machine Learning',88,'A','3-2'),
(2505,'Meghana','Cloud Computing',80,'B+','3-1');

SELECT * FROM students;