#!/usr/bin/octave -qf
% Author    : Bhishan Poudel
% Date      : May 28, 2016

% Private functions reside in subfolders with the special name private.
% They are visible only to functions in the parent folder.


function dis = disc(a,b,c)
%function calculates the discriminant
dis = sqrt(b^2 - 4*a*c);
end % end of sub-function
