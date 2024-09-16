from tkinter import*
from tkinter import messagebox




##### start of importing databases #####
import boss_database_backend
import cars_database_backend
import customers_database_backend
import employee_database_backend
import rentals_database_backend
##### end of importing databases #####








##### Start of frame switches #####
## goes from customer/employee page to customer signup/login
def frame_switch1():
    frame1.forget()
    frame2.pack()




    
## goes from customer/employee page to employee/boss login
def frame_switch2():
    frame1.forget()
    frame3.pack()




    
## goes from customer signup/login to customer signup
def frame_switch3():
    frame2.forget()
    frame4.pack()





## goes from customer signup/login to customer login
def frame_switch4():
    frame2.forget()
    frame7.pack()



    

## goes from customers sign up to customers login 
def frame_switch4_2():
    frame4.forget()
    frame7.pack()



    

## goes from boss/employee login page to employee login page
def frame_switch5():
    frame3.forget()
    frame5.pack()

    



## goes from boss/employee login page to boss login page
def frame_switch6():
    frame3.forget()
    frame6.pack()

    



## goes from customers login page to customers cars page
def customer_cars_frame():
    frame7.forget()
    frame8.pack()



    

## goes from boss loging page to boss menu page
def boss_menu_frame():
    frame6.forget()
    frame10.pack()



    

## goes from employees login page to employees menu page
def employee_menu_frame():
    frame5.forget()
    frame9.pack()



    

## authentication for customer car buy/rent/finance
def authentication():
    frame8.forget()
    frame11.pack()




    
## goes from customers cars page to buy car page
def car_buy():

    global customer_frame
    global frame12

    customer_frame = "buy"

    #records sale and produces a success message 
    def confirm_sale():

        messagebox.showinfo("SUCCESS", "Your car awaits you at hamia motors\nAn email will be sent to you containing the details of the sale\nPlease come into store to complete the transaction.")         

        with open("sales.txt","a") as sales:
            sales.write(str(selected_tuple_ccm[4])+"\n")
            
            
        #makes a list of the transaction details writes them in a file   
        transaction_details = [selected_tuple_ccm, "S"]
        
        with open("car_history.txt","a") as sold_cars:
            sold_cars.write(str(transaction_details)+"\n")

        #removes the car from the main database as its no longer available
        cars_database_backend.delete(selected_tuple_ccm[0])

        cust_loop()


    frame11.forget()


    #Frame12 - buying car page  
    frame12 = Frame(window1)

    #displays car brand
    display_car_buy = Label(frame12, text = f"Car: {selected_tuple_ccm[1]}")
    display_car_buy.grid(row = 0, column = 0)

    #displays car model
    display_model_buy = Label(frame12, text = f"Model: {selected_tuple_ccm[2]}")
    display_model_buy.grid(row = 1, column = 0)

    #displays car price 
    display_price_buy = Label(frame12, text = f"Price: {selected_tuple_ccm[4]}")
    display_price_buy.grid(row = 2, column = 0)

    #confirms purchace 
    confirm_purchase_button = Button(frame12, text = "Confirm Purchase", command = confirm_sale)
    confirm_purchase_button.grid(row = 5, column = 0)
    
    frame12.pack()




    
## goes from customers cars page to rent car page
def car_rent():

    global customer_frame
    global frame13

    customer_frame = "rent"

    #calclates the cost of the rental 
    def calculate_rental(*args):
        global total_rent_cost
        
        total_rent_cost = int(rental_period_text.get().strip()) * int(selected_tuple_ccm[7])

        total_rental_cost.config(text = "Total Cost: " + str(total_rent_cost))


        
    #books the rental and produces success message 
    def book_rental():
        global current_user
        global value

        #inserts rental details into database
        rentals_database_backend.insert(current_user, selected_tuple_ccm[0], rental_date_text.get().strip(), rental_period_text.get().strip())
        cars_database_backend.update(selected_tuple_ccm[0], selected_tuple_ccm[1], selected_tuple_ccm[2], selected_tuple_ccm[3], selected_tuple_ccm[4], selected_tuple_ccm[5], selected_tuple_ccm[6], selected_tuple_ccm[7], selected_tuple_ccm[8], selected_tuple_ccm[9], str(current_user))
        #need to delete car and write price into database
        messagebox.showinfo("SUCCESS", "Your rental has been booked.\nPlease collect your vehicle on the specified date.\nAn email containing the details of the rentals will be sent to you shortly.\nIf any changes are to be made please contact us.")         

        #records the transaction
        with open("rental_sales.txt","a") as rental_sales:
            rental_sales.write(str(total_rent_cost)+"\n")


        #makes a list of the transaction details writes them in a file   
        transaction_details = [selected_tuple_ccm, "R"]
        
        with open("car_history.txt","a") as sold_cars:
            sold_cars.write(str(transaction_details)+"\n")


        cust_loop()

        





    #validates inputs for rentals 
    def check_rental():

        #activates booking check
        if booking_check(rental_date_text.get().strip()) == False:
            messagebox.showerror("Error","ERROR: Invalid rental date")
            return None

        #checks rental period is a digit 
        if not rental_period_text.get().strip().isdigit():
            messagebox.showerror("Error","ERROR: Invalid rental period")
            return None

        #checks if the rental period is less than one 
        if int(rental_period_text.get().strip()) < 1:
            messagebox.showerror("Error","ERROR: Invalid rental period")
            return None
            
        book_rental()


    frame11.destroy()


    #Frame13 - renting car page 
    frame13 = Frame(window1)

    #display car brand
    display_car_buy = Label(frame13, text = f"Car: {selected_tuple_ccm[1]}")
    display_car_buy.grid(row = 0, column = 0)

    #display car model
    display_model_buy = Label(frame13, text = f"Model: {selected_tuple_ccm[2]}")
    display_model_buy.grid(row = 1, column = 0)

    #display car price per week
    display_price_rent = Label(frame13, text = f"Price (per week) : {selected_tuple_ccm[7]}")
    display_price_rent.grid(row = 2, column = 0)

    #enter rental date
    rental_date = Label(frame13, text = "Date of Rental (DD/MM/YY): ")
    rental_date.grid(row = 3, column = 0)

    rental_date_text = StringVar()
    rental_date_entry = Entry(frame13, textvariable = rental_date_text)
    rental_date_entry.grid(row = 3, column = 1)

    #enter rental period 
    rental_period = Label(frame13, text = f"Rental Period (weeks): ")
    rental_period.grid(row = 4, column = 0)

    rental_period_text = StringVar()
    rental_period_entry = Entry(frame13, textvariable = rental_period_text)
    rental_period_entry.grid(row = 4, column = 1)

    #total price of rental
    total_rental_cost = Label(frame13, text = 'Total Cost: ')
    total_rental_cost.grid(row = 5, column = 0)


    #rent_price.trace("w", calculate)
    rental_period_text.trace("w", calculate_rental)

    #confirm rental button
    confirm_rental_button = Button(frame13, text = "Confirm Rental", command = check_rental)
    confirm_rental_button.grid(row = 6, column = 0)


    frame13.pack()




    
## goes from customers cars page to finance car page
def car_finance():

    global customer_frame
    global frame14

    customer_frame = "finance"

    #records the transaction and produces success message 
    def finalise_finance():
        
        messagebox.showinfo("SUCCESS", "Your car awaits you at hamia motors\nAn email will be sent to you containing the details of the sale\nPlease come into store to complete the transaction.")         

        with open("sales.txt","a") as sales:
            sales.write(str(round(total_finance_cost,2))+"\n")
            

        #makes a list of the transaction details writes them in a file   
        transaction_details = [selected_tuple_ccm, "F"]
        
        with open("car_history.txt","a") as sold_cars:
            sold_cars.write(str(transaction_details)+"\n")

        #removes the car from the main database as its no longer available
        cars_database_backend.delete(selected_tuple_ccm[0])

        cust_loop()




    
    #validates finance inputs 
    def check_finance():

        #checks if length of deposit is greater than zero 
        if len(deposit_text.get().strip()) < 1:
            messagebox.showerror("Error","ERROR: No deposit entered")
            return None
            
        #checks the deposit is a number 
        if not deposit_text.get().isdigit():
            messagebox.showerror("Error","ERROR: Invalid deposit")
            return None

        #checks the deposit is less than the car cost 
        if int(deposit_text.get()) > int(selected_tuple_ccm[4]):
            messagebox.showerror("Error","ERROR: Invalid deposit")
            return None

        #checks the length of the finance term is not empty 
        if len(term_text.get().strip()) < 1:
            messagebox.showerror("Error","ERROR: Invalid financing term")
            return None

        #checks that the term is a digit
        if not term_text.get().strip().isdigit():
            messagebox.showerror("Error","ERROR: Invalid financing term")
            return None
     

        finalise_finance()

        
    #calculates finace total and monthly payment 
    def calculate_finance(*args):
        try:
            global total_finance_cost

            total_finance_cost = (int(selected_tuple_ccm[4]) - int(deposit_text.get().strip())) * 1.106

            monthly_finance_cost = float(total_finance_cost) / int(term_text.get().strip())

            total_pay_amount.config(text = "Total amount payed: " + str(round(total_finance_cost,2)))
            monthly_payments_label.config(text = "Monthly Payments: " + str(round(monthly_finance_cost,2)))
        except:
            total_pay_amount.config(text = "Total amount payed: Invalid input(s)")
            monthly_payments_label.config(text = "Monthly Payments: Invalid input(s)")

    frame11.forget()


    #frame14 - financing page 
    frame14 = Frame(window1)

    display_car_buy = Label(frame14, text = f"Car: {selected_tuple_ccm[1]}")
    display_car_buy.grid(row = 0, column = 0)

    display_model_buy = Label(frame14, text = f"Model: {selected_tuple_ccm[2]}")
    display_model_buy.grid(row = 1, column = 0)

    display_price_buy = Label(frame14, text = f"Price: {selected_tuple_ccm[4]}")
    display_price_buy.grid(row = 2, column = 0)

    interest_label = Label(frame14, text = "Interest Rate at 10.6%")
    interest_label.grid(row = 3, column = 0)

    #deposit
    deposit_label = Label(frame14, text = "Deposit (if none put 0): ")
    deposit_label.grid(row = 4, column = 0)

    deposit_text = StringVar()
    deposit_text_entry = Entry(frame14, textvariable = deposit_text)
    deposit_text_entry.grid(row = 4, column = 1)

    #months
    term_label = Label(frame14, text = "Finance term (months): ")
    term_label.grid(row = 5, column = 0)

    term_text = StringVar()
    term_entry = Entry(frame14, textvariable = term_text)
    term_entry.grid(row = 5, column = 1)

    #monthy payments
    monthly_payments_label = Label(frame14, text = "Monthly Payments: ")
    monthly_payments_label.grid(row = 6, column = 0)


    #total payment
    total_pay_amount = Label(frame14, text = "Total amount payed: ")
    total_pay_amount.grid(row = 7, column = 0)
    
    deposit_text.trace("w", calculate_finance)
    term_text.trace("w", calculate_finance)

    confirm_finance_button = Button(frame14, text = "Confirm Finance", command = check_finance)
    confirm_finance_button.grid(row = 8, column = 0)
    
    frame14.pack()





