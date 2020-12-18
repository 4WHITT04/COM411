import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


fig, ax = plt.subplots()

def animate(framenum):
  global ax   
  # your code here (use ax to draw)
  
  ax.set_xlim(0, 720)
  
  ax.set_ylim(-1, 1)

  numx = np.arange(0, framenum)

  numxr  = numx * (np.pi / 180)

  numy = np.sin(numxr)

  ax.plot(numx, numy)

def run():

  sineanimation = animation.FuncAnimation(fig, animate, frames = 720, interval = 1)
  plt.show()

run()