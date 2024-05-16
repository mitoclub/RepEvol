#coding=utf8






import time
import timeit
import os

import sqlite3
import sys

#aim = "AncestorsOfHominida.muscle.sequester.fasta"
#aim = "Mitochondria_GreatApes.muscle.sequester PLUS HOMO SAPIENS.fasta"

aim = "SupraHominida.muscle.sequester.fasta"

def maper(a,n):

    #print(a)


    ########## path3 = 'maps/' + aim + '/' + n + '.csv'
    ########## reps3 = open(path3, "w")


    con = sqlite3.connect('maps/%s/%s.sqlite' % (aim,n))
    cur = con.cursor()
    cur.execute('CREATE TABLE species (id INTEGER PRIMARY KEY, ori INTEGER, tar INTEGER, nuc VARCHAR(1))')
    con.commit()







    j = 0


    l = len(a)
    print(l)


    for i in range(l):

        if a[i]!="-":
            ##################### reps3.write("%s;%s;%s\n" % (j,i,a[i]))
            q = "INSERT INTO species (id, ori, tar, nuc) VALUES(NULL, %s, %s, \"%s\")" % (j,i,a[i])
            cur.execute(q)

            j+=1

    con.commit()




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
    


















# # Importing of libraries
# import time
# import timeit
# import os
# import sqlite3
# import sys

# try:
#     from StringIO import StringIO ## for Python 2
# except ImportError:
#     from io import StringIO ## for Python 3


# """
# Structure of working tables:
# repeats (
# id INTEGER PRIMARY KEY,  
# spece_id INTEGER,              - id of species in table species
# first_start INTEGER,           - position of first sequence in genome
# second_start INTEGER,          - position of second sequence in genome
# length INTEGER,                - length of repeat
# id_type INTEGER,               - type of repeat
# first_seq VARCHAR(1000),       - first sequence
# second_seq VARCHAR(1000),      - second sequence
# alt_second_seq VARCHAR(1000),  - second sequence transformed in accordance to the type of repeat
# errs (INTEGER)                 - number of errors
# )
# species (
# id INTEGER PRIMARY KEY,        - id of species
# spece TEXT                     - species name
# )          
# types (
# id INTEGER PRIMARY KEY,        - id of type of repeat
# type TEXT                      - type of repeat
# )
# """

# front=[0,99999] # !!!!!!!!!!!!!!!!!!!!!!!!!

# #AncestorsOfHominida.muscle.sequester.fasta
# #Mitochondria_GreatApes.muscle.sequester.fasta
# #SupraHominida.muscle.sequester.fasta
# pgen_path = 'genomes/Homo_sapiens.fa'

# folder = "HUMAN"


# dirpath = os.getcwd() + "/" + folder
# # if __name__ == "__main__":

# #     if len (sys.argv) > 2:
# #         pgen_path = sys.argv[1]
# #         dirpath = os.getcwd() + "/" + sys.argv[2]
# #     elif len (sys.argv) > 1:
# #         pgen_path = sys.argv[1]
# pgen = open(pgen_path,'r')
# nucAlphabet = {'a', 't', 'g', 'c', 'x'}

# gcount=sum(1 for line in pgen)/2
# print("We have %s genomes for analysis" % gcount)

# pgen = open(pgen_path,'r')


# try:
#     os.mkdir(dirpath)
# except OSError:
#     print ("FOUND directory is exist")
# else:
#     print ("FOUND directory created")


# # creating of empty dot-plot (matrix)
# def zeros(shape):
#     retval = []
#     for x in range(shape[0]):
#         retval.append([])
#         for y in range(shape[1]):
#             retval[-1].append(0)
#     return retval

# # Slicing sequenses from genome of length 10 with a shift of 1
# def extractWordsTen(s, alphabet):
#     arr = []
#     n=10
#     for i in range(len(s)-n+1):
#         arr.append(''.join(s[i:i+n]))
#     return arr

# # Counter of searching time
# class Profiler(object):
#     def __enter__(self):
#         self._startTime = time.time()      
#     def __exit__(self, type, value, traceback):
#         print("Elapsed time: {:.3f} sec".format(time.time() - self._startTime))

# # Matches checking
# def  match_check (words,invert,score,oi,oj,i,j,e,reptype,origlen):
#     lengthj=len(score[oi])
#     lengthi=len(score)
#     match=1 # matches
#     dmatch=e # mismatches
#     # ten cells passage
#     for k in range(1, 10-dmatch): 
#         ci=i+k
#         cj=j+k
#         if ((ci>(lengthi-1)) or (cj>(lengthj-1))): # Output to the end of the genome    
#                 return 0
#         if score[ci][cj]==10: # Match of the nucleotides marked in the cell
#             match=match+1  
#             if (match>8): # If there is 9-10 matches record a repeat
#                 if invert:
#                     point=lengthj-oj-11 # Position for inverted sequence
#                 else:
#                     point=oj
#                 if point>origlen-1:
#                     point=point-origlen   
#                 if oi>origlen-1:
#                     oi=oi-origlen
#                 q = "INSERT INTO repeats (id,first_start, second_start, length, id_type, first_seq, second_seq) VALUES(NULL,?,?,?,?,?,?)"
#                 cur.execute(q,(oi,point,10,reptype,words[oi],words[point]))
#                 return 1
#         else:                 
#             dmatch=dmatch+1
#             if (dmatch>1) :          
#                 return 0
#     if (match>8):
#         if invert:
#             point=lengthj-oj-11
#         else:
#             point=oj
#         if point>origlen-1:
#             point=point-origlen   
#         if oi>origlen-1:
#             oi=oi-origlen
#         q = "INSERT INTO repeats (first_start, second_start, length, id_type, first_seq, second_seq) VALUES(?,?,?,?,?,?)"
#         cur.execute(q,(oi,point,10,reptype,words[oi],words[point]))
#         return 1
#     else: 	
#     	return 0

# # The procedure for working with the matrix
# def master (seq1, seq2, invert,reptype,origlen):
#     seq2=seq2.replace("X","N")
#     m, n = len(seq1), len(seq2)
#     words=extractWordsTen(seq1, nucAlphabet)
#     score = zeros((m+1, n+1)) 
#     if invert: # For mirror and inverted repeats 
#         print("matching invert")
#         for i in range(0, m): # Проверка соответсвия каждого в обычном геноме каждому в преобразованном геноме checking of match every repeat in ordinary genome and transformed genome 
#             print("%s\r" % i),
#             for j in range(0, m-i+10 +1):
#                 if j<m:
#                     if seq1[i] == seq2[j]:
#                         score[i][j]=10
#         print("checking invert")
#         lengthj=lengthi=len(score)
#         for i in range(0, m): # Searching of matches of length 10 with as many as one error by diagonals of matrix 
#             print("%s\r" % i),
#             for j in range(1, m-i-9):
#                 if j<m:             
#                     if score[i][j]==10: 
#                         match_check(words,invert,score,i,j,i,j,0,reptype,origlen) # если есть совпадение в первом же
#                     elif score[i+1][j+1]==10:
#                         match_check(words,invert,score,i,j,i+1,j+1,1,reptype,origlen) # если совпадение началось со второго
#     else: # For direct and complimentary ones         
#         print("matching")
#         for i in range(0, m):       
#             print("%s\r" % i),
#             for j in range(i+10, n):
#                 if seq1[i] == seq2[j]:
#                     score[i][j]=10
#         print("checking")
#         lengthj=lengthi=len(score)
#         for i in range(0, m-10  +1):
#             print("%s\r" % i),
#             for j in range(i+10, n-10): 
#                 if score[i][j]==10: 
#                     match_check(words,invert,score,i,j,i,j,0,reptype,origlen)
#                 elif score[i+1][j+1]==10:
#                     match_check(words,invert,score,i,j,i+1,j+1,1,reptype,origlen)  

