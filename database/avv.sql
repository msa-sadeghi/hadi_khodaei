-- SELECT * FROM online_shop.order_details;
-- ALTER table online_shop.order 
-- DROP foreign key order_ibfk_1;
-- ALTER table online_shop.order DROP INDEX user_id;
-- ALTER table online_shop.order ADD foreign key(user_id) references user(id);


-- ALTER TABLE online_shop.cart DROP quantity;
ALTER TABLE online_shop.cart DROP foreign key cart_ibfk_2;

ALTER TABLE online_shop.cart DROP product_id;