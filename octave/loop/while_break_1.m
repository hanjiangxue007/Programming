#!/usr/bin/octave -qf
% Author    : Bhishan Poudel
% Date      : May 25, 2016
% Ref       : https://www.mathworks.com/help/matlab/ref/break.html

fprintf("Sum a sequence of random numbers until the next random number is greater than an upper limit. Then, exit the loop using a break statement.\n\n");

limit = 0.8
s = 0

while 1
    tmp = rand
    if tmp > limit
        break
    end
    s = s + tmp
end
