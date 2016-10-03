# euler 061:
'''
	Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all figurate (polygonal) 
	numbers and are generated by the following formulae:
	Triangle	 	P3,n=n(n+1)/2	 	1, 3, 6, 10, 15, ...
	Square	 	P4,n=n2	 	1, 4, 9, 16, 25, ...
	Pentagonal	 	P5,n=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
	Hexagonal	 	P6,n=n(2n−1)	 	1, 6, 15, 28, 45, ...
	Heptagonal	 	P7,n=n(5n−3)/2	 	1, 7, 18, 34, 55, ...
	Octagonal	 	P8,n=n(3n−2)	 	1, 8, 21, 40, 65, ...
	The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties.

	The set is cyclic, in that the last two digits of each number is the first two digits of the next number
	(including the last number with the first).
	Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and pentagonal (P5,44=2882),
	is represented by a different number in the set.

	This is the only set of 4-digit numbers with this property.
	
Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, square,
pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.
'''

def trianglular(n):
''' returns nth triangular number '''
	if n < 1 or n != n // 1:
		raise(ValueError('input must be a positive integer'))
	else:
		return (n*n+1) //2
def square(n):
''' returns nth square number '''
	if n < 1 or n != n // 1:
		raise(ValueError('input must be a positive integer'))
	else:
		return n**2
def pentagonal(n):
''' returns nth pentagonal number '''
	if n < 1 or n != n // 1:
		raise(ValueError('input must be a positive integer'))
	else:
		return (n*(3*n-1))//2
def hexagonal(n):
'''returns nth hexagonal number '''
	if n < 1 or n != n // 1:
		raise(ValueError('input must be a positive integer'))
	else:
		return n*(2*n-1)	
def heptagonal(n):
''' returns nth heptagonal number '''
	if n < 1 or n != n // 1:
		raise(ValueError('input must be a positive integer'))
	else:
		return (n*((5*n)-3))//2
def octagonal(n):
''' returns nth octagonal number '''
	if n < 1 or n != n // 1:
		raise(ValueError('input must be a positive integer'))
	else:
		return (n*(3*n-2))


def set_fourdigit_strings(function):
	n = 1
	def internal_generator():
		fn = function(n)
		while fn < 10000:
			if fn >= 1000
				yield fn
			n += 1
			fn = f(n)
	return {str(x) for x in internal_generator()}

geometricFunctions = (trianglular, square, pentagonal, hexagonal, heptagonal, octagonal)
triangles, squares, pentagons, hexagons, heptagons, octagons = tuple( 
	set_fourdigit_strings(function) for function in geometricFunctions)
	
geometricSets = (triangles, squares, pentagons, hexagons, heptagons, octagons)

# find geometric numbers whose end digits match the starting digits for at least some of the elements in the next set

def whittle_down(geometricSets):
	for setIndex, geom in enumerate(geometricSets):
		nextGeom = geometricSets[setIndex+1] if setIndex+1 < len(geometricSets) else geometricSets[0]
		nextGeomStartChars = {string[:2] for string in nextGeom}
		geom = {x for x in geom if x[2:] in nextGeomStartChars}
	return geometricSets:
	
for n in range(10):
	geometricSets = whittle_down(geometricSets)

for x in geometricSets:
	print(x)