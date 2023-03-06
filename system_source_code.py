import datetime
from os import remove
import random
from datetime import date, timedelta




                            ############################# Book section ##############################
books = {}
all_books=[]

class Books:
      
    # constructor to build an object
 def __init__(self):
          
      self.book_ID = random.randint(0,1000)
 #methods to set each of the books attribute and check if duplicate title or title is empty or less than 3 characters or in digits 
 def setTitle(self): 
             self.title = input('Enter Title: ')
             while len(self.title)== 0 or len(self.title)< 3 or self.title.isdigit(): 
              print("Enter correct title to proceed")
              self.title = input('Enter title: ')
              
             for item in all_books:
              while self.title == item["Title"]:              
                 print("Duplicate title")
                 self.title = input('Enter Title: ')

        
               
 def setAuthor(self):
             self.author = input('Enter Author: ')
             while len(self.author)== 0 or len(self.author)< 3 or self.author.isdigit(): 
              print("Enter correct author to proceed")
              self.author = input('Enter author: ')
 def setYear(self): # check if year in digit or if less than 3 digits
            self.year = input('Enter Year: ')
            while (self.year).isnumeric()==False or len(self.year)< 4: 
             print("Enter correct Year to proceed")
             self.year = input('Enter Year: ')

 def setPublisher(self):
             self.publisher = input('Enter Publisher: ')
 def set_numberofCopies(self):
             self.available_copies = input('Enter Number of available copies: ')
 def set_publicationDate(self):
             self.publication_date = input('Enter Publication Date: ')
 def set_bookID(self):
        print("Generated ID:",self.book_ID)

 #methods to return each attribute for the book 
 def return_bookID(self):
        print("**Current book ID:** ", self.book_ID)

 def return_title(self):
        print("**Current book title:**", self.title)
 
 def return_author(self):
        print("**Current book author:**", self.author)  

 def return_year(self):
        print("**Current book year:** ", self.year)
 
 def return_publisher(self):
        print("**Current book publisher:** ", self.publisher)

 def return_number_copies(self):
        print("**Number of available copies for Current book:** ", self.available_copies)

 def return_date(self):
        print("**Publication date of current book:** ", self.publication_date)

 
  # method to modify the book entries
 def modify_book(self):
       ask = input("Do you want to modify attribute (Please enter Yes or NO) ")
       ask = ask.upper()
       if ask =="YES":
         modifier=(input("which entry do you want to modify?"))
         while modifier not in Book_modifiers:
          print("you have to choose from",modifiers)
          modifier=(input("which attribute you want to modify?"))
         if modifier == "title":
          self.title = input('Enter Title: ')
         elif modifier == "author":
             self.author = input('Enter Author: ')
         elif modifier == "year":
             self.year = input('Enter Year: ')
            
         elif modifier == "publisher":
             self.publisher = input('Enter Publisher: ')
             
         elif modifier == "number of copies":
             self.available_copies = input('Enter number of available copies: ')
             
         elif modifier not in Book_modifiers:
              print("you have to choose from",Book_modifiers)

       else:
              pass

 





                   ############################# Users Section ##############################
