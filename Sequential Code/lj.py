import random
import math
import csv
import time

#initializing constants
epsilon=16.5402* math.pow(10,-22)
sigma=0.3405* math.pow(10,-9)
rcut=math.pow(2,1/6)*sigma
rcutsquare=math.pow(rcut,2)

#calculating force
def calculateforce(r):
	A=sigma/r
	force = 4 * epsilon * ( math.pow(A,12) - math.pow(A,6) )
	return force


#initializing a list to store location of atoms 
atomLocation = [0]*5000

#initializing a 2D list for storing atomLocation[i] and F[i]
mylist = [ [0]*2 for i in range(5000)]


#generating random values for atomLocation[i]
for i in range(5000):
	atomLocation[i]=random.uniform(0,100)
	mylist[i][0]=atomLocation[i]

#calculating F[i]
start_time=time.time()
for i in range(5000):
	totalforce=0
	for j in range(5000):
		if(i != j):
			d=abs(atomLocation[i]-atomLocation[j])* math.pow(10,-9)
			dsquare=math.pow(d,2)
			#print(dsquare)
			if dsquare < rcutsquare:
				force=calculateforce(d)
				totalforce=totalforce+force	
	mylist[i][1]=totalforce

end_time=time.time()
total_time=end_time-start_time
print total_time 


#write the values to csv file
my_new_list = open('ljdataset.csv', 'wb')
csv_writer = csv.writer(my_new_list)
csv_writer.writerows(mylist)
my_new_list.close() 

