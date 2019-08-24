from sys import argv

verbosity = 0
version = "0.01"

def help(cmds=None, command_descriptions=None):
    global verbosity

    if (cmds is None) or (command_descriptions is None):
        raise Exception("[EE] Exception: Can't display help message, something went wrong.")

    if verbosity > 0:
        print("[II] We are verbose")

    print("[II] Stub help()")

    for command in cmds:
        #print(command)
        print("[II] {0}: {1}".format(command, command_descriptions[str(command)]))
    pass


def version():
    global verbosity
    global version

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

    return 0


def main(argv=None):
    arg = argv[1:]

    help_arg = ["-h", "-?", "--help"]
    vers_arg = ["-v", "-ver", "--version"]
    verbose = ["-V", "--debug", "--verbose"]

    # I know this is \extremely/ inelegant, but it works.
    descriptions = {str(help_arg): "help", str(vers_arg): "version", str(verbose): "debug"}

    cmds = [help_arg, vers_arg, verbose]

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

    # print(verbosity)
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
    a = currentStatus

    global verbosity

    if (helpFunction is None):
        raise Exception("[EE] Exception: Bad help()")
    if (versionFunction is None):
        raise Exception("[EE] Exception: Bad version()")
    if (normalRuntime is None):
        raise Exception("[EE] Exception: Bad runtime")



    if (a != 0) and (not a is None):
        if (a & 2):
            if (a & 4):
                helpFunction(cmds, descriptions)
                return 0
            elif (a & 8):
                versionFunction()
                return 0
            else:
                raise Exception("[EE] Exception: Invalid state. Exiting")
        elif (a & 1):
            normalRuntime()

    return 0


if __name__ == '__main__':
    main(argv)
