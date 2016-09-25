#!/usr/bin/octave -qf
% Author    : Bhishan Poudel
% Date      : May 28, 2016
% Ref       : http://www.tutorialspoint.com/matlab/matlab_gnu_octave.htm

[x,y] = meshgrid(-2:.2:2);
g = x .* exp(-x.^2 - y.^2);
surf(x, y, g)
print -deps graph.eps
pause;
