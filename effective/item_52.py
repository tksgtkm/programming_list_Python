import random
random.seed(1234)

import logging
from pprint import pprint
from sys import stdout as STDOUT

import atexit
import gc
import io
import os
import tempfile

TEST_DIR = tempfile.TemporaryDirectory()
atexit.register(TEST_DIR.cleanup)

OLD_CWD = os.getcwd()
atexit.register(lambda: os.chdir(OLD_CWD))
os.chdir(TEST_DIR.name)

def close_open_files():
    everything = gc.get_objects()
    for obj in everything:
        if isinstance(obj, io.IOBase):
            obj.close()

atexit.register(close_open_files)

import subprocess

result = subprocess.run(
    ['echo', 'Hello from the child!'],
    capture_output=True,
    encoding='utf-8'
)

result.check_returncode()
print(result.stdout)

proc = subprocess.Popen(['sleep', '1'])
while proc.poll() is None:
    print('Working...')
    import time
    time.sleep(0.3)

print('Exit status', proc.poll())

import time

start = time.time()
sleep_procs = []
for _ in range(10):
    proc = subprocess.Popen(['sleep', '1'])
    sleep_procs.append(proc)

def run_encrypt(data):
    env = os.environ.copy()
    env['password'] = 'zf7ShyBhZOraQDdE/FiZpm/m/8f9X+M1'
    proc = subprocess.Popen(
        ['openssl', 'enc', '-des3', '-pass', 'env:password'],
        env=env,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE
    )
    proc.stdin.write(data)
    proc.stdin.flush()
    return proc

procs = []
for _ in range(3):
    data = os.urandom(10)
    proc = run_encrypt(data)
    procs.append(proc)

for proc in procs:
    out, _ = proc.communicate()
    print(out[-10:])