# # Preprocedure of genome preparation for finding complimentary repeats
# def mastercomp (seq1, seq2,origlen):
#     reptype=2      
#     print("\nCompliment:")
#     arr1=[]
#     s2=""
#     for char in seq1:
#         if char=='A':
#             arr1.append('T') 
#         elif char=='T':
#             arr1.append('A')
#         elif char=='G':
#             arr1.append('C')
#         elif char=='C':
#             arr1.append('G')
#         else:
#             arr1.append('X')
#     s2=(''.join(arr1))
#     master (seq1, s2,False,reptype,origlen)

# # Preprocedure of genome preparation for finding mirror repeats
# def masterpoli (seq1, seq2,origlen):
#     reptype=3      
#     print("\nMirror:")
#     arr2=[]
#     s3=""
#     for char in seq1:
#         arr2.append(char)
#     s3=(''.join(reversed(arr2)))
#     master (seq1, s3,True,reptype,origlen)

# # Preprocedure of genome preparation for finding inverted repeats
# def masterinvert (seq1, seq2,origlen):
#     reptype=4
#     print("\nInvert:")    
#     arr1=[]
#     s2=""
#     for char in seq1:  
#         if char=='A':
#             arr1.append('T')
#         elif char=='T':
#             arr1.append('A')
#         elif char=='G':
#             arr1.append('C')
#         elif char=='C':
#             arr1.append('G')
#         else:
#             arr1.append('X')
#     arr3=reversed(arr1)
#     s4=""
#     s4=(''.join(arr3))
#     master (seq1, s4,True,reptype,origlen)



# # Alternate start searching for different types of repeats in each genome

# pr=1
# while True:
#     if pr>front[0]:
#         break
#     name = pgen.readline().strip()[1:]
#     genome = pgen.readline().strip()

#     pr+=1


# while True:
#     # if pr>front[1]:
#     #     break



#     name = pgen.readline().strip()[1:]

#     if name == "":
#         break


#     genome = pgen.readline().strip()

#     print("GENOME: " + name)
#     length=len(genome)
#     genome=genome[:-1]+genome[:10] # genome expansion 
#     print('%s/%s_%s.sqlite' % (dirpath,pr,name))
#     con = sqlite3.connect('%s/%s_%s.sqlite' % (dirpath,pr,name))
#     cur = con.cursor()
#     cur.execute('CREATE TABLE species (id INTEGER PRIMARY KEY, name VARCHAR(100))')
#     con.commit()
#     cur.execute('CREATE TABLE repeats (id INTEGER PRIMARY KEY, spece_id INTEGER, first_start INTEGER, second_start INTEGER, length INTEGER, id_type INTEGER, first_seq VARCHAR(50), second_seq VARCHAR(50))')
#     con.commit()
#     reptype=1
#     q = "INSERT INTO species (id, name) VALUES(NULL, \""+name+"\")"
#     cur.execute(q)
    
#     with Profiler() as p:   
#         with Profiler() as a:
#             print("\nSuper direct  for "+name+":")
#             master(genome,genome,False,1,length)
#             con.commit()
#         with Profiler() as b:
#             print("\nSuper compliment for "+name+":")
#             mastercomp(genome,genome,length)
#             con.commit()          
#         with Profiler() as c:
#             print("\nSuper mirror for "+name+":")
#             masterpoli(genome,genome,length)
#             con.commit()
#         with Profiler() as d:
#             print("\nSuper invert for "+name+":")
#             masterinvert(genome,genome,length)
#             con.commit()
#         print("\nSuper all for "+name+":")
#     con.commit()
    
#     pr=pr+1
#     if pr>gcount:
# 	    break



























# """
# Structure of working tables:
# repeats (
# id INTEGER PRIMARY KEY,  
# spece_id INTEGER,              - id of species in table species
# first_start INTEGER,           - position of first sequence in genome
# second_start INTEGER,          - position of second sequence in genome
# length INTEGER,                - length of repeat
# id_type INTEGER,               - type of repeat
# first_seq VARCHAR(1000),       - first sequence
# second_seq VARCHAR(1000),      - second sequence
# alt_second_seq VARCHAR(1000),  - second sequence transformed in accordance to the type of repeat
# errs (INTEGER)                 - number of errors
# )
# repeats_gap (
# id INTEGER PRIMARY KEY,  
# spece_id INTEGER,              -id of species in table species
# first_start INTEGER,           - position of first sequence in genome
# second_start INTEGER,          - position of second sequence in genome
# length INTEGER,                - length of repeat
# id_type INTEGER,               - type of repeat
# first_seq VARCHAR(1000),       - first sequence
# second_seq VARCHAR(1000),      - second sequence
# alt_second_seq VARCHAR(1000),  - second sequence transformed in accordance to the type of repeat
# errs (INTEGER)                 - number of errors
# )
# species (
# id INTEGER PRIMARY KEY,        - id of species
# spece TEXT                     - name of species
# )          
# types (
# id INTEGER PRIMARY KEY,        - id of type
# type TEXT                      - type
# )
# """

# # Specifying a file with genomes

# # pgen_path = 'genomes.fa'
# # Input paths to databases and genome
# # if __name__ == "__main__":
# #     if len (sys.argv) > 2:
# #         files = os.listdir(sys.argv[1])
# #         prepath=("%s\\" % (sys.argv[1]))
# #         pgen_path = sys.argv[2]

# #     elif len (sys.argv) > 1:
# #         files = os.listdir(sys.argv[1])
# #         prepath=("%s\\" % (sys.argv[1]))

# #     else: 
# files=os.listdir(folder)
# prepath=os.getcwd()+"/" + folder + "/"

# pgen = open(pgen_path,'r')
# nucAlphabet = {'a', 't', 'g', 'c', 'x'}
# xersh=0

# def extractWordsTen(s, alphabet):
#     arr = []
#     n=10
#     for i in range(len(s)-n+1):
#         arr.append(''.join(s[i:i+n]))
#     return arr

# # Receiving of sequense that complymentary to given one 
# def compmaster (seq1):    
#     arr1=[]
#     s2=""
#     for char in seq1:
#         if char=='A':
#             arr1.append('T')
#         elif char=='T':
#             arr1.append('A')
#         elif char=='G':
#             arr1.append('C')
#         elif char=='C':
#             arr1.append('G')
#         else:
#             arr1.append('X')
#     s2=(''.join(arr1))
#     return s2

# # Receiving of sequense that mirror to given one
# def polimaster (seq1):
#     arr2=[]
#     s3=""
#     for char in seq1:
#         arr2.append(char)
#     s3=(''.join(reversed(arr2)))  
#     return s3

# # Receiving of sequense that inverted to given one
# def invertmaster (seq1):   
#     arr1=[]
#     s2=""
#     for char in seq1:   
#         if char=='A':
#             arr1.append('T')
#         elif char=='T':
#             arr1.append('A')
#         elif char=='G':
#             arr1.append('C')
#         elif char=='C':
#             arr1.append('G')
#         else:
#             arr1.append('X')
#     arr3=reversed(arr1)
#     s4=""  
#     s4=(''.join(arr3))  
#     return s4

# # Computation of Levenshtein distance between two sequence
# def lev(s, t):
#     if s == t: return 0
#     elif len(s) == 0: return len(t)
#     elif len(t) == 0: return len(s)
#     v0 = [None] * (len(t) + 1)
#     v1 = [None] * (len(t) + 1)
#     for i in range(len(v0)):
#         v0[i] = i
#     for i in range(len(s)):
#         v1[0] = i + 1
#         for j in range(len(t)):
#             cost = 0 if s[i] == t[j] else 1
#             v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)
#         for j in range(len(v0)):
#             v0[j] = v1[j]
#     return v1[len(t)]

