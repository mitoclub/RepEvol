import time
import timeit
import os
import sqlite3
import sys













def sqler(inf,outf):


	file = open(inf,'r')


	con = sqlite3.connect(outf)
	cur = con.cursor()
	cur.execute('CREATE TABLE repeats (id INTEGER PRIMARY KEY, first_start INTEGER, second_start INTEGER, length INTEGER, id_type INTEGER, first_seq VARCHAR(50), second_seq VARCHAR(50), alt_second_seq VARCHAR(50), errs INTEGER)')
	con.commit()
	# cur.execute('CREATE TABLE reps (id INTEGER PRIMARY KEY, ori INTEGER, tar INTEGER, nuc VARCHAR(1))')
	# con.commit()


	head = file.readline()

	while True:
		r = file.readline().strip().split(";")

		if r == ['']:
			break

		q = "INSERT INTO repeats (first_start, second_start, length, id_type, first_seq, second_seq, alt_second_seq, errs) VALUES(%s,%s,%s,%s,\"%s\",\"%s\",\"%s\",%s)" % (r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7])
		cur.execute(q)
		# q = "INSERT INTO species (id, ori, tar, nuc) VALUES(NULL, %s, %s, \"%s\")" % (j,i,a[i])
		# cur.execute(q)

	con.commit()



def maper(num,n,g):

	#print(a)
	g = list(g)

	xstr = list('X' * len(g))
	m = "maps/"+aim+"/"+n+".sqlite"
	con = sqlite3.connect(m)
	cur = con.cursor()
	


	f = open(fo+"/"+num+"_"+n+".csv",'r')

	head = f.readline().strip()

	while True:

		raw = f.readline().strip()
		if raw == "":
			break

		row = raw.split(";")


		cur.execute('SELECT * FROM species WHERE tar=%s' % (row[0]))
		good=cur.fetchall()

		cur.execute('SELECT * FROM species WHERE tar=%s' % (row[1]))
		good2=cur.fetchall()


		#print(row[0] , row[1])
		if len(good) != 0 and len(good2) != 0:   
			start = int(good[0][1])
			end = start+int(row[2])


			if start > 575 and end < 16023:

				cur.execute('SELECT * FROM species WHERE ori=%s' % (start))
				good=cur.fetchall()

				start = int(good[0][2])

				cur.execute('SELECT * FROM species WHERE ori=%s' % (end))
				good=cur.fetchall()

				end = int(good[0][2])



				#print(row[4]+" "+''.join(g[start:end]))



				for i in range(start,end):
					xstr[i] = g[i]







				start = int(good2[0][1])
				end = start+int(row[2])


				if start > 575 and end < 16023:

					cur.execute('SELECT * FROM species WHERE ori=%s' % (start))
					good=cur.fetchall()

					start = int(good[0][2])

					cur.execute('SELECT * FROM species WHERE ori=%s' % (end))
					good=cur.fetchall()

					end = int(good[0][2])



					#print(row[5]+" "+''.join(g[start:end]))



					for i in range(start,end):
						xstr[i] = g[i]





	for i in range(len(g)):
		if g[i] == '-':
			xstr[i] = '-'


	return ''.join(xstr)


	# j = 0


	# l = len(a)
	# print(l)


	# for i in range(l):

	# 	if a[i]!="-":
	# 		reps3.write("%s;%s;%s\n" % (j,i,a[i]))
	# 		j+=1


	# while True:
	# 	if i >= lh or j >= la:
	# 		break
	
	# 	if a[j]!="-":
	# 		reps3.write("%s;%s;%s;%s\n" % (i,j,h[i],a[j]))
	# 		i+=1

	# 	if h[i]!="X":
	# 		j+=1




outfol = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/SPLITS"

first = 9114 
second = 14105