## goes from employee menu to manage cars menu
def manage_cars_employee():
    frame9.forget()
    frame15.pack()




    
## goes from boss menu to manage cars menu
def manage_cars_boss():
    frame10.forget()
    frame15.pack()





## goes from employee menu page to manage rentals page
def manage_rental_employee():
    frame9.forget()
    frame16.pack()





## goes from boss menu page to manage rentals page
def manage_rental_boss():
    frame10.forget()
    frame16.pack()



    

#goes from employee menu page to manage customers page
def manage_customers_employee():
    frame9.forget()
    frame17.pack()





## goes from boss menu page to manage customers page
def manage_customers_boss():
    frame10.forget()
    frame17.pack()





## goes from boss menu page to manage employees page
def manage_employees_boss():
    frame10.forget()
    frame18.pack()





## goes from boss menu page to view sales page 
def display_sales():

    #calculates all the sales statistics so they can be displayed
    def get_sales_stats():
        global total_sales
        global rent_revenue
        global total_revenue

        total_sales = 0
        rent_revenue = 0
        total_revenue = 0

        try:

            with open("rental_sales.txt","r") as rental_sales:
                for line in rental_sales:
                    rent_revenue += float(line)
                    total_revenue += float(line)

            with open("sales.txt","r") as sales:
                for row in sales:
                    total_sales += float(line)
                    total_revenue += float(line)

        except:
            pass




    def list_view():

       #opens car history and inserts each element into the list box  
       with open("car_history.txt","r") as sold_cars:
           for line in sold_cars:
               transaction_history_list.insert(END,line)
           
        
                
    frame10.forget()       
            

    #frame19 - view sales
    frame19 = Frame(window1)

    get_sales_stats()

    #displays sales revenue
    total_sales_text = Label(frame19, text = f"Sales: {total_sales}")
    total_sales_text.grid(row =0, column = 0)

    #displays rental revenue
    total_rent_text = Label(frame19, text = f"Rentals Revenue: {rent_revenue}")
    total_rent_text.grid(row =0, column = 1)

    #displays total revenue 
    total_revenue_text = Label(frame19, text = f"Total Revenue: {total_revenue}")
    total_revenue_text.grid(row =0, column = 2)


    #creates a list box and sroll bar for the transaction history to be displayed 
    transaction_history_list = Listbox(frame19, height = 15, width = 75)
    transaction_history_list.grid(row = 5, column = 0, columnspan = 2)

    transaction_history_bar = Scrollbar(frame19)
    transaction_history_bar.grid(row = 5, column = 2 , rowspan=6)

    transaction_history_list.configure(yscrollcommand=transaction_history_bar.set)
    transaction_history_bar.configure(command=transaction_history_list.yview)

    list_view()



    frame19.pack()



    

## loops customer back to cars page
def cust_loop():
    global customer_frame

    if customer_frame == "buy":
        frame12.forget()
        frame8.pack()
        view()

    if customer_frame == "rent":
        frame13.forget()
        frame8.pack()
        view()

    if customer_frame == "finance":
        frame14.forget()
        frame8.pack()
        view()
    
##### End of frame switches ######







    
##### start of validation subroutines #####
    
## pressence check
def pressence_check(data):
    if len(data) < 1:
        print("no")
        return False




    
## alphabet check
def alpha_check(data):
    if not data.isalpha():
        return False





## digit check
def digit_check(data):
    if not data.isdigit():
        return False






## same check
def is_same(data,check):
    if not data == check:
        return False






## date check
def date_valid(date):
    try:
        #check date is 10 charcters long
        if not len(date) == 10:
            return False

        #checks if the day is greater than 31
        if int(date[0:2]) > 31:
            return False

        #checks if the month is greater than 12
        if int(date[3:5]) > 12:
            return False

        #checks if the year is greater than 2005
        if int(date[6:]) > 2005:
            return False

        #check the / are in the right place
        if not date[2] == "/" and not date[5] == "/":
            return False
    #handles errors such as a letters entered
    except:
        return False






## email check
def email_valid(email):
    #makes sure @ is in the email 
    if not "@" in email :
        return False

    #check the email has .com at the end 
    if not email[-4:] == ".com":
        print("2")
        return False

    #checks to see if the email has already been used 
    for rows in customers_database_backend.view():
        print("use")
        if email in rows:
            return False





## update email check
def update_email_valid(email):
    #makes sure @ is in the email 
    if not "@" in email :
        return False

    #check the email has .com at the end 
    if not email[-4:] == ".com":
        print("2")
        return False




## phone check
def phone_valid(phone):
    try:
        #checks the number is 11 characters long 
        if not len(phone) == 11:
            return False

        #makes sure the number is all digits
        if not phone.isdigit():
            return False

        #makes sure the number has the uk calling code
        if not phone[:2] == "07":
            return False
    #error handling 
    except:
        return False




    

## date check for bookings
def booking_check(date):
    try:
        #check date is 10 charcters long
        if not len(date) == 10:
            return False

        #checks if the day is greater than 31
        if int(date[0:2]) > 31:
            return False

        #checks if the month is greater than 12
        if int(date[3:5]) > 12:
            return False

        #checks that the year is 2023 or above
        if int(date[6:]) < 2023:
            return False

        #check the / are in the right place
        if not date[2] == "/" and not date[5] == "/":
            return False
        
    #handles errors such as a letters entered
    except:
        return False






## year check for cars 
def year_check(year):
    try:
        #checks that the length of the year is 4 
        if not len(year) == 4:
            return False

        #checks that the year is a digit 
        if not year.isdigit():
            return False
        
    #handles any errors that can occur     
    except:
        return False






## fuel check
def fuel_check(fuel):

    #checks that the fuel entered is either petrol, deisel or electric 
    fuels = ["Petrol" , "Diesel" , "Electric"]

    if not fuel in fuels:
        return False






## plate check
def plate_check(plate):

    #checks that every character in a number plate is either a letter digit or space
    for character in plate:
        if not character.isdigit() and not character.isalpha() and not character == " ":
            return False





## customerID check
def customerID_check(data):

    for rows in customers_database_backend.view():

        if str(data) == str(rows[0]):
            return True
        
    return False





## carID check
def carID_check(data):

    for rows in cars_database_backend.view():

        if str(data) == str(rows[0]):
            return True
    return False






##rented check
def rented_check(data):
    for rows in customers_database_backend.view():
        if not str(data) == "0" and customerID_check(data) == False:
            return False 
            
        
##### end of validation subroutines ######







        
##### start of calls for validation for customer signup page #####

## activates validation calls for customer signup        
def confirm_signup():

        #gets all the deatils in a list 
        signup_details = [firstname_text.get().title().strip(), surname_text.get().title().strip(), password_text.get().strip(), password_conf_text.get().strip(), dob_text.get().strip(), emailadd_text.get().strip(), phonenum_text.get().strip()]




        
        #activates pressence check
        for entry in signup_details:
            if pressence_check(entry) == False:
                messagebox.showerror("ERROR","ERROR: Missing field(s)")
                return None




            
        #activates alphabet checks 
        for name in signup_details[0:2]:
            if alpha_check(name) == False:
                messagebox.showerror("Error","ERROR: Name(s) is not alphabetical")
                return None




            
        #activates same check
        if is_same(signup_details[2],signup_details[3]) == False:
            messagebox.showerror("Error","ERROR: Passwords do not match")
            return None




        
        #activates date check
        if date_valid(signup_details[4]) == False:
            messagebox.showerror("Error","ERROR: Date is erroneous")
            return None



        #activates email check
        if email_valid(signup_details[5]) == False:
            messagebox.showerror("Error","ERROR: Email not valid")
            return None




        
        #activates phone check
        if phone_valid(signup_details[6]) == False:
            messagebox.showerror("Error","ERROR: Number not valid")
            return None




        
        #write details into database once validation is passed
        customers_database_backend.insert(firstname_text.get().title().strip(), surname_text.get().title().strip(), password_text.get().strip(), dob_text.get().strip(), emailadd_text.get().strip(), phonenum_text.get().strip())
        messagebox.showinfo("SUCCESS", "Your details have now been added to the system\nplease click to continue to login")


        frame_switch4_2()
