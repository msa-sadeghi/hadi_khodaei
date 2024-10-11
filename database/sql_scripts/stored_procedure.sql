DROP PROCEDURE IF EXISTS get_clients_by_state;

CREATE PROCEDURE get_clients_by_state(s char(2), INOUT r refcursor) 
LANGUAGE plpgsql
AS $$

BEGIN

    IF  s  IS NULL THEN
		  open r for SELECT *  FROM public.clients ;
		
	ELSE
		  open r for SELECT *  FROM public.clients c WHERE s = c.state;
		
	END IF;
	
END; $$;

CALL get_clients_by_state('CA', 'test');
fetch all in "test";



CREATE PROCEDURE get_clients_by_state_2(state char(2), INOUT r refcursor)
LANGUAGE plpgsql
AS $$
BEGIN
	open r for SELECT * FROM public.clients c
	WHERE c.state = NULLIF(state, c.state);
END; $$;

CALL get_clients_by_state(NULL, 'test');
fetch all in "test";