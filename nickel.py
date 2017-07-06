#!/usr/bin/env python

from argparse import *
from xml.etree import ElementTree
from os import makedirs, system, path

parser = ArgumentParser(description="Type command")
parser.add_argument("command", help="\"check\" for print all tasks or \"add\" to add new task")

arguments = parser.parse_args()
if arguments.command == "check":
    tree = ElementTree.parse("/home/.nickel/tasks.xml")
    root = tree.getroot()
    iterator = 0

    print("Here is all tasks created:")
    for task in root.findall("task"):
        iterator += 1
        print(str(iterator) + "        " + task.text)

if arguments.command == "init":
    if not path.exists("/home/.nickel"):
        makedirs("/home/.nickel")

    with open("/home/.nickel/tasks.xml", "w") as f:
        f.write("<?xml version=\"1.0\"?>\n<tasks> \n</tasks>")

    print("Path initialized!")
elif arguments.command == "add":
    tree = ElementTree.parse("/home/.nickel/tasks.xml")
    root = tree.getroot()

    task = ElementTree.SubElement(root, "task")
    task.text = raw_input()
