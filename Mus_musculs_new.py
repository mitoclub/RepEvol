nenado = ["Homo_sapiens", 'Pan_troglodytes', 'Gorilla_gorilla', 'Heterocephalus_glaber', 'Bos_taurus', 'Sus_scrofa_domesticus',
         'Panthera_leo', 'Felis_catus', 'Canis_lupus', 'Canis_lupus_familiaris', 'Loxodonta_africana', 'Balaenoptera_musculus',
         'Delphinus_capensis']
f = ["Homo_sapiens", 'Pan_troglodytes', 'mus_musculs', 'Gorilla_gorilla', 'Heterocephalus_glaber', 'Bos_taurus', 'Sus_scrofa_domesticus',
         'Panthera_leo', 'Felis_catus', 'Canis_lupus', 'Canis_lupus_familiaris', 'Loxodonta_africana', 'Balaenoptera_musculus',
         'Delphinus_capensis']
a = open('Selected.fa', 'r+')
counter = 0
i = 0
while counter != 14:
    #for line in f:
        for n in nenado:
            line = f[i]
            #i = i + 1
            if n == line:
                f.remove(line)
                nenado.remove(line)
                counter += 1
                #i = i + 1
                break
            else:
                i += 1
                #f[i]
                counter += 1
                break
else:
    print(f)
    lines = a.readlines()[3:4]
    print(lines)
a.close()
a = open('Selected.fa', 'w')
f = ' '.join(f)
lines = ' '.join(lines)
a.write(f)
a.write(lines)
print(a.read())