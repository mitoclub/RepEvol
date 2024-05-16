import time
import timeit
import os
import sqlite3
import sys









# outfol = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/SPLITS"

# first = 9114 
# second = 14105











# def comparer(main,sqlfol,fafile,f):
# 	print(main)

# 	con = sqlite3.connect(sqlfol + "/" + main)
# 	cur = con.cursor()
# 	cur.execute('SELECT * FROM repeats')
# 	ori=cur.fetchall()


# 	# Поиск соответствующих предковых повторов
# 	print(f)

# 	scon = sqlite3.connect(sqlfol + "/" + f)
# 	scur = scon.cursor()


# 	# Разметка на выравнивании
# 	file = open(fafile,'r')

# 	while True:
# 		row = file.readline().strip()
# 		if row[1:] in main:
# 			des = file.readline().strip()
# 			break

# 	file = open(fafile,'r')

# 	while True:
# 		row = file.readline().strip()
# 		if row[1:] in f:
# 			anc = file.readline().strip()
# 			break




# 	xstr = ["0" for x in range(len(des))]
# 	ystr = ["0" for x in range(len(des))]

# 	for i in range(len(des)):
# 		if des[i] != anc[i] and des[i]!="N" and anc[i]!="N":
# 			xstr[i] = "1"


# 	for o in ori:
# 		if ((o[1] >= first - 115) and (o[1] <= first + 128)) and ((o[2] >= second - 115) and (o[2] <= second + 128)):
# 			print(o)
# 			scur.execute('SELECT * FROM repeats WHERE id_type=%s AND (first_start>%s-5 AND first_start<%s+5) OR (second_start>%s-5 AND second_start<%s+5)' % (o[4],o[1],o[1],o[2],o[2]))
# 			sec=scur.fetchall()
# 			for s in sec:
# 				for a in range(int(s[1]),int(s[1])+int(s[3])):
# 					if ystr[a]=="0" or ystr[a]=="1":
# 						ystr[a]="1"
# 					else:
# 						ystr[a]="3"

# 				for a in range(int(s[2]),int(s[2])+int(s[3])):
# 					if ystr[a]=="0" or ystr[a]=="1":
# 						ystr[a]="1"
# 					else:
# 						ystr[a]="3"

# 			if len(sec)==0:
# 				for a in range(int(o[1]),int(o[1])+int(o[3])):
# 					if ystr[a]=="0":
# 						ystr[a]="2"
# 					else:
# 						ystr[a]="4"

# 				for a in range(int(o[2]),int(o[2])+int(o[3])):	
# 					if ystr[a]=="0":
# 						ystr[a]="2"
# 					else:
# 						ystr[a]="4"


# 	prof = open(outfol+"/"+f.replace(".sqlite",".line"),'w')


# 	print(des[first - 100:first + 113])  
# 	prof.write("%s\n" % des)
# 	print(anc[first - 100:first + 113])
# 	prof.write("%s\n" % anc)
# 	print(''.join(xstr[first - 100:first + 113]))
# 	prof.write("%s\n" % ''.join(xstr))
# 	print(''.join(ystr[first - 100:first + 113]))
# 	prof.write("%s\n" % ''.join(ystr))

# 	print(des[second - 100:second + 113])  
# 	prof.write("%s\n" % des)
# 	print(anc[second - 100:second + 113])
# 	prof.write("%s\n" % anc)
# 	print(''.join(xstr[second - 100:second + 113]))
# 	prof.write("%s\n" % ''.join(xstr))
# 	print(''.join(ystr[second - 100:second + 113]))
# 	prof.write("%s\n" % ''.join(ystr))


# def varcomparer(main,sqlfol,fafile,name):


	
# 	print(main)

# 	con = sqlite3.connect(sqlfol + "/" + main)
# 	cur = con.cursor()
# 	cur.execute('SELECT * FROM repeats')
# 	ori=cur.fetchall()


# 	# Поиск соответствующих предковых повторов
# 	print(f)

# 	scon = sqlite3.connect(sqlfol + "/" + f)
# 	scur = scon.cursor()


# 	# Разметка на выравнивании
# 	file = open(fafile,'r')

# 	while True:
# 		row = file.readline().strip()
# 		if row[1:] in main:
# 			des = file.readline().strip()
# 			break

# 	file = open(fafile,'r')

# 	while True:
# 		row = file.readline().strip()
# 		if row[1:] in f:
# 			anc = file.readline().strip()
# 			break




# 	xstr = ["0" for x in range(len(des))]
# 	ystr = ["0" for x in range(len(des))]

# 	for i in range(len(des)):
# 		if des[i] != anc[i] and des[i]!="N" and anc[i]!="N":
# 			xstr[i] = "1"


