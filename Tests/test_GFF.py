#!/usr/bin/env python
"""Test the Bio.GFF module and dependencies
"""

import Bio.GFF
import Bio.GFF.GenericTools
import Bio.GFF.easy

print "Running Bio.GFF.GenericTools doctests..."
Bio.GFF.GenericTools._test()
print "Bio.GFF.GenericTools doctests complete."

print "Running Bio.GFF.easy doctests..."
Bio.GFF.easy._test()
print "Bio.GFF.easy doctests complete."

print "Running Bio.GFF doctests..."
Bio.GFF._test()
print "Bio.GFF doctests complete."