all_users=[]
users={}
countUsers=[]
class Users:
      
    # constructor
 def __init__(self):
      
   self.username = input('Enter Username: ')
 # methods to set each attribute 
 def setfirstname(self):
             self.firstname = input('Enter Firstname: ')
             while len(self.firstname)== 0 or len(self.firstname)< 3 or self.firstname.isdigit(): 
              print("Enter correct name to proceed")
              self.firstname = input('Enter Firstname: ')
             
 def setsurname(self):
             self.surname = input('Enter Surname: ')
             while len(self.surname)== 0 or len(self.surname)< 3 or self.surname.isdigit(): 
              print("Enter correct surname to proceed")
              self.surname = input('Enter Surname: ')
 def sethouse_number(self):
            self.house_number = input('Enter House Number: ')
 def set_street_name(self):
             self.street_name = input('Enter Street Name: ')
             while len(self.street_name)== 0 or len(self.street_name)< 3 or self.street_name.isdigit(): 
              print("Enter correct street_name to proceed")
              self.street_name = input('Enter Street Name: ')
 def setpostcode(self):
             self.postcode = input('Enter Post Code: ')
 def setemail_address(self):
             self.email_address = input('Enter Email Address: ')
 def setdate_of_birth(self):
             self.date_of_birth = input('Enter Date of Birth: ')
 
 # method to modify the user data 
 
 def modify(self):
       ask = input("Do you want to modify attribute (Please enter Yes or NO) ")
       ask = ask.upper()
       if ask =="YES":
         modifying=(input("which attribute you want to modify?"))
         while modifying not in modifiers:
          print("you have to choose from",modifiers)
          modifying=(input("which attribute you want to modify?"))
       
         if modifying == "username":
          self.username = input('Enter Username: ')
         elif modifying == "firstname":
             self.firstname = input('Enter Firstname: ')
             while len(self.firstname)== 0 or len(self.firstname)< 3 or self.firstname.isdigit(): 
              print("Enter correct firstname to proceed")
              self.firstname = input('Enter Firstname: ')
         elif modifying == "surname":
             self.surname = input('Enter Surname: ')
             while len(self.surname)== 0 or len(self.surname)< 3 or self.surname.isdigit(): 
              print("Enter correct surname to proceed")
              self.firstname = input('Enter Firstname: ')
         elif modifying == "housenumber":
             self.house_number = input('Enter House Number: ')
         elif modifying == "streetname":
             self.street_name = input('Enter Street Name: ')
         elif modifying == "postcode":
             self.postcode = input('Enter Post Code: ')
         elif modifying == "email":
             self.email_address = input('Enter Email Address: ')
         elif modifying == "birthdate":
             self.date_of_birth = input('Enter Date of Birth: ')
         elif modifying not in modifiers:
              print("you have to choose from",modifiers)

       else:
              pass
       
 # methods to edit the user data 
 def return_username(self):
             print('**Username:',self.username)
 def return_firstname(self):
             print('** Firstname: ',self.firstname)
 def return_surname(self):
             print('** Surname: ',self.surname)
 def return_house_number(self):
             print('** House Number: ',self.house_number)        
 def return_street_name(self):
             print('** Street Name: ',self.street_name)         
 def return_postcode(self):
             print('** Post Code:',self.postcode)       
 def return_email(self):
             print('** Email Address: ',self.email_address)           
 def return_date_of_birth(self):
             print('** Date of Birth: ',self.date_of_birth)              
 def edit_username(self):
       value=(input(" Enter the new username"))
       self.username=value
       print(" **The new username :", self.username)  
 def edit_firstname(self):
       value=(input(" Enter the new firstname: "))
       self.firstname=value
       print(" ** The new firstname :",  self.firstname)  
 def edit_Surname(self):
       value=(input("Enter the new surname: "))
       self.surname=value
       print(" ** The new surname :",  self.surname)    
 def edit_housenumber(self):
       value=(input("Enter the new house_number: "))
       self.house_number=value
       print(" ** The new house_number :",  self.house_number)    
 def edit_streetname(self):
       value=(input("Enter the new street_name: "))
       self.street_name=value
       print("** The new street_name :", self.street_name)         
 def edit_postcode(self):
       value=(input("Enter the new postcode: "))
       self.postcode=value
       print("** The new postcode :", self.postcode)         
 def edit_email(self):
       value=(input("Enter the new email_address: "))
       self.email_address=value
       print("** The new email_address:", self.email_address)         
 def editdate_ofBirth(self):
       value=(input("Enter the new date_of_birth: "))
       self.date_of_birth=value
       print("** The new date_of_birth :", self.date_of_birth)                 

            ############################# Bookslists Section ##############################

