import psycopg2

try:
    connection= psycopg2.connect(user ='webadmin',
                                password ='YKQnti46682',
                                host = 'node36984-env-papop.proen.app.ruk-com.cloud', 
                                port = '11256',
                                database ='workspace')

    connection.autocommit = True

    cursor = connection.cursor()   
    #Not null บังคับใส่
    create_table_query = ''' CREATE TABLE Students 
            (student_id  CHAR(13) PRIMARY KEY,
             f_name      VARCHAR(30) NOT NULL,     
             l_name      VARCHAR(30) NOT NULL,
             e_mail      VARCHAR(50)   );'''
    
    #Creating a database 
    cursor.execute(create_table_query)
    connection.commit()
    print("Database created successfully in PostgreSQL")


except (Exception, psycopg2.DatabaseError) as error : 
    print('Error while connectiong to PostgreSQL',error)
    
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")