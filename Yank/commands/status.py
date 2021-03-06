#!/usr/local/bin/env python

#=============================================================================================
# MODULE DOCSTRING
#=============================================================================================

"""
Query output files for quick status.

"""

#=============================================================================================
# MODULE IMPORTS
#=============================================================================================

#=============================================================================================
# COMMAND DISPATCH
#=============================================================================================

def dispatch(args):
    from yank import analyze
    success = analyze.print_status(args['--store'], verbose=args['--verbose'])
    return success
