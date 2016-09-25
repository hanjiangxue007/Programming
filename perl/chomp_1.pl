#!/usr/bin/perl
# Author  : Bhishan Poudel


use strict;
use warnings;

#chomp() EXAMPLES
$a = "abcdefghijklm";
chomp($a);
print $a;  #would return exact string... nothing to remove


print "\n\n";
$a = "abcdefghij\n";
chomp($a);
print $a;  #would return 'abcdefghij', removed newline


print "\n\n";
$a = "abcdefghij\n";
$b = chomp($a);
print $b;  #would return 1, it did remove something for sure



#chop() EXAMPLES
print "\n\n";
$a = "abcdefghij";
chop($a);
print $a;  #this would return 'abcdefghi'


print "\n\n";
$a = "abcdefghij";
$b = chop($a);
print $b;  #this would return 'j'


# these two functions are very much alike... they both remove one (or more)
# characters from the end of a string... So how are they different you ask?
# Chomp() ONLY removes new line characters (these are specified in $/),
# whereas Chop() removes anything that is at the end of the string
# (it really doesn't care what it is)...
