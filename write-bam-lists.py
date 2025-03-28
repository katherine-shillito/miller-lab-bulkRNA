import pandas as pd

# Ischemic BAM List

isch_mdf = "/metadata/metadata_ischemic.txt"
isch_bamlist = "/bam_files/ischemic_bam_list.txt"

new_isch_mdf = pd.read_csv(isch_mdf, sep="\t")
#print(new_isch_mdf)
#print(new_isch_mdf.columns)

import os
if os.path.exists("/bam_files/ischemic_bam_list.txt"):
    print("File exists")
else:
    print("File does not exist")


with open(isch_bamlist, "w") as f:
    for index, row in new_isch_mdf.iterrows():
        sample_id = row['SampleID']
        bam_file_name = sample_id + "_Aligned.sortedByCoord.out.bam"
        f.write(bam_file_name + "\n")


with open(isch_bamlist, "r") as f:
    print(f.read())
        
print("file created successfully")



# Control BAM List

ctrl_mdf = "/metadata/metadata_control.txt"
ctrl_bamlist = "/bam_files/control_bam_list.txt"

new_ctrl_mdf = pd.read_csv(ctrl_mdf, sep="\t")
#print(new_ctrl_mdf)
#print(new_ctrl_mdf.columns)

import os
if os.path.exists("/bam_files/control_bam_list.txt"):
    print("File exists")
else:
    print("File does not exist")


with open(ctrl_bamlist, "w") as f:
    for index, row in new_ctrl_mdf.iterrows():
        sample_id = row['SampleID']
        bam_file_name = sample_id + "_Aligned.sortedByCoord.out.bam"
        f.write(bam_file_name + "\n")


with open(ctrl_bamlist, "r") as f:
    print(f.read())
        
print("file created successfully")
