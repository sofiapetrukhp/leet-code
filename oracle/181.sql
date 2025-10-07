-- 181. Employees Earning More Than Their Managers

SELECT 
    e1.name as Employee
FROM
    Employee e1
JOIN
    Employee e2
ON
    e1.managerId = e2.id
WHERE
    e1.salary > e2.salary; 