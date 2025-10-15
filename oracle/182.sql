-- 182. Duplicate Emails

SELECT 
    p.email
FROM
    Person p
GROUP BY
    email
HAVING
    COUNT(email) > 1;