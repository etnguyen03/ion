# Stubs for pysftp (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def st_mode_to_int(val): ...

class ConnectionException(Exception):
    message = ... # type: Any
    def __init__(self, host, port): ...

class CredentialException(Exception):
    message = ... # type: Any
    def __init__(self, message): ...

class WTCallbacks:
    flist = ... # type: Any
    dlist = ... # type: Any
    ulist = ... # type: Any
    def __init__(self): ...
    def file_cb(self, pathname): ...
    def dir_cb(self, pathname): ...
    def unk_cb(self, pathname): ...

class Connection:
    def __init__(self, host, username=None, private_key=None, password=None, port=22, private_key_pass=None, ciphers=None, log=False): ...
    @property
    def pwd(self): ...
    def get(self, remotepath, localpath=None, callback=None, preserve_mtime=False): ...
    def get_d(self, remotedir, localdir, preserve_mtime=False): ...
    def get_r(self, remotedir, localdir, preserve_mtime=False): ...
    def getfo(self, remotepath, flo, callback=None): ...
    def put(self, localpath, remotepath=None, callback=None, confirm=True, preserve_mtime=False): ...
    def put_d(self, localpath, remotepath, confirm=True, preserve_mtime=False): ...
    def put_r(self, localpath, remotepath, confirm=True, preserve_mtime=False): ...
    def putfo(self, flo, remotepath=None, file_size=0, callback=None, confirm=True): ...
    def execute(self, command): ...
    def cd(self, remotepath=None): ...
    def chdir(self, remotepath): ...
    cwd = ... # type: Any
    def chmod(self, remotepath, mode=777): ...
    def chown(self, remotepath, uid=None, gid=None): ...
    def getcwd(self): ...
    def listdir(self, remotepath=''): ...
    def listdir_attr(self, remotepath=''): ...
    def mkdir(self, remotepath, mode=777): ...
    def normalize(self, remotepath): ...
    def isdir(self, remotepath): ...
    def isfile(self, remotepath): ...
    def makedirs(self, remotedir, mode=777): ...
    def readlink(self, remotelink): ...
    def remove(self, remotefile): ...
    unlink = ... # type: Any
    def rmdir(self, remotepath): ...
    def rename(self, remote_src, remote_dest): ...
    def stat(self, remotepath): ...
    def lstat(self, remotepath): ...
    def close(self): ...
    def open(self, remote_file, mode='', bufsize=-1): ...
    def exists(self, remotepath): ...
    def lexists(self, remotepath): ...
    def symlink(self, remote_src, remote_dest): ...
    def truncate(self, remotepath, size): ...
    def walktree(self, remotepath, fcallback, dcallback, ucallback, recurse=True): ...
    @property
    def sftp_client(self): ...
    @property
    def active_ciphers(self): ...
    @property
    def security_options(self): ...
    @property
    def logfile(self): ...
    @property
    def timeout(self): ...
    @timeout.setter
    def timeout(self, val): ...
    def __del__(self): ...
    def __enter__(self): ...
    def __exit__(self, etype, value, traceback): ...

def path_advance(thepath, sep=...): ...
def path_retreat(thepath, sep=...): ...
def reparent(newparent, oldpath): ...
def walktree(localpath, fcallback, dcallback, ucallback, recurse=True): ...
def cd(localpath=None): ...
