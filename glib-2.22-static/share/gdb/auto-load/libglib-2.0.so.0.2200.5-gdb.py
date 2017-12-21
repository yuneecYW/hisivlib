import sys
import gdb

# Update module path.
dir = '/home/yf/linux/glib-2.22-static/share/glib-2.0/gdb'
if not dir in sys.path:
    sys.path.insert(0, dir)

from glib import register
register (gdb.current_objfile ())
