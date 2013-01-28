from number_line import number_line


numline = number_line()
examples = ['x>=7','x=4','x<2']

#plot each equation one by one
for e in examples:
	numline.graph(e)
	numline.save('%s.png' % (e))
	numline.clear()
	
#plot all equations on one graph
numline.graph(examples)
numline.save('all.png')

#using different radius and number of tickmarks
larger_numline = number_line(radius = 100, tickmarks = 4)
larger_numline.graph('x>25')
larger_numline.save('x>25.png')
