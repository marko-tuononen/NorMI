# -*- coding: utf-8 -*-
"""Class with helper functions.

MIT License
Copyright (c) 2023, Daniel Nagel
All rights reserved.

"""
__all__ = ['savetxt']  # noqa: WPS410

import datetime
import getpass
import platform
import sys

import numpy as np
from beartype import beartype
from beartype.typing import Optional

from nmi._typing import (  # noqa: WPS436
    FloatMax2DArray,
)


@beartype
def _get_rui() -> str:
    """Get the runetime user information, to store as comment."""
    # get time without microseconds
    date = datetime.datetime.now()
    date = date.isoformat(sep=' ', timespec='seconds')

    rui = {
        'user': getpass.getuser(),
        'pc': platform.node(),
        'date': date,
        'args': ' '.join(sys.argv),
    }

    return (
        'This file was generated by nmi:\n{args}' +
        '\n\n{date}, {user}@{pc}'
    ).format(**rui)


@beartype
def savetxt(
    filename: str,
    array: FloatMax2DArray,
    fmt: str,
    header: Optional[str] = None,
) -> None:
    """Save ndarray with user runtime information."""
    header_generic = _get_rui()
    if header:
        header_generic = f'{header_generic}\n\n{header}'

    np.savetxt(
        filename,
        array,
        fmt=fmt,
        header=header_generic,
    )
