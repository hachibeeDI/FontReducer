# -*- coding: utf-8 -*-
# ==== python2 and 3 compatible ====
from __future__ import (print_function, division, absolute_import, unicode_literals, )

# ==== logging ====

from logging import getLogger, StreamHandler, DEBUG
_logger = getLogger(__name__)
_handler = StreamHandler()
_handler.setLevel(DEBUG)
_logger.setLevel(DEBUG)
_logger.addHandler(_handler)

# ==== scripts ====


def _get_fontname(font):
    if font.cidfamilyname is not None:
        return font.cidfamilyname
    elif font.familyname is not None:
        return font.familyname
    else:
        from os import path
        return path.splitext(font.default_base_filename)[0]


def generate_subset(chars, fontpath):
    '''
    via: http://3846masa.hatenablog.jp/entry/2015/04/08/163149
    >>> font = generate_subset('abc', 'Love Letter Typewriter.ttf')
    >>> font.generate('./hogehoge.ttf')
    '''
    import fontforge
    font = fontforge.open(fontpath)
    fontname = _get_fontname(font)
    _logger.info('reducing font name is ' + fontname)

    for i in range(0, len(chars)):
        char = chars[i]
        try:
            uni = font[char].unicode
        except TypeError:
            _logger.info(unichr(char) + ' is missing font code')
            pass
        else:
            if uni != char:
                chars.append(uni)
            alts = font[char].altuni
            if alts is None:
                continue
            for alt in alts:
                if alt[0] != char:
                    chars.append(alt[0])
    for c in chars:
        font.selection.select((b"more", None), c)
    font.selection.invert()
    font.clear()
    return font