##### start of calls for validation for customer signup page #####







##### start of login validation subroutines #####
    
## customer login 
def customer_login_validation(email,password):
    global current_user

    #checks that the email and password match to a set in the database
    for rows in customers_database_backend.view():
        if email == rows[5].lower() and password == rows[3]:
            
            current_user = rows[0]
            print(current_user)

            return True
        
    return False





## boss login
def boss_login_validation(user,password):

    #checks that the ID and password match to a set in the database
    for rows in boss_database_backend.view():
        if user == rows[1] and password == rows[2]:
            return True
    return False





## employee login
def employee_login_validation(user,password):

    #checks that the ID and password match to a set in the database
    for rows in employee_database_backend.view():
        if str(user) == str(rows[0]) and password == rows[3]:
            return True
    return False
##### end of login validation subroutines #####








##### start of calls for validation for logins #####
        
## customer login
def confirm_customer_login():

    #calls validation for employee login and produces an apropriate output
    if customer_login_validation(customer_email_login_text.get().lower(), customer_password_login_text.get()) == False:
        messagebox.showerror("Error","ERROR: Incorrect details")

    else:
        messagebox.showinfo("SUCCESS","Correct details, logging in...")
        customer_cars_frame()




        
## boss login
def confirm_boss_login():

    #calls validation for boss login and produces an apropriate output 
    if boss_login_validation(boss_user_text.get(), boss_pass_text.get()) == False:
        messagebox.showerror("Error","ERROR: Incorrect details")

    else:
        messagebox.showinfo("SUCCESS","Correct details, logging in...")
        boss_menu_frame()




        
## employee login
def confirm_employee_login():

    #calls validation for employee login and produces an apropriate output
    if employee_login_validation(employee_user_text.get(), employee_pass_login_text.get()) == False:
        messagebox.showerror("Error","ERROR: Incorrect details")

    else:
        messagebox.showinfo("SUCCESS","Correct details, logging in...")
        employee_menu_frame()
##### end of calls for validation for logins #####








####### Start of menu page functions #######
        
##### start of customers car menu subroutines #####

## gets the selected tuple from the list box
def get_selected_row_ccm(event):
    global selected_tuple_ccm

    try:
    
        index = customer_cars_list.curselection()
        selected_tuple_ccm = customer_cars_list.get(index)
        
        
        customer_car_make_entry.delete(0,END)
        customer_car_make_entry.insert(END,selected_tuple_ccm[1])
        
        customer_car_model_entry.delete(0,END)
        customer_car_model_entry.insert(END,selected_tuple_ccm[2])
        
        customer_car_year_entry.delete(0,END)
        customer_car_year_entry.insert(END,selected_tuple_ccm[3])
        
        customer_car_price_entry.delete(0,END)
        customer_car_price_entry.insert(END,selected_tuple_ccm[4])
        
        customer_car_milage_entry.delete(0,END)
        customer_car_milage_entry.insert(END,selected_tuple_ccm[5])
        
        customer_car_fuel_entry.delete(0,END)
        customer_car_fuel_entry.insert(END,selected_tuple_ccm[6])
        
        customer_car_rentprice_entry.delete(0,END)
        customer_car_rentprice_entry.insert(END,selected_tuple_ccm[7])
        
        customer_car_numberplate_entry.delete(0,END)
        customer_car_numberplate_entry.insert(END,selected_tuple_ccm[8])
        
        customer_car_owners_entry.delete(0,END)
        customer_car_owners_entry.insert(END,selected_tuple_ccm[9])
    except:
        pass



    
## checks that a tuple is selected before buy car menu is opened 
def tuple_check_buy():
    
    try:
        global user_action
        global car_details

        
        for i in selected_tuple_ccm:
            car_details.append(i)

            
    except:
        messagebox.showerror("Error","ERROR: No car selected")
        return None
    
    #sets user action to buy  
    user_action = "buy"
    authentication()





## checks that a tuple is selected before rent car menu is opened     
def tuple_check_rent():
    
    try:
        global user_action
        global car_details
        global ammended_price

        
        for i in selected_tuple_ccm:
            car_details.append(i)
            
    except:
        messagebox.showerror("Error","ERROR: No car selected")
        return None

    #sets user action to rent
    user_action = "rent"
    authentication()





## checks that a tuple is selected before finance car menu is opened     
def tuple_check_finance():

    try:
        global user_action
        global car_details
        
        for i in selected_tuple_ccm:
            car_details.append(i)
            
    except:
        messagebox.showerror("Error","ERROR: No car selected")
        return None

    #sets user action to finance 
    user_action = "finance"
    authentication()





##  asks the user to validate before going through with the transaction    
def authenticate_details():
    global user_action
    global current_user
    

    #checks that the current user and password match 
    for rows in customers_database_backend.view():
        if current_user == rows[0] and authenticate_email_text.get().lower() == rows[5].lower() and authenticate_password_text.get() == rows[3]:
            messagebox.showinfo("SUCCESS","Details Have been Athenticated")

            #if the action is buy opens buy menu
            if user_action == "buy":
                car_buy()
                return None

            #if the action is buy opens buy menu    
            if user_action == "rent":
                car_rent()
                return None

            #if the action is finance opens buy menu
            if user_action == "finance":
                car_finance()
                return None

    #if details do not match produce error message
    messagebox.showerror("ERROR","ERROR: Could not authenticate details")
    return None





## function that shows database items in listbox 
def view():
    customer_cars_list.delete(0,END)
    for row in cars_database_backend.view():
        if str(row[-1]) == "0":
            customer_cars_list.insert(END,row[0:-1])






## function that allows user to search database 
def search():
    customer_cars_list.delete(0,END)
    for row in cars_database_backend.search(cmake_text.get().title().strip() , cmodel_text.get().title().strip()  , cyear_text.get().strip()  , cprice_text.get().strip()  , cmilage_text.get().strip()  , cfuel_text.get().title().strip()  , crentprice_text.get().strip()  , cnumberplate_text.get().upper().strip()  , cowners_text.get().strip() , ""):
        if str(row[-1]) == "0":
            customer_cars_list.insert(END,row[0:-1])

##### end of customers car menu subroutines #####


        








###### start of employees edit cars page #####

## gets the selected tuple from the list box    
def get_selected_row_ecm(event):
    global selected_tuple_ecm

    try:
    
        index = employees_car_list.curselection()
        selected_tuple_ecm = employees_car_list.get(index)

        
        employee_car_make_entry.delete(0,END)
        employee_car_make_entry.insert(END,selected_tuple_ecm[1])
        
        employee_car_model_entry.delete(0,END)
        employee_car_model_entry.insert(END,selected_tuple_ecm[2])
        
        employee_car_year_entry.delete(0,END)
        employee_car_year_entry.insert(END,selected_tuple_ecm[3])
        
        employee_car_price_entry.delete(0,END)
        employee_car_price_entry.insert(END,selected_tuple_ecm[4])
        
        employee_car_milage_entry.delete(0,END)
        employee_car_milage_entry.insert(END,selected_tuple_ecm[5])
        
        employee_car_fuel_entry.delete(0,END)
        employee_car_fuel_entry.insert(END,selected_tuple_ecm[6])
        
        employee_car_rentprice_entry.delete(0,END)
        employee_car_rentprice_entry.insert(END,selected_tuple_ecm[7])
        
        employee_car_numberplate_entry.delete(0,END)
        employee_car_numberplate_entry.insert(END,selected_tuple_ecm[8])
        
        employee_car_owners_entry.delete(0,END)
        employee_car_owners_entry.insert(END,selected_tuple_ecm[9])

        employee_car_rented_entry.delete(0,END)
        employee_car_rented_entry.insert(END,selected_tuple_ecm[10])
    except:
        pass



## function that shows database items in listbox     
def view_cars():
    employees_car_list.delete(0,END)
    for row in cars_database_backend.view():
        employees_car_list.insert(END,row)





## function that validates car inputs before they are added to the database
def add_cars_validation():
    
    #gets car details in one list gets all numerical inputs in another list 
    car_details = [make_text.get().title().replace(" ", "") , model_text.get().title().replace(" ", "") , year_text.get().strip() , price_text.get().strip() , milage_text.get().strip() , fuel_text.get().title().strip() , rentprice_text.get().strip() , numberplate_text.get().upper().strip() , owners_text.get().strip(), rented_text.get().strip()]
    digits = [car_details[3], car_details[4], car_details[6], car_details[8], car_details[9]]

    #activates pressence check
    for entry in car_details:
        if pressence_check(entry) == False:
            messagebox.showerror("ERROR","ERROR: Missing field(s)")
            return None

    #activates alphabet check
    for word in car_details[0]:
        if alpha_check(word) == False:
            messagebox.showerror("ERROR","ERROR: Invalid car name or make")
            return None

    #activates year check
    if year_check(car_details[2]) == False:
        messagebox.showerror("ERROR","ERROR: Invalid year")
        return None

    #activates digit check
    for value in digits:
        if digit_check(value) == False:
            messagebox.showerror("ERROR","ERROR: Invalid number(s) entered")
            return None

    #activates fuel check
    if fuel_check(car_details[5]) == False:
        messagebox.showerror("ERROR","ERROR: Invalid fuel type")
        return None

    #activates plate check
    if plate_check(car_details[7]) == False:
        messagebox.showerror("ERROR","ERROR: Invalid plate")
        return None

    #activated rented check
    if rented_check(car_details[9]) == False:
        messagebox.showerror("ERROR","ERROR: Invalid rental ID")
        return None
        

    add_cars()