booklists=[]
booklisting={}

class booklist:
   # constructor

 def __init__(self):
          
    self.collection_name = input('Enter Booklist Title: ')
    booklists.append(self.collection_name)
    #create book instance from Books class inside a booklist 
 def add_book(self): 
  new_book=Books()
  new_book.ID=random.randint(0,1000)
  new_book.title=(input("Enter the book title: "))
  new_book.author=(input("Enter author: "))
  new_book.year=(input("Enter year: "))
  new_book.publisher=(input("Enter publisher: "))
  new_book.available_copies=(input("Enter available_copies: "))
  new_book.publication_date=(input("Enter you book publication date: "))
   # save new instance in books class
  books= {'ID':new_book.book_ID,'Title':new_book.title,'Author':new_book.author,'Year':new_book.year,'publisher':new_book.publisher,'Number':new_book.available_copies,'Date':new_book.publication_date}
  all_books.append(books)
  
  # save the book inside the booklist 
  booklisting={'Collection name':self.collection_name,'Book ID':new_book.ID,'Title':new_book.title,'Author':new_book.author,'Year':new_book.year,'Publisher':new_book.publisher,'Number of Available copiees':new_book.available_copies,'Publication Date':new_book.publication_date}
  booklists.append(booklisting)


  print("Books menu:",all_books)
  print("booklists menu",booklisting)
  print("All booklists menues",booklists)
   
  # Search for book title through the collection
 
 def search():
  
   Searchit= input('Enter the book title to search for it: ')
   for item in all_books:
       if item['Title'] == Searchit :
             print("The book details:",item)
       else:
            print("not found")
  
   


 # count how many books in the current booklist
 def counter(): 
   print("Number of Books:",len(all_books))

 # to remove book
 def remove_book(): # to remove book
  reovebook=(input("Enter the book title: ")) 
  for item in all_books:
    if item['Title'] == reovebook :
     all_books.remove(item)
     print("Book Removed")
    print("Remaining books:",all_books)







           ############################# Userslists Section ##############################

userslists={}
all_lists=[]

class userlist:
 def __init__(self):
  
  self.list_name= (input("Enter your list name: "))
  userslists={'List name':self.list_name}
  all_lists.append(userslists) 
  print("All UsersLists: ", all_lists)

 def create_users(self): # to create_users users in the userlist 

  user_instances=Users()
  user_instances.username=(input("Enter username for the new user: "))
  user_instances.firstname = input('Enter Firstname: ')
  user_instances.surname = input('Enter Surname: ')
  user_instances.house_number = input('Enter House Number: ')
  user_instances.street_name = input('Enter Street Name: ')
  user_instances.postcode = input('Enter Post Code: ')
  user_instances.email_address = input('Enter Email Address: ')
  user_instances.date_of_birth = input('Enter Date of Birth: ')
  
  users={'Username':user_instances.username,'Firstname':user_instances.firstname,'surname':user_instances.surname,'Housenumber':user_instances.house_number,'Streetname':user_instances.street_name,'Postcode':user_instances.postcode,'Email':user_instances.email_address,'DateBirth':user_instances.date_of_birth}

  countUsers.append(user_instances.username)

  userslists={'List name':self.list_name,'Username':user_instances.username,'Firstname':user_instances.firstname,'surname':user_instances.surname,'Housenumber':user_instances.house_number,'Streetname':user_instances.street_name,'Postcode':user_instances.postcode,'Email':user_instances.email_address,'DateBirth':user_instances.date_of_birth}
  all_users.append(userslists) 
  

  print("** All userslist with their users:** ", all_users)
 
 def count_users(): # to count how many users in the system  
    print("Number of users: ",len(countUsers))

 def user_details(): # to print user details based on the username 
     
     user_username=(input("Enter the username: ")) 
     
     for item in all_users:
      if item['Username'] == user_username :
       print("The user details:",item)
   

  
    
        
 
 def remove_user(): # to remove user based on firstname 
    removeuser=(input("Enter the Firstname: ")) #count how many times the name is repeated
    
    count=0
    for item in all_users:
     if removeuser in item["Firstname"]:
      count = count + 1
    
    for item in all_users:
      if item['Firstname'] == removeuser and count < 2: 
       all_users.remove(item)
       break
      else:
        removeuser= print("duplicate names, enter the surname instead")
       
      
   

          




    
      
    print("Userslists:",all_users)



