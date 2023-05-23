#!/usr/bin/env python

import hashlib
import subprocess
import sys
import time

from .languages import get_interpreter

def main():

    if len(sys.argv) == 1:
        return("Please pass the file as command line argument")

    filename = sys.argv[1]
    interpreter, filename, compile = get_interpreter(filename)

    run_commands(interpreter, filename, compile)

    with open(filename, "rb") as f:
        checksum = hashlib.md5(f.read()).hexdigest()

    while True:
        try:
            with open(filename, "rb") as f:
                newChecksum = hashlib.md5(f.read()).hexdigest()
            if checksum != newChecksum:
                run_commands(interpreter, filename, compile)
                checksum = newChecksum
            time.sleep(0.5)
        except KeyboardInterrupt as e:
            sys.exit()


def banner(filename:str):
   
    print("\033[32m")
    print("              🦅              ")
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃    Garuda | Live Reload    ┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    print("\033[0m")
    print("Press ctrl+c to exit.")
    print(f"|-> Currently executing \33[1m\33[33m{filename}\033[0m")
    print("="*(24+len(filename)),"\n")


def run_commands(interpreter:list, filename:str, compile:bool):
    
    filename = sys.argv[1]
    subprocess.run("clear")
    banner(filename)
    interpreter.extend([filename])
    
    try:
        proc = subprocess.check_output(interpreter).decode("utf-8")
        print(f"{proc.strip()}", "\r")
        if compile:
            # Running the binary 
            binary = filename.split(".")[0]
            try:
                proc = subprocess.check_output([f"./{binary}"]).decode("utf-8")
                print(f"{proc.strip()}", "\r")
            except FileNotFoundError as err:
                print("Binary not found. Make sure you are in the same directory as that of your file")
    except subprocess.CalledProcessError as err:
        err = str(err).split("\n")
        err.pop()
        err = ''.join(err)
        print(err)