def comparer(main,sqlfol,fafile,f):
	print(main)

	con = sqlite3.connect(sqlfol + "/" + main)
	cur = con.cursor()
	cur.execute('SELECT * FROM repeats')
	ori=cur.fetchall()


	# Поиск соответствующих предковых повторов
	print(f)

	scon = sqlite3.connect(sqlfol + "/" + f)
	scur = scon.cursor()


	# Разметка на выравнивании
	file = open(fafile,'r')

	while True:
		row = file.readline().strip()
		if row[1:] in main:
			des = file.readline().strip()
			break

	file = open(fafile,'r')

	while True:
		row = file.readline().strip()
		if row[1:] in f:
			anc = file.readline().strip()
			break




	xstr = ["0" for x in range(len(des))]
	ystr = ["0" for x in range(len(des))]

	for i in range(len(des)):
		if des[i] != anc[i] and des[i]!="N" and anc[i]!="N":
			xstr[i] = "1"


	for o in ori:
		if ((o[1] >= first - 115) and (o[1] <= first + 128)) and ((o[2] >= second - 115) and (o[2] <= second + 128)):
			print(o)
			scur.execute('SELECT * FROM repeats WHERE id_type=%s AND (first_start>%s-5 AND first_start<%s+5) OR (second_start>%s-5 AND second_start<%s+5)' % (o[4],o[1],o[1],o[2],o[2]))
			sec=scur.fetchall()
			for s in sec:
				for a in range(int(s[1]),int(s[1])+int(s[3])):
					if ystr[a]=="0" or ystr[a]=="1":
						ystr[a]="1"
					else:
						ystr[a]="3"

				for a in range(int(s[2]),int(s[2])+int(s[3])):
					if ystr[a]=="0" or ystr[a]=="1":
						ystr[a]="1"
					else:
						ystr[a]="3"

			if len(sec)==0:
				for a in range(int(o[1]),int(o[1])+int(o[3])):
					if ystr[a]=="0":
						ystr[a]="2"
					else:
						ystr[a]="4"

				for a in range(int(o[2]),int(o[2])+int(o[3])):	
					if ystr[a]=="0":
						ystr[a]="2"
					else:
						ystr[a]="4"


	prof = open(outfol+"/"+f.replace(".sqlite",".line"),'w')


	print(des[first - 100:first + 113])  
	prof.write("%s\n" % des)
	print(anc[first - 100:first + 113])
	prof.write("%s\n" % anc)
	print(''.join(xstr[first - 100:first + 113]))
	prof.write("%s\n" % ''.join(xstr))
	print(''.join(ystr[first - 100:first + 113]))
	prof.write("%s\n" % ''.join(ystr))

	print(des[second - 100:second + 113])  
	prof.write("%s\n" % des)
	print(anc[second - 100:second + 113])
	prof.write("%s\n" % anc)
	print(''.join(xstr[second - 100:second + 113]))
	prof.write("%s\n" % ''.join(xstr))
	print(''.join(ystr[second - 100:second + 113]))
	prof.write("%s\n" % ''.join(ystr))


