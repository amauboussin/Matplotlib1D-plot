import string
import pylab as plt

class cartesian(object):
	def __init__(self, xradius=5, yradius = 5):

		self.xradius = xradius
		self.yradius = yradius
		

		self.axes_linewidth = 3
		self.arrow_width = 3
		self.grid_linewidth = .5
		
		self.plot_linewidth = 2
		
		self.tick_width = 2
		self.tick_length = .1
		
		self.setup()
		self.drawAxes()
		self.drawGrid()
		
	def setup(self):
		self.fig1 = plt.figure( facecolor='white') #whole background is white
		self.ax = plt.axes(frameon=False) #frame is hidden
		self.ax.axes.get_yaxis().set_visible(False) # turn off y axis
		self.ax.get_xaxis().tick_bottom() #disable ticks at top of plot
		self.ax.axes.get_xaxis().set_ticks([]) #sets ticks on bottom to blank
		plt.axis(map(lambda x:1.2*x, [-self.xradius, self.xradius, -self.yradius, self.yradius])) # sets dimensions of axes to xmin, xmax, ymin, ymax x1.2 to leave room for arrows
	
	def drawAxes(self):
		#plot the main line  (slightly crooked so svg will render)
		plt.plot([-self.xradius,self.xradius],[0,0.001],'k',linewidth=self.axes_linewidth,zorder=1) 
		plt.plot([0,0.001],[-self.yradius*1.05, self.yradius*1.05],'k',linewidth=self.axes_linewidth,zorder=1)


		#horizontal tick marks 
		for i in range(-self.xradius,self.xradius+1):
			 #plot the tick marks (slightly crooked so svg will render)
			plt.plot([i,i-.001],[-self.tick_length,self.tick_length],'k',linewidth=self.tick_width, zorder=1) 
		#vertical tick marks
		for i in range(-self.yradius, self.yradius+1):
			plt.plot([-self.tick_length,self.tick_length],[i,i-.001],'k',linewidth=self.tick_width, zorder=1) 

		
		#draw the horizontalarrows
		self.arrow((self.xradius*1.1,0),'k',facingPositive = True, dir = 'horizontal')
		self.arrow((-self.xradius*1.1,0),'k',facingPositive = False, dir = 'horizontal')
		
		self.arrow2((0,-self.yradius*1.15), (0,100),'k')
		
	def drawGrid(self):
		#horizontal lines
		for y in range(-self.yradius, self.yradius+1):
			plt.plot([-self.xradius,self.xradius],[y,y+0.001],'k',linewidth=self.grid_linewidth,zorder=1)
		
		for x in range(-self.xradius, self.xradius+1):
			plt.plot([x,x+0.001],[-self.yradius*1.05, self.yradius*1.05],'k',linewidth=self.grid_linewidth,zorder=1)

	def arrow2(self, coord1, coord2, color):
		plt.annotate('', xy=coord1,  xycoords='data',
								xytext=coord2, textcoords='offset points',
								arrowprops=dict(arrowstyle="->", linewidth=self.arrow_width , mutation_scale=18,color=color))
							

	def arrow(self, coord, color,facingPositive=True, dir = 'horizontal'):
		tilt = 100 #horizontal left, vertical down
		if  facingPositive: tilt = -tilt #horizontal right, vertical up
		if dir == 'horizontal':
			textcoord = (tilt, 0)
		elif dir == 'vertical':
			textcoord = (0,tilt)
		else:
			raise Exception("Arrow direction should be 'horizontal' or 'vertical'")
			
		plt.annotate('', xy=coord,  xycoords='data',
						xytext=textcoord, textcoords='offset points',
						arrowprops=dict(arrowstyle="->", linewidth=self.arrow_width , mutation_scale=18,color=color))
						
	#y must be isolated is y=2x+1
	
	def plot(self, equation):
		
		xcoords=[];ycoords=[]
		equation = string.replace(equation, 'y=','')
		for x in [-self.xradius, self.xradius+1]:
			toEval = string.replace(equation, 'x', str(x))
			xcoords.append(x)
			ycoords.append(eval(toEval))
		
		plt.plot(xcoords,ycoords,'k', linewidth = self.plot_linewidth)
			
		
		