# # Consistent work with a repeats database for each genome
# for f in files:
#     # The path to DB
#     path = prepath+f
#     # Connection to DB
#     con = sqlite3.connect(path)
#     # Read database to tempfile
#     tempfile = StringIO()
#     for line in con.iterdump():
#         tempfile.write('%s\n' % line)
#     con.close()
#     tempfile.seek(0)
#     # Create a database in memory and import from tempfile
#     in_memory = sqlite3.connect(":memory:")
#     in_memory.cursor().executescript(tempfile.read())
#     in_memory.commit()
#     in_memory.row_factory = sqlite3.Row
#     cur = in_memory.cursor()
#     # Receiving of name of species from DB filename 
#     fname = f[:-7].split("_")
#     lname= fname[1]
#     for fn in fname[2:]:
#         lname=lname+"_"+fn
#     print(lname)   
#     n=0
#     # Opening of file with genomes
#     pgen = open(pgen_path,'r')
#     # Selection of needed species in file with genomes 
#     while True: 
#         name = pgen.readline().strip()[1:] #Name string
#         genome = pgen.readline().strip() # Genome strind
#         if name.strip()==lname: # Matches of name in filename and name in file with genomes 
#             xersh = genome.count("X") # Counting the number of X
#             print(name)
#             words=extractWordsTen(genome, nucAlphabet)
#             dougenome=genome[:-1]+genome
#             break
#         if name.strip()==lname[:-1]: 
#             xersh = genome.count("X")
#             print(name)
#             words=extractWordsTen(genome, nucAlphabet)
#             dougenome=genome[:-1]+genome
#             break
#             break
#         if name=="":
#             print("ACHTUNG!!!DANGER!!!KAPUT!!!ERRRRROOOORRRRR!!!!!")
#             break
#     pgen.close
#     # Getting the length of the database and genome
#     cur.execute("ALTER TABLE species ADD xnum INTEGER")
#     in_memory.commit()
#     cur.execute("UPDATE species SET xnum = %s" % (xersh))
#     in_memory.commit()  
#     cur.execute('SELECT * FROM repeats')
#     reps=cur.fetchall()
#     alllen=reps[-1][0] # Id of the last repeat in DB
#     genlen=len(genome)
#     origlen=len(genome)
#     fivelen=origlen/5
#     dougenome=genome[:-1]+genome # doubled genome

#     # ERRORER
#     print("ERRORER")
#     cur.execute("ALTER TABLE repeats ADD alt_second_seq VARCHAR(50)")
#     in_memory.commit()
#     cur.execute("ALTER TABLE repeats ADD errs INTEGER")
#     in_memory.commit()
#     cur.execute('SELECT * FROM repeats')
#     reps=cur.fetchall()
#     len(reps)
#     for r in range(1,len(reps)+1):
#         print("%s\r" % r),
#         q = ("SELECT * FROM repeats WHERE id=%s" % (r))
#         cur.execute(q)
#         of=cur.fetchall() 
#         if len(of)!=0:
#             if of[0][5]==1:
#                 twbetha=of[0][7]
#             elif of[0][5]==2:
#                 twbetha=compmaster(of[0][7])
#             elif of[0][5]==3:
#                 twbetha=polimaster(of[0][7])
            
#             elif of[0][5]==4:
#                 twbetha=invertmaster(of[0][7])
#             errs=lev(of[0][6],twbetha)
#             q=("UPDATE repeats SET alt_second_seq = \'"+twbetha+"\', errs = %s  WHERE id = %s" % (errs,of[0][0]))
#             cur.execute(q)
#     in_memory.commit()


#     # GLUE
#     print("GLUE DIRTY GAPS")
#     # Copying the original table of repeats 
#     cur.execute('CREATE TABLE repeats_gap (id INTEGER PRIMARY KEY, spece_id INTEGER, first_start INTEGER, second_start INTEGER, length INTEGER, id_type INTEGER, first_seq VARCHAR, second_seq VARCHAR, alt_second_seq VARCHAR, errs INTEGER)')
#     in_memory.commit()
#     cur.execute("INSERT INTO repeats_gap SELECT * FROM repeats")
#     in_memory.commit()
#     cur.execute('SELECT * FROM repeats_gap')
#     reps=cur.fetchall()
#     for r in range(1,alllen+1):
#         print("%s\r" % r),
#         q = ("SELECT * FROM repeats_gap WHERE id=%s" % (r))
#         cur.execute(q)
#         of=cur.fetchall()
#         if len(of)!=0:
#             # Labels for the fulfillment of conditions
#             breakster=False
#             ring=0
#             ring1=0
#             ring2=0
#             # Position of the second sequence in genome
#             bstart=of[0][3]
#             bstart_be=of[0][3]
#             # The first and second sequences
#             alpha=of[0][6]
#             betha=of[0][7]
#             # Length of sequences
#             lenglu=of[0][4]
#             lenglun=of[0][4] 
#             # Id of repeat
#             start=of[0][0]
#             # Position of the first and second sequence in genome
#             start_a=of[0][2]
#             start_b=of[0][3]
#             superlen=1
#             # Counter of shift
#             gi=1
#             gapc=0
#             # Limit of searchind the optimal variant of merging
#             limit=lenglun*2
#             arr_be=[]
#             alpha_be=alpha
#             betha_be=betha
#             astart_be=of[0][2]
#             bstart_be=of[0][3]
#             up=False
#             while True:       
#                 q = "SELECT * FROM repeats WHERE first_start=? and second_start=? and id_type=?"   
#                 if (of[0][5]==1) or (of[0][5]==2): # Direct and complymentary repeats
#                     cur.execute(q,(of[0][2]+gi,of[0][3]+gi,of[0][5]))
#                 elif (of[0][5]==3) or (of[0][5]==4): # Mirror and inverted repeats
#                     cur.execute(q,(of[0][2]+gi,of[0][3]-gi,of[0][5]))
#                 cf=cur.fetchall()
#                 if (of[0][5]==1) or (of[0][5]==2):
#                     q = "SELECT * FROM repeats WHERE first_start=? and second_start=? and id_type=?"
#                     cur.execute(q,(of[0][3]+gi-origlen,of[0][2]+gi,of[0][5]))
#                     dif=cur.fetchall()
#                 elif (of[0][5]==3) or (of[0][5]==4):
#                     lasta=of[0][2]
#                     lastb=of[0][3]

