import time
import timeit
import os

import sqlite3
import sys


# main = "1_AP023485.1_Homo_sapiens_mitochondiral_DNA_complete_genome.csv"
# folder = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/FOUND1_TXT_remaped"
# sqlfol = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/FOUND1_SQL_remaped"
# outfol = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/Checking1"

# main = "2_AP023485.1_Homo_sapiens_mitochondiral_DNA_complete_genome.csv"
# folder = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/FOUND2_TXT_remaped"
# sqlfol = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/FOUND2_SQL_remaped"
# outfol = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/Checking2"

main = "4_CM032116.2_Homo_sapiens_isolate_HG01243_mitochondrion_complete_sequence_whole_genome_shotgun_sequence.csv"
folder = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/FOUND3_TXT_remaped"
sqlfol = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/FOUND3_SQL_remaped"
outfol = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/Checking3"








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





files=os.listdir(folder)
#prepath=os.getcwd()+"/" + folder + "/"

for f in files:

	print(f)

	path = folder + "/" + main

	file = open(path,'r')

	head = file.readline().strip()

	reps_y = open(outfol+"/yes/"+f,'w')
	reps_n = open(outfol+"/no/"+f,'w')
	reps_m = open(outfol+"/may/"+f,'w')

	reps_y.write("%s;id;%s\n" % (head,head))
	reps_n.write("%s;id;%s\n" % (head,head))
	reps_m.write("%s;id;%s\n" % (head,head))



	sqlpath = sqlfol+"/"+ f.replace(".csv",".sqlite")
	#sqler(folder + "/" + f,sqlpath) #################################



	while True: 

		
		raw = file.readline().strip()

		if raw == "":
			break

		row = raw.split(";")



		con = sqlite3.connect(sqlpath)
		cur = con.cursor()


		cur.execute('SELECT * FROM repeats WHERE id_type=%s AND first_start>%s-5 AND first_start<%s+5 AND second_start>%s-5 AND second_start<%s+5' % (row[3],row[0],row[0],row[1],row[1]))
		good=cur.fetchall()
		

		if len(good) == 0:
			reps_n.write("%s\n" % (raw))

		elif good[0][5]!=row[4] or good[0][6]!=row[5]:
			reps_m.write("%s;%s\n" % (raw,';'.join(map(str, good[0])))) 

		else:
			reps_y.write("%s;%s\n" % (raw,';'.join(map(str, good[0]))))


		# aimfile = open(aim,'r')
		# while True:
		# 	xow = aimfile.readline().strip().split(";")
		# 	#print(xow)
		# 	if row == ['']:
		# 		reps.write("%s\n" % (head))
		# 		break

		# 	if xow[0] == row[0] and xow[1] == row[1]:
		# 		break

	#print(raw)
		#maper(genome,name)

		