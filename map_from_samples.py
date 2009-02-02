inf_name = "Genotypes_203 samples/Human610-quad_Gene_Annotation.csv"
outf_name = "203samples_genotypes_FinalReport.map"
inf = open(inf_name)

lines = inf.readlines()

lines = lines[1:]

outf = open(outf_name, "w")

for line in lines:
    fields = line.split(",")
    outf.write("%s %s 0 %s\n" % (fields[1],fields[0],fields[2]))
