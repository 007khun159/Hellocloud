import psycopg2
import 

try:
    connection= psycopg2.connect(user ='webadmin',
                                password ='YKQnti46682',
                                host = 'node36984-env-papop.proen.app.ruk-com.cloud', 
                                port = '11256',
                                database ='workspace')
    
    cursor = connection.cursor()
    postgres_insert_query =""" INSERT INTO students (student_id , f_name , l_name , e_mail) VALUES(%s,%s,%s,%s)"""
    record_to_insert1 = ('6406022610040','Pawarit',
                        'Pitirit','s6406022610040@fitm.kmutnb.ac.th')
    record_to_insert2 = ('6406022610032','Nititat'
                        ,'Bangpha','6406022610032@fitm.kmutnb.ac.th')
    record_to_insert3 = ('6406022610031','Papop','Sangeamsak'
                        ,'6406022610031@fitm.kmutnb.ac.th')


    # cursor.execute(postgres_insert_query,record_to_insert3)

    #connection.commit()
    #count = cursor.rowcount
    #print(count,"Record inserted successfully into students table")

    result = Students.query.all()

except (Exception,psycopg2.Error) as error: 
    if (connection):
        print('Failed to insert record into student table',error)

finally : 
    #closing database conection.
    if(connection):
        cursor.close()
        connection.close()
        print("Postagre conection is closed")

