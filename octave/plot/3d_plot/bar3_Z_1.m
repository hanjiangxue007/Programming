#!/usr/bin/octave -qf
% Author    : Bhishan Poudel
% Date      : May 25, 2016

% Note: the 'bar3' function is not yet implemented in Octave
% it only works in Matlab

X = [1 2 3 4];
Y = [0.1 0.2 0.3 0.4];
Z = [10 11 12 13; 11 12 13 14; 12 13 14 15; 13 14 15 16];

figure;
bar3(Z)
set(gca(gcf), 'xticklabel',{'0.1','0.2','0.3','0.4'})