def varcomparer(main,sqlfol,fafile,name):



	
	









	
	print(main)

	con = sqlite3.connect(sqlfol + "/" + main)
	cur = con.cursor()
	cur.execute('SELECT * FROM repeats')
	ori=cur.fetchall()


	# Поиск соответствующих предковых повторов
	print(f)

	scon = sqlite3.connect(sqlfol + "/" + f)
	scur = scon.cursor()


	# Разметка на выравнивании
	file = open(fafile,'r')

	while True:
		row = file.readline().strip()
		if row[1:] in main:
			des = file.readline().strip()
			break

	file = open(fafile,'r')

	while True:
		row = file.readline().strip()
		if row[1:] in f:
			anc = file.readline().strip()
			break




	xstr = ["0" for x in range(len(des))]
	ystr = ["0" for x in range(len(des))]

	for i in range(len(des)):
		if des[i] != anc[i] and des[i]!="N" and anc[i]!="N":
			xstr[i] = "1"


	for o in ori:
		if ((o[1] >= first - 115) and (o[1] <= first + 128)) and ((o[2] >= second - 115) and (o[2] <= second + 128)):
			print(o)
			scur.execute('SELECT * FROM repeats WHERE id_type=%s AND (first_start>%s-5 AND first_start<%s+5) OR (second_start>%s-5 AND second_start<%s+5)' % (o[4],o[1],o[1],o[2],o[2]))
			sec=scur.fetchall()
			for s in sec:
				for a in range(int(s[1]),int(s[1])+int(s[3])):
					if ystr[a]=="0" or ystr[a]=="1":
						ystr[a]="1"
					else:
						ystr[a]="3"

				for a in range(int(s[2]),int(s[2])+int(s[3])):
					if ystr[a]=="0" or ystr[a]=="1":
						ystr[a]="1"
					else:
						ystr[a]="3"

			if len(sec)==0:
				for a in range(int(o[1]),int(o[1])+int(o[3])):
					if ystr[a]=="0":
						ystr[a]="2"
					else:
						ystr[a]="4"

				for a in range(int(o[2]),int(o[2])+int(o[3])):	
					if ystr[a]=="0":
						ystr[a]="2"
					else:
						ystr[a]="4"


	prof = open(outfol+"/"+f.replace(".sqlite",".line"),'w')


	print(des[first - 100:first + 113])  
	prof.write("%s\n" % des)
	print(anc[first - 100:first + 113])
	prof.write("%s\n" % anc)
	print(''.join(xstr[first - 100:first + 113]))
	prof.write("%s\n" % ''.join(xstr))
	print(''.join(ystr[first - 100:first + 113]))
	prof.write("%s\n" % ''.join(ystr))

	print(des[second - 100:second + 113])  
	prof.write("%s\n" % des)
	print(anc[second - 100:second + 113])
	prof.write("%s\n" % anc)
	print(''.join(xstr[second - 100:second + 113]))
	prof.write("%s\n" % ''.join(xstr))
	print(''.join(ystr[second - 100:second + 113]))
	prof.write("%s\n" % ''.join(ystr))




################# STAGE I ######################
comparer("2_AP023485.1_Homo_sapiens_mitochondiral_DNA_complete_genome.sqlite", \
		"C:/Users/Abathur/Desktop/_SCIENCE/Conserva/FOUND1_SQL_remaped", \
		"C:/Users/Abathur/Desktop/_SCIENCE/Conserva/fa/AncestorsOfHominida.muscle.sequester.fasta", \
		"4_NC_013993.1_Homo_sp._Altai_mitochondrion_complete_genome.sqlite") # AncestorsOfHominida



################# STAGE II ######################

comparer("4_NC_013993.1_Homo_sp._Altai_mitochondrion_complete_genome.sqlite", \
		"C:/Users/Abathur/Desktop/_SCIENCE/Conserva/FOUND1_SQL_remaped", \
		"C:/Users/Abathur/Desktop/_SCIENCE/Conserva/fa/AncestorsOfHominida.muscle.sequester.fasta", \
		"1_NC_023100.1_Homo_heidelbergensis_mitochondrion_complete_genome.sqlite") # AncestorsOfHominida



################# STAGE III ######################

comparer("1_NC_023100.1_Homo_heidelbergensis_mitochondrion_complete_genome.sqlite", \
		"C:/Users/Abathur/Desktop/_SCIENCE/Conserva/FOUND1_SQL_remaped", \
		"C:/Users/Abathur/Desktop/_SCIENCE/Conserva/fa/AncestorsOfHominida.muscle.sequester.fasta", \
		"3_NC_011137.1_Homo_sapiens_neanderthalensis_mitochondrion_complete_genome.sqlite") # AncestorsOfHominida




################# STAGE IV ######################
# Messinian

comparer("3_NC_011137.1_Homo_sapiens_neanderthalensis_mitochondrion_complete_genome.sqlite", \
		"C:/Users/Abathur/Desktop/_SCIENCE/Conserva/FOUND1_SQL_remaped", \
		"C:/Users/Abathur/Desktop/_SCIENCE/Conserva/fa/AncestorsOfHominida.muscle.sequester.fasta", \
		"Messinian") 



################# STAGE V ######################
# Tortonian




################# STAGE VI ######################
# Langhian





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