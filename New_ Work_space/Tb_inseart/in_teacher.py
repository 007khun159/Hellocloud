import psycopg2

try:
    connection= psycopg2.connect(user ='webadmin',
                                password ='YKQnti46682',
                                host = 'node36984-env-papop.proen.app.ruk-com.cloud', 
                                port = '11256',
                                database ='workspace')


    cursor = connection.cursor()


    postgres_insert_query =""" INSERT INTO teachers (teacher_id , f_name , l_name , e_mail) VALUES(%s,%s,%s,%s)"""
    

    #data 
    teacher1 = ('AMK','Anirach','Minkwan','Anirach@gmail.com')
    teacher2 = ('WKN','Warachai','Kongsiriwatana','Warachai@gmail.com')
    teacher3 = ('KMN','Kanitta','Namee','Kanitta@gmail.com')
    cursor.execute(postgres_insert_query,teacher3)


    connection.commit()
    count = cursor.rowcount
    print(count,"Record inserted successfully into teachers table")


except (Exception,psycopg2.Error) as error: 
    if (connection):
        print('Failed to insert record into teachers table',error)

finally : 
    #closing database conection.
    if(connection):
        cursor.close()
        connection.close()
        print("Postagre conection is closed")

