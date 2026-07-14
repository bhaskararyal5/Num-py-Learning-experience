import numpy as np

array =np.array([[1,2,3,4,5],
                [6,7,8,9,10]])


# print(np.sum(array))
# print(np.mean(array))
# print(np.std(array))
# print(np.var(array))
# print(np.min(array))
# print(np.max(array))
# print(np.argmin(array))
# print(np.argmax(array))

# print(np.sum(array,axis=0))

#filtering
ages=np.array([[21,22,18,19,25,30,31,67],
                [39,15,22,99,18,19,20,21]])
    
# teenagers=ages[ages<20]
# adults=ages[(ages>=18) & (ages<65)]
# seniors=ages[ages>=65]

# print(teenagers)
# print(adults)
# print(seniors)

adults=np.where(ages>=18,ages,0)
print(adults)

#generating random num genrator
rng=np.random.default_rng()

print(rng.integers(1,100,size=(3,2)))

print(np.random.uniform(low=-1,high=1))

rng.shuffle(array)
print(array)