import numpy

def getMean():
    s = numpy.random.uniform(0.5, 5, 100)

    i = 0
    for key in s:
        i = i + 1
        #print(i, '=', key)

    return(sum(s) / float(len(s)))

trees = []
for i in range(1000):
    tree = getMean()
    trees.append(tree)
    #print('New tree height =', tree, 'got added.')


sTrees = sorted(trees)

for i in sTrees:
    print(i)

#print('Trees created:', len(sTrees))
print('Mean:', sum(sTrees) / float(len(sTrees)))

#print('Mean =', getMean())

t = []
for i in sTrees:
    if i >= 2.5 and i <= 2.6:
        t.append(i)


print((len(t) / float(len(sTrees))) * 100, '% of the forest')







