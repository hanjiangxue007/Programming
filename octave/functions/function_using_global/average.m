#!/usr/bin/octave -qf
% Author    : Bhishan Poudel
% Date      : May 28, 2016

function avg = average(nums)
global TOTAL                   % e.g. TOTAL = 10 in main.m file
avg = sum(nums)/TOTAL;
end
