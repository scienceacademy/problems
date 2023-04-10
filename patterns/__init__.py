import check50
import check50.c

@check50.check()
def exists():
    """Files exist."""
    check50.exists("patterns1.py")
    check50.exists("patterns2.py")
    check50.exists("patterns3.py")
    
@check50.check(exists)
def submitted():
    """submitted"""
