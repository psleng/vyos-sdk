#!/usr/bin/env python3
#
#    Copyright (C) 2019 VyOS maintainers <maintainers@vyos.net>
#
#    This library is free software; you can redistribute it and/or
#    modify it under the terms of the GNU Lesser General Public
#    License as published by the Free Software Foundation; either
#    version 2.1 of the License, or (at your option) any later version.
#
#    This library is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with this library; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
#    USA
#
#    Checks capitalization of abbreviations/acronyms.
#    In the style file, they should be given one per line,
#    correctly capitalized.

import re
import sys

if len(sys.argv) < 3:
    print("Usage: {0} <style file> <target file>")
    sys.exit(1)

line_no = 1
# Assume success until proven otherwise
exit_code = 0

# Get the style data
with open(sys.argv[1], 'r') as f:
    abbr_list = f.readlines()
abbr_list = map(lambda s: s.strip(), abbr_list)

abbrs = {}
for a in abbr_list:
    abbrs[a.lower()] = a

with open(sys.argv[2], 'r') as f:
    for line in f:
        words = re.split(r'\s+', line)
        for w in words:
            wl = w.lower()
            if (wl in abbrs) and (w != abbrs[wl]):
                print("Line {0}: Incorrect capitalization of {1} ({2})!".format(line_no, abbrs[wl], w))
                print(line)
                exit_code = 1
        line_no += 1

sys.exit(exit_code)

