#Documentation of the Project
# it is a kind of system is created by me in which you can create a files for managing marks,student details,listing making,grading and much more things you can do with system.it is very interactive for the user to work on it.

#limitation of the projects:
#it is may not produce exact result as per your wish.
#it may contain some bugs(Which can only knew by testing it)

def studentDetails():#this function is mainly for retrieving details of the students.
    import pickle #A module namely pickel is imported here. 
    file=open("students_details.dat","ab+") # A file is open namely "students_Details.dat" in append mode(it is used to create a file which simultaneously store data.)
    student={ } #empty dictionary declared
    print("NUMBER OF STUDENTS WANTS TO ENTER IN A FILE")  
    inp=int(input("ENTER A NUMBER OF STUDENTS"))
    for i in range(inp):
        print("........................................")
        print("ENTER THE DETAILS OF THE",inp,"STUDENTS")
        srno=int(input("ENTER SERIAL NUMBER OF THE STUDENT"))#it will take serial number from the user
        name=str(input("ENTER NAME OF THE STUDENT"))#it will take name of the student from the user
        clas=str(input("ENTER CLASS OF THE STUDENT"))#it will take class as well as course from the user
        specialisation=str(input("ENTER SPECIALISATION OF THE STUDENT"))#it will take specialisation of the student from the user
        student["SerialNo"]=srno #this will the value of the 'srno' to key 'serial number'.
        student["Name"]=name #this will the value of the 'name' to key 'Name'.
        student["Class"]=clas #this will the value of the 'clas' to key 'Class'.
        student["Specialisation"]=specialisation #this will the value of the 'specialisation' to key 'serial numbeSpecialisation'.
        pickle.dump(student,file) #all content of the dictionary saved in the file.
        
def viewDetails():
    import pickle
    file=open("students_details.dat","rb+") #a binary file is opened as file in reading mode
    details={} #empty dictionary
    try:
        while True:
            details=pickle.load(file) #file named student_details.dat is readed and assigning content into details.
            for i in details: #all content of variable will be transfered into i variable
                print(details[i]) #printing content of the file here.
                print("\t")
                print("...........................................")
                
            
    except EOFError:
        file.close()
        
        
def marks_uploading():#it is function for uploading Marks of the students.
    import pickle
    marks={}
    with open("Students_marks.dat","ab+") as file: #file namely Students_marks.dat is opened in appending mode (it means that in file content will be append without affect existing one.)
        inp=int(input("ENTER NUMBER OF THE STUDENT"))
        for i in range(inp+1):
                nam=str(input("ENTER THE NAME OF THE STUDENT"))
                sr=str(input("ENTER SERIAL NUMBER OF THE STUDENT OF WHOM YOU WANT'S UPLOAD MARKS"))
                maths=int(input("ENTER THE MARKS OF MATHEMATICS"))
                sst=int(input("ENTER THE MARKS OF SOCIAL SCIENCE"))
                gk=int(input("ENTER THE MARKS OF GENERAL KNOWLEDGE"))
                english=int(input("ENTER THE MARKS OF ENGLISH"))
                hindi=int(input("ENTER THE MARKS OF HINDI"))
                compu=int(input("ENTER THE MARKS OF COMPUTER"))
                science=int(input("ENTER THE NUMBERS OF SCIENCE"))
                marks["NAME"]=nam
                marks["SERIAL NUMBER"] = sr
                marks["MATHEMATICS"] = maths
                marks["SOCIAL SCIENCE"] = sst
                marks["GENERAL KNOWLEDGE"] = gk
                marks["ENGLISH"] = english
                marks["HINDI"] = hindi
                marks["COMPUTER"] = compu
                marks["SCIENCE"] = science
                pickle.dump(marks,file) #data or content of dictionary marks is copied to the file.

def print_report_card():    
    import pickle
    print("IT IS THE RESULT OF ALL THE STUDENTS")
    with open("Students_marks.dat","rb+") as result:
         marks=[]
         marks=pickle.load(result)
         print(marks)
        
