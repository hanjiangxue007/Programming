#!/usr/bin/octave -qf
% Author    : Bhishan Poudel
% Date      : May 25, 2016

fprintf("Display the multiples of 7 from 1 through 50. If a number is not divisible by 7, use continue to skip the disp statement and pass control to the next iteration of the for loop.\n\n");

for n = 1:50
    if mod(n,7)
        continue
    end
    disp(['Divisible by 7: ' num2str(n)])
end
