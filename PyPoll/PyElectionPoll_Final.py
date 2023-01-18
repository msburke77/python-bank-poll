#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Dependancies
import os
import csv

load_ElectionDataFile = os.path.join(".","Resources","election_data.csv")
electionResults_Output =  os.path.join (".","electionResults_Output.txt")

#initialize variables for loop
counter = 0
ccs_Counter = 0
dd_Counter = 0
rad_Counter = 0
winning_vote = 0
winning_candidate = ""
candidate_Counterlist = ["",""]
candidate_FullCounterlist = []
candidate_votes = {}

with open(load_ElectionDataFile) as ED_File:
    read_ED = csv.reader(ED_File)
    header = next(read_ED) #skiphead
    
    for row in  read_ED :
        counter += 1
        
        #candidate = row[2]
        if(row[2]=="Charles Casper Stockham"):
            ccs_Counter += 1
            candidate_Counterlist[0] = row[2]
            candidate_Counterlist[1] = ccs_Counter
            candidate_FullCounterlist.append(candidate_Counterlist[0])
            candidate_votes[row[2]] = ccs_Counter
        elif(row[2]=="Diana DeGette"):
            dd_Counter += 1
            candidate_votes[row[2]] = dd_Counter
            #candidate_Counterlist[0] = row[2]
            #candidate_Counterlist[1] = dd_Counter
        elif(row[2]=="Raymon Anthony Doane"):
            rad_Counter += 1
            candidate_votes[row[2]] = rad_Counter
            
              
      
    else:
        
        for candidate in candidate_votes:
            votes = candidate_votes[candidate]
            
            if(votes > winning_vote):
                winning_vote = votes
                winning_candidate = candidate
    
        output_ED = (f"Election Results\n"
                     f"------------------------------\n"
                     f"Total Votes: {counter}\n"
                     f"------------------------------\n"
                     f"Charles Casper Stockham: {round((int(ccs_Counter) / int(counter))*100, 3)}% ({ccs_Counter})\n"
                     f"Diana DeGette:  {round((int(dd_Counter) / int(counter))*100, 3)}%  ({dd_Counter})\n"
                     f"Raymon Anthony Doane:  {round((int(rad_Counter) / int(counter))*100, 3)}%  ({rad_Counter})\n"
                     f"------------------------------\n"
                     f"Winner: {winning_candidate}\n"
                     f"------------------------------\n"
                     
                     
                    )
        print(output_ED)
        
with open(electionResults_Output , "w") as txt_file:
        txt_file.write(output_ED)
        


# In[ ]:





# In[ ]:




