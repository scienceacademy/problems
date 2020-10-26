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