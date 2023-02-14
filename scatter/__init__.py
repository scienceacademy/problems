import check50
import check50.c

@check50.check()
def exists():
    """Files exist."""
    check50.exists("scatter.py")
    check50.exists("scatter.png")

@check50.check(exists)
def submitted():
    """submitted"""
