import string
import pylab as plt

#Number line plotting with matplotlib.

#TODO 
#Allow "barbell" plots like 2<x<4 or x<2 *intersection* x>4

class number_line(object):
	def __init__(self, radius=10, tickmarks = 20):

		self.radius = radius
		self.span = radius * 1.1 #edges of the graph. leaves room for arrows
		self.ceil = radius + 1 #if a plot goes to this point it means it is going to infinity
		self.floor = -radius - 1 #if a plot goes to this point it means it is going to negative infinity
		
		self.num_tickmarks = tickmarks
		
		#constants
		self.black_linewidth = 3
		self.red_linewidth = 3
		self.arrow_width = 3
		self.circle_size = 11.5
		self.circle_edge_width = 1.5
		
		self.setup()
		self.drawLine()
		
	def setup(self):
		self.fig1 = plt.figure( facecolor='white') #whole background is white
		self.ax = plt.axes(frameon=False) #frame is hidden
		self.ax.axes.get_yaxis().set_visible(False) # turn off y axis
		self.ax.get_xaxis().tick_bottom() #disable ticks at top of plot
		self.ax.axes.get_xaxis().set_ticks([]) #sets ticks on bottom to blank
		plt.axis([-self.span, self.span, -1, 1]) # sets dimensions of axes
	
	#draws the number line
	def drawLine(self):
		
		#plot the main line  (slightly crooked so svg will render in webkit)
		plt.plot([-self.radius,self.radius],[0,0.001],'k',linewidth=self.black_linewidth,zorder=1) 

		#find the interval for tickmarks/labels (divide by two to account for negative numbers)
		tickmark_interval = self.radius/ (self.num_tickmarks/2)
		
		#draw in appropriate places tick marks and labels
		for i in [num for num in range(-self.radius,self.radius+1) if not num % tickmark_interval] :
			length = .03
			tick_y = -.1
			if i==0: 
				length=.05
				tick_y = -.13
			 #plot the tick marks (slightly crooked so svg will render in webkit)
			plt.plot([i,i-.001],[-length,length],'k',linewidth=2, zorder=1) 
			
			#write the labels
			plt.text(i,tick_y,str(i),horizontalalignment='center')
		
		#draw the arrows
		self.arrow((self.span,0),'k',facingRight = True)
		self.arrow((-self.span,0),'k',facingRight = False)

	#draw arrow on plot
	def arrow(self, coord, color,facingRight=True):
		tilt = 20 #horizontal left
		if  facingRight: tilt = -20 #horizontal right
		plt.annotate('', xy=coord,  xycoords='data',
			xytext=(tilt, 0), textcoords='offset points',
			arrowprops=dict(arrowstyle="->", linewidth=self.arrow_width , mutation_scale=18,color=color))
	
	#graph a series of inequalities
	def graph(self,eqs):
		
		#make equations into a list if it is not already
		if isinstance(eqs, str):
			eqs = [eqs]
		
		#get coordinates to graph
		toGraph = []
		for eq in eqs:
			toGraph = self.solve(eq,toGraph)
	
		for piece in toGraph:
			
			#if this piece of the graph is a point
			if len(piece)==1: 
				plt.plot(piece,[0],'or', markersize = self.circle_size, markeredgewidth = self.circle_edge_width, zorder=10)
			
			#if this piece of the graph is a line
			elif len(piece)==2: 
			
				#if line going to negative infinity with arrow draw 
				if piece[0]==self.floor: 
				
					plt.plot([piece[1]],[0],'or',markerfacecolor='white',markeredgecolor='r',markersize = self.circle_size, markeredgewidth = self.circle_edge_width, zorder=10)
					plt.plot([-self.radius,piece[1]],[0,0],'-r',linewidth=self.red_linewidth,zorder=5)
					self.arrow((-self.span,0),'r',facingRight = False)
				
				#if line going to positive infinity with arrow
				if piece[1]==self.ceil:
				
					plt.plot([piece[0]],[0],'or',markerfacecolor='white',markeredgecolor='r',markersize = self.circle_size, markeredgewidth = self.circle_edge_width,zorder=10)
					plt.plot([piece[0],self.radius],[0,0],'-r',linewidth=self.red_linewidth,zorder=5)
					self.arrow((self.span,0),'r',facingRight = True)
				
	#Turns an equation into coordinates to plot
	def solve(self,eq, toGraph):
	    
	    if '>' in eq:
	        toGraph.append([self.getAfter(eq,'>') , self.ceil])
	    elif '<' in eq:
	        toGraph.append([self.floor,self.getAfter(eq,'<')])
	
	    if '=' in eq:
	        toGraph.append([self.getAfter(eq,'=')])
	    return toGraph
	
	#gets float of text in a string after the <, >, <=, or >= sign to help solve equation
	def getAfter(self,s, splitchar ):
		if'>=' in s: 
			splitchar = '>='
		if '<=' in s: 
			splitchar = '<='
		
		#check if number is valid
		try:
			number = float(string.split(s, splitchar)[-1])
		except ValueError:
			raise Exception("Error parsing equations. Make sure they are of the format x>1 where x is any variable and 1 is any number")
			
		#check if within bounds
		if number < -self.radius or number > self.radius:
			raise Exception ("Some points are outside the number line's bounds. Try increasing the radius of the number line or choosing values inside the current radius.")
		return number


	#save figure to specified location
	def save(self, filepath, format='png', transparent = True):
		plt.savefig(filepath, format= format, bbox_inches='tight',transparent = transparent)

	#clears anything that is graphed
	def clear(self):
		plt.close()
		self.setup()
		self.drawLine()
	
	