import matplotlib.pyplot as plt   
import matplotlib.animation as animation
     
fig, ax = plt.subplots()
    
def animate(frameNo): 
  global ax   
  ax.cla()
  
  ax.set_xlim(0,10)
  
  ax.set_ylim(0,10)
  
  ax.plot(frameNo, frameNo, 'ro')
  
  return ax

     
def run():
  global fig  

  simpanimation = animation.FuncAnimation(fig, animate, frames = 10, interval = 1000)
  plt.show()
      
run()  