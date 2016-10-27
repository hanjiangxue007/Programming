#!/usr/bin/octave -qf
% Author    : Bhishan Poudel
% Date      : May 25, 2016
% Ref       : https://www.gnu.org/software/octave/doc/v4.0.0/Two_002dDimensional-Plots.html

x = 0:2;
y = x;
z = x' * y;
contour (x, y, z, 2:3)

%  The contour, contourf and contourc functions produce two-dimensional contour
%  plots from three-dimensional data.

%  Function File: contour (z)
%  Function File: contour (z, vn)
%  Function File: contour (x, y, z)
%  Function File: contour (x, y, z, vn)
%  Function File: contour (…, style)
%  Function File: contour (hax, …)
%  Function File: [c, h] = contour (…)
%  Create a 2-D contour plot.

%  Plot level curves (contour lines) of the matrix z, using the contour matrix c
%  computed by contourc from the same arguments; see the latter for their
%  interpretation.

%  The appearance of contour lines can be defined with a line style style in the
%  same manner as plot. Only line style and color are used; Any markers defined
%  by style are ignored.

%  If the first argument hax is an axes handle, then plot into this axis, rather
%  than the current axes returned by gca.

%  The optional output c contains the contour levels in contourc format.

%  The optional return value h is a graphics handle to the hggroup comprising
%  the contour lines.