#                 # Merging of direct and complymentary repeats with the shift of the first and second sequences
#                 # relative to current sequences for an equal distance forward
#                 if len(cf)!=0 and ((of[0][5]==1) or (of[0][5]==2)):   
#                     seqa_s=start_a
#                     seqa_f=of[0][2]+of[0][4]+gapc+cf[0][4]-9
#                     seqb_s=start_b
#                     seqb_f=of[0][3]+of[0][4]+gapc+cf[0][4]-9    
#                     if ring: # if there was already a merging with the transition to the beginning of the genome
#                         seqa_s=start_a
#                         seqa_f=of[0][3]+of[0][4]+gapc+cf[0][4]-9
#                         seqb_s=start_b
#                         seqb_f=of[0][2]+of[0][4]+gapc+cf[0][4]+origlen  -9                     
#                     lenglu=len(alpha) # new length
#                     alpha=dougenome[seqa_s:seqa_f] # the first merging sequence
#                     betha=dougenome[seqb_s:seqb_f] # the second merging sequence
#                     if of[0][5]==1:
#                         twbetha=betha
#                     elif of[0][5]==2:
#                         twbetha=compmaster(betha)    
#                     elif of[0][5]==3:
#                         twbetha=polimaster(betha)
#                     elif of[0][5]==4:
#                         twbetha=invertmaster(betha)
#                     errs=lev(alpha,twbetha)
#                     length_be=len(alpha)
#                     degen = float ( float(errs) / float(length_be) )
#                     if degen<0.21: # The criterion of optimality is the degeneracy of the merging repeat
#                         # fixing the last optimal merging
#                         alpha_be=dougenome[seqa_s:seqa_f]
#                         betha_be=dougenome[seqb_s:seqb_f]
#                         astart_be=seqa_s
#                         bstart_be=seqb_s
#                         arr_be.append(cf[0][0])
#                     else: # If the merging is not optimal incomplete graduations are cut off and the optimality test is repeated                   
#                         if (alpha[:1]!=twbetha[:1]):           
#                             alpha=alpha[1:]
#                             seqa_s=seqa_s+1
#                             if of[0][5]==1 or of[0][5]==2:
#                                 betha=betha[1:] 
#                                 bstart=bstart+1                                  
#                             elif of[0][5]==3 or of[0][5]==4:                    
#                                 betha=betha[:length_be-1]      
#                             twbetha=twbetha[1:]
#                             length_be=length_be-1
#                             up=True
#                         if (alpha[-1:]!=twbetha[-1:]):
#                             alpha=alpha[:length_be-1]
#                             if of[0][5]==1 or of[0][5]==2:
#                                 betha=betha[:length_be-1]                    
#                             elif of[0][5]==3 or of[0][5]==4:                   
#                                 betha=betha[1:]        
#                                 bstart=bstart+1                
#                             twbetha=twbetha[:length_be-1]
#                             length_be=length_be-1
#                             up=True
#                         if up:
#                             if of[0][5]==1:
#                                 twbetha=betha
#                             elif of[0][5]==2:
#                                 twbetha=compmaster(betha)                        
#                             elif of[0][5]==3:
#                                 twbetha=polimaster(betha)
#                             elif of[0][5]==4:
#                                 twbetha=invertmaster(betha)   
#                         errs=lev(alpha,twbetha)
#                         length_be=len(alpha)
#                         degen = float ( float(errs) / float(length_be) )
#                         if degen<0.21:
#                             alpha_be=dougenome[seqa_s:seqa_f]
#                             betha_be=dougenome[seqb_s:seqb_f]
#                             astart_be=seqa_s
#                             bstart_be=seqb_s
#                             arr_be.append(cf[0][0])     
#                     q = ("SELECT * FROM repeats WHERE id=%s" % (cf[0][0]))
#                     cur.execute(q)
#                     of=cur.fetchall()     
#                     gi=1
#                     gapc=0

#                 # Merging for mirror and inverted repeats with a shift of the first sequence forward  
#                 # and the second sequens backward at the same distance from the current sequences
#                 elif (len(cf)!=0 and ((of[0][5]==3) or (of[0][5]==4))):              
#                     seqa_s=start_a
#                     seqa_f=cf[0][2]+cf[0][4]
#                     seqb_s=cf[0][3]
#                     seqb_f=start_b+cf[0][4]
#                     lenglu=len(alpha)
#                     alpha=dougenome[seqa_s:seqa_f]
#                     betha=dougenome[seqb_s:seqb_f]
#                     if of[0][5]==1:
#                         twbetha=betha
#                     elif of[0][5]==2:
#                         twbetha=compmaster(betha)    
#                     elif of[0][5]==3:
#                         twbetha=polimaster(betha)
#                     elif of[0][5]==4:
#                         twbetha=invertmaster(betha)
#                     errs=lev(alpha,twbetha)
#                     length_be=len(alpha)
#                     degen = float ( float(errs) / float(length_be) )
#                     if degen<0.21:
#                         alpha_be=dougenome[seqa_s:seqa_f]
#                         betha_be=dougenome[seqb_s:seqb_f]
#                         astart_be=seqa_s
#                         bstart_be=seqb_s
#                         arr_be.append(cf[0][0])
#                     else:    
#                         if (alpha[:1]!=twbetha[:1]): 
#                             alpha=alpha[1:]
#                             seqa_s=seqa_s+1
#                             if of[0][5]==1 or of[0][5]==2:     
#                                 betha=betha[1:] 
#                                 bstart=bstart+1                   
#                             elif of[0][5]==3 or of[0][5]==4:
#                                 betha=betha[:length_be-1]      
#                             twbetha=twbetha[1:]
#                             length_be=length_be-1
#                             up=True
#                         if (alpha[-1:]!=twbetha[-1:]):
#                             alpha=alpha[:length_be-1]
#                             if of[0][5]==1 or of[0][5]==2:
#                                 betha=betha[:length_be-1]                    
#                             elif of[0][5]==3 or of[0][5]==4:
#                                 betha=betha[1:]        
#                                 bstart=bstart+1                
#                             twbetha=twbetha[:length_be-1]
#                             length_be=length_be-1
#                             up=True
#                         if up:
#                             if of[0][5]==1:
#                                 twbetha=betha
#                             elif of[0][5]==2:
#                                 twbetha=compmaster(betha)                        
#                             elif of[0][5]==3:
#                                 twbetha=polimaster(betha)
#                             elif of[0][5]==4:
#                                 twbetha=invertmaster(betha) 
#                         errs=lev(alpha,twbetha)
#                         length_be=len(alpha)
#                         degen = float ( float(errs) / float(length_be) )
#                         if degen<0.21:
#                             alpha_be=dougenome[seqa_s:seqa_f]
#                             betha_be=dougenome[seqb_s:seqb_f]
#                             astart_be=seqa_s
#                             bstart_be=seqb_s
#                             arr_be.append(cf[0][0])
#                     q = ("SELECT * FROM repeats WHERE id=%s" % (cf[0][0]))
#                     cur.execute(q)
#                     of=cur.fetchall()
#                     gi=1
#                     gapc=0
#                     lasta=cf[0][2]
#                     lastb=cf[0][3]

