import subprocess

bashCmd = 'echo "Hello, World!"'
output = subprocess.check_output(['bash', '-c', bashCmd])
print(output.decode("utf-8"))
