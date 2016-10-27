#!/usr/bin/octave -qf
% Author    : Bhishan Poudel
% Date      : May 25, 2016
% Ref       : https://www.mathworks.com/help/matlab/ref/meshgrid.html

%  2-D Grid From Vectors
%  Create a full grid from two monotonically increasing grid vectors:

[X,Y] = meshgrid(1:3,10:14) % X = 1 2 3 all rows same, no of rows = len(ygv) = 5
                            % Y = 10; 11; 12; 13; 14 all columns same
			    %     no. of columns = len(xgv) = 3, gv is grid vector


% Plot 3-D Functional Surface
% Use meshgrid to create a gridded (X,Y) domain.

[X,Y] = meshgrid(-2:.2:2, -2:.2:2);
% Evaluate the function  $z(x,y) = xe^{-x^2-y^2}$ over this domain and generate
% a surface plot of the results.

Z = X .* exp(-X.^2 - Y.^2);
surf(X,Y,Z)
pause;

%  Syntax
%  [X,Y] = meshgrid(xgv,ygv)
%  [X,Y,Z] = meshgrid(xgv,ygv,zgv)
%  [X,Y] = meshgrid(gv)
%  [X,Y,Z] = meshgrid(gv)

%  Description
%  [X,Y] = meshgrid(xgv,ygv) replicates the grid vectors xgv and ygv to produce a
%  full grid. This grid is represented by the output coordinate arrays X and Y.
%  The output coordinate arrays X and Y contain copies of the grid vectors xgv
%  and ygv respectively. The sizes of the output arrays are determined by the
%  length of the grid vectors. For grid vectors xgv and ygv of length M and N
%  respectively, X and Y will have N rows and M columns.

%  [X,Y,Z] = meshgrid(xgv,ygv,zgv) produces three-dimensional coordinate arrays.
%  The output coordinate arrays X, Y, and Z contain copies of the grid vectors
%  xgv, ygv, and zgv respectively. The sizes of the output arrays are determined
%  by the length of the grid vectors. For grid vectors xgv, ygv, and zgv of
%  length M, N, and P respectively, X, Y, and Z will have N rows, M columns,
%  and P pages.

%  [X,Y] = meshgrid(gv) is the same as [X,Y] = meshgrid(gv,gv). In other words,
%  you can reuse the same grid vector in each respective dimension.
%  The dimensionality of the output arrays is determined by the
%  number of output arguments.

%  [X,Y,Z] = meshgrid(gv) is the same as [X,Y,Z] = meshgrid(gv,gv,gv).
%  Again, the dimensionality of the output arrays is determined by the
%  number of output arguments.

%  The output coordinate arrays are typically used to evaluate functions of
%  two or three variables. They are also frequently used to create surface
%  and volumetric plots.

%  Input Arguments
%  xgv,ygv,zgv
%  Grid vectors specifying a series of grid point coordinates in the x, y and z
%  directions, respectively.
%  gv
%  Generic grid vector specifying a series of point coordinates.
%  Output Arguments
%  X,Y,Z
%  Output arrays that specify the full grid.
