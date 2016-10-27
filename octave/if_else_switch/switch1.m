#!/usr/bin/octave -qf
% Author    : Bhishan Poudel
% Date      : May 25, 2016
% Ref       : https://www.mathworks.com/help/matlab/ref/switch.html


% Description
fprintf("Tips:\n A case_expression cannot include relational operators \n such as < or > for comparison against the switch_expression. \n\nTo test for inequality, use if, elseif, else statements.\n");






% example 1
x = 5;
switch true
    case x > 10
        fprintf(1, 'x is greater than 10\n')
    case x > 8
        fprintf(1, 'x is greater than 8\n')
    case x < 6
        fprintf(1, 'x is less than 6\n')
    case y == 3
        fprintf(1, 'y equals three\n')
    otherwise
        fprintf(1, 'no conditions were met\n')
end


% example 2
fprintf("\nexample2\n");
fprintf("Compare single value\n");

%n = input('Enter a number: ');
n = 5;

switch n
    case -1
        disp('negative one')
    case 0
        disp('zero')
    case 1
        disp('positive one')
    otherwise
        disp('other value')
end

%% example 3
%fprintf("Compare multiple values.\n");
%x = [12 64 24];
%plottype = 'pie3';

%switch plottype
    %case 'bar'
        %bar(x)
        %title('Bar Graph')
	%pause;
    %case {'pie','pie3'}
        %pie3(x)
        %title('Pie Chart')
	%pause;
    %otherwise
        %warning('Unexpected plot type. No plot created.')
	%pause;
%end

% example 4
fprintf("\n");
fprintf("The MATLAB switch statement does not fall through like a C language switch statement. If the first case statement is true, MATLAB does not execute the other case statements. For example:\n\n");

result = 52;

switch(result)
   case 52
      disp('result is 52')
   case {52, 78}
      disp('result is 52 or 78')
end
% ans = result is 52

% example 5
fprintf("\nDefine all variables necessary for code in a particular case within that case. Since MATLAB executes only one case of any switch statement, variables defined within one case are not available for other cases. For example, if your current workspace does not contain a variable x, only cases that define x can use it:\n");

choice = 1;
switch choice
   case 1
      x = -pi:0.01:pi;
   case 2
      % does not know anything about x
end

% example 6
fprintf("\nDo not use a break statement within a switch block. break is not defined outside a for or while loop.\n");
