import time
import timeit
import os




file = open("MitoBreakDB_121219.csv",'r')

# out = open("MitoBreakDB_121219_group1.csv",'w')
# paz = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/maps/For FOUND1 - AP023485.1_Homo_sapiens_mitochondiral_DNA_complete_genome.csv"

# out = open("MitoBreakDB_121219_group2.csv",'w')
# paz = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/maps/For FOUND2 - Homo_sapiens.csv"

out = open("MitoBreakDB_121219_group3.csv",'w')
paz = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/maps/For FOUND3 - CM032116.2_Homo_sapiens_isolate_HG01243_mitochondrion_complete_sequence_whole_genome_shotgun_sequence.csv"



head = file.readline().strip()

out.write("%s\n" % (head))


#print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")



while True:

	##### Повторы
	raw = file.readline().strip()

	if raw == "Deletions;5' breakpoint;3' breakpoint;Deletion length - bp;Deletion of replication origins;Location of the deleted region;Single mtDNA deletions;Multiple mtDNA deletions;Healthy tissues;Parkinson Disease;Inclusion Body Myositis;Tumour;Other clinical features;References":
		break

	read = raw.split(";")
	print(read[0])


	##### First start 
	mapfile = open(paz,'r')
	while True:
		row = mapfile.readline().strip().split(";")
		if row == ['']:
			break
		#print(row[0] +" f "+ read[0])
		if int(row[0]) == int(read[1])-1:
			print(read[1],row[0],row[1])
			read[1]=row[1]	
			break

	#print("((((((((((((((())))))))))))))))))))))))))")

	##### Second start 
	mapfile = open(paz,'r')
	while True:
		row = mapfile.readline().strip().split(";")
		if row == ['']:
			break
		#print(row[0] +" s "+ read[0])
		if int(row[0]) == int(read[2])-1:
			print(read[2],row[0],row[1])
			read[2]=row[1]
			break	
	print(">>>>>")



	out.write("%s\n" % (';'.join(read)))


