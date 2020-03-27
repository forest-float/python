vec = [2,4,6]
vec1 = [3*x for x in vec]
vec2 = [4, 3, -9]

print(vec1)
vec2.sort()
print(vec2)

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])
print([3*x for x in vec if x > 3])
print( [x*y for x in vec1 for y in vec2])
print([vec1[i]*vec2[i] for i in range(len(vec1))])
print([str(round(355/113, i)) for i in range(1, 6)])

knights = {'gallahad': 'the pure', 'robin': 'the brave'}

for k, v in knights.items():
	print(k, v)

def func(agq):
	return agq

