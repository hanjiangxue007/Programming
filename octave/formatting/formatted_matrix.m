#!/usr/local/octave/3.8.0/bin/octave -qf 
% Author    : Bhishan Poudel 
% Date      : 2016-07-10

fprintf('general example\n');
x = rand(3,2) - 0.5

fprintf('example 1\n');
sprintf('%.6f %.6f\n',rand(3,2))


fprintf('example \n');
A = randn(3,9);
sprintf([repmat('%10.6f',1,size(A,2)) '\n'],A)


fprintf('example \n');
A = 1 - randn(3,9); 
fprintf(strrep(sprintf([repmat('%+10.6f',1,size(A,2)) '\n'],A), '+', ' '));
