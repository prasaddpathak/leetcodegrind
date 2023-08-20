# Write your MySQL query statement below

SELECT student_id, student_name FROM (
SELECT student_id,
        student_name,
        SUM(queit)/COUNT(student_name) AS _check
FROM 
    (
    SELECT *,
        CASE WHEN _rank != MIN(_rank) OVER(PARTITION BY exam_id) 
                AND _rank != MAX(_rank) OVER(PARTITION BY exam_id) THEN 1 ELSE 0
            END AS queit
        FROM
    (
        SELECT e.exam_id,
                e.student_id,
                s.student_name,
                e.score,
                DENSE_RANK() OVER (PARTITION BY exam_id ORDER BY score) AS _rank
            FROM Exam e
                LEFT JOIN Student s 
                    ON e.student_id = s.student_id
    ) a ) b
GROUP BY student_id, student_name
ORDER BY student_id ) c 

WHERE _check = 1