# 	for o in ori:
# 		if ((o[1] >= first - 115) and (o[1] <= first + 128)) and ((o[2] >= second - 115) and (o[2] <= second + 128)):
# 			print(o)
# 			scur.execute('SELECT * FROM repeats WHERE id_type=%s AND (first_start>%s-5 AND first_start<%s+5) OR (second_start>%s-5 AND second_start<%s+5)' % (o[4],o[1],o[1],o[2],o[2]))
# 			sec=scur.fetchall()
# 			for s in sec:
# 				for a in range(int(s[1]),int(s[1])+int(s[3])):
# 					if ystr[a]=="0" or ystr[a]=="1":
# 						ystr[a]="1"
# 					else:
# 						ystr[a]="3"

# 				for a in range(int(s[2]),int(s[2])+int(s[3])):
# 					if ystr[a]=="0" or ystr[a]=="1":
# 						ystr[a]="1"
# 					else:
# 						ystr[a]="3"

# 			if len(sec)==0:
# 				for a in range(int(o[1]),int(o[1])+int(o[3])):
# 					if ystr[a]=="0":
# 						ystr[a]="2"
# 					else:
# 						ystr[a]="4"

# 				for a in range(int(o[2]),int(o[2])+int(o[3])):	
# 					if ystr[a]=="0":
# 						ystr[a]="2"
# 					else:
# 						ystr[a]="4"


# 	prof = open(outfol+"/"+f.replace(".sqlite",".line"),'w')


# 	print(des[first - 100:first + 113])  
# 	prof.write("%s\n" % des)
# 	print(anc[first - 100:first + 113])
# 	prof.write("%s\n" % anc)
# 	print(''.join(xstr[first - 100:first + 113]))
# 	prof.write("%s\n" % ''.join(xstr))
# 	print(''.join(ystr[first - 100:first + 113]))
# 	prof.write("%s\n" % ''.join(ystr))

# 	print(des[second - 100:second + 113])  
# 	prof.write("%s\n" % des)
# 	print(anc[second - 100:second + 113])
# 	prof.write("%s\n" % anc)
# 	print(''.join(xstr[second - 100:second + 113]))
# 	prof.write("%s\n" % ''.join(xstr))
# 	print(''.join(ystr[second - 100:second + 113]))
# 	prof.write("%s\n" % ''.join(ystr))




# def  alicomp(main,sqlfol,fafile,f):





first = 9114 
second = 14105




# ################# STAGE I ######################
# comparer("2_AP023485.1_Homo_sapiens_mitochondiral_DNA_complete_genome.sqlite", \
# 		"C:/Users/Abathur/Desktop/_SCIENCE/Conserva/FOUND1_SQL_remaped", \
# 		"C:/Users/Abathur/Desktop/_SCIENCE/Conserva/fa/AncestorsOfHominida.muscle.sequester.fasta", \
# 		"4_NC_013993.1_Homo_sp._Altai_mitochondrion_complete_genome.sqlite") # AncestorsOfHominida




speces = []
genomes = []

speces.append("Homo_sp._Altai")

for sp in speces:
	file = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/xcards_simple_names/AncestorsOfHominida.muscle.sequester.fasta"

	file = open(file,'r')

	while True:
		row = file.readline().strip()
		if sp in row:
			gen = file.readline().strip()
			genomes.append(gen)
			break

gl = len(genomes[0])
c = 0

# 575        1050    
# 16023      16717



for i in range(1050,16718):
	check=True
	for g in genomes:
		if g[i]!='X':
			check=False
			break
	if check:
		c+=1

print(c)
print(c / (16718-1050))





c=0
for i in range(first - 100,first + 113):
	check=True
	for g in genomes:
		if g[i]!='X':
			check=False
			break
	if check:
		c+=1

print(c)
print(c / 213)


 
c=0
for i in range(second - 100,second + 113):
	check=True
	for g in genomes:
		if g[i]!='X':
			check=False
			break
	if check:
		c+=1

print(c)
print(c / 213)


print("")






# ################# STAGE II ######################

genomes = []

speces.append("Homo_heidelbergensis")



for sp in speces:
	file = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/xcards_simple_names/AncestorsOfHominida.muscle.sequester.fasta"

	file = open(file,'r')

	while True:
		row = file.readline().strip()
		if sp in row:
			gen = file.readline().strip()
			genomes.append(gen)
			break

gl = len(genomes[0])
c = 0

# 575        1050    
# 16023      16717


for i in range(1050,16718):
	check=True
	for g in genomes:
		if g[i]!='X':
			check=False
			break
	if check:
		c+=1

print(c)
print(c / (16718-1050))


c=0
for i in range(first - 100,first + 113):
	check=True
	for g in genomes:
		if g[i]!='X':
			check=False
			break
	if check:
		c+=1

print(c)
print(c / 213)


 
c=0
for i in range(second - 100,second + 113):
	check=True
	for g in genomes:
		if g[i]!='X':
			check=False
			break
	if check:
		c+=1

print(c)
print(c / 213)


print("")





# ################# STAGE III ######################
file = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/xcards_simple_names/AncestorsOfHominida.muscle.sequester.fasta"

