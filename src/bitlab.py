#!/usr/bin/python
import getopt
import os
import sys


def help():
    # TO DO: Add help for creating a venv
    print('Fax, scan and print the internet!')
    return


def cleanup(file):
    try:
        os.remove(file)
    except OSError:
        print('File ' + file + ' doesn\'t exist.')
        return 'Error'
    print('File ' + file + ' has been removed.')
    return 'Done'


class Episodes:
    @staticmethod
    def group_episodes_by_year():
        return None


if __name__ == "__main__":
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(
            argv,
            "h",
            ["help", "cleanup="],
        )
    except getopt.GetoptError:
        print('Invalid options.')
        sys.exit(2)
    if opts:
        for opt, arg in opts:
            if opt in ['-h', '--help']:
                help()
                sys.exit()
            elif opt == '--cleanup':
                cleanup(arg)
                sys.exit()
    else:
        print('Creating the html.')
