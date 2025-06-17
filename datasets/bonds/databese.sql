/*create database bonds_analyze*/

create table result_all_ofz (
	id integer primary key,
	coupon_average decimal(4,2),
	coupon_average_dev decimal(4,2),
	doh_last_average decimal(4,2),
	doh_last_dev_average decimal(3,2),
	price_average decimal(4,2),
	price_dev_average decimal(3,1),
	volume_average bigint
);



