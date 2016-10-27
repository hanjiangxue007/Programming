#!/usr/bin/octave -qf
% Author    : Bhishan Poudel
% Date      : May 25, 2016
% Ref       : https://www.mathworks.com/help/matlab/ref/errorbar.html

% Draw symmetric error bars that are two standard deviation units in length.
%  errorbar(Y,E)
%  errorbar(X,Y,E)
%  errorbar(X,Y,L,U)
%  errorbar(...,LineSpec)
%  errorbar(ax,...)
%  h = errorbar(...)


%% exmaple 1
%x = 0:pi/10:pi;
%y = sin(x);
%e = std(y)*ones(size(x));

%figure
%errorbar(x,y,e)
%pause;

% example 2
x = 1:0.1:10;
y = sin(x);
e = 0.1 * randn(length(x), 1);

errorbar(x,y,e)

set(gca, 'Xlim', [4 10])
set(gca, 'XTick', 4:2:10)
pause;

