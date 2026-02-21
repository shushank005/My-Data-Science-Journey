-- =============================================
-- 📌 Topic: ORDER BY Clause
-- 🎯 Goal: Get id, student_name, age, and marks
--          sorted by marks in descending order
-- 🗂️ Table: students (id, student_name, age, marks)
-- =============================================

SELECT
    id,
    student_name,
    age,
    marks
FROM students
ORDER BY marks DESC;