#!/usr/bin/python3
"""entry point for command interpretor"""

import cmd
import json
import os
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command exits the program\n"""
        return True

    def do_EOF(self, arg):
        """EOF command exits the program\n"""
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it to the JSON file
        and then prints the id"""
        if arg == "BaseModel":
            newModel = BaseModel()
            newModel.save()
            print(newModel.id)
        elif arg == '':
            print("** class name missing **")
            pass
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """given a class and id, prints the associated objects
        string representation"""
        if arg != '':
            argList = arg.split()
            if len(argList) >= 2:
                if argList[0] == 'BaseModel':
                    if argList[0] + '.' + argList[1] in storage.all():
                        tempModel = storage.all()[argList[0] + '.' + argList[1]]
                        print(tempModel.__str__())
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)."""
        if arg != '':
            argList = arg.split()
            if len(argList) >= 2:
                if argList[0] == 'BaseModel':
                    if argList[0] + '.' + argList[1] in storage.all():
                            del storage.all()[argList[0] + '.' + argList[1]]
                            storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist")
            else:
                print("** instance id missing **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
