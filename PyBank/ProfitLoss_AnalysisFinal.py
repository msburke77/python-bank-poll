#!/usr/bin/env python
# coding: utf-8

# In[9]:


import os
import csv

#Get File and load data into reader variable

load_DataFile = os.path.join(".","Resources","budget_data.csv")
load_outputDF = os.path.join(".","ProfitLoss_Output.txt")

with open(load_DataFile) as ProfitLoss_Data:
    read_CSVData = csv.reader(ProfitLoss_Data)
    header = next(read_CSVData)   #To skip header row 
 
    
    #initialize variables for loop
    counter = 0
    total_net = 0
    change_list = []
    
    
    greatest = ["",0]
    least = ["",9999999] 
    
    
  
    #loop thru data
    
    for data in read_CSVData:
        
        counter = counter + 1
        while(counter<=1):
            prv_row = int(data[1])
            break
        total_net += int(data[1]) #adding each amount in second column
        
        total_change = int(data[1]) -  prv_row
        prv_row = int(data[1])
        change_list.append(total_change)
        
        #Searching for greatest amount
        if(total_change  > greatest[1]):
            greatest[0] = data[0]  
            greatest[1] = total_change  
          
         #Searching for least amount
        if(total_change  < least[1]):
            least[0] = data[0]  
            least[1] = total_change
        
    else:
        output_data= (f"Financial Analysis\n"
              f"------------------------------\n"
              f"Total Months: {counter}\n"
              f"Total: ${total_net}\n"
              f"Average Change: ${round(sum(change_list)/len(change_list),2)}\n" #len(change_list)=86 this is dividing the sum by 86 (not 85)
              f"Greatest Increase in Profits: {greatest[0]} (${greatest[1]})\n"
              f"Greatest Decrease in Profits: {least[0]} (${least[1]})\n" 
             )
        print(output_data)
        
    with open(load_outputDF, "w") as txt_file:
        txt_file.write(output_data)

