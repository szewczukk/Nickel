#!/usr/bin/env python

from argparse import *
from xml.etree import ElementTree
from os import makedirs, path

parser = ArgumentParser(description="Type command")
parser.add_argument("command")
parser.add_argument("project")

arguments = parser.parse_args()
if arguments.command == "check":
    tree = ElementTree.parse(path.expanduser("~") + "/.nickel/tasks.xml")
    root = tree.getroot()
    iterator = 0

    print("Here is all tasks created:")
    for task in root.findall("task"):
        iterator += 1

        project = str(task.get("project"))
        given_project = arguments.project

        print(given_project)

        if project != "None":
            print(str(iterator) + ": " + task.text + " : " + project)
        else:
            print(str(iterator) + ": " + task.text + " : ")

if arguments.command == "init":
    if not path.exists(path.expanduser("~") + "/.nickel"):
        makedirs(path.expanduser("~") + "/.nickel")

    root = ElementTree.Element("root")

    tree = ElementTree.ElementTree(root)
    tree.write(path.expanduser("~") + "/.nickel/tasks.xml")

    print("Path initialized!")
elif arguments.command == "add":
    tree = ElementTree.parse(path.expanduser("~") + "/.nickel/tasks.xml")
    root = tree.getroot()

    new_task = ElementTree.Element("task", {"project": arguments.project})
    new_task.text = raw_input("Type new task: ")
    root.append(new_task)
    tree.write("/home/User/.nickel/tasks.xml")
