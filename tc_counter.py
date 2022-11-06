"""Lab5 Pawan Nihure UCID:30160898""" 
import numpy as np 
from datetime import date

class Data:
    '''class to store data input by user'''
    def __init__(self,name,p_n,email):
        '''Method describing user input'''
        self.name = name
        self.phone_number = p_n
        self.email = email
   
    def store_data(self):
        '''Method to store user input input in a sublist'''
        sub_list = [self.name,self.phone_number,self.email]
        return sub_list

  
class ticket(Data):
    '''Class to issue and scan tickets'''
    def __init__(self,name,p_n,email):
        '''Method to inherit user input from class Data'''
        super().__init__(name, p_n,email)
        
    
    def issue(self,tc):  
        '''Method to issue ticket until the count of 200'''
        while tc< 200: 
            dt = date.today()   #generate today's date
            return [dt,self.name,self.phone_number,self.email]
        else:
            return False

    def scan(self,name3,ph3,list):
        '''Method to scan and validate tickets from user inputs stored in a list'''
        nlist = [item[0] for item in list]   # create list for names from nested list
        phlist = [item[1] for item in list]  # create list for phone number from nested list
        if name3 in nlist and ph3 in phlist:
            return True 
        else:
            return False

   
                
        
        
       



        



    

        

