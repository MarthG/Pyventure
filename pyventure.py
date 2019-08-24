import argparse

verbosity = False
version = "0.01"


def verbose(message):
    # message: String
    global verbosity
    if verbosity:
        print(message)
    

def help(cmds=None, command_descriptions=None):
    if (cmds is None) or (command_descriptions is None):
        raise Exception("[EE] Exception: Can't display help message, something went wrong.")

    verbose("[II] We are verbose")

def printVersion():
    verbose("[II] We are verbose")
    
    print(
        "[II]\n" +
        "[II] Version v{0}\n".format(version) +
        "[II]"
    )
    # print("[II] Version v{0}".format(version))


def run():
    verbose("[II] We are verbose")
    print("[II] Stub run()")

def main(argv=None):
    arg = argv[1:]

    help_arg = ["-h", "-?", "--help"]
    vers_arg = ["-v", "-ver", "--version"]
    verbose = ["-V", "--debug", "--verbose"]

    # I know this is \extremely/ inelegant, but it works.
    descriptions = {str(help_arg): "help", str(vers_arg): "version", str(verbose): "debug"}

    cmds = [help_arg, vers_arg, verbose]
    

    # Status bits
    # normal_execution,1 arg_called,2 help_arg,4 vers_arg,8 verbose,16
    status = 0

    # print(arg)
    if argv.verbose == True:
        verbosity = True
        status |= 16
    
    elif argv.version:
        status |= 8

    else:
        status |= 1

    verbose("[II] Current Status: {0}".format(status))
    checkStatus(status, help, version, run, cmds, descriptions)

    return 0


def checkStatus(currentStatus=None, helpFunction=None, versionFunction=None, normalRuntime=None, cmds=None, descriptions=None):
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

    if (helpFunction is None):
        raise Exception("[EE] Exception: Bad help()")
    if (versionFunction is None):
        raise Exception("[EE] Exception: Bad version()")
    if (normalRuntime is None):
        raise Exception("[EE] Exception: Bad runtime")




    if currentStatus != 0 and not currentStatus is None:
        if currentStatus & 2:
            if currentStatus & 4:
                helpFunction(cmds, descriptions)
            elif currentStatus & 8:
                printVersion()
            else:
                raise Exception("[EE] Exception: Invalid state. Exiting")
        elif currentStatus & 1:
            normalRuntime()

    return 0


if __name__ == '__main__':
    # Setup arguments
    parser = argparse.ArgumentParser(description='Pyventure by MarthG')
    parser.add_argument("-V", "--verbose", "--debug", action='store_true', help='Show verbose messages')
    parser.add_argument("-v", "--version", action='store_true', help='Show version number')
    argsv = parser.parse_args()
    main(argsv)
