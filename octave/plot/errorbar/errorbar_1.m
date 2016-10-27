#!/usr/bin/octave -qf
% Author    : Bhishan Poudel
% Date      : May 25, 2016
% Ref       : https://www.gnu.org/software/octave/doc/v4.0.0/Two_002dDimensional-Plots.html

x = 0:0.1:10;
y = sin (x);
yp =  0.1 .* randn (size (x));
ym = -0.1 .* randn (size (x));
errorbar (x, sin (x), ym, yp);
pause;



%  Function File: errorbar (y, ey)
%  Function File: errorbar (y, …, fmt)
%  Function File: errorbar (x, y, ey)
%  Function File: errorbar (x, y, err, fmt)
%  Function File: errorbar (x, y, lerr, uerr, fmt)
%  Function File: errorbar (x, y, ex, ey, fmt)
%  Function File: errorbar (x, y, lx, ux, ly, uy, fmt)
%  Function File: errorbar (x1, y1, …, fmt, xn, yn, …)
%  Function File: errorbar (hax, …)
%  Function File: h = errorbar (…)
%  Create a 2-D plot with errorbars.

%  Many different combinations of arguments are possible. The simplest form is

%  errorbar (y, ey)
%  where the first argument is taken as the set of y coordinates, the second
%  argument ey are the errors around the y values, and the x coordinates are
%  taken to be the indices of the elements (1:numel (y)).

%  The general form of the function is

%  errorbar (x, y, err1, …, fmt, …)
%  After the x and y arguments there can be 1, 2, or 4 parameters specifying
%  the error values depending on the nature of the error values and the plot
%  format fmt.

%  err (scalar)
%  When the error is a scalar all points share the same error value.
%  The errorbars are symmetric and are drawn from data-err to data+err.
%  The fmt argument determines whether err is in the x-direction,
%  y-direction (default), or both.

%  err (vector or matrix)
%  Each data point has a particular error value.
%  The errorbars are symmetric and are drawn from data(n)-err(n) to data(n)+err(n).

%  lerr, uerr (scalar)
%  The errors have a single low-side value and a single upper-side value.
%  The errorbars are not symmetric and are drawn from data-lerr to data+uerr.

%  lerr, uerr (vector or matrix)
%  Each data point has a low-side error and an upper-side error.
%  The errorbars are not symmetric and are drawn from data(n)-lerr(n)
%  to data(n)+uerr(n).

%  Any number of data sets (x1,y1, x2,y2, …) may appear as long as they
%  are separated by a format string fmt.

%  If y is a matrix, x and the error parameters must also be matrices having
%  the same dimensions. The columns of y are plotted versus the
%  corresponding columns of x and errorbars are taken from the corresponding
%  columns of the error parameters.

%  If fmt is missing, the yerrorbars ("~") plot style is assumed.

%  If the fmt argument is supplied then it is interpreted, as in normal plots,
%  to specify the line style, marker, and color. In addition, fmt may include
%  an errorbar style which must precede the ordinary format codes.
%  The following errorbar styles are supported:

%  ‘~’
%  Set yerrorbars plot style (default).

%  ‘>’
%  Set xerrorbars plot style.

%  ‘~>’
%  Set xyerrorbars plot style.

%  ‘#~’
%  Set yboxes plot style.

%  ‘#’
%  Set xboxes plot style.

%  ‘#~>’
%  Set xyboxes plot style.

%  If the first argument hax is an axes handle, then plot into this axis,
%  rather than the current axes returned by gca.

%  The optional return value h is a handle to the hggroup object representing
%  the data plot and errorbars.

%  Note: For compatibility with MATLAB a line is drawn through all data points.
%  However, most scientific errorbar plots are a scatter plot of points with
%  errorbars. To accomplish this, add a marker style to the fmt argument such as
%  ".". Alternatively, remove the line by modifying the returned graphic handle
%  with set (h, "linestyle", "none").

%  Examples:

%  errorbar (x, y, ex, ">.r")
%  produces an xerrorbar plot of y versus x with x errorbars drawn from x-ex to
%  x+ex. The marker "." is used so no connecting line is drawn and the
%  errorbars appear in red.

%  errorbar (x, y1, ey, "~",
          %  x, y2, ly, uy)
%  produces yerrorbar plots with y1 and y2 versus x. Errorbars for y1 are drawn
%  from y1-ey to y1+ey, errorbars for y2 from y2-ly to y2+uy.

%  errorbar (x, y, lx, ux,
          %  ly, uy, "~>")
%  produces an xyerrorbar plot of y versus x in which x errorbars are drawn from
%  x-lx to x+ux and y errorbars from y-ly to y+uy.

