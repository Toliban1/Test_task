Для работы требует установленных Mysql и redis.
В Mysql база данных test, таблица members с полями (
				member_id int(10) PRIkey auto_increment,
				fname  varchar(50)
				iname  varchar(50)
				tel    varchar(50)
				email  varchar(50)  )
В redis используется база 1 без пароля
'сервер' - index_server.py
'клиент' - test_server.py

