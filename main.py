import numpy as np 

#multidimension array
array=np.array([[1 ,2 ,3 ],
               [4 ,5 ,6 ],
               [7 ,8, 9]])
#3d array
array3 = np.array([
    [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
    [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
    [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]
])


print(array.ndim)
print(array3.ndim)
print(array3.shape)

print(array3[1,1,2])

word=array3[1,1,1]+array3[2,0,2]+array3[1,1,0]+array3[1,2,0]+array3[2,2,0]
print(word)

#array slicing
print(array[0:2,1:3])
