Select students.student_id , students.f_name , students.l_name, registration.subject_id ,
subjects.subject_name,registration.grade,teachers.f_name,teachers.l_name
 
 From students
 join registration on students.student_id = registration.student_id
 join subjects on registration.subject_id = subjects.subject_id
 join teachers on subjects.teacher_id  = teachers.teacher_id
 
 
 
 ;