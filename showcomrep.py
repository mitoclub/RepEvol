import time
import timeit
import os
import sqlite3
import sys



ages = MiddlePLE



time = open("comrep/ALLwithTIME.csv",'r')
 


aim = "SupraHominida.muscle.sequester.fasta"
#reps = open(outfol+"/"+f,'w')

first=8551
second=13539

#step1
pre_l="CCCAACTAAATACTACCGTATGGCCCACCATAATTACCCCCATACTCCTTACACTATTCCTCATCACCCAACTAAAAATATTAAACACAAACTACCACTT"
orig_l="ACCTCCCTCACCA"
post_l=""
orig_r="ACCTCCCTCACCA"
#result:
# Hoolock_hoolock tCCcgCtTCcCCA ACCTCCtTaACtA Burdigalian Miocene
# Hoolock_leuconedys tCCcgCtTCcCCA ACtTCCtTaACaA Burdigalian Miocene
# Symphalangus_syndactylus ACCcgCCTCcCCA ACCTCCCTaACtA Burdigalian Miocene
# Hylobates_pileatus ACCcgCCTCcCCA ACCTCCCTaACCA Burdigalian Miocene
# Hylobates_agilis ACCcgCCTCcCCA ACCTCCtTaACCA Burdigalian Miocene
# Hylobates_moloch ACCcgCCTCcCCA ACCTCCCTaACCA Burdigalian Miocene
# Hylobates_lar ACCcgCCTCcCCA ACCTCCtTaACCA Burdigalian Miocene
# Nomascus_leucogenys ACCcgCCTCcCCA ACCTCCCTaACCA Burdigalian Miocene
# Nomascus_siki ACCcgCCTCcCCA ACCTCCCTaACCA Burdigalian Miocene
# Nomascus_gabriellae ACCcgCCTCcCCA ACCTCCCTaACCA Burdigalian Miocene
# Gorilla_gorilla ACCcCCCTtACCA ACCTCCCTagCCA Tortonian Miocene

# Homo_heidelbergensis xxxxxxxxxxxxx ACCTCCCTCACxx MiddlePLE Pleistocene
# Homo_sapiens_neanderthalensis xxxxxxxxxxxxx xxxxxxxxxxxxx MiddlePLE Pleistocene
# Homo_sp._Altai xxxxxxxxxxxxx ACCTCCCTCACxx MiddlePLE Pleistocene

# Pan_paniscus ACCcCCCTCACxx ACCTCCCTCAtCA Messinian Miocene
# Pan_troglodytes ACCcCCCTCACxx ACCTCCCTCACCA Messinian Miocene
# Pongo_pygmaeus ACCcaCCcCACCA ACCTCCCTCACtA Langhian Miocene
# Pongo_abelii ACCcaCCcCACCA ACCTCCCTCACtA Langhian Miocene




time.readline().strip()

while True:
	t = time.readline().strip()
	if t == "":
		break
	sp = t.split(";")[0]

	file = open('xcards_simple_names/' + aim,'r')

	file.readline().strip()
	genome = ""
	num=1
	while True:

		read = file.readline().strip()
		if ">" in read: 
			#print(read)
			if sp==read[1:]:
				name = read[1:]
				read = file.readline().strip()

				new_left = ""
				new_right = ""
				new_ln=0
				new_rn=0
				for i in range(len(orig_l)):
					if read[first:first+13][i]==orig_l[i]:
						new_left+=read[first:first+13][i]
					elif read[first:first+13][i]=="X":
						new_left+=read[first:first+13][i]
					else:
						new_left+=read[first:first+13][i].lower()
						new_ln+=1

				for i in range(len(orig_r)):
					if read[second:second+13][i]==orig_r[i]:
						new_right+=read[second:second+13][i]
					elif read[second:second+13][i]=="X":
						new_right+=read[second:second+13][i]
					else:
						new_right+=read[second:second+13][i].lower()
						new_rn+=1

				print(name,new_left,new_right,t.split(";")[1],t.split(";")[2],str(new_ln),str(new_rn))
				#reps.write("%s\n" % (head))
		if read == "":
			break


