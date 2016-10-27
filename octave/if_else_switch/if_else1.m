#!/usr/bin/octave -qf
% Author    : Bhishan Poudel
% Date      : May 25, 2016
% Ref       :


a = 100;
b = 200;

% check the boolean condition
if( a == 100 )

  % if condition is true then check the following
  if( b == 200 )

    % if condition is true then print the following
    fprintf('Value of a is 100 and b is 200\n' );
  end

end

fprintf('Exact value of a is : %d\n', a );
fprintf('Exact value of b is : %d\n', b );


# example 2
# Ref: https://www.mathworks.com/help/matlab/ref/if.html
fprintf("\nexample2\n")
limit = 0.75
A = rand(10,1)
if any(A > limit)
    disp('There is at least one value above the limit.')
else
    disp('All values are below the limit.')
end


# example 3
fprintf("\nexample3\n");
a = randi(100, 1)

if a < 30
    disp('small')
elseif a < 80
    disp('medium')
else
    disp('large')
end

