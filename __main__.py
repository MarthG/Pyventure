from sys import argv

def main(argv=None):
    if len(argv) <= 1:
        raise Exception("Null arguments")
        return -1
    print("argc: {0}\nargv: {1}".format(len(argv)-1, argv))
    return 0

if __name__ == '__main__':
    main(argv)
