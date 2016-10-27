#!/usr/bin/octave -qf
% Author    : Bhishan Poudel
% Date      : May 25, 2016
% Ref       : https://www.gnu.org/software/octave/doc/v4.0.0/Two_002dDimensional-Plots.html


contour3 (peaks (19));
colormap cool;
hold on;
surf (peaks (19), "facecolor", "none", "edgecolor", "black");
pause;

%  Function File: contour3 (z)
%  Function File: contour3 (z, vn)
%  Function File: contour3 (x, y, z)
%  Function File: contour3 (x, y, z, vn)
%  Function File: contour3 (…, style)
%  Function File: contour3 (hax, …)
%  Function File: [c, h] = contour3 (…)
%  Create a 3-D contour plot.

%  contour3 plots level curves (contour lines) of the matrix z at a Z level
%  corresponding to each contour. This is in contrast to contour which plots
%  all of the contour lines at the same Z level and produces a 2-D plot.

%  The level curves are taken from the contour matrix c computed by contourc for
%  the same arguments; see the latter for their interpretation.

%  The appearance of contour lines can be defined with a line style style in the
%  same manner as plot. Only line style and color are used; Any markers defined
%  by style are ignored.

%  If the first argument hax is an axes handle, then plot into this axis, rather
%  than the current axes returned by gca.

%  The optional output c are the contour levels in contourc format.

%  The optional return value h is a graphics handle to the hggroup comprising
%  the contour lines.
