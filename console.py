#!/usr/bin/python3
"""entry point for command interpretor"""

import cmd
import json
import os
from models.base_model import BaseModel
from models import storage
from models.helpers import classDict


class HBNBCommand(cmd.Cmd):
    """this class serves as my console"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command exits the program\n"""
        return True

    def do_EOF(self, arg):
        """EOF command exits the program\n"""
        print()
        raise SystemExit()

    def emptyline(self):
        """passes an empty line entry"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it to the JSON file
        and then prints the id"""
        if arg in classDict.keys():
            newModel = classDict[arg]()
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
                if argList[0] in classDict.keys():
                    if argList[0] + '.' + argList[1] in storage.all():
                        tempModel = storage.all()[argList[0] +
                                                  '.' + argList[1]]
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
                if argList[0] in classDict.keys():
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

    def do_all(self, arg):
        """shows every instance of objects"""
        argList = arg.split()
        if len(argList) > 0:
            if argList[0] in classDict:
                for key, value in storage.all().items():
                    tempObj = storage.all()[key]
                    print(tempObj.__str__())
            else:
                print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                tempObj = storage.all()[key]
                print(tempObj.__str__())

    def do_update(self, arg):
        """updates an attribute of a given class"""
        argList = arg.split()
        if len(argList) >= 4:
            if argList[0] in classDict.keys():
                if argList[0] + '.' + argList[1] in storage.all().keys():
                    tempObj = storage.all()[argList[0] + '.' + argList[1]]
                    argF = argList[3]
                    for key, value in storage.all().items():
                        for attName, attVal in value.to_dict().items():
                            if argList[2] == attName:
                                if type(value) is int:
                                    argF = int(argList[3])
                                if type(value) is float:
                                    argF = float(argList[3])
                                else:
                                    argfS = slice(1, -1)
                                    argF = (argList[3])[argfS]
                    setattr(tempObj, argList[2], argF)
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        else:
            if len(argList) == 3:
                print("** value missing **")
            elif len(argList) == 2:
                print("** attribute name missing **")
            elif len(argList) == 1:
                print("** instance id missing **")
            elif len(argList) == 0:
                print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