#                 # Merging for mirror and inverted repeats with a shift of the second sequence forward to the beginning of the genome
#                 # and a shift of the first sequence  at the same distance from the current sequences
#                 elif len(dif)!=0: 
#                     ring=1
#                     seqa_s=start_a
#                     seqa_f=of[0][2]+of[0][4]+gapc+dif[0][4]
#                     seqb_s=start_b
#                     seqb_f=of[0][3]+of[0][4]+gapc+dif[0][4]
#                     lenglu=len(alpha)
#                     alpha=dougenome[seqa_s:seqa_f]
#                     betha=dougenome[seqb_s:seqb_f]                   
#                     if of[0][5]==1:
#                         twbetha=betha
#                     elif of[0][5]==2:
#                         twbetha=compmaster(betha)    
#                     elif of[0][5]==3:
#                         twbetha=polimaster(betha)
#                     elif of[0][5]==4:
#                         twbetha=invertmaster(betha)
#                     errs=lev(alpha,twbetha)
#                     length_be=len(alpha)
#                     degen = float ( float(errs) / float(length_be) )
#                     if degen<0.21:
#                         alpha_be=dougenome[seqa_s:seqa_f]
#                         betha_be=dougenome[seqb_s:seqb_f]
#                         astart_be=seqa_s
#                         bstart_be=seqb_s
#                         arr_be.append(dif[0][0])
#                     else:
#                         if (alpha[:1]!=twbetha[:1]):
#                             alpha=alpha[1:]
#                             seqa_s=seqa_s+1
#                             if of[0][5]==1 or of[0][5]==2:
#                                 betha=betha[1:] 
#                                 bstart=bstart+1                   
#                             elif of[0][5]==3 or of[0][5]==4:
#                                 betha=betha[:length-1]      
#                             twbetha=twbetha[1:]
#                             length_be=length_be-1
#                             up=True
#                         if (alpha[-1:]!=twbetha[-1:]):
#                             alpha=alpha[:length_be-1]
#                             if of[0][5]==1 or of[0][5]==2:
#                                 betha=betha[:length_be-1]                    
#                             elif of[0][5]==3 or of[0][5]==4:
#                                 betha=betha[1:]        
#                                 bstart=bstart+1                
#                             twbetha=twbetha[:length_be-1]
#                             length_be=length_be-1
#                             up=True
#                         if up:
#                             if of[0][5]==1:
#                                 twbetha=betha
#                             elif of[0][5]==2:
#                                 twbetha=compmaster(betha)                        
#                             elif of[0][5]==3:
#                                 twbetha=polimaster(betha)
#                             elif of[0][5]==4:
#                                 twbetha=invertmaster(betha) 
#                         errs=lev(alpha,twbetha)
#                         length_be=len(alpha)
#                         degen = float ( float(errs) / float(length_be) )
#                         if degen<0.21:
#                             alpha_be=dougenome[seqa_s:seqa_f]
#                             betha_be=dougenome[seqb_s:seqb_f]
#                             astart_be=seqa_s
#                             bstart_be=seqb_s
#                             arr_be.append(cf[0][0])
#                     q = ("SELECT * FROM repeats WHERE id=%s" % (dif[0][0]))
#                     cur.execute(q)
#                     of=cur.fetchall()    
#                     gi=1
#                     gapc=0
#                 else: # If the current parameters of the repeat is not found
#                     gi=gi+1 # a sift increases
#                     if gi>lenglun: # If the shift is outside the current repeat
#                         gapc=gapc+1                  
#                     if (gapc > 100) : # The permanently defined limit for finding the optimal merging
#                         for be in arr_be:
#                             q=("DELETE FROM repeats_gap WHERE id=%s" % (be))
#                             cur.execute(q)
#                         if of[0][5]==1:
#                             twbetha=betha_be
#                         elif of[0][5]==2:
#                             twbetha=compmaster(betha_be)       
#                         elif of[0][5]==3:
#                             twbetha=polimaster(betha_be)
#                         elif of[0][5]==4:
#                             twbetha=invertmaster(betha_be)
#                         up=False
#                         length_be=len(alpha_be)
#                         errs=lev(alpha_be,twbetha)
#                         if (alpha_be[:1]!=twbetha[:1]):
#                             alpha_be=alpha_be[1:]
#                             astart_be=astart_be+1
#                             if of[0][5]==1 or of[0][5]==2:
#                                 betha_be=betha_be[1:] 
#                                 bstart_be=bstart_be+1                   
#                             elif of[0][5]==3 or of[0][5]==4:
#                                 betha_be=betha_be[:length_be-1]      
#                             twbetha=twbetha[1:]
#                             length_be=length_be-1
#                             up=True
#                         if (alpha_be[-1:]!=twbetha[-1:]):
#                             alpha_be=alpha_be[:length_be-1]
#                             if of[0][5]==1 or of[0][5]==2:
#                                 betha_be=betha_be[:length_be-1]                    
#                             elif of[0][5]==3 or of[0][5]==4:
#                                 betha_be=betha_be[1:]        
#                                 bstart_be=bstart_be+1                
#                             twbetha=twbetha[:length_be-1]
#                             length_be=length_be-1
#                             up=True
#                         if up:
#                             if of[0][5]==1:
#                                 twbetha=betha_be
#                             elif of[0][5]==2:
#                                 twbetha=compmaster(betha_be)                        
#                             elif of[0][5]==3:
#                                 twbetha=polimaster(betha_be)
#                             elif of[0][5]==4:
#                                 twbetha=invertmaster(betha_be)
#                         errs=lev(alpha_be,twbetha)
#                         q=("UPDATE repeats_gap SET length = %s, first_seq = ?, second_seq = ?,alt_second_seq=?, errs = %s, first_start= %s, second_start = %s  WHERE id = %s" % (len(alpha_be),errs,astart_be,bstart_be,start))
#                         cur.execute(q,(alpha_be,betha_be,twbetha))
#                         break
#                     if gi>limit : # The limit for finding the optimal merging has been reached
#                         revringexit=0
#                         up=False
#                         # Merging for mirror and inverted repeats with a shift of the second sequence forward to the beginning of the genome 
#                         # and a shift of the first sequence to the end of the genome at the same distance from the current sequences
#                         if (((of[0][5]==3) or (of[0][5]==4)) and (of[0][2]<limit and of[0][3]>origlen-limit)):
#                             breaksterrr=False
#                             ring1=0
#                             q = ("SELECT * FROM repeats_gap WHERE id=%s" % (r))
#                             cur.execute(q)
#                             eof=cur.fetchall()                            
#                             ebstart=eof[0][3]
#                             ebstart_be=eof[0][3]
#                             eastart_be=eof[0][2]
#                             ealpha=eof[0][6]
#                             ebetha=eof[0][7]
#                             elenglu=eof[0][4]
#                             elenglun=eof[0][4]
#                             estart=eof[0][0]
#                             estart_a=eof[0][2]
#                             estart_b=eof[0][3]
#                             esuperlen=1
#                             egi=1
#                             egapc=0
#                             elimit=elenglun*2
#                             earr_be=[]
#                             ealpha_be=ealpha
#                             ebetha_be=ebetha
#                             elength=of[0][4]
#                             eup=False
#                             while True:
#                                 if breaksterrr:
#                                     break        
#                                 q = "SELECT * FROM repeats WHERE first_start=? and second_start=? and id_type=?"
#                                 cur.execute(q,(eof[0][3]+egi-origlen,eof[0][2]-egi+origlen,eof[0][5]))
#                                 cef=cur.fetchall()
#                                 if len(cef)!=0:  
#                                     ring1=1
#                                     q = "SELECT * FROM repeats_gap WHERE id=%s" % cef[0][0]
#                                     cur.execute(q)
#                                     sup=cur.fetchall()
#                                     eseqa_s=cef[0][3]
#                                     eseqa_f=lasta+origlen+10
#                                     eseqb_s=lastb
#                                     eseqb_f=cef[0][2]+10+origlen
#                                     elenglu=len(ealpha)
#                                     ealpha=dougenome[eseqa_s:eseqa_f]
#                                     ebetha=dougenome[eseqb_s:eseqb_f]
#                                     if eof[0][5]==1:
#                                         etwbetha=ebetha
#                                     elif eof[0][5]==2:
#                                         etwbetha=compmaster(ebetha)
#                                     elif eof[0][5]==3:
#                                         etwbetha=polimaster(ebetha)
#                                     elif eof[0][5]==4:
#                                         etwbetha=invertmaster(ebetha)
#                                     elength=len(ealpha)
#                                     eerrs=lev(ealpha,etwbetha)
#                                     eup=True
#                                     if (ealpha[:1]!=etwbetha[:1]):
#                                         ealpha=ealpha[1:]
#                                         eseqa_s=eseqa_s+1
#                                         if eof[0][5]==1 or eof[0][5]==2:
#                                             ebetha=ebetha[1:] 
#                                             eseqb_s=eseqb_s+1                   
#                                         elif eof[0][5]==3 or eof[0][5]==4:
#                                             ebetha=ebetha[:elength-1]      
#                                         etwbetha=etwbetha[1:]
#                                         elength=elength-1
#                                         eup=True
#                                     if (ealpha[-1:]!=etwbetha[-1:]):
#                                         ealpha=ealpha[:elength-1]
#                                         if eof[0][5]==1 or eof[0][5]==2:
#                                             ebetha=ebetha[:elength-1]                    
#                                         elif eof[0][5]==3 or eof[0][5]==4:
#                                             ebetha=ebetha[1:]        
#                                             eseqb_s=eseqb_s+1                
#                                         etwbetha=etwbetha[:elength-1]
#                                         elength=elength-1
#                                         eup=True
#                                     if eup:
#                                         if eof[0][5]==1:
#                                             etwbetha=ebetha
#                                         elif eof[0][5]==2:
#                                             etwbetha=compmaster(ebetha)                        
#                                         elif eof[0][5]==3:
#                                             etwbetha=polimaster(ebetha)
#                                         elif eof[0][5]==4:
#                                             etwbetha=invertmaster(ebetha)
#                                     eerrs=lev(ealpha,etwbetha)
#                                     elength_be=len(ealpha)
#                                     edegen = float ( float(eerrs) / float(elength_be) )
#                                     if edegen<0.21:
#                                         q=("UPDATE repeats_gap SET length = %s, first_seq = ?, second_seq = ?,alt_second_seq=?, errs = %s, first_start = %s , second_start = %s WHERE id = %s" % (len(ealpha),eerrs,eseqa_s,eseqb_s,estart))
#                                         cur.execute(q,(ealpha,ebetha,etwbetha))
#                                         for be in arr_be:
#                                             q=("DELETE FROM repeats_gap WHERE id=%s" % (be))
#                                             cur.execute(q)
#                                     revringexit=1
#                                     break
#                                 else:
#                                     egi=egi+1
#                                     if egi>elenglun:
#                                         egapc=egapc+1
#                                     if egapc > 100:
#                                         break
#                                     if egi>elimit :
#                                         if ring1:
#                                             eseqa_s_e=eof[0][3]
#                                             eseqa_f_e=estart_a+elenglun
#                                             eseqb_f_e=eof[0][2]+eoriglen+1
#                                             eseqb_s_e=estart_b
#                                         else:
#                                             eseqa_s_e=estart_a
#                                             eseqa_f_e=estart_a+elenglun+egapc
#                                             eseqb_s_e=estart_b-egapc
#                                             eseqb_f_e=estart_b+elenglun
#                                         if eseqb_s_e>eseqb_f_e:
#                                             breaksterrr=True
#                                             break
#                                         ealpha_e=dougenome[eseqa_s_e:eseqa_f_e]
#                                         ebetha_e=dougenome[eseqb_s_e:eseqb_f_e]
#                                         if eof[0][5]==1:
#                                             etwbetha_e=ebetha_e
#                                         elif eof[0][5]==2:
#                                             etwbetha_e=compmaster(ebetha_e)
#                                         elif eof[0][5]==3:
#                                             etwbetha_e=polimaster(ebetha_e)
#                                         elif eof[0][5]==4:
#                                             etwbetha_e=invertmaster(ebetha_e)
#                                         eerrs=lev(ealpha_e,etwbetha_e)
#                                         elength_e=len(ealpha_e)
#                                         edegen = float ( float(eerrs) / float(elength_e) )
#                                         if edegen>0.4:
#                                             break
#                                         else:
#                                             elimit=elimit+elenglun
#                         # Merging for mirror and inverted repeats with a shift of the second sequence forward to the beginning of the genome 
#                         # and a shift of the first sequence backward at the same distance from the current sequences
#                         elif (((of[0][5]==3) or (of[0][5]==4)) and (of[0][3]>origlen-limit)):                            
#                             breaksterrr=False
#                             ring1=0
#                             q = ("SELECT * FROM repeats_gap WHERE id=%s" % (r))
#                             cur.execute(q)
#                             eof=cur.fetchall()                            
#                             ebstart=eof[0][3]
#                             ebstart_be=eof[0][3]
#                             eastart_be=eof[0][2]
#                             ealpha=eof[0][6]
#                             ebetha=eof[0][7]
#                             elenglu=eof[0][4]
#                             elenglun=eof[0][4]
#                             estart=eof[0][0]
#                             estart_a=eof[0][2]
#                             estart_b=eof[0][3]
#                             esuperlen=1
#                             egi=1
#                             egapc=0
#                             elimit=elenglun*2
#                             earr_be=[]
#                             ealpha_be=ealpha
#                             ebetha_be=ebetha
#                             elength=of[0][4]
#                             eup=False
#                             while True:
#                                 if breaksterrr:
#                                     break        
#                                 q = "SELECT * FROM repeats WHERE first_start=? and second_start=? and id_type=?"
#                                 cur.execute(q,(eof[0][3]+egi-origlen,eof[0][2]-egi,eof[0][5]))
#                                 cef=cur.fetchall()                
#                                 if len(cef)!=0:  
#                                     ring1=1
#                                     q = "SELECT * FROM repeats_gap WHERE id=%s" % cef[0][0]
#                                     cur.execute(q)
#                                     sup=cur.fetchall()                                
#                                     if len(sup)!=0:
#                                         eseqa_s=sup[0][3]
#                                         eseqa_f=lasta+10
#                                         eseqb_s=lastb
#                                         eseqb_f=sup[0][2]+sup[0][4]
#                                     else:
#                                         eseqa_s=cef[0][2]
#                                         eseqa_f=eof[0][3]+eof[0][4]
#                                         eseqb_s=eof[0][2]
#                                         eseqb_f=cef[0][3]+origlen+1
#                                     elenglu=len(ealpha)
#                                     ealpha=dougenome[eseqa_s:eseqa_f]
#                                     ebetha=dougenome[eseqb_s:eseqb_f]
#                                     if eof[0][5]==1:
#                                         etwbetha=ebetha
#                                     elif eof[0][5]==2:
#                                         etwbetha=compmaster(ebetha)
                        
