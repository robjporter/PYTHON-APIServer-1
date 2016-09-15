class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    YELLOW = '\033[93m'
    MAGENTA = '\033[95m'
    GREY = '\033[90m'
    BLACK = '\033[90m'
    DEFAULT = '\033[39m'

    def getInfo():
        return colors.WHITE + "INFO: " + colors.DEFAULT

    def getDebug():
        return colors.YELLOW + "DEBUG: " + colors.DEFAULT

    def getWarning():
        return colors.MAGENTA + "WARNING: " + colors.DEFAULT

    def getError():
        return colors.RED + "ERROR: " + colors.DEFAULT
