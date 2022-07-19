import matplotlib.pyplot as plt
import random as rnd
from vector import Vector
from epidemic import Agent


p = []
for i in range(20):
    p.append(
                Agent(
                            Vector( rnd.uniform(0., 50), rnd.uniform(0., 50) ),
                            Vector.random(), 
                            2,
                )
    )

fig, ax = plt.subplots(figsize=[6,6])

ax.set(xlim = [0, 50], ylim = [0, 50])


for t in range(100):
    ax.cla()

    print(t)

    for pi in p:
        x, y = pi.pos.astuple()
        plt.plot(x, y, 'o', ms = 5, color = 'blue')
        pi.drift(constraints=[0, 0, 50, 50], bc = 'reflect')
    
    ax.set(xlim = [0, 50], ylim = [0, 50])
    
    plt.pause(0.001)


plt.show()
