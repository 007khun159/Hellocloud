import psycopg2

try:
    connection= psycopg2.connect(user ='webadmin',
                                password ='YKQnti46682',
                                host = 'node36984-env-papop.proen.app.ruk-com.cloud', 
                                port = '11256',
                                database ='postgres')

    connection.autocommit = True

    cursor = connection.cursor()

    sql = """CREATE database Newingwork_space"""

    cursor.execute(sql)

    print('Data create sucessful....')

except (Exception,psycopg2.Error) as error:
    print('Error while create',error)


finally:
    if(connection):
        cursor.close()
        connection.close()
        print('Postgres is closed')


