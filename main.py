#assignment
class Assignment:
    def __init__(self,subject,title,score, max_score,due_date, assignment_type):
        self.subject=subject
        self.title=title
        self.score=float(score)
        self.max_score=float(max_score)
        self.due_date=due_date
        self.assignment_type=assignment_type

#Inheritance
class Homework(Assignment):
    def __init__(self,subject,title, score, max_score, due_date, assignment_type,contribution_homework):
        self.contribution_homework= contribution_homework
        super().__init__(subject, title, score, max_score, due_date,assignment_type)  

class Exam(Assignment):
    def __init__(self,subject,title, score, max_score, due_date, assignment_type,contribution_exam):
        self.contribution_exam= contribution_exam
        super().__init__(subject, title, score, max_score, due_date,assignment_type) 

#Grade tracker: is an object that manage all assignments
#Adding, Listing, Filtering, Summarizing

class GradeTracker:
    def __init__(self):
        self.assignments=[]
#Adding:
    def add_assignment(self, assignment):
        if assignment.score<=assignment.max_score and assignment.score>=0 and assignment.max_score>0:
           self.assignments.append(assignment)  
        else:
            print("invalid score")      

#listing assignment
    def list_assignments(self):
        if self.assignments==[]:
            print("No listed asssignments available")
            print()
            return
        for assignment in self.assignments:
           print("subject:", assignment.subject)
           print("score:", assignment.score)
           print("maximum score:", assignment.max_score)
           print("title:", assignment.title)
           print("assignment type:", assignment.assignment_type)
           print("due date:", assignment.due_date)
           print()
#filtering assignment
    def filter_assignments(self):
        if self.assignments==[]:
            print("No filtered assignments available")
            print()
            return
        filter_requirement=input("what do you want to filter your assignment by (subject, type or month? ").strip().lower()
        

#filtering by subject     
        if filter_requirement=="subject":
            subject_name=input("subject name: ").strip().lower() #removing the white space and lowering the case
            for assignment in self.assignments:
                if subject_name==assignment.subject.strip().lower(): #removing the white space and lowering the case
                    print(assignment.subject)
                    print(assignment.title)
                    print(assignment.score)

#filtering by type               
        elif filter_requirement=="type":
            filter_type=input("Assignment type (homework or exam)?: ").strip().lower()   
            for assignment in self.assignments:
                if filter_type==assignment.assignment_type:
                    print(assignment.assignment_type)
                    print(assignment.subject)
                    print(assignment.title)
                    print(assignment.score)

#filtering by month
        elif filter_requirement=="month":
            month=input("Assignment month? ")
            match_count=0
            for assignment in self.assignments:
                if month==assignment.due_date.split("/")[1]:
                    match_count+=1
                    print(assignment.assignment_type)
                    print(assignment.subject)
                    print(assignment.title)
                    print(assignment.score)
                    print()
            if match_count==0:
                print("No assignment found in that month")                
        
        else:
            print("invalid filtering requirement")                    

#summarizing grades
    def summary(self):
        if self.assignments==[]:
            print("No asssignments available")
            print()
            return
        
        total_score=0
        total_max=0
#overall average scores
        for assignment in self.assignments:
            total_score+=assignment.score 
            total_max+=assignment.max_score
        average= (total_score/total_max)*100
        print("overall average in percentage=",((round(average,2))),"%")

# per subject average
        subject_scores={}
# incase it happens that the assignment has the exam and homework of the same subject
        for assignment in self.assignments: 
            if assignment.subject in subject_scores:
                    subject_scores[assignment.subject]+=assignment.score
            else:
                     subject_scores[assignment.subject]=assignment.score 

        subject_max_scores={}
        for assignment in self.assignments: 
            if assignment.subject in subject_max_scores:
                  subject_max_scores[assignment.subject]+=assignment.max_score
            else:
                subject_max_scores[assignment.subject]=assignment.max_score                                    

#the  per subject average of the assignment
        for subject in subject_scores:
            per_subject_average=(subject_scores[subject]/subject_max_scores[subject])*100
            print(subject,"= ", round(per_subject_average, 1),"%")
            print()

#highest/ lowest scoring assignment
#highest scoring assignment
        highest_assignment=max(self.assignments, key=lambda assignment:assignment.score/assignment.max_score)
        print("highest assignment subject= ", highest_assignment.subject)
        print("highest assignment score= ", highest_assignment.score)
        print("highest assignment max score= ", highest_assignment.max_score)
        print("highest assignment type= ", highest_assignment.assignment_type)
        print()

#lowest scoring assignment
        lowest_assignment=min(self.assignments, key=lambda assignment: assignment.score/assignment.max_score)
        print("lowest assignment subject= ", lowest_assignment.subject)
        print("lowest assignment score= ", lowest_assignment.score)
        print("lowest assignment max score= ", lowest_assignment.max_score)
        print("lowest assignment type= ", lowest_assignment.assignment_type)
        print()

grade_tracker=GradeTracker() 

def add_homework(grade_tracker):
    subject=input("Enter your subject: ")
    title=input("Enter your title: ")
    try:
        score=float(input("Enter your score: "))
        max_score=float(input("Enter your max score: "))
    except ValueError:
        print("Score and Max_score must be numbers")
    else:
        if score<=max_score and score>=0 and max_score>0:
            due_date=input("Enter your assignment date: ")
            new_homework=Homework(subject,title,score,max_score, due_date, "homework", 40)
            grade_tracker.add_assignment(new_homework)
        else:
              print("Invalid score")

def add_exam(grade_tracker):
    subject=input("Enter your subject: ")
    title=input("Enter your title: ")
    try:
        score=float(input("Enter your score: "))
        max_score=float(input("Enter your max score: "))
    except ValueError:
        print("Score and Max_score must be numbers")
    else:
        if score<=max_score and score>=0 and max_score>0:
            due_date=input("Enter your assignment date: ")
            new_exam=Exam(subject,title,score,max_score, due_date, "exam", 60)
            grade_tracker.add_assignment(new_exam)
        else:
            print("Invalid score")                

#menu choices
while True:
    print("1. Add homework")
    print("2. Add exam")
    print("3. List assignments")
    print("4. Filter assignments by(subject, type, month?)")
    print("5. Show summary")
    print("0. Exit")
    menu_choice=input("Enter your choice: ")
    if menu_choice=="1":
        add_homework(grade_tracker)

    elif menu_choice=="2":
        add_exam(grade_tracker)
                     

    elif menu_choice=="3":
        grade_tracker.list_assignments()

    elif menu_choice=="4":
        grade_tracker.filter_assignments()

    elif menu_choice=="5":
        grade_tracker.summary()

    elif menu_choice=="0":
        break
    
    else:
        print("Invalid menu choice")
    print()
    




            

 