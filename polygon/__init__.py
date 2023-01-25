import check50
import check50.c

@check50.check()
def exists():
    """Files exist."""
    check50.exists("polygon.py")

