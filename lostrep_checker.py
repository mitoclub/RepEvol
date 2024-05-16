import time
import timeit
import os



#folder = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/Checking1"


# folder = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/Checking2"


folder = "C:/Users/Abathur/Desktop/_SCIENCE/Conserva/Checking3"








reps = open(folder+"/"+"no_count.csv",'w')

#reps.write("%s;Deletions;5_breakpoint;3_breakpoint;Deletion_length_bp;Deletion_of_replication_origins;Location_of_the_deleted_region;Single_mtDNA_deletions;Multiple_mtDNA_deletions;Healthy_tissues;Parkinson_Disease;Inclusion_Body_Myositis;Tumour;Other_clinical_features;References\n" % (head))

files=os.listdir(folder+"/no_real")
#prepath=os.getcwd()+"/" + folder + "/"

for f in files:

	print(f)


	# For NO
	c_all = 0
	c_dir = 0
	c_com = 0
	c_mir = 0
	c_inv = 0



	path = folder+"/no_real/"+f

	file = open(path,'r')

	head = file.readline().strip()



	while True:

		
		raw = file.readline().strip()
		print(raw)

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
		


	reps.write("%s;%s;%s;%s;%s;%s\n" % (f,c_all,c_dir,c_com,c_mir,c_inv))














# reps = open(folder+"/"+"yes_count.csv",'w')

# #reps.write("%s;Deletions;5_breakpoint;3_breakpoint;Deletion_length_bp;Deletion_of_replication_origins;Location_of_the_deleted_region;Single_mtDNA_deletions;Multiple_mtDNA_deletions;Healthy_tissues;Parkinson_Disease;Inclusion_Body_Myositis;Tumour;Other_clinical_features;References\n" % (head))

# files=os.listdir(folder+"/yes_real")
# #prepath=os.getcwd()+"/" + folder + "/"

# for f in files:

# 	print(f)


# 	# For YES
# 	c_all = 0
# 	c_all_diff = 0
# 	c_all_same = 0



# 	path = folder+"/no_real/"+f

# 	file = open(path,'r')

# 	head = file.readline().strip()



# 	while True:

		
# 		raw = file.readline().strip()
# 		print(raw)

# 		if raw == "":
# 			break

# 		row = raw.split(";")



# 		c_all += 1

# 		if row[3]=="1":	
# 			c_all_diff = 0

# 		if row[3]=="2":	
# 			c_all_same = 0

# 		if row[3]=="3":	
# 			c_mir += 1

# 		if row[3]=="4":	
# 			c_inv += 1		
		


# 	reps.write("%s;%s;%s\n" % (f,c_all,c_dir,c_com,c_mir,c_inv))