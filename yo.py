yo_path = r"c:\Vim\python\yo.dat"       # FIXME here
## Import part {{{1
try: import text
except ImportError:
    raise ImportError(
            "This module available only from Vim editor, only with text module"
            )
#reload(text)
try:
    if text.HEXVERSION < 0x10003: raise "Too old text module"
except AttributeError:
    raise "Too old text module"

import shelve
# There no need to import re module, because text.Text object provide access to
# them

## }}}
## Initialize part {{{1

print "I'm initialize database, this may be long, so please wait..."

## shelf contain two dictionary objects in unicode
shelf = shelve.open(yo_path)
MAY_BE_YO = shelf["may_be_yo"]
ONLY_YO   = shelf["only_yo"]
shelf.close()

## Definitions {{{2
## vim buffer
buffer = text.Text()

## Regular expression
# unicode flag put into compile function automatically
E_WORD = buffer.re.compile(ur"\b\w*[\u0435\u0415]\w*\b")

def fix_case(first, second):
    """\
    fix_case(first, second) -> string or None

    look to case of FIRST argument and return SECOND argument in sane
    case. But if the case can't recognized, return None
    """
    if   first.islower(): return second.lower()
    elif first.istitle(): return second.title()
    elif first.isupper(): return second.upper()
## }}}
## }}}
## Prepearing part {{{1
for i in buffer.re.finditer(E_WORD):
    try:
        yo = fix_case(i.mo.group(), ONLY_YO[i.mo.group().lower()])
        if yo:
            s,e = i.span()
            buffer[s:e] = yo
    except KeyError:
        try:
            yo = fix_case(i.mo.group(), MAY_BE_YO[i.mo.group().lower()])
            if yo:
                s,e = i.span()
                buffer.replace_i(s,e,[yo])
        except KeyError:
            pass
        except buffer.exceptions.CancelDialog:
            break
## }}}
## vim: fdm=marker:ro
