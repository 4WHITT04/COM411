import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()

def animate (framenum):

  global ax   

  ax.cla()

  ax.set_xlim(0, 2*np.pi)
  
  ax.set_ylim(-1, 1)

  numx = np.arange(0, 2*np.pi, 0.01)

  numy = np.sin(numx + (framenum / 50))

  ax.plot(numx, numy)

def run():

  sineanimation = animation.FuncAnimation(fig, animate, frames = 720, interval = 100)
  plt.show()

run()