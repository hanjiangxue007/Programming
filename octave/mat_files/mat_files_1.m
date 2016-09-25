#!/usr/bin/octave -qf 
% Author    : Bhishan Poudel 
% Date      : 2016-06-13

% Create some variables
x = rand(3);
y = magic(3);
z = eye(3);

% Save the variable x,y,z into one *.mat file
save bathymetry.mat x y z

% Clear them out of the workspace
clear x y z

% Load them again
load bathymetry.mat

