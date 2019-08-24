import argparse

verbosity = False
version = "0.01"

def verbose(message):
    # message: String
    global verbosity
    if verbosity:
        print(message)

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
    global verbosity

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

    print("Verbose Level: " + str(verbosity))
    verbose("[II] Current Status: {0}".format(status))
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
    if (helpFunction is None) or (versionFunction is None) or (normalRuntime is None):
        raise Exception("[EE] Exception: Bad function pass")

    if currentStatus != 0 and not currentStatus is None:
        if currentStatus & 2:
            if currentStatus & 8:
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
