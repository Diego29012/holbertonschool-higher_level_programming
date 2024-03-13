-- Write a script that lists all cities contained in the database 
SELECT cities.id, cities.name, states.name
FROM cities
ORDER BY cities.id ASC;
