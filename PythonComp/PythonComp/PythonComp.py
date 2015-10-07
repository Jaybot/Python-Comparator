#!/usr/bin/env python
# Author: Jan-Erik Bolz | Life and Brain GmbH | 2015-10-21 | GPU-Licence



# additional imports:

import os
import time

# necessary import:

import difflib


with open(f1path, 'rU') as f1:
    with open(f2path, 'rU') as f2:
        readable_last_modified_time1 = time.ctime(os.path.getmtime(f1path)) # not required
        readable_last_modified_time2 = time.ctime(os.path.getmtime(f2path)) # not required
        print(''.join(difflib.unified_diff(
          f1.readlines(), f2.readlines(), fromfile=f1path, tofile=f2path, 
          fromfiledate=readable_last_modified_time1, # not required
          tofiledate=readable_last_modified_time2, # not required
          )))


# EOF