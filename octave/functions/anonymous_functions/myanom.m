#!/usr/bin/octave -qf
% Author    : Bhishan Poudel
% Date      : May 28, 2016

% You can define an anonymous function right at the MATLAB command
% line or within a function or script.

% This way you can create simple functions without
% having to create a file for them.

% The syntax for creating an anonymous function from an expression is

% f = @(arglist)expression

power = @(x, n) x.^n;
result1 = power(7, 3)
result2 = power(49, 0.5)
result3 = power(10, -10)
result4 = power (4.5, 1.5)
