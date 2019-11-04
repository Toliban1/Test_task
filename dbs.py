class Mysql_inter:

    def read(connection):
        with connection.cursor() as cursor:
            sql = "SELECT * FROM members"
            cursor.execute(sql)
            data = cursor.fetchall()
        return data

    def write(connection, fname, iname, tel, email):
        with connection.cursor() as cursor:
            sql = "INSERT INTO members (fname, iname, tel, email) VALUES ('{}', '{}', '{}', '{}')".format(fname, iname, tel, email)
            cursor.execute(sql)
            return True


class Redis_inter:

    key = 'test_key'

    def read(r):
        response = r.get(Redis_inter.key)
        if type(response) == 'NoneType':
            return 'Нет ключа ' + Redis_inter.key
        else:
            return response.decode("utf-8")


    def write(r, value):
        print('set to redis : ', Redis_inter.key, ' : ', value)
        r.set(Redis_inter.key, value)
        return True







