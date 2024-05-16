import time
import timeit
import os



folder = "FOUND1_TXT"
group = "AncestorsOfHominida.muscle.sequester.fasta"

# main = "For FOUND1 - AP023485.1_Homo_sapiens_mitochondiral_DNA_complete_genome.csv"



files=os.listdir(folder)
prepath=os.getcwd()+"/" + folder + "/"



for f in files:
	print(f)


	path = prepath+f

	file = open(path,'r')


	head = file.readline().strip()

	reps = open(path.replace(folder, folder+"_remaped"),'w')

	reps.write("%s\n" % (head))


	#print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")



	while True:
	
		##### Повторы
		raw = file.readline().strip()

		if raw == "":
			break

		read = raw.split(";")
		print(read[0])

		##### Карты
		fol = "maps/"+group
		fils=os.listdir(fol)
		prep=os.getcwd()+"/" + fol + "/"
		for ph in fils:
			if ph in f:
				paz = prep+ph
				break
		# print(paz)


		##### First start 
		mapfile = open(paz,'r')
		while True:
			row = mapfile.readline().strip().split(";")
			if row == ['']:
				break
			#print(row[0] +" f "+ read[0])
			if row[0] == read[0]:
				read[0]=row[1]	

		#print("((((((((((((((())))))))))))))))))))))))))")

		##### Second start 
		mapfile = open(paz,'r')
		while True:
			row = mapfile.readline().strip().split(";")
			if row == ['']:
				break
			#print(row[0] +" s "+ read[0])
			if row[0] == read[1]:
				read[1]=row[1]	



		reps.write("%s\n" % (';'.join(read)))


