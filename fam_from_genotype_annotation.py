import csv

excl_name = "to_exclude.txt"
inf_name = "Samples annotation/203_samples_genotyping_annotation.csv"
outf_name = "203samples_genotypes_FinalReport.fam"

excl = open(excl_name)
excludes = excl.readlines()
excludes = [a.strip() for a in excludes]
excl.close()
print excludes

inf = open(inf_name)
reader = csv.reader(inf)

outf = open(outf_name, "w")

reader.next()
for fields in reader:
    famid = fields[0]
    if famid not in excludes:
        indid = "1"
        if fields[3] == "M":
            sex = 1
        elif fields[3] == "F":
            sex = 2
        line = "%s 0 0 %s %s 0\n" % (famid,indid,sex)
        outf.write(line)

