import check50
import check50.c

@check50.check()
def exists():
    """Files exist."""
    check50.exists("patterns4.py")
    check50.exists("patterns5.py")
    check50.exists("patterns6.py")

@check50.check(exists)
def submitted():
    """submitted"""
