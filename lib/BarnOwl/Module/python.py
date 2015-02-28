from perl import BarnOwl
m = BarnOwl.Module.Python

def cmd_python(cmd, *args):
    BarnOwl.message(repr(eval(' '.join(args))))

def cmd_ppython(cmd, *args):
    BarnOwl.popless_text(repr(eval(' '.join(args))))

def cmd_epython(cmd, *args):
    BarnOwl.start_edit_win("Enter Python code:", m.cb_epython)

def cb_epython(python):
    exec(python)

def init():
    BarnOwl.new_command("python", m.cmd_python, {
        "summary": "evaluate a Python expression",
        "usage": "python [args .. ]",
    })
    BarnOwl.new_command("ppython", m.cmd_ppython, {
        "summary": "evaluate a Python expression and display in a popup window",
        "description": "ppython [args .. ]",
    })
    BarnOwl.new_command("epython", m.cmd_epython, {
        "summary": "open the edit window for Python code",
        "description": "epython"
    })
    return 1
