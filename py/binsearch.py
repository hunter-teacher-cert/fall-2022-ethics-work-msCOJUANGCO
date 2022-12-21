# filename: binsearch.py
# Nicole Cojuangco
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: pythonfu, Saranii, Ed!!


#setup function
def binSearch(data,val):
    min=0;
    max=len(data)-1
    
    while (min != max):
      MID = int((min+max)/2)
    
      if (data [MID] == val):
        return MID
      elif(data[MID] < val):
        min =  MID + 1
      else:
        max = MID - 1  
  
  #exit loop
    if(data[max] == val):  
      return max


    return -1


#data set to test
TestSet =[2,4,6,7,9,11,25,29,84,84]

#test --> call binSearch and print result
print (binSearch(TestSet,9)) 

