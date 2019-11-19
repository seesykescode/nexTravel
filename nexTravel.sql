-- Question 1
select * FROM users WHERE companyID IS NULL;

-- Question 2
select * from users b WHERE isDeleted = 0 AND EXISTS ( select * from companies a WHERE a.isDeleted = 1 AND b.companyId = a.id );
-- Question 3
select b.name, count(*) from companies b JOIN users a ON b.id = a.companyId WHERE a.isDeleted = 0 AND b.isDeleted = 0 GROUP BY b.name DESC;

-- Question 4
select * from users b WHERE NOT EXISTS ( select * from companies a WHERE b.companyId = a.id );

-- Question 5
INSERT INTO users (name, companyId, isDeleted) VALUES ('Leto', 1, 0)

-- Question 6
UPDATE users SET name = 'Leo' WHERE name = "Leto"

-- Question 7
DELETE FROM users where name = 'Bob';
