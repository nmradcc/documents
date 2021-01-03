#!/usr/bin/env python3

import argparse
import os
import subprocess

parser = argparse.ArgumentParser(description='Gnereate PDF files form MS Word *.docx files')
parser.add_argument("-f", "--force", action="store_true",
                    help="force PDF creation regardless of timestamps")
args = parser.parse_args()

OFFICETOPDF = "../bin/OfficeToPDF.exe"

inputs = []
outputs = []

for file in os.listdir("."):
    if file.startswith("~$"):
        # This is an error artifact, skip it
        continue
    if file.endswith(".docx"):
        # Generate the output file name
        output = file.replace(".docx", ".pdf")
        # test if the output file is out of date
        imod = os.path.getmtime(file)
        omod = 0
        try:
            omod = os.path.getmtime(output)
        except OSError:
            omod = 0
        if omod < imod or args.force:
            # output file is out of date, add it to the list
            inputs.append(file)
            outputs.append(file.replace(".docx", ".pdf"))

i = 0
while i < len(inputs) :
    print("Generating \"" + outputs[i] + "\" from \"" + inputs[i] + "\"")
    p = subprocess.run([OFFICETOPDF, "/readonly", "/print", "/bookmarks", "/excludetags", inputs[i], outputs[i]])
    #if p.returncode != 0:
    #    print("Error: " + str(p.returncode) + ", try again")
    #    try:
    #        os.remove(outputs[i])
    #    except OSError:
    #        pass
    #    continue
    i += 1
