import os

def file_md5_size(f):
    import md5
    c = open(f, 'rb').read()
    return md5.md5(c).hexdigest(), len(c)

def md5_to_path(md5, url):
    ext = os.path.splitext(url)[1]
    return os.path.join(md5[:2], md5[2:]) + ext

def get_real_path(f):
    _, ext = os.path.splitext(f.url)
    return os.path.join(f.md5[:2], f.md5[2:]+ext)

def check_file_exists(f, path='.'):
    p = get_real_path(f)
    p = os.path.join(path, p)
    if not os.path.exists(p):
        return False
    if os.path.getsize(p)!=f.size:
        return False
    return True

def ensure_directory_exists(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)
