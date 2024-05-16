import time
import timeit
import os

import sqlite3
import sys


main = "1_AP023485.1_Homo_sapiens_mitochondiral_DNA_complete_genome.csv"
folder = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/FOUND1_TXT_remaped"
outfol = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/Checking"

# main = "2_AP023485.1_Homo_sapiens_mitochondiral_DNA_complete_genome.csv"
# folder = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/FOUND2_TXT_remaped"
# outfol = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/Checking2"

# main = "4_CM032116.2_Homo_sapiens_isolate_HG01243_mitochondrion_complete_sequence_whole_genome_shotgun_sequence.csv"
# folder = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/FOUND3_TXT_remaped"
# outfol = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/Checking3"




aim = folder + "/" + main
sqlfol = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/SQL_remaped_mains"
sqlpath = sqlfol+"/"+ main.replace(".csv",".sqlite")



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



sqler(aim,sqlpath)


files=os.listdir(folder)
#prepath=os.getcwd()+"/" + folder + "/"

for f in files:

	print(f)

	path = folder+"/"+f

	file = open(path,'r')

	head = file.readline().strip()

	reps = open(outfol+"/"+f,'w')

	reps.write("%s\n" % (head))



	while True:

		
		raw = file.readline().strip()

		if raw == "":
			break

		row = raw.split(";")



		con = sqlite3.connect(sqlpath)
		cur = con.cursor()


		cur.execute('SELECT * FROM repeats WHERE id_type=%s AND first_start=%s AND second_start=%s' % (row[3],row[0],row[1]))
		good=cur.fetchall()
		

		if len(good) == 0:
			reps.write("%s\n" % (raw))


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

		