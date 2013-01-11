from number_line import number_line
import pylab as plt

numline = number_line(radius = 10)


examples = ['x>=7','x=4','x<2']

#plot each equation one by one
for s in examples:
	numline.graph([s])
	plt.savefig('/Users/Andrew/Documents/Matplotlib1D-plot/%s.png' % (s), format='png',bbox_inches='tight',transparent = True)
	numline.clear()
	
#plot all equations on one graph
numline.graph(examples)
plt.savefig('/Users/Andrew/Documents/Matplotlib1D-plot/all.png', format='png',bbox_inches='tight',transparent = True)
