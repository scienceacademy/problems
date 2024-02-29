import check50
import check50.c

@check50.check()
def exists():
    """Files exist."""
    check50.exists("rabbits.py")
    check50.exists("rabbits.png")

@check50.check(exists)
def submitted():
    """submitted"""
