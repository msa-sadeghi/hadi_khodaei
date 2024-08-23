SELECT ROUND(5.7345, 3);
SELECT CEILING(5.7);
SELECT FLOOR(5.7);
SELECT ABS(-5.2);
SELECT random();
SELECT LENGTH('sky');
SELECT UPPER('sky');
SELECT LOWER('SKY');
SELECT LTRIM('       sky');
SELECT LENGTH(LTRIM('       sky'));
SELECT RTRIM('sky      ');
SELECT TRIM('     sky      ');

SELECT LEFT('salaaammmmm', 4);
SELECT RIGHT('salaaammmmm', 4);
SELECT SUBSTRING('salaaammmmmmm', 3,3);
SELECT SUBSTRING('salaaammmmmmm', 3);
SELECT POSITION('l' IN 'salaaam');
SELECT REPLACE('salamchetori', 'chetori', 'khoobi');
SELECT CONCAT('first','name');

SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM public.customers;

SELECT NOW(), CURRENT_DATE, CURRENT_TIME;
SELECT EXTRACT(YEAR FROM NOW());
SELECT EXTRACT(DAY FROM NOW());
SELECT EXTRACT(HOUR FROM NOW());
SELECT EXTRACT(DAYNAME FROM NOW());
SELECT date_part('year', NOW());
