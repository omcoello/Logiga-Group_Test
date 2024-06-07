#2.1

SELECT COUNT(*), musica
FROM persona
WHERE edad <= 20 AND musica = 'rock'
GROUP BY musica;

#2.2

SELECT COUNT(*) AS 'People number', musica AS 'Musical Preference', 
(COUNT(*) / (SELECT COUNT(*) FROM persona WHERE edad <= 20)) * 100 AS 'Percentage'
FROM persona
WHERE edad <= 20
GROUP BY musica;

#2.3

SELECT COUNT(*), musica
FROM persona
WHERE edad BETWEEN 20 AND 50
GROUP BY musica;

#2.4

SELECT COUNT(*) 
FROM persona
WHERE genero = 'F' AND edad > 60 AND musica = 'C & W';

#2.5

SELECT COUNT(*) AS 'People number', arte
FROM persona
WHERE genero = 'F' AND edad > 60 AND musica = 'C & W'
GROUP BY arte;

#2.6

SELECT genero, SUM(CASE WHEN musica = 'rock' THEN 1 ELSE 0 END) AS 'total_rock', SUM(CASE WHEN musica = 'jazz' THEN 1 ELSE 0 END) AS 'total_jazz'
FROM persona
WHERE musica IN ('rock', 'jazz')
GROUP BY genero;


#In case is being tested in mysql console:
#2.1

SELECT COUNT(*), musica FROM persona WHERE edad <= 20 AND musica = 'rock' GROUP BY musica;

#2.2

SELECT COUNT(*) AS 'People number', musica AS 'Musical Preference', (COUNT(*) / (SELECT COUNT(*) FROM persona WHERE edad <= 20)) * 100 AS 'Percentage' FROM persona WHERE edad <= 20 GROUP BY musica;

#2.3
SELECT COUNT(*), musica FROM persona WHERE edad BETWEEN 20 AND 50 GROUP BY musica;

#2.4
SELECT COUNT(*) FROM persona WHERE genero = 'F' AND edad > 60 AND musica = 'C & W';

#2.5
SELECT COUNT(*) AS 'People number', arte FROM persona WHERE genero = 'F' AND edad > 60 AND musica = 'C & W' GROUP BY arte;

#2.6
SELECT genero, SUM(CASE WHEN musica = 'rock' THEN 1 ELSE 0 END) AS 'total_rock', SUM(CASE WHEN musica = 'jazz' THEN 1 ELSE 0 END) AS 'total_jazz' FROM persona WHERE musica IN ('rock', 'jazz') GROUP BY genero;
