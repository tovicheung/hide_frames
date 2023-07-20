def hide_nframes(n):
    def decorator(f):
        def _inner(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except Exception as e:
                tb = e.__traceback__
                tb = tb.tb_next # manually hide THIS frame
                for _ in range(n):
                    tb = tb.tb_next
                e.__traceback__ = tb
                raise
        return _inner
    return decorator

def hide_frame(f):
    return hide_nframes(1)(f)
