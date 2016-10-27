#!/usr/bin/octave -qf
% Author    : Bhishan Poudel
% Date      : May 25, 2016
% Ref       : https://www.rosettacode.org/wiki/Check_that_file_exists#MATLAB_.2F_Octave


% first create a file and dir
fopen('input.txt','w')
mkdir('docs')
ls()

% now check if file exist
logic = exist('input.txt','file')
logic = exist('/input.txt','file')
logic = exist('docs','dir')
logic = exist('/docs','dir')
