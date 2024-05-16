import time
import timeit
import os


aim = "Mitochondria_GreatApes.muscle.sequester PLUS HOMO SAPIENS.fasta"


def maper(a,n):

	#print(a)

	path3 = 'maps/' + aim + '/' + n + '.csv'
	reps3 = open(path3, "w")


	j = 0


	l = len(a)
	print(l)


	for i in range(l):

		if a[i]!="-":
			reps3.write("%s;%s;%s\n" % (j,i,a[i]))
			j+=1


	# while True:
	# 	if i >= lh or j >= la:
	# 		break
	
	# 	if a[j]!="-":
	# 		reps3.write("%s;%s;%s;%s\n" % (i,j,h[i],a[j]))
	# 		i+=1

	# 	if h[i]!="X":
	# 		j+=1




filepath = 'Homi/' + aim
file = open(filepath,'r')

name = file.readline().strip().replace(">","")
print(name)

genome = ""
while True:
	
	read = file.readline().strip()

	if read == "":

		maper(genome,name)
		break
	elif ">" in read: 

		maper(genome,name)
		name = read.replace(">","")
		print(name)
		genome = ""
	else: 
		genome += read.replace("","")
	