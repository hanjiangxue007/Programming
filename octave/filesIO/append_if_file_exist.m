#!/usr/bin/octave -qf
% Author    : Bhishan Poudel
% Date      : May 25, 2016

FileName = 'append_if_file_exist.txt'

if exist(FileName, 'file')
  save(FileName, '-append');
else
  save(FileName);
end
