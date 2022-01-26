import re
import os,glob, sys

found_match = 0

def replacefunc(matchobj):
	global found_match
	found_match = 1
	res = "mysqli_query("
	if matchobj.group(4) is not None:
		return (res + matchobj.group(4) + ", " + matchobj.group(2) + ")")
	else:
		return (res + "$cn, " + matchobj.group(2) + ")")


if len(sys.argv) != 2:
	print("\n Expects one input parameter: Directory location of source files")
	exit()

folder_path = sys.argv[1]
for filename in glob.glob(os.path.join(folder_path, '*')):
	with open(filename, 'r') as f:
		filetext = f.read()
		found_match = 0
		pattern = "(mysql_query)\s*\(([\"']\w+[\"']|\$\w+)(,\s*(\$\w+))?\)"
		p = re.compile(pattern, re.IGNORECASE)
		resulttext = re.sub(p, replacefunc, filetext)
		f.close()
		if found_match == 1:
			with open(filename, 'w') as f:
				f.write(resulttext)
				f.close()