## function that adds cars into database once validated
def add_cars():
    cars_database_backend.insert(make_text.get().title().strip() , model_text.get().title().strip() , year_text.get().strip() , price_text.get().strip() , milage_text.get().strip() , fuel_text.get().title().strip() , rentprice_text.get().strip() , numberplate_text.get().upper().strip() , owners_text.get().strip(), rented_text.get().strip())
    
    view_cars()
    
    employee_car_make_entry.delete(0,END)
    employee_car_model_entry.delete(0,END)
    employee_car_year_entry.delete(0,END)
    employee_car_price_entry.delete(0,END) 
    employee_car_milage_entry.delete(0,END) 
    employee_car_fuel_entry.delete(0,END)    
    employee_car_rentprice_entry.delete(0,END)
    employee_car_numberplate_entry.delete(0,END)
    employee_car_owners_entry.delete(0,END)
    employee_car_rented_entry.delete(0,END)





## function that checks car inputs before they are updated 
def update_cars_validation():
    
    #gets car details in one list gets all numerical inputs in another list 
    car_details = [make_text.get().title().replace(" ", "") , model_text.get().title().replace(" ", "") , year_text.get().strip() , price_text.get().strip() , milage_text.get().strip() , fuel_text.get().title().strip() , rentprice_text.get().strip() , numberplate_text.get().upper().strip() , owners_text.get().strip(), rented_text.get().strip()]
    digits = [car_details[3], car_details[4], car_details[6], car_details[8], car_details[9]]


    #activates pressence check
    for entry in car_details:
        if pressence_check(entry) == False:
            messagebox.showerror("ERROR","ERROR: Missing field(s)")
            return None

    #activates alphabet check
    for word in car_details[0]:
        if alpha_check(word) == False:
            messagebox.showerror("ERROR","ERROR: Invalid car name or make")
            return None

    #activates year check
    if year_check(car_details[2]) == False:
        messagebox.showerror("ERROR","ERROR: Invalid year")
        return None

    #activates digit check
    for value in digits:
        if digit_check(value) == False:
            messagebox.showerror("ERROR","ERROR: Invalid number(s) entered")
            return None

    #activates fuel check
    if fuel_check(car_details[5]) == False:
        messagebox.showerror("ERROR","ERROR: Invalid fuel type")
        return None

    #activates plate check
    if plate_check(car_details[7]) == False:
        messagebox.showerror("ERROR","ERROR: Invalid plate")
        return None


    #activated rented check
    if rented_check(car_details[9]) == False:
        messagebox.showerror("ERROR","ERROR: Invalid rental ID")
        return None
    

    update_cars()





## function that updates cars in database 
def update_cars():
    cars_database_backend.update(selected_tuple_ecm[0], make_text.get().title().strip() , model_text.get().title().strip() , year_text.get().strip() , price_text.get().strip() , milage_text.get().strip() , fuel_text.get().title().strip() , rentprice_text.get().strip() , numberplate_text.get().upper().strip() , owners_text.get().strip(), rented_text.get().strip())
    view_cars()
    
    employee_car_make_entry.delete(0,END)
    employee_car_model_entry.delete(0,END)
    employee_car_year_entry.delete(0,END)
    employee_car_price_entry.delete(0,END) 
    employee_car_milage_entry.delete(0,END) 
    employee_car_fuel_entry.delete(0,END)    
    employee_car_rentprice_entry.delete(0,END)
    employee_car_numberplate_entry.delete(0,END)
    employee_car_owners_entry.delete(0,END)
    employee_car_rented_entry.delete(0,END)





## function that deletes a car from the database 
def delete_cars():
    cars_database_backend.delete(selected_tuple_ecm[0])
    
    employee_car_make_entry.delete(0,END)
    employee_car_model_entry.delete(0,END)
    employee_car_year_entry.delete(0,END)
    employee_car_price_entry.delete(0,END) 
    employee_car_milage_entry.delete(0,END) 
    employee_car_fuel_entry.delete(0,END)    
    employee_car_rentprice_entry.delete(0,END)
    employee_car_numberplate_entry.delete(0,END)
    employee_car_owners_entry.delete(0,END)
    employee_car_rented_entry.delete(0,END)
    
    view_cars() 





## fucntion that allows user to search for cars in the database 
def search_cars():
    employees_car_list.delete(0,END)
    for row in cars_database_backend.search(make_text.get().title().strip() , model_text.get().title().strip() , year_text.get().strip() , price_text.get().strip() , milage_text.get().strip() , fuel_text.get().title().strip() , rentprice_text.get().strip() , numberplate_text.get().upper().strip() , owners_text.get().strip(), rented_text.get().strip()):
        employees_car_list.insert(END,row)
###### end of employees edit cars page #####









        
##### start of employee rentals menu #####

## function that shows database items in listbox 
def view_rentals():
    employee_rent_list.delete(0,END)
    for row in rentals_database_backend.view():
        employee_rent_list.insert(END,row)




        
## gets the selected tuple from the box    
def get_selected_row_erm(event):
    global selected_tuple_erm

    try:
    
        index = employee_rent_list.curselection()
        selected_tuple_erm = employee_rent_list.get(index)

        
        employee_rent_customerid_entry.delete(0,END)
        employee_rent_customerid_entry.insert(END,selected_tuple_erm[1])
        
        employee_rent_carid_entry.delete(0,END)
        employee_rent_carid_entry.insert(END,selected_tuple_erm[2])
        
        employee_rent_rentdate_entry.delete(0,END)
        employee_rent_rentdate_entry.insert(END,selected_tuple_erm[3])
        
        employee_rent_rentlength_entry.delete(0,END)
        employee_rent_rentlength_entry.insert(END,selected_tuple_erm[4])
    except:
        pass




## function that validates inputs before updating rental
def update_rentals_validation():

    #gets details into a list 
    rental_details = [customerID_text.get().strip(), carID_text.get().strip(), rentdate_text.get().strip(), rentlength_text.get().strip()]

    #checks both IDs are digits
    for data in rental_details[:2]:
        if digit_check(data) == False:
            messagebox.showerror("ERROR","ERROR: Invalid data entered")
            return None
        

    #checks rent length is a digit
    if digit_check(rentlength_text.get()) == False:
            messagebox.showerror("ERROR","ERROR: Invalid data entered")
            return None
            

    #checks the booking date iis correct
    if booking_check(rental_details[2]) == False:
        messagebox.showerror("ERROR","ERROR: Invalid rent date")
        return None


    #checks both IDs are valid IDs
    if customerID_check(customerID_text.get().strip()) == False or carID_check(carID_text.get().strip()) == False:
        messagebox.showerror("ERROR","ERROR: Invalid ID(s)")
        return None


    

    update_rentals()
        


## function that updates cars in database 
def update_rentals():
    rentals_database_backend.update(selected_tuple_erm[0], customerID_text.get().strip(), carID_text.get().strip(), rentdate_text.get().strip(), rentlength_text.get().strip())
    
    employee_rent_customerid_entry.delete(0,END)
    employee_rent_carid_entry.delete(0,END)
    employee_rent_rentdate_entry.delete(0,END)
    employee_rent_rentlength_entry.delete(0,END)
    
    view_rentals()





## function that deletes a rental from the database 
def delete_rentals():
    rentals_database_backend.delete(selected_tuple_erm[0])
    view_rentals()
    
    employee_rent_customerid_entry.delete(0,END)
    employee_rent_carid_entry.delete(0,END)
    employee_rent_rentdate_entry.delete(0,END)
    employee_rent_rentlength_entry.delete(0,END)





## function that allows user to search for rental in database 
def search_rentals():
    employee_rent_list.delete(0,END)
    for row in rentals_database_backend.search(customerID_text.get().strip(), carID_text.get().strip(), rentdate_text.get().strip(), rentlength_text.get().strip()):
        employee_rent_list.insert(END,row)
##### end of employee rentals menu ######









       
##### start of employee manage customers menu ######

## function that shows database items in listbox     
def view_customers():
    manage_customers_list.delete(0,END)
    for row in customers_database_backend.view():
        manage_customers_list.insert(END,row)





## gets the selected tuple from the box        
def get_selected_row_emcm(event):
    global selected_tuple_emcm

    try:
    
        index = manage_customers_list.curselection()[0]
        selected_tuple_emcm= manage_customers_list.get(index)
        
        customer_firstname_entry.delete(0,END)
        customer_firstname_entry.insert(END,selected_tuple_emcm[1])
        
        customer_surname_entry.delete(0,END)
        customer_surname_entry.insert(END,selected_tuple_emcm[2])
        
        customer_password_entry.delete(0,END)
        customer_password_entry.insert(END,selected_tuple_emcm[3])
        
        customer_dob_entry.delete(0,END)
        customer_dob_entry.insert(END,selected_tuple_emcm[4])
        
        customer_email_entry.delete(0,END)
        customer_email_entry.insert(END,selected_tuple_emcm[5])
        
        customer_phone_entry.delete(0,END)
        customer_phone_entry.insert(END,selected_tuple_emcm[6])
    except:
        pass