def percentage_calculator():#it is a function for performing percentage calculation
    print("ENTER NUMBER OF SUBJECTS YOU WANTS TO CALCULATE")
    aggregate=0
    no_subjects=int(input("ENTER NO OF SUBJECTS"))
    if(no_subjects>=3) and (no_subjects!=8):
            if(no_subjects==3):
                sub_1=int(input("ENTER MARKS OF FIRST SUBJECT"))
                sub_2=int(input("ENTER MARKS OF SECOND SUBJECT"))
                sub_3=int(input("ENTER MARKS OF THIRD SUBJECT"))
                aggregate=sub_1+sub_2+sub_3
                print("YOUR TOTAL OF AGGREGATE OF ABOVE THREE SSUBJECTS",aggregate)
                maxi_marks=int(input("ENTER MAXIMUM MARLKS:"))
                percentage=aggregate/maxi_marks*100
                print("YOUR PECENTAGE IS:",percentage)
            if(no_subjects==4):
                sub_1=int(input("ENTER MARKS OF FIRST SUBJECT"))
                sub_2=int(input("ENTER MARKS OF SECOND SUBJECT"))
                sub_3=int(input("ENTER MARKS OF THREE  SUBJECT"))
                sub_4=int(input("ENTER MARKS OF FOURTH SUBJECT"))
                aggregate=sub_1+sub_2+sub_3+sub_4
                print("YOUR TOTAL OF AGGREGATE OF ABOVE THREE SSUBJECTS",aggregate)
                maxi_marks=int(input("ENTER MAXIMUM MARLKS:"))
                percentage=aggregate/maxi_marks*100
                print("YOUR PECENTAGE IS:",percentage)
            if(no_subjects==5):
                sub_1=int(input("ENTER MARKS OF FIRST SUBJECT"))
                sub_2=int(input("ENTER MARKS OF SECOND SUBJECT"))
                sub_3=int(input("ENTER MARKS OF THIRD SUBJECT"))
                sub_4=int(input("ENTER MARKS OF FOURTH SUBJECT"))
                sub_5=int(input("ENTER MARKS OF FIVETH SUBJECT"))
                aggregate=sub_1+sub_2+sub_3+sub_4+sub_5
                print("YOUR TOTAL OF AGGREGATE OF ABOVE THREE SSUBJECTS",aggregate)
                maxi_marks=int(input("ENTER MAXIMUM MARLKS:"))
                percentage=aggregate/maxi_marks*100
                print("YOUR PECENTAGE IS:",percentage)
            if(no_subjects==6):
                sub_1=int(input("ENTER MARKS OF FIRST SUBJECT"))
                sub_2=int(input("ENTER MARKS OF SECOND SUBJECT"))
                sub_3=int(input("ENTER MARKS OF THIRD SUBJECT"))
                sub_4=int(input("ENTER MARKS OF FOURTH SUBJECT"))
                sub_5=int(input("ENTER MARKS OF FIVETH SUBJECT"))
                sub_6=int(input("ENTER MARKS OF SIXTH SUBJECT"))
                aggregate=sub_1+sub_2+sub_3+sub_4+sub_5+sub_6
                print("YOUR TOTAL OF AGGREGATE OF ABOVE THREE SSUBJECTS",aggregate)
                maxi_marks=int(input("ENTER MAXIMUM MARLKS:"))
                percentage=aggregate/maxi_marks*100
                print("YOUR PECENTAGE IS:",percentage)

def listofstudents():#it is a function for creating a list of the student for different purposes.
    file=open("Studentlistbyfunction.txt","a+") #studentlisby function is text file means that it will store data in text form as well as in particular format
    namelist=str(input("ENTER THE NAME OF THE LIST"))
    file.write(namelist+"\n")
    print("NAME OF THE LIST IS SUCCESSFULLY ADDED IN  TEXT FILE")
    no_of_student=int(input("ENTER NO OF STUDENT YOU WANTS TO ENTER"))
    print("......................................................")
    for i in range(no_of_student+1):
        name=str(input("ENTER THE NAME OF STUDENT"))
        clas=str(input("ENTER THE CLASS OF STUDENT"))
        roll=str(input("ENTER THE ROLL NUMBER OF THE STUDENT"))
        sec=str(input("ENTER SESSION OF THE STUDENT"))
        detail=" NAME: "+name+" CLASS: "+clas+" ROLL NO: "+roll+" SESSION: "+sec+"\n"
        file.writelines(detail)
        print("DETAIL OF STUDENT IS SUCCESSFUL SAVED IN TEXT FILE\n")

def GradingSystem():
    print("ENTER YOUR PERCENTAGE TO KNOW ABOUT GRADE")
    percent=int(input("ENTER PERCENTAGE:"))
    print("..........................................................")
    grade=percent
    if(percent>0)and(percent<100):
        if grade >=100:
            print("A1")

        elif grade>=90:
            print("A2")
        
        elif grade>=80:
            print("B1")
        
        elif grade>=70:
            print("B2")

        elif grade>=60:
            print("C1")

        elif grade>=50:
            print("C2") 

        else:
            print("NO GRADE IS AVAILABLE    ")       
        
while True:
    print("1.ENTER THE DETAILS OF STUDENTS")
    print("2.MARKS UPLOADING")
    print("3.VIEW REPORT CARD OF STUDENTS")
    print("4.VIEW DETAILS OF ALL STUDENTS")
    print("5.CALCULATE PERCENTAGE")
    print("6.MAKE A LIST OF STUDENTS IN TEXT FILE.")
    print("7.VIEW GRADING SYSTEM")
    print("8.EXIT")
    choice=int(input("ENTER YOUR CHOICE"))
    if choice ==1:
        studentDetails()
        print("YOUR CHOICE IS PROCESSED...")
    elif choice==2:
        marks_uploading()
        print("YOUR CHOICE IS PROCESSED...")
        
    elif choice==3:
        print_report_card()
        print("YOUR CHOICE IS PROCESSED...")

    elif choice==4:
        viewDetails()
        print("YOUR CHOICE IS PROCESSED...")
        
    elif choice==5:
        percentage_calculator()
        print("YOUR CHOICE IS PROCESSED...")
    elif choice==6:
        listofstudents()
        print("YOUR CHOICE IS PROCESSED...")  
    elif choice==7:
        GradingSystem()
        print("YOUR CHOICE IS PROCESSED...")
    elif choice==8:
        print("YOUR CHOICE IS PROCESSED...")
        break
    else:
        print("YOUR CHOICE IS PROCESSED...")
        break
