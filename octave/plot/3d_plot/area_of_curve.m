#!/usr/bin/octave -qf
% Author    : Bhishan Poudel
% Date      : May 28, 2016
% Ref       : http://www.tutorialspoint.com/matlab/matlab_gnu_octave.htm

pkg load symbolic
%symbols

x = sym("x");

f = inline("x^2*cos(x)");

ezplot(f, [-4,9])
print -deps area_of_curve.eps

[a, ierror, nfneval] = quad(f, -4, 9);

display('Area: '), disp(double(a));
pause;
