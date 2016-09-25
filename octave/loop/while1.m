#!/usr/bin/octave -qf
% Author    : Bhishan Poudel
% Date      : May 25, 2016
% Ref       : https://www.mathworks.com/help/matlab/ref/while.html


% example 1
fprintf("a while loop to calculate factorial\n");
n = 3;
f = n;
while n > 1
    n = n-1;
    f = f*n;
end
disp(['n! = ' num2str(f)])


%% example 2
%fprintf("Sum a sequence of random numbers until the next random number is greater than an upper limit. Then, exit the loop using a break statement.\n\n");

%limit = 0.8;
%s = 0;

%while 1
    %tmp = rand;
    %fprintf("tmp = %f\n",tmp);
    %if tmp > limit
        %break
    %end
    %s = s + tmp;
%end
%fprintf("s = %f\n",s);


% example 3
fprintf("\nExample 3\n");
x = 40;  % note: myfunction is square function
while exist('myfunction.m','file') && (myfunction(x) >= 50)
    disp('Expressions are true')
    break
end

