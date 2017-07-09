#!/usr/bin/env python

from argparse import *
from xml.etree import ElementTree
from os import makedirs, path

parser = ArgumentParser(description="Type command")
parser.add_argument("command")
parser.add_argument("--project", default="None")
parser.add_argument("--task", default=0, type=int)

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

        status = ""
        if task.get("status") == "Completed":
            status = "\x1b[6;30;42m" + "Completed!" + "\x1b[0m"
        if task.get("status") == "Progress":
            status = "\x1b[7;31;40m" + "In progress.." + "\x1b[0m"

        if given_project != "None":
            if project == given_project:
                print(str(iterator) + ": " + str(task.text) + " : " + status)
        elif project == "None":
            project = ""
            print(str(iterator) + ": " + str(task.text) + " : " + str(project) + " : " + status)

if arguments.command == "init":
    if not path.exists(path.expanduser("~") + "/.nickel"):
        makedirs(path.expanduser("~") + "/.nickel")

    root = ElementTree.Element("root")

    tree = ElementTree.ElementTree(root)
    tree.write(path.expanduser("~") + "/.nickel/tasks.xml")

    print('\x1b[6;30;42m' + 'Path initialized!' + '\x1b[0m')

elif arguments.command == "remove":
    if arguments.task == 0:
        print("Add --task argument!")
    else:
        tree = ElementTree.parse(path.expanduser("~") + "/.nickel/tasks.xml")
        root = tree.getroot()

        iterator = 0
        for task in root.findall("task"):
            iterator += 1
            if iterator == arguments.task:
                root.remove(task)
                tree.write(path.expanduser("~") + "/.nickel/tasks.xml")
                print('\x1b[6;30;42m' + 'Removed!' + '\x1b[0m')
                break

elif arguments.command == "complete":
    if arguments.task == 0:
        print("Add --task argument!")
    else:
        tree = ElementTree.parse(path.expanduser("~") + "/.nickel/tasks.xml")
        root = tree.getroot()

        iterator = 0
        for task in root.findall("task"):
            iterator += 1
            if iterator == arguments.task:
                task.set("status", "Completed")
                tree.write(path.expanduser("~") + "/.nickel/tasks.xml")
                print('\x1b[6;30;42m' + 'Completed!' + '\x1b[0m')
                break

elif arguments.command == "add":
    tree = ElementTree.parse(path.expanduser("~") + "/.nickel/tasks.xml")
    root = tree.getroot()

    new_task = ElementTree.Element("task", {"project": arguments.project, "status": "Progress"})
    new_task.text = raw_input("Type new task: ")
    root.append(new_task)
    tree.write(path.expanduser("~") + "/.nickel/tasks.xml")
    print('\x1b[6;30;42m' + 'Added!' + '\x1b[0m')

elif arguments.command == "undone":
    if arguments.task == 0:
        print("Add --task argument!")
    else:
        tree = ElementTree.parse(path.expanduser("~") + "/.nickel/tasks.xml")
        root = tree.getroot()

        iterator = 0
        for task in root.findall("task"):
            iterator += 1
            if iterator == arguments.task:
                task.set("status", "Progress")
                tree.write(path.expanduser("~") + "/.nickel/tasks.xml")
                print('\x1b[6;30;42m' + 'Completed!' + '\x1b[0m')
                break
