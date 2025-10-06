-- 175. Combine Two Tables (Easy)

SELECT 
    p.firstName,
    p.lastName,
    a.city,
    a.state

FROM 
    Address a
RIGHT JOIN
    Person p
    ON
    a.personId = p.personId;