#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 18, 2016
# Ref       : http://stackoverflow.com/questions/10964444/how-can-i-add-a-new-line-of-text-at-top-of-a-file

# Imports
from __future__ import print_function
import fileinput

shebang = "#!/usr/bin/env python"
with open('a.py', "r+") as f:
    first_line = f.readline()
    if first_line != "#!/usr/bin/env python":
        lines = f.readlines()
        f.seek(0)
        f.write(shebang+ "\n")
        f.write(first_line)
        f.writelines(lines)
