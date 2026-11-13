from common import *
tag,script,*args=sys.argv[1:]
r=run([sys.executable,'-B',str(R/'scripts'/script),*args],tag,check=False)
print(r.stdout.decode('utf-8',errors='replace'),end='')
if r.stderr:print(r.stderr.decode('utf-8',errors='replace'),file=sys.stderr,end='')
raise SystemExit(r.returncode)
