import sys
if len(sys.argv) > 1:
    arguments = ' '.join(sys.argv[1:]).split()
    for arg in arguments:
        print(arg)
else:
    print("No arguments.")
