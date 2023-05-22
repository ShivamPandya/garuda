#!/usr/bin/env python

import hashlib
import subprocess
import sys
import time

def main():

    if len(sys.argv) == 1:
        return("Please pass the python file as command line argument")

    filename = sys.argv[1]
    run_commands(filename)

    with open(filename, "rb") as f:
        checksum = hashlib.md5(f.read()).hexdigest()

    while True:
        try:
            with open(filename, "rb") as f:
                newChecksum = hashlib.md5(f.read()).hexdigest()
            if checksum != newChecksum:
                run_commands(filename)
                checksum = newChecksum
            time.sleep(0.5)
        except KeyboardInterrupt as e:
            sys.exit()


def banner(filename):
    print("\033[32m")
    print("              🦅              ")
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃    Garuda | Live Realod    ┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    print("\033[0m")
    print("Press ctrl+c to exit. Type rs to restart")
    print(f"|-> Currently executing \33[1m\33[33m{filename}\033[0m")
    print("="*(24+len(filename)),"\n")


def run_commands(filename):
    filename = sys.argv[1]
    subprocess.run("clear")
    banner(filename)
    try:
        proc = subprocess.check_output(["python", filename]).decode("utf-8")
        print(f"{proc.strip()}", "\r")
    except subprocess.CalledProcessError as err:
        err = str(err).split("\n")
        err.pop()
        err = ''.join(err)
        print(err)
