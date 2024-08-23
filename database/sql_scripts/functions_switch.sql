SELECT
	order_id,
	CASE
		WHEN to_char(order_date::date, 'yyyy') = to_char(now()::date, 'yyyy') THEN 'Active'
		WHEN CAST(to_char(order_date::date, 'yyyy') AS INTEGER) = CAST(to_char(now()::date, 'yyyy')AS INTEGER)  - 1 THEN 'Last Year'
		WHEN CAST(to_char(order_date::date, 'yyyy') AS INTEGER) = CAST(to_char(now()::date, 'yyyy')AS INTEGER)  - 2 THEN 'Archived'
		ELSE 'Future'
	END AS category
FROM public.orders;