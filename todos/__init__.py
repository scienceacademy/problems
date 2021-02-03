import check50

@check50.check()
def exists():
    """application.py exists"""
    check50.exists("application.py")

@check50.check(exists)
def del_route():
    """application.py contains /del route"""

    app = open("application.py").read()
    if 'route("/del")' not in app:
        raise check50.Failure(f"missing /del route in application.py")

@check50.check(exists)
def layout_style():
    """layout.html contains <style> tag"""

    page = open("templates/layout.html").read()
    if "<style>" not in page:
        raise check50.Failure(f"missing <style> tag in layout.html")


@check50.check(exists)
def tasks_del():
    """tasks.html contains links to /del"""

    page = open("templates/tasks.html").read()
    if "/del" not in page:
        raise check50.Failure(f"no links to /del in tasks.html")


@check50.check(exists)
def tasks_iter():
    """tasks.html contains loop.index0 for iteration"""

    page = open("templates/tasks.html").read()
    if "loop.index0" not in page:
        raise check50.Failure(f"not using iteration in tasks.html")
