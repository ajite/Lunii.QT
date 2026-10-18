import os
import shutil
import sys


def _ignore_vanished(func, path, exc):
    if not isinstance(exc, FileNotFoundError):
        raise exc


def rmtree(path):
    # on macOS, FAT AppleDouble sidecars "._<name>" vanish with their file during the walk
    os.lstat(path)  # bad path must still raise
    if sys.version_info >= (3, 12):
        shutil.rmtree(path, onexc=_ignore_vanished)
    else:
        shutil.rmtree(
            path,
            onerror=lambda func, p, exc_info: _ignore_vanished(func, p, exc_info[1]),
        )
