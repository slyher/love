import sys
import datetime
import getopt


def print_manpage():
    print("""LOVE(1) User Commands LOVE(1)

NAME
       love - listing objects very efficiently

SYNOPSIS
       love [OPTION]... [FILE]...

DESCRIPTION
       love lists objects efficiently.

       When invoked without arguments, love reminds you that
       not everything needs parameters.

       Love is recursive.
       Love respects permissions.
       Love never follows broken symlinks.

EXIT STATUS
       0 if love was found
       1 otherwise

AUTHOR
       Written with ❤️ for Unix users.

SEE ALSO
       ls(1), tree(1), find(1), fortune(6)
""")


def easter_egg():
    month = datetime.datetime.now().month

    if month == 12:
        print("""
❤️ Ho ho ho! ❤️
Love is like a good folder:
– sometimes hidden,
– sometimes nested,
– but always worth recursion

Merry Christmas and a lot of ❤️ at ~/
""")
    elif month == 2:
        print("""
❤️❤️❤️ Valentines ❤️❤️❤️
love doesn't need parameters.
""")
    else:
        print("No arguments given.\nBut love doesn't need parameters ❤️")


def show_love():
    print("""
You are loved.
Even if your code doesn't compile today ❤️
    """)


if __name__ == "__main__":
    input_file = None
    output_file = None
    try:
        opts, args = getopt.getopt(sys.argv[1:], "f:o:h:", [
                                   "file=", "output=", "show-love", "help"])
    except getopt.GetoptError as err:
        print(f"Error: {err}")
        sys.exit(1)
    for opt, arg in opts:
        if opt in ("-f", "--file"):
            print(f"Input file: {arg}")
            input_file = arg
        elif opt in ("-o", "--output"):
            print(f"Output file: {arg}")
            output_file = arg
        elif opt in ("--show-love"):
            show_love()
            sys.exit(0)
        elif opt in ("-h", "--help"):
            print_manpage()
            sys.exit(0)
    if len(sys.argv) == 1:
        easter_egg()
    elif input_file == None or output_file == None:
        print(f"Error: No input and output parameter found")
        sys.exit(1)
    else:
        # program execucion
        sys.exit(0)
