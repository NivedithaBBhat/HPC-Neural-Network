import csv
import random
import time


number_of_sample_data = 105472
number_of_iteration = 5000

def func( a,b,c,x ): 
	return a * x * x +b * x + c

def derivFunc( a,b,c,x ): 
	return 2*a * x +b 

# Function to find the root 
def newtonRaphson( a,b,c,x): 
	i=0
	E=0.0001
	h = func(a,b,c,x) / derivFunc(a,b,c,x) 
	while abs(h) > E and i < number_of_iteration: 
		h = func(a,b,c,x)/derivFunc(a,b,c,x) 
		#print(x ,"  ",h)
		# x(i+1) = x(i) - f(x) / f'(x) 
		x = x - h 
		i = i+1
	return x	


def generaterandom(mylist,i,j):
	a=random.uniform(-10,10)
	b=random.uniform(-30,30)
	c=random.uniform(-50,50)
	x0=random.uniform(-10,10)
	if(b*b - 4*a*c >= 0):
		j=1
		mylist[i][0]=a
		mylist[i][1]=b
		mylist[i][2]=c
		mylist[i][4]=x0
	return j		

mylist = [ [0]*5 for i in range(number_of_sample_data)]

i=0
start_time=time.time()
while i < number_of_sample_data:
	if(i==5120):
		ans1=time.time()-start_time
	elif (i==6144):
		ans2=time.time()-start_time
	elif(i==7168):
		ans3=time.time()-start_time
	elif(i==8192):
		ans4=time.time()-start_time
	elif(i==9216):
		ans5=time.time()-start_time
	elif(i==10240):
		ans6=time.time()-start_time
	j=0
	while(j!=1):
		j=generaterandom(mylist,i,j)
	mylist[i][3] = newtonRaphson(float(mylist[i][0]),float(mylist[i][1]),float(mylist[i][2]),float(mylist[i][4]))
	i=i+1

end_time=time.time()
total_time=end_time-start_time
print("5120-",ans1)
print("6144-",ans2)
print("7168-",ans3)
print("8192-",ans4)
print("9216-",ans5)
print("10240-",ans6)
my_new_list = open('NR.csv', 'wb')
csv_writer = csv.writer(my_new_list)
csv_writer.writerows(mylist)
my_new_list.close() 


