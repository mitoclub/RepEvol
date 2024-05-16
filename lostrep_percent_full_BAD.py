import time
import timeit
import os

import sqlite3
import sys



for i in ("1","2","3"):

	for cat in ("yes","may","no", "no_real"):

		folder = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/Checking%s" % i
		sqlfol = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/FOUND%s_SQL_remaped/" % i






		reps = open(folder+"/"+"%s_count.csv" % cat,'w')


		reps.write("f;c_all;f_all;perc_all;c_dir;f_dir;perc_dir;c_com;f_com;perc_com;c_mir;f_mir;perc_mir;c_inv;f_inv;perc_inv\n")




		files=os.listdir(folder+"/" + cat)


		for f in files:

			print(f)



			con = sqlite3.connect(sqlfol + f.replace(".csv",".sqlite"))
			cur = con.cursor()


			cur.execute('SELECT * FROM repeats WHERE id_type=1')
			good=cur.fetchall()
			f_dir = len(good)

			cur.execute('SELECT * FROM repeats WHERE id_type=2')
			good=cur.fetchall()
			f_com = len(good)

			cur.execute('SELECT * FROM repeats WHERE id_type=3')
			good=cur.fetchall()
			f_mir = len(good)

			cur.execute('SELECT * FROM repeats WHERE id_type=4')
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









