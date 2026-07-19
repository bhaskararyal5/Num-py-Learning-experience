import matplotlib.pyplot as plt
import numpy as np

x=np.array([0,1,1,2,3,4,5,6,7,7,8])#hrs studied
y=np.array([55,60,63,66,69,70,74,78,83,86,90])#Grades

x1=np.array([0,1,2,2,3,3,5,6,7,8,9])#hrs studied
y1=np.array([50,57,66,66,64,73,72,79,84,89,97])#Grades

plt.scatter(x,y,color="red",
                alpha=0.5,
                s=100,
                label="Class A")

plt.scatter(x1,y1,color="blue",
                alpha=0.5,
                s=100,
                label="Class B")

plt.xlabel("Hours Studied")
plt.ylabel("Grade")

plt.legend()
plt.show()