import sys

total = 0
for argument in sys.argv[1:]:
    int_argv = int(argument)
    total +=int_argv
    print(total)
