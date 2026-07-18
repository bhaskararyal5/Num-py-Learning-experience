import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([2023,2024,2025,2026])
y1 = np.array([15,25,30,20])
y2 = np.array([5,45,50,34])

line_style=dict(marker=".",
                markersize=10,
                markerfacecolor="red",
                mec="red",
                linestyle="solid",
                linewidth=4,
                )

plt.title("Class size",fontsize=20,
                        family="Arial",
                        fontweight="bold",
                        color="blue")

plt.xlabel("Year",fontsize=20)
plt.ylabel("Students",fontsize=20)

plt.plot(x1,y1,color="cyan",**line_style)
plt.plot(x1,y2,color="green",**line_style)

plt.xticks(x1)

plt.show()