"""Read inert exports only. Freeze a first-divergence witness rather than adjusting either kernel."""
import argparse,hashlib,json
from pathlib import Path


def main():
    p=argparse.ArgumentParser()
    for name in ('historical','current','out'):p.add_argument('--'+name,required=True)
    args=p.parse_args();a=json.loads(Path(args.historical).read_bytes());b=json.loads(Path(args.current).read_bytes())
    def difference(left,right,path=()):
        if type(left) is not type(right):return dict(path=path,historical=left,current=right)
        if isinstance(left,dict):
            if left.keys()!=right.keys():return dict(path=path,historical=list(left),current=list(right))
            for key in left:
                found=difference(left[key],right[key],(*path,key))
                if found:return found
        elif isinstance(left,list):
            if len(left)!=len(right):return dict(path=path,historical=len(left),current=len(right))
            for i,(x,y) in enumerate(zip(left,right)):
                found=difference(x,y,(*path,i))
                if found:return found
        elif left!=right:return dict(path=path,historical=left,current=right)
        return None
    witness=difference(a,b)
    result=dict(status='STOP_UNEXPECTED_DIVERGENCE' if witness else 'PASS',first_divergence=witness,
        one_cases=len(a['one']),multisteps=sum(len(row['steps']) for row in a['multi']),
        comparison='EXACT_HEX_TOKENS_INCLUDING_SIGNED_ZERO',
        historical_sha256=hashlib.sha256(Path(args.historical).read_bytes()).hexdigest(),
        current_sha256=hashlib.sha256(Path(args.current).read_bytes()).hexdigest())
    Path(args.out).write_bytes((json.dumps(result,indent=2)+'\n').encode())
    print(json.dumps(result))
    if witness:raise SystemExit(2)

if __name__=='__main__':main()
