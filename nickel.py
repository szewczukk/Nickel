#!/usr/bin/env python

from argparse import *

parser = ArgumentParser(description="Type command")
parser.add_argument("command", help="\"check\" for print all tasks or \"add\" to add new task")

arguments = parser.parse_args()
if arguments.command == "check":
    print ("Check")

elif arguments.command == "add":
    print ("Adding")