genomes = []

speces.append("Homo_sapiens_neanderthalensis")



for sp in speces:
	file = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/xcards_simple_names/AncestorsOfHominida.muscle.sequester.fasta"

	file = open(file,'r')

	while True:
		row = file.readline().strip()
		if sp in row:
			gen = file.readline().strip()
			genomes.append(gen)
			break

gl = len(genomes[0])
c = 0

# 575        1050    
# 16023      16717


for i in range(1050,16718):
	check=True
	for g in genomes:
		if g[i]!='X':
			check=False
			break
	if check:
		c+=1

print(c)
print(c / (16718-1050))


c=0
for i in range(first - 100,first + 113):
	check=True
	for g in genomes:
		if g[i]!='X':
			check=False
			break
	if check:
		c+=1

print(c)
print(c / 213)


 
c=0
for i in range(second - 100,second + 113):
	check=True
	for g in genomes:
		if g[i]!='X':
			check=False
			break
	if check:
		c+=1

print(c)
print(c / 213)


print("")


# ################# STAGE IV ######################
# # Messinian

SupraHominida.muscle.sequester

Pan_paniscus
Pan_troglodytes





# comparer("3_NC_011137.1_Homo_sapiens_neanderthalensis_mitochondrion_complete_genome.sqlite", \
# 		"C:/Users/Abathur/Desktop/_SCIENCE/Conserva/FOUND1_SQL_remaped", \
# 		"C:/Users/Abathur/Desktop/_SCIENCE/Conserva/fa/AncestorsOfHominida.muscle.sequester.fasta", \
# 		"Messinian") 



################# STAGE V ######################
# Tortonian
Gorilla_beringei
Gorilla_gorilla


################# STAGE VI ######################
# Langhian
Pongo_abelii
Pongo_pygmaeus


################# STAGE VII ######################
# Burdigalian



################# STAGE VIII ######################
# Chattian










# Сократить выравнивания (3 строки вместе с нулями) до генома
# если не '-' то вставить 


















# 	# reps_y = open(outfol+"/yes/"+f,'w')
# 	# reps_n = open(outfol+"/no/"+f,'w')
# 	# reps_m = open(outfol+"/may/"+f,'w')




# 	sqlpath = sqlfol+"/"+ f.replace(".csv",".sqlite")
# 	#sqler(folder + "/" + f,sqlpath) #################################



# 	while True: 

		
# 		raw = file.readline().strip()

# 		if raw == "":
# 			break

# 		row = raw.split(";")



# 		con = sqlite3.connect(sqlpath)
# 		cur = con.cursor()


# 		cur.execute('SELECT * FROM repeats WHERE id_type=%s AND first_start>%s-5 AND first_start<%s+5 AND second_start>%s-5 AND second_start<%s+5' % (row[3],row[0],row[0],row[1],row[1]))
# 		good=cur.fetchall()
		

# 		if len(good) == 0:
# 			reps_n.write("%s\n" % (raw))

# 		elif good[0][5]!=row[4] or good[0][6]!=row[5]:
# 			reps_m.write("%s;%s\n" % (raw,';'.join(map(str, good[0])))) 

# 		else:
# 			reps_y.write("%s;%s\n" % (raw,';'.join(map(str, good[0]))))


# 		# aimfile = open(aim,'r')
# 		# while True:
# 		# 	xow = aimfile.readline().strip().split(";")
# 		# 	#print(xow)
# 		# 	if row == ['']:
# 		# 		reps.write("%s\n" % (head))
# 		# 		break

# 		# 	if xow[0] == row[0] and xow[1] == row[1]:
# 		# 		break

# 	#print(raw)
# 		#maper(genome,name)

		









# aim = "AncestorsOfHominida.muscle.sequester.fasta"
# fo = "Checking1/no_real"

# aim = "Mitochondria_GreatApes.muscle.sequester PLUS HOMO SAPIENS.fasta"
# fo = "Checking2/no_real"

# aim = "SupraHominida.muscle.sequester.fasta"
# fo = "Checking3/no_real"



# path = 'xcards/' + aim 
# reps = open(path, "w")










# # Соединение выравнивания в геномы


# # XXX такой же длины

# # Брать реальные координаты повторов из карты

# # От начал до концов все что в повторах превращать из X в нуклеотиды





# filepath = 'Homi/' + aim
# file = open(filepath,'r')




# name = file.readline().strip()
# print(name)

# genome = ""
# num=1
# while True:

# 	read = file.readline().strip()
# 	if read == "":
# 		reps.write("%s\n" % name)
# 		reps.write("%s\n" % maper(str(num),name[1:],genome))


# 		break
# 	elif ">" in read: 
# 		reps.write("%s\n" % name)
# 		reps.write("%s\n" % maper(str(num),name[1:],genome))


# 		name = read
# 		print(name)
# 		genome = ""
# 		num+=1
# 	else: 
# 		genome += read
# 	