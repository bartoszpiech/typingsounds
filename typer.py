import subprocess

class _Getch:
    """Gets a single character from standard input.  Does not echo to the screen."""
    def __init__(self):
        try:
            self.impl = _GetchUnix()
        except ImportError:
            self.impl = _GetchWindows()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()
while(1):
    char = getch()
    if ord(char) == 27:
        exit()
    if ord(char) == 127:
        char = 'backspace'
    elif ord(char) == 13:
        char = 'enter'
    elif ord(char) == 13:
        char = 'enter'
    elif ord(char) == 32:
        char = 'space'
    cmd = char + '.mp3'
    subprocess.Popen(['afplay', cmd])
    print(char)
