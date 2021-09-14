#!/usr/bin/env python
from csv import reader
import sys
# skip first line (the header)
next(sys.stdin)

for line in reader(sys.stdin):
    boro, crime = (line[13].strip(), line[7].strip())
    if not boro or not crime:
        continue
    print ("%s\t%s" % (boro, crime))

