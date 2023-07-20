# hide_frames
Ever had nested wrappers (probably from many libraries) ... and your traceback look messy? There's just `func(*args, **kwargs)` everywhere!

Not anymore, using `hide_frames`, you can (ironically) use a simple decorator to hide your ugly frames!

## Installation
`pip install hide_frames`

## Example
Suppose we have a wrapper:
```py
def useless(f):
    def wrapped_function(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapped_function
```
If we have a function that raises an exception and we wrap it:
```py
@useless
def oops():
    raise Exception
```
We would get an ugly traceback if we call it:
```py
Traceback (most recent call last):
  File "myfile.py", line 10, in <module>
    oops()
  File "myfile.py", line 3, in wrapped_function
    return f(*args, **kwargs)      # <--- ugly
           ^^^^^^^^^^^^^^^^^^
  File "myfile.py", line 8, in oops
    raise Exception
Exception
```
We can use the hide_frame decorator to modify our `useless` decorator:
```py
def useless(f):
    @hide_frame      # <-- important
    def wrapped_function(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapped_function
```
Now, our traceback looks like this:
```py
Traceback (most recent call last):
  File "myfile.py", line 13, in <module>
    oops()
  File "myfile.py", line 11, in oops
    raise Exception
Exception
```
Hooray! No more `f(*args, **kwargs)` !

The best part: it works with any number of decorators!

If you have more than one frame that needs to be hidden, use `hide_nframes()`

(There's another simple example in `test.py`)
