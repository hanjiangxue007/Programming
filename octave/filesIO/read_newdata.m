# Author   : Bhishan Poudel
# Date     : May 21, 2016

load stack25148040.mat
A
# A = 1x10 struct array containing the fields:
#    f0 f1 ... f8

A.f8  # string field
A(1)  # 1st row
#  scalar structure containing the fields:
#   f0 =  18
#   f1 = 8
...
#   f8 = chevrolet chevelle malibu

%Newer Octave (3.8) has an importdata function. It handles the original data file without any extra arguments. It returns a structure with 2 fields

%x.data is a (10,11) matrix.  x.data(:,1:8) is the desire numerical data.  x.data(:,9:11) is a mix of NA and random numbers. The NA stand in for the words at the end of the lines. x.textdata is a (24,1) cell with those words. The quoted string s could be reassembled from those words, using the NA and quotes to determine how many words belong to which line.

%To read the numeric data it uses dlmread. Since the rest of importdata is written in Octave, it could be used as the starting point for a custom function that handles the string data properly.

dlmread ('stack25148040.txt')(:,1:8)
textread ('stack25148040.txt','')(:,1:8)