##############################Loans##############################

Loans={}
all_loans=[]

class loan:
  # constructor
 def __init__(self):
          
        # keys are initialized with
        # their respective values
   
  self.username = input('Enter username: ')
  self.Firstname = input('Enter firstname: ')
  self.bookname = input('Enter the book name: ')
  today = date.today()# to give the loan date 
  self.date = today.strftime("%Y-%m-%d")

  self.surname = input('Enter the surname: ')
  self.house_number = input('Enter the house_number: ')
  self.street_name = input('Enter the street_name: ')
  self.postcode = input('Enter postcode: ')
  self.email_address = input('Enter email_address: ')
  self.date_of_birth = input('Enter date_of_birth: ')
  
  Loans={'username':self.username,'first_name':self.Firstname,'bookname':self.bookname,'date':self.date}
  all_loans.append(Loans)
  print("Loans:",all_loans)
  
 def borrow():
  
  new_loan=loan()
  Loans={'username':new_loan.username,'first_name':new_loan.Firstname,'bookname':new_loan.bookname,'date':new_loan.date}

  users={'Username':new_loan.username,'Firstname':new_loan.Firstname,'surname':new_loan.surname,'Housenumber':new_loan.house_number,'Streetname':new_loan.street_name,'Postcode':new_loan.postcode,'Email':new_loan.email_address,'DateBirth':new_loan.date_of_birth} ## To save it in the user class, so when we call users they will show up.
  all_users.append(users)
  print("All Loans:",all_loans)
  


 def unborrow():# to return a book 

  un_borrowed_book=(input("Enter the book name to return: "))
  
  for item in all_loans:
    if item['bookname'] == un_borrowed_book:
       all_loans.remove(item)
  print("All Loans", all_loans)



 def overdue_Loans(): #calculating loans over due

   for item in all_loans:
    Begindate = datetime.datetime.strptime(item['date'], "%Y-%m-%d")
    Enddate = Begindate + timedelta(days=7)
    end_date = Begindate + datetime.timedelta(days=int(7))
    s=end_date.strftime('%Y-%m-%d')
    #print("** Loan Details Username:",item['username'],"Loan Due Date:",s)
    n=item['username']
    for item in userslists:
     if item['Username'] == n :
      print("The user details:",item)
    print("** Loan Details Username:",item ,"LoanDue date:",s)

   






 # count how many books the user is currently borrowing
 def countLoans():
  user=(input("Enter the username: ")) #count how many loans the user have
  count=0
  for item in all_loans:
    if user == item["username"]:
      count = count + 1
  print("the number of borrowed books:",count)
    
   
 
 ############################## For the main function ##############################           
        
#function used with all classes, after each process that the user done, it asks if the user needs to repeat the same process again for different entries 
def more():
            new_user = input("Do you want to add more? (Please enter Yes or NO) ")
            new_user = new_user.upper()
            if new_user =="YES":
                return True
                
            else:
                return False


# accepted entries for modifying user's attribute 
modifiers=["username","firstname","surname","housenumber","streetname","postcode","email","birthdate"]
Book_modifiers=["title","author","year","publisher","number of copies"]
answers=["1","3","4","5","6","7","8","9","10","11","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27"]




##############################MAIN##############################
 # the main function
