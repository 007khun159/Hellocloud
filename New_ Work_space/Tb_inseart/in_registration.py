import psycopg2

try:
    connection= psycopg2.connect(user ='webadmin',
                                password ='YKQnti46682',
                                host = 'node36984-env-papop.proen.app.ruk-com.cloud', 
                                port = '11256',
                                database ='workspace')
    
    cursor = connection.cursor()
    postgres_insert_query =""" INSERT INTO registration (id,student_id , subject_id, year , semester, grade ) VALUES(%s,%s,%s,%s,%s,%s)"""
    
    
    
    registration1 = (1,'6406022610031','060233113','2022','1','A')
    registration2 = (2,'6406022610031','060233201','2022','1','C')
    registration3 = (3,'6406022610032','060233113','2022','1','B')
    registration4 = (4,'6406022610032','060233201','2022','1','B+')
    registration5 = (5,'6406022610040','060233113','2022','1','C+')
    registration6 = (6,'6406022610040','060233201','2022','1','A')


    cursor.execute(postgres_insert_query,registration6)

    connection.commit()
    count = cursor.rowcount
    print(count,"Record inserted successfully into students table")


except (Exception,psycopg2.Error) as error: 
    if (connection):
        print('Failed to insert record into student table',error)

finally : 
    #closing database conection.
    if(connection):
        cursor.close()
        connection.close()
        print("Postagre conection is closed")

