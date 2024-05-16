import time
import timeit
import os

import sqlite3
import sys




i = 1
#main = "2_AP023485.1_Homo_sapiens_mitochondiral_DNA_complete_genome.sqlite" # 1 and 2
main = "4_CM032116.2_Homo_sapiens_isolate_HG01243_mitochondrion_complete_sequence_whole_genome_shotgun_sequence.sqlite"



folder = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/Checking%s" % i
sqlfol = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/FOUND%s_SQL_remaped/" % i


for cat in ("yes","may","no", "no_real"):




	reps = open(folder+"/"+"%s_count.csv" % cat,'w')


	reps.write("f;c_all;f_all;perc_all;c_dir;f_dir;perc_dir;c_com;f_com;perc_com;c_mir;f_mir;perc_mir;c_inv;f_inv;perc_inv\n")




	files=os.listdir(folder+"/" + cat)


	for f in files:

		print(f)



		con = sqlite3.connect(sqlfol + main)
		cur = con.cursor()




		# D-loop
		# от 0 до 575
		# от 16023 до 16568
		

		cur.execute('SELECT * FROM repeats WHERE id_type=1 and (first_start >= 575 and first_start <= 16023) and (second_start >= 575 and second_start <= 16023)')
		good=cur.fetchall()
		f_dir = len(good)

		cur.execute('SELECT * FROM repeats WHERE id_type=2 and (first_start >= 575 and first_start <= 16023) and (second_start >= 575 and second_start <= 16023)')
		good=cur.fetchall()
		f_com = len(good)

		cur.execute('SELECT * FROM repeats WHERE id_type=3 and (first_start >= 575 and first_start <= 16023) and (second_start >= 575 and second_start <= 16023)')
		good=cur.fetchall()
		f_mir = len(good)

		cur.execute('SELECT * FROM repeats WHERE id_type=4 and (first_start >= 575 and first_start <= 16023) and (second_start >= 575 and second_start <= 16023)')
		good=cur.fetchall()
		f_inv = len(good)


		# For NO
		c_all = 0
		c_dir = 0
		c_com = 0
		c_mir = 0
		c_inv = 0



		path = folder+"/"+cat+"/"+f

		file = open(path,'r')

		head = file.readline().strip()



		while True:

			
			raw = file.readline().strip()
			#print(raw)

			if raw == "":
				break

			row = raw.split(";")


			if       (int(row[0]) >= 575 and int(row[0]) <= 16023) and (int(row[1]) >= 575 and int(row[1]) <= 16023):
				c_all += 1

				if row[3]=="1":	
					c_dir += 1

				if row[3]=="2":	
					c_com += 1

				if row[3]=="3":	
					c_mir += 1

				if row[3]=="4":	
					c_inv += 1		
			

		print("%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s" % (f,f_dir+f_com+f_mir+f_inv,c_all,f_dir,c_dir,f_com,c_com,f_mir,c_mir,f_inv,c_inv))

		if c_all != 0:

			reps.write("%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s\n" % (f,c_all,(f_dir+f_com+f_mir+f_inv),c_all/(f_dir+f_com+f_mir+f_inv)*100,c_dir,f_dir,c_dir/f_dir*100,c_com,f_com,c_com/f_com*100,c_mir,f_mir,c_mir/f_mir*100,c_inv,f_inv,c_inv/f_inv*100))









