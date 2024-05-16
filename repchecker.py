import time
import timeit
import os




folder = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/FOUND1_TXT_remaped"
aim = folder + "/2_AP023485.1_Homo_sapiens_mitochondiral_DNA_complete_genome.csv"
outfol = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/Checking/AncestorsOfHominida.muscle.sequester"


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


		aimfile = open(aim,'r')
		while True:
			xow = aimfile.readline().strip().split(";")
			#print(xow)
			if row == ['']:
				reps.write("%s\n" % (raw))
				break

			if xow[0] == row[0] and xow[1] == row[1]:
				break

	#print(raw)
		#maper(genome,name)

		