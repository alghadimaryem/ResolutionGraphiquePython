import matplotlib.pyplot
from matplotlib.pyplot import *
import numpy
from numpy import arange
figure()
A = arange(-10, 20, 10)
B = arange(-10, 20, 10)


# constraint equation
B1 = 2 - 2*A
B2 = 3 - 3*A


xlim = (-10, 20)
ylim= (-10, 20)
hlines(0, -10, 20, color = 'k')
vlines(0, -10, 20, color = 'k')
grid(True)


xlabel('X-axis')
ylabel('Y-axis')


#Plotting graph


plot(A, B1, color = 'r')
plot(A, B2, color = 'y')
axhline(y = 0, color = 'b')
axvline(x = 0, color = 'b')









title('objective function: z = A+B with following constarints')
legend(['2A+B<=2','3A+B<=3','A>=0','B>=0'])#Les fonctions contraines
# get the co-ordinates of intersection points by mere visualisation
A = [0.0,0.0,1.0]
B = [0.0,2.0,0.0]
fill(A,B,'g+')


show()


#Getting Solution
checker = 0
#La fonction objetive
for i,j in zip(A,B):
    print('\n calculating for point: A = {0:f} and B = {1:f}' .format(i,j))
    print('solution for z = ',1*j+1*i)
    if(checker <= (1*j+1*i)):
        checker = (1*j+1*i)
        X,Y = i,j

    print('\n the maximum profit z = ${0:f} @ A = {1:f} and B = {2:f}' .format(checker,X,Y))