## function that allows user to search for a customer in database     
def search_customers():
    manage_customers_list.delete(0,END)
    for row in customers_database_backend.search(customer_firstname_text.get().title().strip(), customer_surname_text.get().title().strip(), customer_pass_text.get().strip(), customer_dob_text.get().strip(), customer_email_text.get().strip(), customer_phone_text.get().strip()):
        manage_customers_list.insert(END,row)





## function that adds a customer to the database
def add_customers():
    customers_database_backend.insert(customer_firstname_text.get().title().strip(), customer_surname_text.get().title().strip(), customer_pass_text.get().strip(), customer_dob_text.get().strip(), customer_email_text.get().strip(), customer_phone_text.get().strip())
    view_customers()
    
    customer_firstname_entry.delete(0,END)
    customer_surname_entry.delete(0,END)
    customer_password_entry.delete(0,END)
    customer_dob_entry.delete(0,END)
    customer_email_entry.delete(0,END)
    customer_phone_entry.delete(0,END)






## function that validates inputs before adding customer to database 
def add_customers_validation():
    details = [customer_firstname_text.get().title().strip(), customer_surname_text.get().title().strip(), customer_pass_text.get().strip(), customer_dob_text.get().strip(), customer_email_text.get().strip(), customer_phone_text.get().strip()]



    ##activates pressence check
    for entry in details:
        if pressence_check(entry) == False:
            messagebox.showerror("ERROR","ERROR: Missing field(s)")
            return None

    ##activates alphabet checks 
    for name in details[0:2]:
        if alpha_check(name) == False:
            messagebox.showerror("Error","ERROR: Name(s) is not alphabetical")
            return None

    ##activates date check
    if date_valid(details[3]) == False:
        messagebox.showerror("Error","ERROR: Date is erroneous")
        return None

    ##activates email check
    if email_valid(details[4]) == False:
        messagebox.showerror("Error","ERROR: Email not valid")
        return None

    ##activates phone check
    if phone_valid(details[5]) == False:
        messagebox.showerror("Error","ERROR: Number not valid")
        return None

    add_customers()





## function that updates a customer in the database  
def update_customers():
    customers_database_backend.update(selected_tuple_emcm[0], customer_firstname_text.get().title().strip(), customer_surname_text.get().title().strip(), customer_pass_text.get().strip(), customer_dob_text.get().strip(), customer_email_text.get().strip(), customer_phone_text.get().strip())

    view_customers()
    
    customer_firstname_entry.delete(0,END)
    customer_surname_entry.delete(0,END)
    customer_password_entry.delete(0,END)
    customer_dob_entry.delete(0,END)
    customer_email_entry.delete(0,END)
    customer_phone_entry.delete(0,END)





## function that validates inputs before updating customer 
def update_customers_validation():
    #gets all details into a list
    details = [customer_firstname_text.get().title().strip(), customer_surname_text.get().title().strip(), customer_pass_text.get().strip(), customer_dob_text.get().strip(), customer_email_text.get().strip(), customer_phone_text.get().strip()]



    ##activates pressence check
    for entry in details:
        if pressence_check(entry) == False:
            messagebox.showerror("ERROR","ERROR: Missing field(s)")
            return None

    ##activates alphabet checks 
    for name in details[0:2]:
        if alpha_check(name) == False:
            messagebox.showerror("Error","ERROR: Name(s) is not alphabetical")
            return None

    ##activates date check
    if date_valid(details[3]) == False:
        messagebox.showerror("Error","ERROR: Date is erroneous")
        return None

    ##activates update email check
    if update_email_valid(details[4]) == False:
        messagebox.showerror("Error","ERROR: Email not valid")
        return None

    ##activates phone check
    if phone_valid(details[5]) == False:
        messagebox.showerror("Error","ERROR: Number not valid")
        return None

    update_customers()





## function that deletes customer from database 
def delete_customers():
    customers_database_backend.delete(selected_tuple_emcm[0])
    view_customers()
    
    customer_firstname_entry.delete(0,END)
    customer_surname_entry.delete(0,END)
    customer_password_entry.delete(0,END)
    customer_dob_entry.delete(0,END)
    customer_email_entry.delete(0,END)
    customer_phone_entry.delete(0,END)
##### end of employee manage customers menu ######









    
##### start of boss manage employees menu #####

## gets the selected tuple from the box 
def get_selected_row_bmem(event):
    global selected_tuple_bmem

    try:
    
        index = boss_employee_list.curselection()
        selected_tuple_bmem = boss_employee_list.get(index)

        
        boss_employee_firstname_entry.delete(0,END)
        boss_employee_firstname_entry.insert(END,selected_tuple_bmem[1])
        
        boss_employee_surname_entry.delete(0,END)
        boss_employee_surname_entry.insert(END,selected_tuple_bmem[2])
        
        boss_employee_password_entry.delete(0,END)
        boss_employee_password_entry.insert(END,selected_tuple_bmem[3])
        
        boss_employee_dob_entry.delete(0,END)
        boss_employee_dob_entry.insert(END,selected_tuple_bmem[4])
        
        boss_employee_email_entry.delete(0,END)
        boss_employee_email_entry.insert(END,selected_tuple_bmem[5])
        
        boss_employee_phone_entry.delete(0,END)
        boss_employee_phone_entry.insert(END,selected_tuple_bmem[6])
    except:
        pass





## displays elements of database in listbox 
def view_employees():
    boss_employee_list.delete(0,END)
    for row in employee_database_backend.view():
        boss_employee_list.insert(END,row)





## function that validates inputs before adding employee to database 
def add_employees_validation():
    employees_details = [employee_fn_text.get().title().strip() , employee_sn_text.get().title().strip() , employee_pass_text.get().strip() , employee_date_text.get().strip() , employee_email_text.get().strip() , employee_phone_text.get().strip()]

    for entry in employees_details:
        if pressence_check(entry) == False:
            messagebox.showerror("ERROR","ERROR: Missing field(s)")
            return None

    ##activates alphabet checks 
    for name in employees_details[0:2]:
        if alpha_check(name) == False:
            messagebox.showerror("Error","ERROR: Name(s) is not alphabetical")
            return None

    ##activates date check
    if date_valid(employees_details[3]) == False:
        messagebox.showerror("Error","ERROR: Date is erroneous")
        return None

    ##activates email check
    if email_valid(employees_details[4]) == False:
        messagebox.showerror("Error","ERROR: Email not valid")
        return None

    ##activates phone check
    if phone_valid(employees_details[5]) == False:
        messagebox.showerror("Error","ERROR: Number not valid")
        return None

    add_employees()





## function that adds employee to database
def add_employees():
    employee_database_backend.insert(employee_fn_text.get().title().strip() , employee_sn_text.get().title().strip() , employee_pass_text.get().strip() , employee_date_text.get().strip() , employee_email_text.get().strip() , employee_phone_text.get().strip())
    
    view_employees()
    
    boss_employee_firstname_entry.delete(0,END)
    boss_employee_surname_entry.delete(0,END)
    boss_employee_password_entry.delete(0,END)
    boss_employee_dob_entry.delete(0,END)
    boss_employee_email_entry.delete(0,END)
    boss_employee_phone_entry.delete(0,END)





## function that updates emloyees in databases 
def update_employees():
    employee_database_backend.update(selected_tuple_bmem[0], employee_fn_text.get().title().strip() , employee_sn_text.get().title().strip() , employee_pass_text.get().strip() , employee_date_text.get().strip() , employee_email_text.get().strip() , employee_phone_text.get().strip())

    view_employees()
    
    boss_employee_firstname_entry.delete(0,END)
    boss_employee_surname_entry.delete(0,END)
    boss_employee_password_entry.delete(0,END)
    boss_employee_dob_entry.delete(0,END)
    boss_employee_email_entry.delete(0,END)
    boss_employee_phone_entry.delete(0,END)





## function that validates inputs before updating employees
def update_employees_validation():
    employees_details = [employee_fn_text.get().title().strip() , employee_sn_text.get().title().strip() , employee_pass_text.get().strip() , employee_date_text.get().strip() , employee_email_text.get().strip() , employee_phone_text.get().strip()]

    for entry in employees_details:
        if pressence_check(entry) == False:
            messagebox.showerror("ERROR","ERROR: Missing field(s)")
            return None

    ##activates alphabet checks 
    for name in employees_details[0:2]:
        if alpha_check(name) == False:
            messagebox.showerror("Error","ERROR: Name(s) is not alphabetical")
            return None

    ##activates date check
    if date_valid(employees_details[3]) == False:
        messagebox.showerror("Error","ERROR: Date is erroneous")
        return None

    ##activates update email check
    if update_email_valid(employees_details[4]) == False:
        messagebox.showerror("Error","ERROR: Email not valid")
        return None

    ##activates phone check
    if phone_valid(employees_details[5]) == False:
        messagebox.showerror("Error","ERROR: Number not valid")
        return None

    update_employees()