#                                     elif eof[0][5]==3:
#                                         etwbetha=polimaster(ebetha)
#                                     elif eof[0][5]==4:
#                                         etwbetha=invertmaster(ebetha)
#                                     elength=len(ealpha)
#                                     eerrs=lev(ealpha,etwbetha)
#                                     eup=True
#                                     if (ealpha[:1]!=etwbetha[:1]):
#                                         ealpha=ealpha[1:]
#                                         eseqa_s=eseqa_s+1
#                                         if eof[0][5]==1 or eof[0][5]==2:
#                                             ebetha=ebetha[1:] 
#                                             eseqb_s=eseqb_s+1                   
#                                         elif eof[0][5]==3 or eof[0][5]==4:
#                                             ebetha=ebetha[:elength-1]      
#                                         etwbetha=etwbetha[1:]
#                                         elength=elength-1
#                                         eup=True
#                                     if (ealpha[-1:]!=etwbetha[-1:]):
#                                         ealpha=ealpha[:elength-1]
#                                         if eof[0][5]==1 or eof[0][5]==2:
#                                             ebetha=ebetha[:elength-1]                    
#                                         elif eof[0][5]==3 or eof[0][5]==4:
#                                             ebetha=ebetha[1:]        
#                                             eseqb_s=eseqb_s+1                
#                                         etwbetha=etwbetha[:elength-1]
#                                         elength=elength-1
#                                         eup=True
#                                     if eup:
#                                         if eof[0][5]==1:
#                                             etwbetha=ebetha
#                                         elif eof[0][5]==2:
#                                             etwbetha=compmaster(ebetha)                        
#                                         elif eof[0][5]==3:
#                                             etwbetha=polimaster(ebetha)
#                                         elif eof[0][5]==4:
#                                             etwbetha=invertmaster(ebetha)
#                                     eerrs=lev(ealpha,etwbetha)
#                                     elength_be=len(ealpha)
#                                     edegen = float ( float(eerrs) / float(elength_be) )
#                                     if edegen<0.21:
#                                         q=("UPDATE repeats_gap SET length = %s, first_seq = ?, second_seq = ?,alt_second_seq=?, errs = %s, first_start = %s , second_start = %s WHERE id = %s" % (len(ealpha),eerrs,eseqa_s,eseqb_s,estart))
#                                         cur.execute(q,(ealpha,ebetha,etwbetha))
#                                         for be in arr_be:
#                                             q=("DELETE FROM repeats_gap WHERE id=%s" % (be))
#                                             cur.execute(q)
#                                         q=("DELETE FROM repeats_gap WHERE id=%s" % (sup[0][0]))
#                                         cur.execute(q)
#                                     revringexit=1
#                                     break
#                                 else: 
#                                     egi=egi+1
#                                     if egi>elenglun:
#                                         egapc=egapc+1
#                                     if egapc > 100:                        
#                                         break
#                                     if egi>elimit :
#                                         if ring1:
#                                             eseqa_s_e=eof[0][3]
#                                             eseqa_f_e=estart_a+elenglun
#                                             eseqb_f_e=eof[0][2]+eoriglen+1
#                                             eseqb_s_e=estart_b
#                                         else:
#                                             eseqa_s_e=estart_a
#                                             eseqa_f_e=estart_a+elenglun+egapc
#                                             eseqb_s_e=estart_b-egapc
#                                             eseqb_f_e=estart_b+elenglun
#                                         if eseqb_s_e>eseqb_f_e:
#                                             breaksterrr=True
#                                             break
#                                         ealpha_e=dougenome[eseqa_s_e:eseqa_f_e]
#                                         ebetha_e=dougenome[eseqb_s_e:eseqb_f_e]
#                                         if eof[0][5]==1:
#                                             etwbetha_e=ebetha_e
#                                         elif eof[0][5]==2:
#                                             etwbetha_e=compmaster(ebetha_e)
#                                         elif eof[0][5]==3:
#                                             etwbetha_e=polimaster(ebetha_e)
#                                         elif eof[0][5]==4:
#                                             etwbetha_e=invertmaster(ebetha_e)
#                                         eerrs=lev(ealpha_e,etwbetha_e)
#                                         elength_e=len(ealpha_e)
#                                         edegen = float ( float(eerrs) / float(elength_e) )
#                                         if edegen>0.4:
#                                             break
#                                         else:                        
#                                             elimit=elimit+elenglun                        
#                         # Merging for mirror and inverted repeats with a shift of the first sequence backward to the end of the genome and a shift of the second sequence forward at the same distance from the current sequences
#                         elif (((of[0][5]==3) or (of[0][5]==4)) and (of[0][2]<limit)):                            
#                             breaksterrr=False
#                             ring1=0
#                             q = ("SELECT * FROM repeats_gap WHERE id=%s" % (r))
#                             cur.execute(q)
#                             eof=cur.fetchall()                            
#                             ebstart=eof[0][3]
#                             ebstart_be=eof[0][3]
#                             eastart_be=eof[0][2]
#                             ealpha=eof[0][6]
#                             ebetha=eof[0][7]
#                             elenglu=eof[0][4]
#                             elenglun=eof[0][4]
#                             estart=eof[0][0]
#                             estart_a=eof[0][2]
#                             estart_b=eof[0][3]
#                             esuperlen=1
#                             egi=1
#                             egapc=0
#                             elimit=elenglun*2
#                             earr_be=[]
#                             ealpha_be=ealpha
#                             ebetha_be=ebetha
#                             elength=of[0][4]
#                             eup=False
#                             while True:
#                                 if breaksterrr:
#                                     break        
#                                 q = "SELECT * FROM repeats WHERE first_start=? and second_start=? and id_type=?"
#                                 cur.execute(q,(eof[0][3]+egi,eof[0][2]-egi+origlen,eof[0][5]))
#                                 cef=cur.fetchall()             
#                                 #############################  CENTER  RING
#                                 if len(cef)!=0:  
#                                     ring1=1
#                                     q = "SELECT * FROM repeats_gap WHERE id=%s" % cef[0][0]
#                                     cur.execute(q)
#                                     sup=cur.fetchall()                                
#                                     eseqa_s=cef[0][3]
#                                     eseqa_f=lasta+origlen+10
#                                     eseqb_s=lastb
#                                     eseqb_f=cef[0][2]+10
#                                     elenglu=len(ealpha)
#                                     ealpha=dougenome[eseqa_s:eseqa_f]
#                                     ebetha=dougenome[eseqb_s:eseqb_f]
#                                     if eof[0][5]==1:
#                                         etwbetha=ebetha
#                                     elif eof[0][5]==2:
#                                         etwbetha=compmaster(ebetha)
                        
