#!/usr/bin/octave -qf
% Author    : Bhishan Poudel
% Date      : May 25, 2016

a=5;  std_a=1.0;
b=6;  std_b=0.5;
c=7;  std_c=0.2;

bar([a,b,c]);
hold on
errorbar([a,b,c],[std_a,std_b,std_c],'r*'); % style r=red . is solid line
pause;                                      % * is star
