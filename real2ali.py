import time
import timeit
import os
import sqlite3
import sys


aim = "AncestorsOfHominida.muscle.sequester.fasta"
fo = "Checking1/no_real"

aim = "Mitochondria_GreatApes.muscle.sequester PLUS HOMO SAPIENS.fasta"
fo = "Checking2/no_real"

aim = "SupraHominida.muscle.sequester.fasta"
fo = "Checking3/no_real"



path = 'xcards/' + aim 
reps = open(path, "w")


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







# Соединение выравнивания в геномы


# XXX такой же длины

# Брать реальные координаты повторов из карты

# От начал до концов все что в повторах превращать из X в нуклеотиды





filepath = 'Homi/' + aim
file = open(filepath,'r')




name = file.readline().strip()
print(name)

genome = ""
num=1
while True:

	read = file.readline().strip()
	if read == "":
		reps.write("%s\n" % name)
		reps.write("%s\n" % maper(str(num),name[1:],genome))


		break
	elif ">" in read: 
		reps.write("%s\n" % name)
		reps.write("%s\n" % maper(str(num),name[1:],genome))


		name = read
		print(name)
		genome = ""
		num+=1
	else: 
		genome += read
	