#                                     elif eof[0][5]==3:
#                                         etwbetha=polimaster(ebetha)
#                                     elif eof[0][5]==4:
#                                         etwbetha=invertmaster(ebetha)
#                                     elength=len(ealpha)
#                                     eerrs=lev(ealpha,etwbetha)
#                                     eup=True
#                                     if (ealpha[:1]!=etwbetha[:1]):
#                                         ealpha=ealpha[1:]
#                                         eseqa_s=eseqa_s+1
#                                         if eof[0][5]==1 or eof[0][5]==2:
#                                             ebetha=ebetha[1:] 
#                                             eseqb_s=eseqb_s+1                   
#                                         elif eof[0][5]==3 or eof[0][5]==4:
#                                             ebetha=ebetha[:elength-1]      
#                                         etwbetha=etwbetha[1:]
#                                         elength=elength-1
#                                         eup=True
#                                     if (ealpha[-1:]!=etwbetha[-1:]):
#                                         ealpha=ealpha[:elength-1]
#                                         if eof[0][5]==1 or eof[0][5]==2:
#                                             ebetha=ebetha[:elength-1]                    
#                                         elif eof[0][5]==3 or eof[0][5]==4:
#                                             ebetha=ebetha[1:]        
#                                             eseqb_s=eseqb_s+1                
#                                         etwbetha=etwbetha[:elength-1]
#                                         elength=elength-1
#                                         eup=True
#                                     if eup:
#                                         if eof[0][5]==1:
#                                             etwbetha=ebetha
#                                         elif eof[0][5]==2:
#                                             etwbetha=compmaster(ebetha)                        
#                                         elif eof[0][5]==3:
#                                             etwbetha=polimaster(ebetha)
#                                         elif eof[0][5]==4:
#                                             etwbetha=invertmaster(ebetha)
#                                     eerrs=lev(ealpha,etwbetha)
#                                     elength_be=len(ealpha)
#                                     edegen = float ( float(eerrs) / float(elength_be) )
#                                     if edegen<0.21:
#                                         q=("UPDATE repeats_gap SET length = %s, first_seq = ?, second_seq = ?,alt_second_seq=?, errs = %s, first_start = %s , second_start = %s WHERE id = %s" % (len(ealpha),eerrs,eseqa_s,eseqb_s,estart))
#                                         cur.execute(q,(ealpha,ebetha,etwbetha))
#                                         for be in arr_be:
#                                             q=("DELETE FROM repeats_gap WHERE id=%s" % (be))
#                                             cur.execute(q)
#                                         q=("DELETE FROM repeats_gap WHERE id=%s" % (sup[0][0]))
#                                         cur.execute(q)
#                                     revringexit=1
#                                     break
#                                 else: 
#                                     egi=egi+1
#                                     if egi>elenglun:
#                                         egapc=egapc+1
#                                     if egapc > 100:                        
#                                         break
#                                     if egi>elimit :
#                                         if ring1:
#                                             eseqa_s_e=eof[0][3]
#                                             eseqa_f_e=estart_a+elenglun
#                                             eseqb_f_e=eof[0][2]+eoriglen+1
#                                             eseqb_s_e=estart_b
#                                         else:
#                                             eseqa_s_e=estart_a
#                                             eseqa_f_e=estart_a+elenglun+egapc
#                                             eseqb_s_e=estart_b-egapc
#                                             eseqb_f_e=estart_b+elenglun
#                                         if eseqb_s_e>eseqb_f_e:
#                                             breaksterrr=True
#                                             break
#                                         ealpha_e=dougenome[eseqa_s_e:eseqa_f_e]
#                                         ebetha_e=dougenome[eseqb_s_e:eseqb_f_e]
#                                         if eof[0][5]==1:
#                                             etwbetha_e=ebetha_e
#                                         elif eof[0][5]==2:
#                                             etwbetha_e=compmaster(ebetha_e)
#                                         elif eof[0][5]==3:
#                                             etwbetha_e=polimaster(ebetha_e)
#                                         elif eof[0][5]==4:
#                                             etwbetha_e=invertmaster(ebetha_e)
#                                         eerrs=lev(ealpha_e,etwbetha_e)
#                                         elength_e=len(ealpha_e)
#                                         edegen = float ( float(eerrs) / float(elength_e) )
#                                         if edegen>0.4:
#                                             break
#                                         else:
#                                             elimit=elimit+elenglun
#                         if revringexit:
#                             break
#                         if (of[0][5]==1) or (of[0][5]==2):
#                             seqa_s_e=start_a
#                             seqa_f_e=of[0][2]+of[0][4]+gapc
#                             seqb_s_e=start_b
#                             seqb_f_e=of[0][3]+of[0][4]+gapc   
#                             if ring:
#                                 seqa_s_e=start_a
#                                 seqa_f_e=of[0][3]+of[0][4]+gapc
#                                 seqb_s_e=start_b
#                                 seqb_f_e=of[0][2]+of[0][4]+gapc+origlen
#                         elif (of[0][5]==3) or (of[0][5]==4):
#                             seqa_s_e=start_a
#                             seqa_f_e=of[0][2]+of[0][4]+gapc
#                             seqb_s_e=start_b+lenglun
#                             seqb_f_e=of[0][3]-gapc
#                         if seqb_s_e>seqb_f_e:
#                             breakster=True
#                         alpha_e=dougenome[seqa_s_e:seqa_f_e]
#                         betha_e=dougenome[seqb_s_e:seqb_f_e]
#                         if of[0][5]==1:
#                             twbetha_e=betha_e
#                         elif of[0][5]==2:
#                             twbetha_e=compmaster(betha_e)
#                         elif of[0][5]==3:
#                             twbetha_e=polimaster(betha_e)
#                         elif of[0][5]==4:
#                             twbetha_e=invertmaster(betha_e)
#                         errs=lev(alpha_e,twbetha_e)
#                         length_e=len(alpha_e) 
#                         degen = float ( float(errs) / float(length_e) )
#                         if degen>0.4:
#                             for be in arr_be:
#                                 q=("DELETE FROM repeats_gap WHERE id=%s" % (be))
#                                 cur.execute(q)
#                             if of[0][5]==1:
#                                 twbetha=betha_be
#                             elif of[0][5]==2:
#                                 twbetha=compmaster(betha_be)        
#                             elif of[0][5]==3:
#                                 twbetha=polimaster(betha_be)
#                             elif of[0][5]==4:
#                                 twbetha=invertmaster(betha_be)
#                             up=False
#                             length_be=len(alpha_be)
#                             errs=lev(alpha_be,twbetha)
#                             if (alpha_be[:1]!=twbetha[:1]):
#                                 alpha_be=alpha_be[1:]
#                                 astart_be=astart_be+1
#                                 if of[0][5]==1 or of[0][5]==2:
#                                     betha_be=betha_be[1:] 
#                                     bstart_be=bstart_be+1                   
#                                 elif of[0][5]==3 or of[0][5]==4:
#                                     betha_be=betha_be[:length_be-1]      
#                                 twbetha=twbetha[1:]
#                                 length_be=length_be-1
#                                 up=True
#                             if (alpha_be[-1:]!=twbetha[-1:]):
#                                 alpha_be=alpha_be[:length_be-1]
#                                 if of[0][5]==1 or of[0][5]==2:
#                                     betha_be=betha_be[:length_be-1]                    
#                                 elif of[0][5]==3 or of[0][5]==4:
#                                     betha_be=betha_be[1:]        
#                                     bstart_be=bstart_be+1                
#                                 twbetha=twbetha[:length_be-1]
#                                 length_be=length_be-1
#                                 up=True
#                             if up:
#                                 if of[0][5]==1:
#                                     twbetha=betha_be
#                                 elif of[0][5]==2:
#                                     twbetha=compmaster(betha_be)                        
#                                 elif of[0][5]==3:
#                                     twbetha=polimaster(betha_be)
#                                 elif of[0][5]==4:
#                                     twbetha=invertmaster(betha_be)
#                             errs=lev(alpha_be,twbetha)
#                             q=("UPDATE repeats_gap SET length = %s, first_seq = ?, second_seq = ?,alt_second_seq=?, errs = %s, first_start = %s, second_start = %s  WHERE id = %s" % (len(alpha_be),errs,astart_be,bstart_be,start))
#                             cur.execute(q,(alpha_be,betha_be,twbetha))
#                             break
#                         else:
#                             if breakster:
#                                 break    
#                             limit=limit+lenglun
#     in_memory.commit()

