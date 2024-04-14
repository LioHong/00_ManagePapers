# -*- coding: utf-8 -*-
"""
Filename: read_contents.py
Date created: 2024/04/06, Sat, 22:10:11 (UTC+8)
@author: Julio Hong
Purpose: Read contents of XX_Papers folder on current device.
Steps: 
1. Check folder structure (proxy for device identity).
2. Choose output path.
3. List directories in XX_Papers folder (should be super-folder).
4. Write to output path.
5. Compare two different output paths and return diff.
"""
from pathlib import Path
from difflib import unified_diff
# Check folder structure (proxy for device identity).
# https://stackoverflow.com/questions/55516779/how-to-move-up-n-directories-in-pythonic-way
cwd_p = Path.cwd()
grandparent = cwd_p.parents[1].name
dpath = Path(".") / "desktop.txt"
lpath = Path(".") / "laptop.txt"
# Choose output path.
if grandparent == "00_My Files":
    op_path = dpath
elif grandparent == "Documents":
    op_path = lpath
else:
    print("Old grandparents missing. Is this a new device?")

# List directories in XX_Papers folder (should be super-folder).
pfiles = cwd_p.parent.glob("**/*")
# Too-long filenames cause issues, so I compressed the offending webpage.
papers = [str(p).split(cwd_p.parent.name+'\\')[1] for p in pfiles if p.is_file()]
# Exclude 00_PapersMgmt folder itself.
papers = [p for p in papers if cwd_p.name not in p]
op_path.write_text("\n".join(papers), encoding="utf-8")

# Compare different output paths and return diff. Desktop as default.
udf = unified_diff(dpath.read_text(encoding="utf-8").splitlines(),lpath.read_text(encoding="utf-8").splitlines(),lineterm='')
print('\n'.join(list(udf)))
