import string
import pylab as plt

class number_line(object):
	def __init__(self, radius=10):

		self.radius = radius
		self.span = radius * 1.1 #edges of the graph. leaves room for arrows
		self.ceil = radius + 1 #if a plot goes to this point it means it is going to infinity
		self.floor = -radius - 1 #if a plot goes to this point it means it is going to negative infinity
		
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
		plt.axis([-self.span, self.span, -1, 1]) # sets dimensions of axes to xmin, xmax, ymin, ymax
	
	def drawLine(self):
		#plot the main line  (slightly crooked so svg will render)
		plt.plot([-self.radius,self.radius],[0,0.001],'k',linewidth=self.black_linewidth,zorder=1) 


		#tick marks and labels
		for i in range(-self.radius,self.radius+1):
			length = .03
			tick_y = -.1
			if i==0: 
				length=.05
				tick_y = -.13
			 #plot the tick marks (slightly crooked so svg will render)
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
		
		toGraph = []
		for eq in eqs:
			toGraph = self.solve(eq,toGraph)

		for piece in toGraph:
			
			#if this piece of the graph is a point
			if len(piece)==1: 
				plt.plot(piece,[0],'or', markersize = self.circle_size, markeredgewidth = self.circle_edge_width, zorder=10)
			
			#if this piece of the graph is a line
			elif len(piece)==2: 
			
				#if line going to negative infinity with arrow
				if piece[0]==self.floor: 
				
					plt.plot([piece[1]],[0],'or',markerfacecolor='white',markeredgecolor='r',markersize = self.circle_size, markeredgewidth = self.circle_edge_width, zorder=10)
					plt.plot([-self.radius,piece[1]],[0,0],'-r',linewidth=self.red_linewidth,zorder=5)
					self.arrow((-self.span,0),'r',facingRight = False)
				
				#if line going to positive infinity with arrow
				if piece[1]==self.ceil:
				
					plt.plot([piece[0]],[0],'or',markerfacecolor='white',markeredgecolor='r',markersize = self.circle_size, markeredgewidth = self.circle_edge_width,zorder=10)
					plt.plot([piece[0],self.radius],[0,0],'-r',linewidth=self.red_linewidth,zorder=5)
					self.arrow((self.span,0),'r',facingRight = True)
				
	#helper method for graph turns the equations into coordinates
	def solve(self,eq, toGraph):
	    
		
	    if '>' in eq:
	        toGraph.append([self.getAfter(eq,'>') , self.ceil])
	    elif '<' in eq:
	        toGraph.append([self.floor,self.getAfter(eq,'<')])
	
	    if '=' in eq:
	        toGraph.append([self.getAfter(eq,'=')])
	    return toGraph
	
	#helper method for solve helps parse the equations
	def getAfter(self,s, char ):
		if'>=' in s: char = '>='
		if '<=' in s: char = '<='
		return float(string.split(s,char)[-1])

	#clears anything that is graphed
	def clear(self):
		plt.close()
		self.setup()
		self.drawLine()
	
	