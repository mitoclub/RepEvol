import time
import timeit
import os




# folder = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/Checking1/no"
# outfol = folder + "_real"
# aim = "MitoBreakDB_121219_group1.csv"

# folder = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/Checking1/yes"
# outfol = folder + "_real"
# aim = "MitoBreakDB_121219_group1.csv"


# folder = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/Checking2/no"
# outfol = folder + "_real"
# aim = "MitoBreakDB_121219_group2.csv"

# folder = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/Checking2/yes"
# outfol = folder + "_real"
# aim = "MitoBreakDB_121219_group2.csv"


folder = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/Checking3/no"
outfol = folder + "_real"
aim = "MitoBreakDB_121219_group3.csv"

# folder = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/Checking3/yes"
# outfol = folder + "_real"
# aim = "MitoBreakDB_121219_group3.csv"






files=os.listdir(folder)
#prepath=os.getcwd()+"/" + folder + "/"

for f in files:

	print(f)

	path = folder+"/"+f

	file = open(path,'r')

	head = file.readline().strip()

	reps = open(outfol+"/"+f,'w')

	reps.write("%s;Deletions;5_breakpoint;3_breakpoint;Deletion_length_bp;Deletion_of_replication_origins;Location_of_the_deleted_region;Single_mtDNA_deletions;Multiple_mtDNA_deletions;Healthy_tissues;Parkinson_Disease;Inclusion_Body_Myositis;Tumour;Other_clinical_features;References\n" % (head))



	while True:

		
		raw = file.readline().strip()
		#print(raw)

		if raw == "":
			break

		row = raw.split(";")


		aimfile = open(aim,'r')
		aimfile.readline()
		while True:
			xaw = aimfile.readline().strip()
			xow = xaw.split(";")
			#print(xow)
			if xaw == "":
				break

			ori = int(xow[1])
			end = int(xow[2])
			rori = int(row[0])
			rend = int(row[1])
			if ori >= rori - 15 and ori <= rori + 15 and end >= rend - 15 and end <= rend + 15:
				reps.write("%s;%s\n" % (raw,xaw))

				break



		