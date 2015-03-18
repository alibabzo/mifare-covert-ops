#
# Once we've collected some UIDs, we need to clean up the database to make sure
# we don't have any duplicates. Duplicates aren't any good, so delete them.
#

#!/usr/bin/python
import csv

with open('uid.csv','r') as in_file, open('uid-clean.csv','w') as out_file:
  seen = set() # set for fast O(1) amortized lookup
  for line in in_file:
    if line in seen: continue # skip duplicate

    seen.add(line)
    out_file.write(line)
