#!/usr/bin/octave -qf
% Author    : Bhishan Poudel
% Date      : May 25, 2016


% method 1
%year = 1998;  % 1900 1996 1998 2000
year = input ("Enter the year e.g. 1900 \n"); % 1900

if( mod(year,4) == 0 )
  fprintf("\nThe year %d is divisible by 4. \nIt may be a leap year.\n",year);
  if( mod(year,100) == 0 )
    % if condition is true then print the following
    fprintf('The year %d is century year.\n', year );
    if(  mod(year,400) == 0  )
      fprintf("The year %d is century year and divisible by 400.\n",year);
      fprintf("The year %d is leap year.\n",year);

    else
      fprintf("The year %d is century year, but not divisible by 400.\n",year);
      fprintf("The year %d is not a century year.\n",year);

    end
  else
    fprintf("The year %d is divisible by 4, but not a century year.\n",year);
    fprintf("The year %d is leap year.\n", year);
  end

else
  fprintf("\nThe given year %d is not divisible by 4.", year);
  fprintf("\nThe given year %d is not a leap year.\n",year);

end

% method 2
% https://www.rosettacode.org/wiki/Leap_year#MATLAB_.2F_Octave
%MATLAB, conveniently, provides a function that returns the last day of an
%arbitrary month of the calendar given the year. Using the fact that February is
%29 days long during a leap year, we can write a one-liner that solves this task.


fprintf("\n");
year = 1996
logic = (eomday(year,2) == 29);
if (logic == 1)
  fprintf("\nThe year %d is a leap year.",year);

else
  fprintf("\nThe year %d is not a leap year.", year);

end



