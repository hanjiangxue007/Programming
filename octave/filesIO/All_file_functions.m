#!/usr/bin/octave -qf
% Author    : Bhishan Poudel
% Date      : May 25, 2016

%  dir	        List folder contents
%  ls	        List folder contents
%  pwd	        Identify current folder
%  fileattrib	Set or get attributes of file or folder
%  exist	Check existence of variable, function, folder, or class
%  isdir	Determine whether input is folder
%  type	        Display contents of file
%  visdiff	Compare two text files, MAT-Files, binary files, Zip files, folders
%  what	        List MATLAB files in folder
%  which 	Locate functions and files
%  cd	        Change current folder
%  copyfile	Copy file or folder
%  delete	Delete files or objects
%  recycle	Set option to move deleted files to recycle folder
%  mkdir	Make new folder
%  movefile	Move file or folder
%  rmdir	Remove folder
%  open	        Open file in appropriate application
%  fopen        fopen(filename, mode)  mode = r w a


%dir()
%ls()
pwd()

%fileattrib('auto.txt')
if exist('auto.txt')
    fprintf("The file auto.txt exists.\n");

end

%what()   %M-files in directory ...    :
	  %Mat-files in directory ...  :


mkdir('tmp_folder')
%cd('tmp_folder');
%pwd = pwd()
%fopen('tmp.txt','w')
%fopen('tmp2.txt','w')

fopen('tmp_folder/tmp.txt','w')
if (exist('tmp_folder/tmp2.txt', 'file')==2)
  delete('tmp_folder/tmp2.txt');
end



