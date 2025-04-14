# -*- coding: utf-8 -*-

# Enter your candidate ID here: AF23176
# Enter your student ID here: 21210302
# Do NOT enter your name

# 4QQMN506 Coursework Q3

import breezypythongui as bpg   #Importing breezypythongui for creating the GUI
from datetime import datetime #Importing datetime to work with dates and times

class AgeCalculator(bpg.EasyFrame):
    """Age Calculator Application """
    
    def __init__(self):
        
        bpg.EasyFrame.__init__(self, title="Age Calculator", width=400, height=600)
        self.addLabel("Enter Your Birthdate", 0, 0, columnspan=2) #Initializies Age calculator GUI frame
        # Adding input fields for the user to enter their birth year, month, and day:
        self.addLabel("Year (Enter Integer):", 1, 0)
        self.birthYear = self.addIntegerField(0, 1, 1)
        
        self.addLabel("Month (Enter Integer between 1-12):", 2, 0)
        self.birthMonth = self.addIntegerField(0, 2, 1)
        
        self.addLabel("Day (Enter Integer between 1-31):", 3, 0)
        self.birthDay = self.addIntegerField(0, 3, 1)
        
        
        self.addLabel("Enter Your Birth Time", 4, 0)
        self.addLabel("Hour (Enter Integer between 0-23):", 5, 0)
        self.birthHour = self.addIntegerField(0, 5, 1)
        
        self.addLabel("Minute:(Enter Integer between 0-59)", 6, 0)
        self.birthMinute = self.addIntegerField(0, 6, 1)  #input fields for user to enter their birthday
        
        self.addButton("Calculate", 7, 0, command=self.calculate)  #button for calculation
        self.addButton("Clear", 8, 0, command=self.clear) #button for clearing
        
        self.outputArea = self.addTextArea("", 9, 0, columnspan=2, width=50, height=5)#text area to display the results
    def calculate(self):
        
        try:
             #Check if the user has filled in all the fields
            if (self.birthYear.getValue() == 0 or 
                self.birthMonth.getValue() == 0 or
                self.birthDay.getValue() == 0 ):
                
                
                self.messageBox(title="Input Error", 
                               message="Please fill in all fields before calculating.",
                               width=30)
                return
            
            year = self.birthYear.getNumber()
            month = self.birthMonth.getNumber()
            day = self.birthDay.getNumber()
            hour = self.birthHour.getNumber()
            minute = self.birthMinute.getNumber()
            
             # Checking for valid values in the input fields:
            error_message = ""
            if month < 1 or month > 12:
                error_message += "Month must be between 1 and 12.\n"
            if day < 1 or day > 31:
                error_message += "Day must be between 1 and 31.\n"
            if hour < 0 or hour > 23:
                error_message += "Hour must be between 0 and 23.\n"
            if minute < 0 or minute > 59:
                error_message += "Minute must be between 0 and 59.\n"
            
            
            if error_message:
                self.messageBox(title="Invalid Input", 
                               message=error_message,
                               width=30)
                return
            
            try:
                birth_datetime = datetime(year, month, day, hour, minute)               
               
                current_datetime = datetime.now()                
                
                if birth_datetime > current_datetime:
                    self.messageBox(title="Invalid Date", 
                                   message="Birth date cannot be in the future.",
                                   width=30)  #Get invalid date if birthdate is in the future
                    return
                #Calculating the time(years,days,hours,minutes,seconds) difference between the current date and the birthdate                   
                time_diff = current_datetime - birth_datetime              
                total_seconds = time_diff.total_seconds()                
                
                years = round(total_seconds / (365.25 * 24 * 60 * 60), 2)
                days = round(total_seconds / (24 * 60 * 60), 2)
                hours = round(total_seconds / (60 * 60), 2)
                minutes = round(total_seconds / 60, 2)
                seconds = round(total_seconds, 2)                
                
                result_message = f"You have been alive for:\n"
                result_message += f"{years} years,\n"
                result_message += f"{days} days,\n"
                result_message += f"{hours} hours,\n"
                result_message += f"{minutes} minutes,\n"
                result_message += f"{seconds} seconds"
                
                self.outputArea.setText(result_message)
            
            except ValueError as e:                
                self.messageBox(title="Invalid Date", 
                               message="Invalid date combination. Please check your inputs.",
                               width=30)
                
        except Exception as e:
            self.outputArea.setText(f"Error: {str(e)}\nPlease check your inputs.")
    
    def clear(self):
        
        self.birthYear.setNumber(0)
        self.birthMonth.setNumber(0)
        self.birthDay.setNumber(0)
        self.birthHour.setNumber(0)
        self.birthMinute.setNumber(0)
        self.outputArea.setText("")

def main():    
    AgeCalculator().mainloop()# Main method to run the AgeCalculator application

if __name__ == "__main__":
    main()
