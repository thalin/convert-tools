import csv
import os
import logging

logging.basicConfig(level=logging.INFO)

inf = "203samples_genotypes_FinalReport.csv"
outf = "203samples_genotypes_FinalReport.lgen"
#inf = "test_samples.csv"
#outf = "test_samples.lgen"
inf_obj = open(inf)

logging.info("Reading file %s into memory..." % inf)
in_lines = inf_obj.readlines()
inf_obj.close()

in_lines = in_lines[10:]

outf_obj = open(outf, "w")

logging.info("Reformatting & writing to %s..." % outf) 
for line in in_lines:
    fields = line.split(",")
    outf_obj.write("%s 1 %s %s %s\n" % (fields[1], fields[0], fields[2], fields[3]))

outf_obj.close()    
