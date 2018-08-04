def get_file_path(fn):
    import os
    return os.path.join(os.path.dirname(__file__), fn)


def get_file_contents(fn):
    f = get_file_path(fn)
    with open(f,'r') as fh:
        return fh.read()


def strip_cr_lf(s): return s.replace("\n", "").replace("\r", "")
