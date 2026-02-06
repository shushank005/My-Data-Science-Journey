-- Table: students
-- Columns: id, student_name, age, marks

-- 📝 Topic: Basic Select with Filtering data
-- 🎯 Goal: select student name, age and id from students table whose marks is greater than 60


SELECT 
    id,
    student_name,
    age
FROM students
WHERE marks > 60;