## function that allows user to search for empolyee in database 
def search_employees():
    boss_employee_list.delete(0,END)
    for row in employee_database_backend.search(employee_fn_text.get().title().strip() , employee_sn_text.get().title().strip() , employee_pass_text.get().strip() , employee_date_text.get().strip() , employee_email_text.get().strip() , employee_phone_text.get().strip()):
        boss_employee_list.insert(END,row)





## function that deletes a employee from database 
def delete_employees():
    employee_database_backend.delete(selected_tuple_bmem[0])
    view_employees()
    
    boss_employee_firstname_entry.delete(0,END)
    boss_employee_surname_entry.delete(0,END)
    boss_employee_password_entry.delete(0,END)
    boss_employee_dob_entry.delete(0,END)
    boss_employee_email_entry.delete(0,END)
    boss_employee_phone_entry.delete(0,END)
##### start of boss manage employees menu #####






###### ^ backend functions / frontend functions v #######################################################################################







##create the window the system will use
global window1
window1 = Tk()

window1.geometry("800x350")
window1.title("Hamia Motors")


logo = Label(window1, text = "Hamia Motors")
logo.pack()








##### start of frames #####

## frame1 - customer or employee login
frame1 = Frame(window1)



customer_button = Button(frame1,text = "Customer signup/login", height = 5, width = 20, bg = "red", command = frame_switch1)#to signup/login
customer_button.grid(row = 3, column = 5, pady = (100,0))



employee_button = Button(frame1, text = "Staff Login", height = 5, width = 20, bg = "red",  command = frame_switch2)#to staff logins
employee_button.grid(row = 3, column = 6,  pady = (100,0), padx = (50,0))
## end of frame1








##frame2 - customer login/signup
frame2 = Frame(window1)

signup_button = Button(frame2, text = "Customer Signup",height = 5, width = 15,bg = "red",  command = frame_switch3) #to sign up
signup_button.grid(row = 3, column = 5, pady = (100,0))



login_button = Button(frame2, text = "Customer Login", height = 5, width = 15,bg = "red",  command = frame_switch4) #to login 
login_button.grid(row = 3, column = 6, pady = (100,0), padx = (50,0))
## end of frame2








##frame3 - boss/employee login
frame3 = Frame(window1)

employee_login_button = Button(frame3, text = "Employee Login", height = 5, width = 15, bg = "red", command = frame_switch5)#to employee login
employee_login_button.grid(row = 3, column = 5, pady = (100,0))



boss_login_button = Button(frame3, text = "Boss Login", height = 5, width = 15, bg = "red",  command = frame_switch6)#to boss login 
boss_login_button.grid(row = 3, column = 6, pady = (100,0), padx = (50,0))
## end of frame3









##frame4 - customer sign up page - takes details and validates them 
frame4 = Frame(window1)

#label and entry for customer forename
forename = Label(frame4, text = "Forename: ")
forename.grid(row = 0, column = 0)

firstname_text = StringVar()
fn_enter = Entry(frame4, textvariable = firstname_text)
fn_enter.grid(row = 0, column = 1)



#label and entry for customer surname
surname = Label(frame4, text = "Surname: ")
surname.grid(row = 1, column = 0)

surname_text = StringVar()
sn_enter = Entry(frame4, textvariable = surname_text)
sn_enter.grid(row = 1, column = 1)



#label and entry for customer password
password = Label(frame4, text = "Password: ")
password.grid(row = 2, column = 0)

password_text = StringVar()
pass_enter = Entry(frame4, textvariable = password_text)
pass_enter.grid(row = 2, column = 1)



#label and entry for customer password confirm
password_conf = Label(frame4, text = "Password Confirm: ")
password_conf.grid(row = 3, column = 0)

password_conf_text = StringVar()
passw_conf_enter = Entry(frame4, textvariable = password_conf_text)
passw_conf_enter.grid(row = 3, column = 1)



#label and entry for customer date of birth
dob = Label(frame4, text = "DOB (DD/MM/YYYY): ")
dob.grid(row = 4, column = 0)

dob_text = StringVar()
dob_enter = Entry(frame4, textvariable = dob_text)
dob_enter.grid(row = 4, column = 1)



#label and entry for customer email 
em = Label(frame4, text = "Email: ")
em.grid(row = 5, column = 0)

emailadd_text = StringVar()
em_enter = Entry(frame4, textvariable = emailadd_text)
em_enter.grid(row = 5, column = 1)



#label and entry for customer phone number
pn = Label(frame4, text = "Phone Number: ")
pn.grid(row = 6, column = 0)

phonenum_text = StringVar()
pn_enter = Entry(frame4, textvariable = phonenum_text)
pn_enter.grid(row = 6, column = 1)




#confirm button
confirm_account = Button(frame4, text = "Confirm", bg = "red", command = confirm_signup)
confirm_account.grid(row = 8, column = 1, pady = (20,0), padx = (0,140))
## end of frame4 









##frame5 - employee login page
frame5 = Frame(window1)

#employee username
employee_user = Label(frame5, text = "User ID: ")
employee_user.grid(row = 0, column = 0)

employee_user_text = StringVar()
employee_user_enter = Entry(frame5, textvariable = employee_user_text)
employee_user_enter.grid(row = 0, column = 1)



#employee password
employee_pass = Label(frame5, text = "Password: ")
employee_pass.grid(row = 1, column = 0)

employee_pass_login_text = StringVar()
employee_pass_enter = Entry(frame5, textvariable = employee_pass_login_text)
employee_pass_enter.grid(row = 1, column = 1)



#confirm button 
confirm_account = Button(frame5, text = "Confirm", bg = "red", command = confirm_employee_login)
confirm_account.grid(row = 3, column = 1, pady = (20,0), padx = (0,80))
## end of frame5








##frame6 - boss login
frame6 = Frame(window1)

#boss username
boss_user = Label(frame6, text = "Username: ")
boss_user.grid(row = 0, column = 0)

boss_user_text = StringVar()
boss_user_enter = Entry(frame6, textvariable = boss_user_text)
boss_user_enter.grid(row = 0, column = 1)



#boss password
boss_pass= Label(frame6, text = "Password: ")
boss_pass.grid(row = 1, column = 0)

boss_pass_text = StringVar()
boss_pass_enter = Entry(frame6, textvariable = boss_pass_text)
boss_pass_enter.grid(row = 1, column = 1)



#confirm buttom
confirm_account = Button(frame6, text = "Confirm", bg = "red", command = confirm_boss_login)
confirm_account.grid(row = 3, column = 1, pady = (20,0), padx = (0,80))
## end of frame6








##frame7 - customer login
frame7 = Frame(window1)

#customer username  
customer_email_login = Label(frame7, text = "Email: ")
customer_email_login.grid(row = 0, column = 0)

customer_email_login_text = StringVar()
customer_email_login_entry = Entry(frame7, textvariable =  customer_email_login_text)
customer_email_login_entry.grid(row = 0 , column = 1)



#customer password
customer_password_login = Label(frame7, text = "Password: ")
customer_password_login.grid(row = 1, column = 0)

customer_password_login_text = StringVar()
customer_password_login_entry = Entry(frame7, textvariable =  customer_password_login_text)
customer_password_login_entry.grid(row = 1 , column = 1)



#confirm button 
confirm_customer_login = Button(frame7, text = "Confirm", bg = "red", command = confirm_customer_login)
confirm_customer_login.grid(row = 8, column = 1, pady = (20,0), padx = (0,80))
## end of frame7








##frame8 - customers cars page
frame8 = Frame(window1)

#car make  
customer_car_make_label= Label(frame8,text = "Make:")
customer_car_make_label.grid(row = 0,column=0)

cmake_text=StringVar()
customer_car_make_entry= Entry(frame8,textvariable = cmake_text)
customer_car_make_entry.grid(row=0,column=1)



#car model
customer_car_model_label = Label(frame8,text = "Model:")
customer_car_model_label.grid(row = 0,column=2)

cmodel_text=StringVar()
customer_car_model_entry = Entry(frame8,textvariable = cmodel_text)
customer_car_model_entry.grid(row=0,column=3)



#year made
customer_car_year_label = Label(frame8,text = "Year:")
customer_car_year_label.grid(row = 0,column=4)

cyear_text=StringVar()
customer_car_year_entry = Entry(frame8,textvariable = cyear_text)
customer_car_year_entry.grid(row=0,column=5)



#price of car
customer_car_price_label = Label(frame8,text = "Price:")
customer_car_price_label.grid(row = 1,column=0)

cprice_text=StringVar()
customer_car_price_entry = Entry(frame8,textvariable = cprice_text)
customer_car_price_entry.grid(row=1,column=1)



#car milage 
customer_car_milage_label = Label(frame8,text = "Milage:")
customer_car_milage_label.grid(row = 1,column=2)

cmilage_text=StringVar()
customer_car_milage_entry = Entry(frame8,textvariable = cmilage_text)
customer_car_milage_entry.grid(row=1,column=3)



#fuel type
customer_car_fuel_label= Label(frame8,text = "Fuel:")
customer_car_fuel_label.grid(row = 1,column=4)

cfuel_text=StringVar()
customer_car_fuel_entry = Entry(frame8,textvariable = cfuel_text)
customer_car_fuel_entry.grid(row=1,column=5)



#rent price 
customer_car_rentprice_label= Label(frame8,text = "Rent Price:")
customer_car_rentprice_label.grid(row = 2,column=0)

crentprice_text=StringVar()
customer_car_rentprice_entry = Entry(frame8,textvariable = crentprice_text)
customer_car_rentprice_entry.grid(row=2,column=1)



