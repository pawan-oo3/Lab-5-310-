import tc_counter as tcc
from colorama import Fore , Back , Style
import pandas as pd

def user_int2():
    '''Function propting to user to choose the method to be implemented by displaying messages'''
    print('WELCOME TO THE TICKET STATION')
    print ('Do you want to use a pre-issued ticket database with costummer info ---1 ')
    print('Do you want to buy a ticket? ---2')
    print('Do you want to eqnuire about the tickets? ---3')
    print('Do you want to scan your ticket? ---4')
    print ('Do you want to exit? ---5')
    ch_1 = int(input('Please enter the appropriate number '))  #input user to choose a particular methos
    return ch_1

tc1 = () 
list = []
ph_no =[]
tc=0
while True:    #assigning loop for the menu-driven program
    a = user_int2()  #call the funtion for user input
 
    if a ==1: 
        '''If user want to use a pre-issued ticket database'''
        n = int(input('Enter the number of entries you want in the dataset.(choose 200 max) ')) #allow user to choose the number of entries they want in the database 
        df = pd.read_csv ('sampleset.csv',header = 200-n)  #read the CSV file
        df5r = df.loc[:n-1,:]  #assign the locations in the CSV file
        list = df5r.values.tolist()  #create a nested list for each row from the CSV file
        tc = len(list)+1  #iterate for number tickets issued for that day

    elif a ==2: 
        '''If user want to buy tickets manually''' 
        name =  input('Enter your name. ')  #ask user for their name
        try:
            ph_n = int(input('Enter your phone number. '))  #ask user for their phone number(only integer)
            if ph_n in ph_no:  #check for phonenumber in the previous input list
                print(Fore.RED+'Phone number already in use') # print error message if true
                print (Style.RESET_ALL)#reset colour patterns
                continue #loop back to the start
            else: 
                ph_no.append(ph_n) # add phonenumber in the list 
        except ValueError:
            print(Fore.RED+'Please re-enter the phonenumber.') # display error message if string entered
            print (Style.RESET_ALL)#reset colour patterns
            continue #loop back to the start 
        email = input('Enter your email. ') #ask user for their email 
        tc1 = tcc.ticket(name,ph_n,email).issue(tc)  #call the class ticket and function to issue ticket
        if  tc1 != False:  #if not returned false
            tc =tc+1 #count for the number of ticket 
            list.append(tcc.Data(name,ph_n,email).store_data()) #ask the user inputs innto the nested loop 
            print (Fore.YELLOW + 'TICKET ISSUED:') #print a message
            print (Fore.RED, Back.BLUE + '|||', tc,tc1[0] , tc1[1] , tc1[2] , tc1[3] ,'|||' ) #print the issued ticket 
            print (Style.RESET_ALL)#reset colour patterns
        else:  #if false ()
            print (Fore.RED +'Tickets Unavailable Today')  #print a error mesage
            print (Style.RESET_ALL)  #reset colour patterns
    elif a == 3:
        '''If user wants to enquire of the tickets for today.'''
        print (200 - tc,'tickets available for today.') #display number of tickets for today
        a1 = input('Do you want to continue (y/n) ') #asks user if they want to continue
        if a1 == 'n' :  #if user wants to exit 
            print (Fore.GREEN+'Thank you for visiting !!!') #print a exit message
            print (Style.RESET_ALL) #reset colour patterns
            break  #end the program
    elif a == 4:
        '''If user wants to scan their ticket'''
        name3 = input('Enter your name on the ticket ')   #ask user to enter the name on the ticket
        ph_n3 = int(input('Enter your phone nummber on the ticket ')) #for double checking ask user to enter their phone number
        name = [item[0] for item in list] #create list of names from nested list
        ph_n = [item[1] for item in list] #create list of phone number from nested list
        email = [item[2] for item in list] #create list of email from nested list 
        a = tcc.ticket(name,ph_n,email).scan(name3,ph_n3,list) #call the class ticket and function scan
        if a == True:  #if finction calls true
            print (Fore.GREEN + 'Ticket Found ----- ACCESS GRANTED') #print a success message
            print (Style.RESET_ALL) #reset colour patterns
            for idx, (name,ph_n,email) in enumerate(list): #in list 
                if name == name3 and ph_n == ph_n3: #if found replace the name and phone numberwith scannes values
                    list[idx][0] = 'scanned' #replacing name
                    list[idx][1] = 0      #replacing phone number      
        elif a == False: #if not in list
            print (Fore.RED+'Ticket Not Found')      #print error message
            print (Style.RESET_ALL)     #reset colour patterns 
    else:
        print(Fore.YELLOW+'THANK YOU FOR VISITING. SEE YOU AGAIN !!!')
        print (Style.RESET_ALL)     #reset colour patterns 
        break #end the program 
        
        


        
        
    
    
   
   
   

