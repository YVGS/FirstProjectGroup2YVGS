import numpy as np
import matplotlib.pyplot as plt

#Question 1 

A=np.array([5,2,8,4,7,1,5,10,4,7,3,6,3,5,2,7,4,9,5,11])

#(a)

Mean=np.mean(A)
Median=np.median(A)

#(b)

Sample_variance=np.var(A,ddof=1)
standard_deviation=np.std(A,ddof=1)

#(c)

A2=A.copy()
A2[2]=12
print(A2)

Mean2=np.mean(A2)
Median2=np.median(A2)

Sample_variance2=np.var(A2,ddof=1)
standard_deviation2=np.std(A2,ddof=1)

#(d)

plt.hist(A2, bins=np.arange(0.5,13.5,1), edgecolor='black')
plt.title('Histogram of A2')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

print("Mean=", Mean)
print("Median=", Median)
print("Sample Variance=", Sample_variance)
print("Standard Deviation=", standard_deviation)

print("Mean2=", Mean2)
print("Median2=", Median2)
print("Sample Variance2=", Sample_variance2)
print("Standard Deviation2=", standard_deviation2)