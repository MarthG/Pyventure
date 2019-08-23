from sys import argv

def main(argv=None):
    arg = argv[1:]
    help_arg = ["-h", "-?", "--help"]
    vers_arg = ["-v", "-ver", "--version"]

    # Status bits
    # normal_execution,1 arg_called,2 help_arg,4 vers_arg,8
    status = 0
    if len (arg) >= 1:
        status |= 2
        for i in arg:
            if i in help_arg:
                status |= 4
            elif i in vers_arg:
                status |= 8
            else:
                print("Bad arguments. Try {0} for help".format(help_arg[1]))
                return -1
    else:
        status |= 1

    checkStatus(status)

    return 0

def checkStatus(currentStatus=None):
    if (currentStatus is None):
        pass

    return 0

if __name__ == '__main__':
    main(argv)