def main():      

    done=False
    while done==False:
            print("""                  
                  ========== Books Menu ===========
                  1. Add book
                   
   
                  ========== Users Menu ===========
                  3. Add user
                  4. Change user username
                  5. Change user firstname
                  6. Change user Surname
                  7. Change user house number
                  8. Change user street name
                  9.Change user post code
                  10.Change user email address
                  11.Change user data of birth
                  
                  


                   ========= Bookslists Menu ===========
                  13. Add booklist 
                  14.Add book to the booklist
                  15.Search for book
                  16.Number of books in collection
                  17.Remove Book

                  ========= Userlists Menu ===========
                  18. Add userslists
                  19.create_users collection of users in list
                  20.Number of users 
                  21.Return user's detail
                  22.Remove user based on firstname 
                  

                  ========== Loans Menu ===========
                  23.Add new loan
                  24.borrow book
                  25.return book
                  26.Loans due date   
                  27.Number of Loans
                  
                  """)
             # ask the user for choice and check the coice entry 
            choice=int(input("Enter Choice:"))
            if choice==1:
                  book = Books()
      
                  book.setTitle()
                  book.setAuthor()
                  book.setYear()
                  book.setPublisher()
                  book.set_numberofCopies()
                  book.set_publicationDate()
                  book.set_bookID()
                  book.modify_book()
                  #print(book.__dict__)
                  books= {'ID':book.book_ID,'Title':book.title,'Author':book.author,'Year':book.year,'publisher':book.publisher,'Number':book.available_copies,'Date':book.publication_date}
                  all_books.append(books)

                  book.return_bookID()
                  book.return_title()
                  book.return_author()
                  book.return_year()
                  book.return_publisher()
                  book.return_number_copies()
                  book.return_date()
                  
                  
                  
                  print("All Books in the library:",all_books)

                  while more():
                        book = Books()
                        book.setTitle()
                        book.setAuthor()
                        book.setYear()
                        book.setPublisher()
                        book.set_numberofCopies()
                        book.set_publicationDate()
                        book.set_bookID()
                        book.modify_book()
                        books= {'ID':book.book_ID,'Title':book.title,'Author':book.author,'Year':book.year,'publisher':book.publisher,'Number':book.available_copies,'Date':book.publication_date}
                        all_books.append(books)
                        
                       

                        book.return_bookID()
                        book.return_title()
                        book.return_author()
                        book.return_year()
                        book.return_publisher()
                        book.return_number_copies()
                        book.return_date()
                       
                        
                        print("All Books in the library:",all_books)
                        
            

            elif choice==3:
                        # object user of class Users
                  user = Users()
                  user.setfirstname()
                  user.setsurname()
                  user.sethouse_number()
                  user.set_street_name()
                  user.setpostcode()
                  user.setemail_address()
                  user.setdate_of_birth()
                  user.return_username()
                  user.return_firstname()
                  user.return_surname()
                  user.return_house_number()
                  user.return_street_name()
                  user.return_postcode()
                  user.return_email()
                  user.return_date_of_birth()
                  user.modify()
                  users={'Username':user.username,'Firstname':user.firstname,'surname':user.surname,'Housenumber':user.house_number,'Streetname':user.street_name,'Postcode':user.postcode,'Email':user.email_address,'DateBirth':user.date_of_birth}
                  all_users.append(users)
                  countUsers.append(user.username)
                  
                  while more():
                       user = Users()
                       user.setfirstname()
                       user.setsurname()
                       user.sethouse_number()
                       user.set_street_name()
                       user.setpostcode()
                       user.setemail_address()
                       user.setdate_of_birth()

                       user.return_username()
                       user.return_firstname()
                       user.return_surname()
                       user.return_house_number()
                       user.return_street_name()
                       user.return_postcode()
                       user.return_email()
                       user.return_date_of_birth()

                       user.modify()
                       
                  
                       users={'Username':user.username,'Firstname':user.firstname,'surname':user.surname,'Housenumber':user.house_number,'Streetname':user.street_name,'Postcode':user.postcode,'Email':user.email_address,'DateBirth':user.date_of_birth}
                       all_users.append(users)
                       print("All users:", all_users)
                       countUsers.append(user.username)
                  
            elif choice==13:
              
             newbooklist= booklist()
             print("Booklists", booklists)
              
            elif choice==18:
             new_list=userlist()
             while more():
              new_list=userlist()

            elif choice==4:
                user.edit_username()
                users={'Username':user.username,'Firstname':user.firstname,'surname':user.surname,'Housenumber':user.house_number,'Streetname':user.street_name,'Postcode':user.postcode,'Email':user.email_address,'DateBirth':user.date_of_birth}
                print("Users:",users)
            elif choice==5:
                user.edit_firstname()
                users={'Username':user.username,'Firstname':user.firstname,'surname':user.surname,'Housenumber':user.house_number,'Streetname':user.street_name,'Postcode':user.postcode,'Email':user.email_address,'DateBirth':user.date_of_birth}
                print("Users:",users)
            elif choice==6:
                user.edit_Surname()
                users={'Username':user.username,'Firstname':user.firstname,'surname':user.surname,'Housenumber':user.house_number,'Streetname':user.street_name,'Postcode':user.postcode,'Email':user.email_address,'DateBirth':user.date_of_birth}
                print("Users:",users)
            elif choice==7:
                user.edit_housenumber()
                users={'Username':user.username,'Firstname':user.firstname,'surname':user.surname,'Housenumber':user.house_number,'Streetname':user.street_name,'Postcode':user.postcode,'Email':user.email_address,'DateBirth':user.date_of_birth}
                print("Users:",users)
            elif choice==8:
                user.edit_streetname()
                users={'Username':user.username,'Firstname':user.firstname,'surname':user.surname,'Housenumber':user.house_number,'Streetname':user.street_name,'Postcode':user.postcode,'Email':user.email_address,'DateBirth':user.date_of_birth}
                print("Users:",users)
            elif choice==9:
                user.edit_postcode()
                users={'Username':user.username,'Firstname':user.firstname,'surname':user.surname,'Housenumber':user.house_number,'Streetname':user.street_name,'Postcode':user.postcode,'Email':user.email_address,'DateBirth':user.date_of_birth}
                print("Users:",users)
            elif choice==10:
                user.edit_email()
                users={'Username':user.username,'Firstname':user.firstname,'surname':user.surname,'Housenumber':user.house_number,'Streetname':user.street_name,'Postcode':user.postcode,'Email':user.email_address,'DateBirth':user.date_of_birth}
                print("Users:",users)
            elif choice==11:
                user.editdate_ofBirth()
                users={'Username':user.username,'Firstname':user.firstname,'surname':user.surname,'Housenumber':user.house_number,'Streetname':user.street_name,'Postcode':user.postcode,'Email':user.email_address,'DateBirth':user.date_of_birth}
                print("Users:",users)  
            elif choice==15:
                booklist.search()
            elif choice==16:
                booklist.counter()
            elif choice==17:
              booklist.remove_book()
              while more():
               booklist.remove_book()
            elif choice==23:
              new_loan=loan()
              while more():
               new_loan=loan()
            elif choice==24:
              loan.borrow()
            elif choice==25:
              loan.unborrow()
            elif choice==26:
              loan.overdue_Loans()
            elif choice==19:
              new_list=userlist()
              new_list.create_users()
              while more():
               new_list.create_users() 
            elif choice==20:
              userlist.count_users()
            elif choice==21:
              userlist.user_details()
            elif choice==22:
              userlist.remove_user()
            elif choice==14:
              newbooklist= booklist()
              newbooklist.add_book()
              while more():
                newbooklist.add_book()
            elif choice==27:
              loan.countLoans()
            
            elif choice not in answers:
              print("Wrong option")


# Run the system and error handling            
            
try:
 main()
except:
       print("something went wrong try again")
       main()



