import subprocess
counter=254
counter += 1
if counter==255:
	subprocess.call(["sudo", "shutdown", "-h", "now"])
