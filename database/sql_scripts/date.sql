select to_char(NOW(), 'dd/mm/yy') ;

SELECT NOW() + INTERVAL '1 DAY';



SELECT DATE_ADD(NOW(), INTERVAL '1 DAY');
select * from orders
where EXTRACT('year' FROM order_date) = EXTRACT ('year' FROM DATE_ADD( NOW(), INTERVAL '-3 YEAR'));