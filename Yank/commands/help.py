#!/usr/local/bin/env python

#=============================================================================================
# MODULE DOCSTRING
#=============================================================================================

"""
Print YANK help.

"""

#=============================================================================================
# MODULE IMPORTS
#=============================================================================================

#=============================================================================================
# COMMAND DISPATCH
#=============================================================================================

def dispatch(args):
    from yank import cli
    print cli.usage
    return True