#number plate 
customer_car_numberplate_label = Label(frame8,text = "Number Plate:")
customer_car_numberplate_label.grid(row = 2,column=2)

cnumberplate_text=StringVar()
customer_car_numberplate_entry = Entry(frame8,textvariable = cnumberplate_text)
customer_car_numberplate_entry.grid(row=2,column=3)



#owners 
customer_car_owners_label = Label(frame8,text = "Owners:")
customer_car_owners_label.grid(row = 2,column=4)

cowners_text=StringVar()
customer_car_owners_entry = Entry(frame8,textvariable = cowners_text)
customer_car_owners_entry.grid(row=2,column=5)



#creating a list box and scroll bar
customer_cars_list = Listbox(frame8, height = 15, width = 65)
customer_cars_list.grid(row = 4, column = 0, pady = 20, rowspan=6, columnspan = 3)

customer_cars_bar = Scrollbar(frame8)
customer_cars_bar.grid(row = 5, column = 2)

customer_cars_list.configure(yscrollcommand = customer_cars_bar.set)
customer_cars_bar.configure(command = customer_cars_list.yview)

customer_cars_list.bind('<<ListboxSelect>>',get_selected_row_ccm)



#buttons
#buy car button
buy_car_button = Button(frame8,text="Buy",width=12, bg = "red", command = tuple_check_buy)
buy_car_button.grid(row = 4,column=3)

#rent car button
rent_car_button = Button(frame8,text="Rent",width=12, bg = "red", command = tuple_check_rent)
rent_car_button.grid(row=5,column=3)

#finance car button
finance_car_button = Button(frame8,text="Finance",width=12, bg = "red", command = tuple_check_finance)
finance_car_button.grid(row=6,column=3)

#view cars button
customers_view_cars_button = Button(frame8,text="View Cars",width=12, bg = "red", command = view)
customers_view_cars_button.grid(row=7,column=3)

#search car button
search_car_button = Button(frame8, text = "Search", width = 12, bg = "red", command = search)
search_car_button.grid(row =8,column=3)

view()
## end of frame8









##frame9 - employee menu page
frame9 = Frame(window1)

#manage cars button
edit_cars = Button(frame9,text="Edit Cars",width=15, bg = "red", command = manage_cars_employee)
edit_cars.grid(row = 0,column=0, pady = (20,5))

#manage rental button
edit_rentals = Button(frame9,text="Edit Rentals",width=15, bg = "red", command = manage_rental_employee)
edit_rentals.grid(row = 1,column=0, pady = (5,5))

#manage customers button
manage_customers = Button(frame9,text="Manage Customers",width=15, bg = "red", command = manage_customers_employee)
manage_customers.grid(row = 2,column=0, pady = (5,5))
##end of frame9








##frame10 -boss menu page
frame10 = Frame(window1)

#manage cars button
edit_cars = Button(frame10,text="Edit Cars",width=15, bg = "red", command = manage_cars_boss)
edit_cars.grid(row = 0,column=0, pady = (20,5))

#manage rental button
edit_rentals = Button(frame10,text="Edit Rentals",width=15, bg = "red", command = manage_rental_boss)
edit_rentals.grid(row = 1,column=0, pady = (5,5))

#manage employees button
manage_employees = Button(frame10,text="Manage Employees",width=15, bg = "red", command = manage_employees_boss)
manage_employees.grid(row = 2,column=0, pady = (5,5))

#manage customers button
manage_customers = Button(frame10,text="Manage Customers",width=15, bg = "red", command = manage_customers_boss)
manage_customers.grid(row = 3,column=0, pady = (5,5))

#view sales button
view_sales = Button(frame10,text="View Sales",width=15, bg = "red", command = display_sales)
view_sales.grid(row = 4,column=0, pady = (5,5))
## end of frame10





        



##frame11 - authentication
frame11 = Frame(window1)


#customer username  
authenticate_email_label = Label(frame11, text = "Email: ")
authenticate_email_label.grid(row = 0, column = 0)

authenticate_email_text = StringVar()
authenticate_email_entry = Entry(frame11, textvariable =  authenticate_email_text)
authenticate_email_entry.grid(row = 0 , column = 1)



#customer password
authenticate_password_label = Label(frame11, text = "Password: ")
authenticate_password_label.grid(row = 1, column = 0)

authenticate_password_text = StringVar()
authenticate_password_entry = Entry(frame11, textvariable =  authenticate_password_text)
authenticate_password_entry.grid(row = 1 , column = 1)



#confirm button 
confirm_customer_login = Button(frame11, text = "Confirm", bg = "red", command = authenticate_details)
confirm_customer_login.grid(row = 8, column = 1, pady = (20,0), padx = (0,80))
## end of frame11








##frame15 - employees edit cars
frame15 = Frame(window1)

#car make
employee_car_make_label = Label(frame15,text = "Make:")
employee_car_make_label.grid(row = 0,column=0)

make_text=StringVar()
employee_car_make_entry = Entry(frame15,textvariable = make_text)
employee_car_make_entry.grid(row=0,column=1)


#car model
employee_car_model_label = Label(frame15,text = "Model:")
employee_car_model_label.grid(row = 0,column=2)

model_text=StringVar()
employee_car_model_entry = Entry(frame15,textvariable = model_text)
employee_car_model_entry.grid(row=0,column=3)


#year made
employee_car_year_label = Label(frame15,text = "Year:")
employee_car_year_label.grid(row = 0,column=4)

year_text=StringVar()
employee_car_year_entry = Entry(frame15,textvariable = year_text)
employee_car_year_entry.grid(row=0,column=5)


#price of car
employee_car_price_label = Label(frame15,text = "Price:")
employee_car_price_label.grid(row = 1,column=0)

price_text=StringVar()
employee_car_price_entry = Entry(frame15,textvariable = price_text)
employee_car_price_entry.grid(row=1,column=1)

#car milage 
employee_car_milage_label = Label(frame15,text = "Milage:")
employee_car_milage_label.grid(row = 1,column=2)

milage_text=StringVar()
employee_car_milage_entry = Entry(frame15,textvariable = milage_text)
employee_car_milage_entry.grid(row=1,column=3)

#fuel type 
employee_car_fuel_label = Label(frame15,text = "Fuel:")
employee_car_fuel_label.grid(row = 1,column=4)

fuel_text=StringVar()
employee_car_fuel_entry = Entry(frame15,textvariable = fuel_text)
employee_car_fuel_entry.grid(row=1,column=5)


#rent price 
employee_car_rentprice_label = Label(frame15,text = "Rent Price:")
employee_car_rentprice_label.grid(row = 2,column=0)

rentprice_text=StringVar()
employee_car_rentprice_entry = Entry(frame15,textvariable = rentprice_text)
employee_car_rentprice_entry.grid(row=2,column=1)


#number plate 
employee_car_numberplate_label = Label(frame15,text = "Number Plate:")
employee_car_numberplate_label.grid(row = 2,column=2)

numberplate_text=StringVar()
employee_car_numberplate_entry = Entry(frame15,textvariable = numberplate_text)
employee_car_numberplate_entry.grid(row=2,column=3)


#owners 
employee_car_owners_label = Label(frame15,text = "Owners:")
employee_car_owners_label.grid(row = 2,column=4)

owners_text=StringVar()
employee_car_owners_entry = Entry(frame15,textvariable = owners_text)
employee_car_owners_entry.grid(row=2,column=5)


#rented 
employee_car_rented_label = Label(frame15,text = "Rented (enter 0 if not):")
employee_car_rented_label.grid(row = 3,column=0)

rented_text=StringVar()
employee_car_rented_entry = Entry(frame15,textvariable = rented_text)
employee_car_rented_entry.grid(row=3,column=1)



#creating a list box and scroll bar
employees_car_list = Listbox(frame15, height = 15, width = 65)
employees_car_list.grid(row = 4, column = 0, pady = 20, rowspan=6, columnspan = 3)

employees_car_bar = Scrollbar(frame15)
employees_car_bar.grid(row = 5, column = 2 , rowspan=6)

employees_car_list.configure(yscrollcommand=employees_car_bar.set)
employees_car_bar.configure(command=employees_car_list.yview)

employees_car_list.bind('<<ListboxSelect>>',get_selected_row_ecm)



#buttons
#view cars button
employees_view_cars_button = Button(frame15,text="View",width=12, bg = "red", command = view_cars)
employees_view_cars_button.grid(row = 4,column=3)

#add cars button
employees_add_cars_button = Button(frame15,text="Add",width=12, bg = "red", command = add_cars_validation)
employees_add_cars_button.grid(row=5,column=3)

#update cars button
employees_update_cars_button = Button(frame15,text="Update",width=12, bg = "red", command = update_cars_validation)
employees_update_cars_button.grid(row=6,column=3)

#delete cars button
employees_delete_cars_button = Button(frame15, text = "Delete", width = 12, bg = "red", command = delete_cars)
employees_delete_cars_button.grid(row =7,column=3)

#search cars button
employees_search_cars_button = Button(frame15, text = "Search", width = 12, bg = "red", command = search_cars)
employees_search_cars_button.grid(row =8,column=3)

view_cars()
## end of frame15








##frame16 - edit rentals
frame16 = Frame(window1)


#customer id  
employee_rent_customerid_label = Label(frame16,text = "Customer ID:")
employee_rent_customerid_label.grid(row = 0,column=0)

