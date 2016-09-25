#!/usr/bin/octave -qf
% Author    : Bhishan Poudel
% Date      : May 25, 2016
% Ref       : https://www.mathworks.com/help/matlab/ref/return.html

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% define a function
%In your current working folder, create a function, findSqrRootIndex,
%to find the index of the first occurrence of the square root of a value
%within an array. If the square root isn't found, the function returns NaN.

% invoke the function
A = [3 7 28 14 42 9 0] % do not change this, depend on myFunction1.m
b = 81;
index = findSqrRootIndex(b,A)
fprintf("index = %d\n",index);


% example 2
fprintf("\nexample 2\n");
% In a file, myFunction1.m, in your current working folder.
myFunction1(49)

