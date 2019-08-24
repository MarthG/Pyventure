from sys import argv

verbosity = 0
version = "0.01"

def help():
    global verbosity

    if verbosity > 0:
        print("[II] We are verbose")
        print("[II] Stub help()")

    pass

def printVersion():
    global verbosity
    if verbosity > 0:
        print("[II] We are verbose")
    print(
        '''
        [II]
        [II] Version v{0}
        [II]
        '''.format(version)
    )
    pass

def run():
    global verbosity

    if verbosity > 0:
        print("[II] We are verbose")
    print("[II] Stub run()")

    pass

def main(argv=None):
    arg = argv[1:]
    help_arg = ["-h", "-?", "--help"]
    vers_arg = ["-v", "-ver", "--version"]
    verbose = ["-V", "--debug", "--verbose"]

    global verbosity

    # Status bits
    # normal_execution,1 arg_called,2 help_arg,4 vers_arg,8 verbose,16
    status = 0

    # print(arg)

    if len (arg) >= 1:
        status |= 2
        for i in arg:
            if i in help_arg:
                status |= 4
            elif i in vers_arg:
                status |= 8
            elif i in verbose:
                status |= 16
                verbosity = 1
            else:
                print("[EE] Bad arguments. Try {0} for help".format(help_arg[1]))
                return -1
    else:
        status |= 1

    print(verbosity)
    checkStatus(status, help, version, run)

    return 0

def checkStatus(currentStatus=None, helpFunction=None, versionFunction=None, normalRuntime=None):
    # # # # checkStatus(status)
    # Flag: [PRIORITY]
    # Verbosity:        +++
    # Arguments called: +++
    # Help arg:     ++
    # Version arg:  ++
    # Normal:       +
    #
    # Usage: checkStatus( State variable, help f(), version f(), run f())
    global verbosity

    if (helpFunction is None) or (versionFunction is None) or (normalRuntime is None):
        raise Exception("[EE] Exception: Bad function pass")

    if currentStatus != 0 and not currentStatus is None:
        if currentStatus & 2:
            if currentStatus & 4:
                helpFunction()
            elif currentStatus & 8:
                versionFunction()
            else:
                raise Exception("[EE] Exception: Invalid state. Exiting")
        elif currentStatus & 1:
            normalRuntime()

    return 0

if __name__ == '__main__':
    main(argv)
