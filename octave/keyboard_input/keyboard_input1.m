#!/usr/bin/octave -qf
% Author    : Bhishan Poudel
% Date      : May 25, 2016


% for numbers: ans = input (prompt)
num = input ("Pick a number, any number! \n"); % 3.5
fprintf("The square of entered number is = %f\n", num^2);

% for strings: ans = input (prompt, "s")
string = input ("Enter a string! \n", "s"); % bhishan poudel (it reads whitespace)
fprintf("The  entered string is = %s\n", string);

