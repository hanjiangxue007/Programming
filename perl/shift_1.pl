#!/usr/bin/perl
# Author  : Bhishan Poudel


use strict;
use warnings;

@array = (1..5);
while ($element = shift(@array)) {
    print("$element - ");
}
print("The End\n");

# Description

# This function returns the first value in an array, deleting it and shifting
# the elements of the array list to the left by one. If ARRAY is not specified,
# shifts the @_ array within a subroutine, or @ARGV otherwise. shift is
# essentially identical to pop, except values are taken from the start of the
# array instead of the end.
