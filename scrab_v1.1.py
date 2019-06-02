scrab = dict(
a=1,
b=3,
c=3,
d=2,
e=1,
f=4,
g=2,
h=4,
i=1,
j=8,
k=5,
l=1,
m=3,
n=1,
o=1,
p=3,
q=10,
r=1,
s=1,
t=1,
u=1,
v=4,
w=4,
x=8,
y=4,
z=10,
)

# Takes all the player names from the text file and fills them into our algorithm
basketball_names = open('basketball.txt','r')
name = basketball_names.read().split(', ')
len_of_list =len(name)


x = 0
while x < len_of_list:
	for names in name:
		score = sum(scrab.get(value,0) for value in name[x].lower())
		print(f"{names} is worth {score} scrabble points!")
		x += 1
