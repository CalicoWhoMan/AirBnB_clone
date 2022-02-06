#!/usr/bin/python3
"""entry point for command interpretor"""

import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
