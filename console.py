#!/usr/bin/python3

"""Interactive shell for Airbnb project."""

import json
import cmd
import sys
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class."""

    prompt = '(hbnb) '
    supported_classes = ["BaseModel"]

    def do_help(self, line):
        """Display help."""
        # Your help logic here

    def do_quit(self, line):
        """Quit the shell."""
        return True

    def default(self, line):
        """Handle unknown syntax."""
        if line == 'EOF':
            sys.exit(0)
        else:
            self.stdout.write('*** Unknown syntax: %s\n' % line)

    def emptyline(self):
        """Handle empty line"""
        pass

    def do_create(self, class_):
        """Creates a new instance of a given class and saves it to a given class"""
        supported_classes = ["BaseModel"]
        if not class_:
            print("** class name missing **")
        elif class_ not in supported_classes:
            print("** class doesn't exist **")
        else:
            instance = BaseModel()
            print(instance.id)
            inst_dict = instance.to_dict()
            with open(file="data.json", mode="w") as data_file:
                json.dump(inst_dict, data_file, indent=4)


if __name__ == '__main__':
    try:
        HBNBCommand().cmdloop()
    except KeyboardInterrupt:
        print("\nExiting...")