customerID_text=StringVar()
employee_rent_customerid_entry = Entry(frame16,textvariable = customerID_text)
employee_rent_customerid_entry.grid(row=0,column=1)


#car id
employee_rent_carid_label = Label(frame16,text = "Car ID:")
employee_rent_carid_label.grid(row = 0,column=2)

carID_text=StringVar()
employee_rent_carid_entry = Entry(frame16,textvariable = carID_text)
employee_rent_carid_entry.grid(row=0,column=3)


#rent date
employee_rent_rentdate_label = Label(frame16,text = "Rent Date:")
employee_rent_rentdate_label.grid(row = 0,column=4)

rentdate_text=StringVar()
employee_rent_rentdate_entry = Entry(frame16,textvariable = rentdate_text)
employee_rent_rentdate_entry.grid(row=0,column=5)


#rent length
employee_rent_rentlength_label = Label(frame16,text = "Rent Length:")
employee_rent_rentlength_label.grid(row = 1,column=0)

rentlength_text=StringVar()
employee_rent_rentlength_entry = Entry(frame16,textvariable = rentlength_text)
employee_rent_rentlength_entry.grid(row=1,column=1)


#creating a list box and scroll bar
employee_rent_list = Listbox(frame16, height = 15, width = 65)
employee_rent_list.grid(row = 4, column = 0, pady = 20, rowspan=6, columnspan = 3)

employee_rent_bar = Scrollbar(frame16)
employee_rent_bar.grid(row = 5, column = 2 , rowspan =6)

employee_rent_list.configure(yscrollcommand = employee_rent_bar.set)
employee_rent_bar.configure(command=employee_rent_list.yview)

employee_rent_list.bind('<<ListboxSelect>>',get_selected_row_erm)



#buttons
#view rentals button
employees_view_rentals_button = Button(frame16,text="View",width=12, bg = "red", command = view_rentals)
employees_view_rentals_button.grid(row = 4,column=3)

#update rentals button
employees_update_rentals_button = Button(frame16,text="Update",width=12, bg = "red", command = update_rentals_validation)
employees_update_rentals_button.grid(row=5,column=3)

#delete rentals button
employees_delete_rentals_button = Button(frame16, text = "Delete", width = 12, bg = "red", command = delete_rentals)
employees_delete_rentals_button.grid(row =6,column=3)

#search rentals button
employees_search_rentals_button = Button(frame16, text = "Search", width = 12, bg = "red", command = search_rentals)
employees_search_rentals_button.grid(row =7,column=3)

view_rentals()
## end of frame16








##frame17 - manage customers
frame17 = Frame(window1)

#first name
customer_firstname_label = Label(frame17, text = "Forename: ")
customer_firstname_label.grid(row = 0, column = 0)

customer_firstname_text = StringVar()
customer_firstname_entry = Entry(frame17, textvariable = customer_firstname_text)
customer_firstname_entry.grid(row = 0, column = 1)

#surname
customer_surname_label = Label(frame17, text = "Surname: ")
customer_surname_label.grid(row = 0, column = 2)

customer_surname_text = StringVar()
customer_surname_entry = Entry(frame17, textvariable = customer_surname_text)
customer_surname_entry.grid(row = 0, column = 3)

#password
customer_password_label = Label(frame17, text = "Password: ")
customer_password_label.grid(row = 0, column = 4)

customer_pass_text = StringVar()
customer_password_entry = Entry(frame17, textvariable = customer_pass_text)
customer_password_entry.grid(row = 0, column = 5)

#dob
customer_dob_label = Label(frame17, text = "DOB (DD/MM/YYYY): ")
customer_dob_label.grid(row = 1, column = 0)

customer_dob_text = StringVar()
customer_dob_entry = Entry(frame17, textvariable = customer_dob_text)
customer_dob_entry.grid(row = 1, column = 1)

#email
customer_email_label = Label(frame17, text = "Email: ")
customer_email_label.grid(row = 1, column = 2)

customer_email_text = StringVar()
customer_email_entry = Entry(frame17, textvariable = customer_email_text)
customer_email_entry.grid(row = 1, column = 3)

#phone
customer_phone_label = Label(frame17, text = "Phone Number: ")
customer_phone_label.grid(row = 1, column = 4)

customer_phone_text = StringVar()
customer_phone_entry = Entry(frame17, textvariable = customer_phone_text)
customer_phone_entry.grid(row = 1, column = 5)



#creating a list box and scroll bar
manage_customers_list = Listbox(frame17, height = 15, width = 75)
manage_customers_list.grid(row = 4, column = 0, pady = 20, rowspan=6, columnspan = 3)

manage_customers_bar = Scrollbar(frame17)
manage_customers_bar.grid(row = 5, column = 2 , rowspan=6)

manage_customers_list.configure(yscrollcommand=manage_customers_bar.set)
manage_customers_bar.configure(command=manage_customers_list.yview)

manage_customers_list.bind('<<ListboxSelect>>',get_selected_row_emcm)


#buttons
#view customers button
boss_view_customer_button = Button(frame17,text="View",width=12, bg = "red", command = view_customers)
boss_view_customer_button.grid(row = 4,column=3)

#add customers button
boss_add_customer_button = Button(frame17,text="Add",width=12, bg = "red", command = add_customers_validation)
boss_add_customer_button.grid(row=5,column=3)

#update customers button
boss_update_customer_button = Button(frame17,text="Update",width=12, bg = "red", command = update_customers_validation)
boss_update_customer_button.grid(row=6,column=3)

#delete customers button
boss_delete_customer_button = Button(frame17, text = "Delete", width = 12, bg = "red", command = delete_customers)
boss_delete_customer_button.grid(row =7,column=3)

#search customers button
boss_search_customer_button = Button(frame17, text = "Search", width = 12, bg = "red", command = search_customers)
boss_search_customer_button.grid(row =8,column=3)

view_customers()
## end of frame17









##frame18 - manage employees
frame18 = Frame(window1)

#first name
boss_employee_firstname_label = Label(frame18, text = "Forename: ")
boss_employee_firstname_label.grid(row = 0, column = 0)

employee_fn_text = StringVar()
boss_employee_firstname_entry = Entry(frame18, textvariable = employee_fn_text)
boss_employee_firstname_entry.grid(row = 0, column = 1)

#surname
boss_employee_surname_label = Label(frame18, text = "Surname: ")
boss_employee_surname_label.grid(row = 0, column = 2)

employee_sn_text = StringVar()
boss_employee_surname_entry = Entry(frame18, textvariable = employee_sn_text)
boss_employee_surname_entry.grid(row = 0, column = 3)

#password
boss_employee_password_label = Label(frame18, text = "Password: ")
boss_employee_password_label.grid(row = 0, column = 4)

employee_pass_text = StringVar()
boss_employee_password_entry = Entry(frame18, textvariable = employee_pass_text)
boss_employee_password_entry.grid(row = 0, column = 5)

#dob
boss_employee_dob_label = Label(frame18, text = "DOB (DD/MM/YYYY): ")
boss_employee_dob_label.grid(row = 1, column = 0)

employee_date_text = StringVar()
boss_employee_dob_entry = Entry(frame18, textvariable = employee_date_text)
boss_employee_dob_entry.grid(row = 1, column = 1)

#email
boss_employee_email_label = Label(frame18, text = "Email: ")
boss_employee_email_label.grid(row = 1, column = 2)

employee_email_text = StringVar()
boss_employee_email_entry = Entry(frame18, textvariable = employee_email_text)
boss_employee_email_entry.grid(row = 1, column = 3)

#phone
boss_employee_phone_label = Label(frame18, text = "Phone Number: ")
boss_employee_phone_label.grid(row = 1, column = 4)

employee_phone_text = StringVar()
boss_employee_phone_entry = Entry(frame18, textvariable = employee_phone_text)
boss_employee_phone_entry.grid(row = 1, column = 5)



#creating a list box and scroll bar
boss_employee_list = Listbox(frame18, height = 15, width = 75)
boss_employee_list.grid(row = 4, column = 0, pady = 20, rowspan=6, columnspan = 3)

boss_employee_bar = Scrollbar(frame18)
boss_employee_bar.grid(row = 5, column = 2 , rowspan=6)

boss_employee_list.configure(yscrollcommand=boss_employee_bar.set)
boss_employee_bar.configure(command=boss_employee_list.yview)

boss_employee_list.bind('<<ListboxSelect>>',get_selected_row_bmem)


#buttons
#view employees button
boss_view_employees_button = Button(frame18,text="View",width=12, bg = "red", command = view_employees)
boss_view_employees_button.grid(row = 4,column=3)

#add employee button
boss_add_employees_button = Button(frame18,text="Add",width=12, bg = "red", command = add_employees_validation)
boss_add_employees_button.grid(row=5,column=3)

#update employee button
boss_delete_employees_button = Button(frame18, text = "Update", width = 12, bg = "red", command = update_employees_validation)
boss_delete_employees_button.grid(row =6,column=3)

#delete employee button
boss_delete_employees_button = Button(frame18, text = "Delete", width = 12, bg = "red", command = delete_employees)
boss_delete_employees_button.grid(row =7,column=3)

#search employee button
boss_search_employees_button = Button(frame18, text = "Search", width = 12, bg = "red", command = search_employees)
boss_search_employees_button.grid(row =8,column=3)

view_employees()
##end of frame18





##opens the system on frame1
car_details = []

frame1.pack()
window1.mainloop()
