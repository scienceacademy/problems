import check50

@check50.check()
def exists():
    """Files exist."""
    check50.exists("orbit.py")

@check50.check(exists)
def submitted():
    """submitted"""
