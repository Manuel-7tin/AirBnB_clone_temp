#!/usr/bin/python3

"""Interactive shell for Airbnb project."""

import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class."""

    prompt = '(hbnb) '

    def do_help(self, line):
        """Display help."""

    def do_quit(self, line):
        """Quit the shell."""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()

