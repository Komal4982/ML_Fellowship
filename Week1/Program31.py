import subprocess

get_output = subprocess.run(['ls', '-1'], stdout=subprocess.PIPE).stdout.decode('utf-8')

print("list cmd \n", get_output)
