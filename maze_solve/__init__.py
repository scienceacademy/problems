import check50
import check50.c

@check50.check()
def exists():
    """Files exist."""
    check50.exists("maze_solve.py")
    check50.exists("maze_solve.txt")

@check50.check(exists)
def submitted():
    """submitted"""
