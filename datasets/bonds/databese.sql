/*create database bonds_analyze*/

create table result_ofz (
	id Integer primary key,
    dat date,
    coupon decimal(4,2),
    coupon_dev decimal(3,2),
    doh_last decimal(4,2),
    doh_last_dev decimal(3,2),
    price decimal(4,2),
    price_dev decimal(3,1),
    volume integer
);

create table result_all_ofz (
	coupon_average decimal(4,2),
    coupon_average_dev decimal(4,2),
    doh_last_average decimal(4,2),
    doh_last_dev_average decimal(3,2),
    volume_average integer
    
);



