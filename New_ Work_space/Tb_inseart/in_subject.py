import psycopg2

try:
    connection= psycopg2.connect(user ='webadmin',
                                password ='YKQnti46682',
                                host = 'node36984-env-papop.proen.app.ruk-com.cloud', 
                                port = '11256',
                                database ='workspace')
    
    cursor = connection.cursor()
    postgres_insert_query =""" INSERT INTO subjects ( subject_id, subject_name , creadit    , teacher_id   ) VALUES(%s,%s,%s,%s)"""

    subject1 = ('060233113','ADVANCED COMPUTER PROGRAMMIN',3,'AMK')
    subject2 = ('060233201','NETWORK ENGINEERING LABORATO',1,'WKN')
    subject3 = ('060233205','ADVANCED NETWORK AND PROTOCO',3,'KNM')


    cursor.execute(postgres_insert_query,subject3)

    connection.commit()
    count = cursor.rowcount
    print(count,"Record inserted successfully into subjects table")


except (Exception,psycopg2.Error) as error: 
    if (connection):
        print('Failed to insert record into subjects table',error)

finally : 
    #closing database conection.
    if(connection):
        cursor.close()
        connection.close()
        print("Postagre conection is closed")

