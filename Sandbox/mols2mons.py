#!/usr/bin/env python

import re
import os

# ==================================================================
#def mols2mons():
def main():
    """Takes molecules and filters and a list of proximity to the center of the supercell, generated by the proximity() function.
    Writes new files with molecules indexed by increasing proximity to the center of the supercell."""

    directory = os.getcwd()
    molfiles = os.listdir(directory)
    monidx = 0

    for file in molfiles:

        if re.match('^m[0-9]+.xyz$', file): # Match filenames with pattern
            monidx += 1
            monfname = "1-" + str(file)[1:]

            with open(file, 'r') as moleculef, open(monfname, 'w') as monomerf:

                for l in moleculef.readlines():

                    if l.startswith("Molecule"):
                        newl = "Monomer " + str(monidx) + "\n"
                        monomerf.write(newl)

                    else:
                        monomerf.write(l)

            os.remove(os.path.join(directory, file))

            print("Molecule " + str(file) + " has been rewritten to: " + str(monfname))

    print("")

    return
# ==================================================================

if __name__ == "__main__":
    main()