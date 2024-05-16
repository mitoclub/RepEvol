f = open('D:\da\Selected.fa', 'r+')
nenado = ["Homo_sapiens", 'Pan_troglodytes', 'Gorilla_gorilla', 'Heterocephalus_glaber', 'Bos_taurus', 'Sus_scrofa_domesticus',
         'Panthera_leo', 'Felis_catus', 'Canis_lupus', 'Canis_lupus_familiaris', 'Loxodonta_africana', 'Balaenoptera_musculus',
         'Delphinus_capensis']
counter = 0
i = 0
while counter != 26:
    for line in f:
        for nenado[i] in nenado:
            if nenado[i] in line:
                line.replace('', '')
                next(f).replace('', '')
                counter += 1
                i = i + 1
            else:
                next(f)
                i += 1
print(f.read())
