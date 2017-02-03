import os, errno


# SilentRemove - removes the file, if the file doesnt exist then skips the exception
# Useful at the initialisation of the program, to delete the previosuly created files
def SilentRemove(filename):
    try:
        os.remove(filename)
    except OSError as e: # this would be "except OSError, e:" before Python 2.6
        if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
            raise # re-raise exception if a different error occured