

directions = {
	"up" : [-1, 0],
	"left": [0, -1],
	"right": [0, 1],
	"down": [1, 0]
};
# Direction que peut avoir la tete du robot
dir_order = [
	"up",
	"right",
	"down",
	"left"
]

# Lecture des dimensions de l'univers du Robot 
f = open("universe.txt", "r")
fl = f.readlines()

fl[0] = fl[0].strip()
Inst_N = fl[0].split(": ")
width = int(Inst_N[1])

fl[1] = fl[1].strip()
Inst_N = fl[1].split(": ")
height = int(Inst_N[1])

f.close()

# Initialisation de la direction de la tete du robot 0 : Up
B_VZXR_dir = 0
# Initialisation de la position du robot (99,0)
B_VZXR_position = [height-1, 0]

# Changer la direction de la tete du robot 
def change_direction(direction):
	global B_VZXR_dir
	if(direction == "right"):
		B_VZXR_dir = (B_VZXR_dir + 1) % len(dir_order)
	else: # direction == left
		B_VZXR_dir = (B_VZXR_dir - 1) % len(dir_order)

# Changer la position du robot 
def change_cell(cell):
	global dir_order, directions,B_VZXR_dir, B_VZXR_position, width, height
	dir = dir_order[B_VZXR_dir];
	dir_coord = directions[dir];
	for i in range(0, cell):
		if(B_VZXR_position[0] + dir_coord[0] < height and B_VZXR_position[0] + dir_coord[0] >= 0):
			B_VZXR_position[0] += dir_coord[0]

		if(B_VZXR_position[1] + dir_coord[1] < width and B_VZXR_position[1] + dir_coord[1] >= 0):
			B_VZXR_position[1] += dir_coord[1]

# deplacement du robot (changement de position du robot et direction de sa tete )
def move(direction, cell,Univers_Robot):
	global B_VZXR_dir, B_VZXR_position,width,height
	Univers_Robot[B_VZXR_position[0]][B_VZXR_position[1]] = 0
	change_direction(direction)
	change_cell(cell)
	Univers_Robot[B_VZXR_position[0]][B_VZXR_position[1]] = 1

# affichage de l'univers du robot ( 1 : position du robot )
def print_Univers_Robot(Univers_Robot):
	global width,height
	for i in range(0, height):
		for j in range(0, width):
			print(Univers_Robot[i][j] , end='') # affichage de Univer Robot 
		print()  #saut de ligne 

def main(): 

	Univers_Robot = [[0 for x in range(width)] for y in range(height)] 

	print("position initiale du Robot B_VZXR est : ( ", B_VZXR_position[0] ,",", B_VZXR_position[1],")","tete vers le haut")

	# lecture du fichier d'instructions
	f = open("instruction_list.txt", "r")
	fl = f.readlines()
	i = 0
	for element in fl :
		fl[i] = element.strip()
		Inst_N = fl[i].split(", ")
		move(Inst_N[0],int(Inst_N[1]),Univers_Robot)
		i=i+1
	f.close()
	print_Univers_Robot(Univers_Robot)
	print()
	print("position finale du Robot B_VZXR est : (", B_VZXR_position[0] ,",", B_VZXR_position[1],")")
	if B_VZXR_dir == 0 :
		print("direction de la tete du robot : vers le haut ")
	if B_VZXR_dir == 1 :
		print("direction de la tete du robot : vers la droite")
	if B_VZXR_dir == 2 :
		print("direction de la tete du robot : vers la gauche")
	if B_VZXR_dir == 3 :
		print("direction de la tete du robot : vers le bas")

if __name__ == '__main__':
	main()