#     # Cutting of the mismatched ends of the repeats
#     for r in range(1,alllen+1,1):
#         print("%s\r" % r),
#         q = ("SELECT * FROM repeats_gap WHERE id=%s and length=10" % (r))
#         cur.execute(q)
#         of=cur.fetchall()  
#         if len(of)!=0:
#             starta=of[0][2]
#             startb=of[0][3]
#             alpha=of[0][6]
#             betha=of[0][7]
#             twbetha=of[0][8]
#             length=of[0][4]
#             errs=of[0][9]
#             up=False
#             if twbetha == None:
#                 if of[0][5]==1:
#                     twbetha=betha
#                 elif of[0][5]==2:
#                     twbetha=compmaster(betha)      
#                 elif of[0][5]==3:
#                     twbetha=polimaster(betha)
#                 elif of[0][5]==4:
#                     twbetha=invertmaster(betha)
#                 errs=lev(alpha,twbetha)
#                 up=True
#             if (alpha[:1]!=twbetha[:1]):
#                 alpha=alpha[1:]
#                 starta=starta+1
#                 if of[0][5]==1 or of[0][5]==2:   
#                     betha=betha[1:] 
#                     startb=startb+1                   
#                 elif of[0][5]==3 or of[0][5]==4:
#                     betha=betha[:length-1]      
#                 twbetha=twbetha[1:]
#                 length=length-1
#                 up=True
#             if (alpha[-1:]!=twbetha[-1:]):
#                 alpha=alpha[:length-1]
#                 if of[0][5]==1 or of[0][5]==2:         
#                     betha=betha[:length-1]                             
#                 elif of[0][5]==3 or of[0][5]==4:           
#                     betha=betha[1:]        
#                     startb=startb+1                
#                 twbetha=twbetha[:length-1]
#                 length=length-1
#                 up=True
#             if up:
#                 if of[0][5]==1:
#                     twbetha=betha
#                 elif of[0][5]==2:
#                     twbetha=compmaster(betha)                        
#                 elif of[0][5]==3:
#                     twbetha=polimaster(betha)
#                 elif of[0][5]==4:
#                     twbetha=invertmaster(betha)
#                 errs=lev(alpha,twbetha)
#                 q=("UPDATE repeats_gap SET first_start = %s, second_start = %s, length = %s, first_seq = ?, second_seq = ?, alt_second_seq = ?, errs = %s  WHERE id = %s" % (starta,startb,length,errs,of[0][0]))
#                 cur.execute(q,(alpha,betha,twbetha))
#     q=("DELETE FROM repeats_gap WHERE length < 10")
#     cur.execute(q)

#     in_memory.commit()

#     #Return from RAM to the database file
#     con = sqlite3.connect(path)
#     con.execute('drop table repeats')
#     con.execute('drop table species')
#     for line in in_memory.iterdump():
#         if line == "COMMIT;":
#             break
#         con.execute(line)
#     con.commit()
#     in_memory.close()
#     con.close()