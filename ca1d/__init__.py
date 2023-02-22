import check50
import check50.c

@check50.check()
def exists():
    """Files exist."""
    check50.exists("ca.py")
    check50.exists("1.png")
    check50.exists("2.png")
    check50.exists("3.png")
    check50.exists("ca.txt")

@check50.check(exists)
def submitted():
    """submitted"""
