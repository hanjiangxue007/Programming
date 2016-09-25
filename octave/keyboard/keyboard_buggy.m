#!/usr/bin/octave -qf
% Author    : Bhishan Poudel
% Date      : May 25, 2016


%  keyboard pauses execution of a running program and gives control to the keyboard.
%  Place the keyboard function in a program at the location where you want MATLAB®
%  to pause. When the program pauses, the prompt in the Command Window changes
%  to debug>, indicating that MATLAB is in debug mode.
%    You then can view or change  the values of variables to see if the new
%    values produce expected results.
%  The keyboard function is useful for debugging your functions.

buggy(5)


%Multiply the variable x by 2 and continue running the program.
% MATLAB executes the rest of the program using the new value of x.

%on terminal type:  x = x * 2
%                   dbcont

% Tips
% To terminate debug mode and continue execution, use the dbcont command.
% To terminate debug mode and exit the file without completing execution,
% use the dbquit command.
