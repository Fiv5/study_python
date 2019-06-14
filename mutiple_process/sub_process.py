import subprocess
print('$ ls -l')
r = subprocess.call(['ls', '-l'])
print('Exit code: : %s' % r)

print('$ test python command')
p = subprocess.Popen(
    ['node'],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)
output, err = p.communicate(b'console.log("cxk, nmsl")\n1+1\n.exit\n')
print(output.decode('utf-8'))
print(err)
print('Exit code: %s' % p.returncode)
