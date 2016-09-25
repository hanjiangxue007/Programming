#!/usr/local/octave/3.8.0/bin/octave -qf 
% Author    : Bhishan Poudel 
% Date      : Jun 24, 2016

%% plotting
%%==================================

%% data
x = 1:10
y = 20:29

plot(x, y, 'rx', 'MarkerSize', 10, 'LineWidth', 1.5);

# title and axes labels
title('title')
xlabel('xlabel')
ylabel('ylabel')

legend({'data ', 'hypothesis '},  'Location', 'NorthWest');


# axes limit
axis([0 13 0 150])


pause;

