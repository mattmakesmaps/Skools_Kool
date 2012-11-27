__author__ = 'matt'

import string.
clean = []

for line in open('J:/274 TANANA TRIBAL COUNCIL/274B Former IHS Hospital Remediation/274B6 Tanana Soil Removal/Analytical Data/Lab Data for Validation/EnvD_Import/SGS_Column_Names.txt'):
    if chr(line) not in string.whitespace:
        pass
    line.strip()
    if len(line) > 0:
        clean.append(line)

print clean
