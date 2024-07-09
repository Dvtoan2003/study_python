from student import Student
sv=[]
while True:
    print(
        '''
        Please choose option:
        0.exit
        1.View all student
        2.add student
        3.delete student
        4.edit student
        '''
    )
    select=input('what do you want choose option?')
    if select.isdigit():
        select=int(select)
        if select==0:
            break
        elif select==1:
            if len(sv)==0: print('has no student')
            else: 
                for i in sv:
                    i.show()
        elif select==2:
            id = input('ID student:')
            name= input('name student:')
            sv.append(Student(id,name))
        elif select==3:
            id = input('enter ID student want to Delele:')
            for i in sv:
                if i.id==id:
                    sv.remove(i)
        elif select==4:
            id = input('Enter ID student want to Update:')
            for i in sv:
                if i.id==id:
                    i.set_name(input('enter new name: '))
            
        
    else:
        print('please choose again!')
