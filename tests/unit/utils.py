def capture(f):
    """
    Decorator to capture standard output
    """
    def captured(*args, **kwargs):
        import sys
        from io import StringIO

        backup = sys.stdout
        try:
            sys.stdout = StringIO()
            f(*args, **kwargs)
            output = sys.stdout.getvalue()
        finally:
            sys.stdout.close()
            sys.stdout = backup

        return output
    return captured
