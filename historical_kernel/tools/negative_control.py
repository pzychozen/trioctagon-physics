"""Remove only this external installed candidate, prove tests fail, restore it."""
import argparse,json,os,subprocess,sys
from pathlib import Path


def main():
    p=argparse.ArgumentParser();p.add_argument('--tests',required=True);p.add_argument('--out',required=True);a=p.parse_args()
    import trioctagon_historical_kernel
    package=Path(trioctagon_historical_kernel.__file__).resolve().parent
    prefix=Path(sys.prefix).resolve();assert prefix!=Path(sys.base_prefix).resolve()
    assert package.is_relative_to(prefix) and package.name=='trioctagon_historical_kernel'
    absent=package.with_name('H6B_TEST_ONLY_REMOVED_IMPLEMENTATION');assert not absent.exists()
    assert absent.resolve().is_relative_to(prefix)
    command=[sys.executable,'-I','-B','-m','pytest',str(Path(a.tests)/'test_science.py'),'-q','-p','no:cacheprovider',
             '--rootdir='+a.tests,'--confcutdir='+a.tests]
    try:
        package.rename(absent)
        result=subprocess.run(command,capture_output=True,text=True,cwd=Path(a.out),env=dict(os.environ,PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'))
        assert result.returncode!=0 and 'ModuleNotFoundError' in result.stdout+result.stderr
    finally:absent.rename(package)
    Path(a.out,'negative-control.log').write_text(result.stdout+result.stderr,encoding='utf-8')
    Path(a.out,'negative-control.json').write_text(json.dumps(dict(status='PASS',test_exit=result.returncode,
        failure='ModuleNotFoundError',implementation_restored=package.is_dir(),checkout_mutated=False),indent=2)+'\n')

if __name__=='__main__':main()
