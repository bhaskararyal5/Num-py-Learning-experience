import matplotlib.pyplot as plt
import numpy as np

categories1=np.array(["Freshman","Sophomores","Junior","Seniors"])
values1=np.array([300,250,275,225])
colors=np.array(["red","yellow","blue","grey"])

plt.pie(values1,labels=categories1,
                autopct="%1.1f%%",
                colors=colors,
                explode=[0,0,0,0.1],
                shadow=True,
                startangle=180)
plt.title("College",size=25)
plt.show()