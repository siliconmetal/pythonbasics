#well python is a high level interpreted langauge created by Guido van Rossum and first released in 1991



#Basic for loop
rates = [100, 200, 700, 915]
a = 0
for rate in rates:
   a = a + rate
print(f'Total: {a}')

#Nasted for loop(loop inside a loop) using range function
print('following are the coordinates for x and y:')
for x in range(3):
   for y in range(3):
       print(f'\t({x}, {y})')

#Replacing a value in a matrix and then print elements individually using for-loop
matrix = [
   [1,2,3],
   [4,5,6],
   [7,8,9]
]
print(f'in matrix form: \n{matrix}')
matrix[0][2] = 4
print('\nindividually:')
for row in matrix:
    for item in row:
       print(item)

#Operations on List
#Functions including: append, insert, remove, sort, reverse,

def set():
    numbers = [42, 5, 96, 47, 28]
def run():
    print(f'\t >>{numbers}')
numbers = [42,5,96,47,28]

numbers.append(20)
run()

numbers.insert(0,3)
run()


numbers.remove(47)
run()

numbers.sort()
run()

numbers.reverse()
run()


numbers_new = numbers.copy()
print(f'\t >>{numbers_new} ')


#Unpacking_in_python

points=(1,2,3,4,5)
a, b, c, d, e = points
print(f'the value of a: {a}')
print(f'the value of d: {d}')


#Dictionary_in_python

student1={
    'name':'john',
    'marks':'45',
    'promoted to next class':True
}
student2={
    'name':'kelly',
    'marks':'30',
    'promoted to next class':False
}

print(student1['name'])
print(student2['promoted to next class'])


#Tuples

my_tuple=("john", 23, 45, "kennedy", "root")
print(my_tuple[0])

my_tuple=my_tuple+("LAGalaxy","kuzma",12)
print(my_tuple[5])


#Split

"john kennedy".split()
"a,b,c,d".split(",")






