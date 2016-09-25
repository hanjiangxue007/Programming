#!/usr/bin/octave -qf
% Author    : Bhishan Poudel
% Date      : Jun 04, 2016

% idx = find (x)
% idx = find (x, n)
% idx = find (x, n, direction)
% [i, j] = find (…)
% [i, j, v] = find (…)

% Return a vector of indices of nonzero elements of a matrix,
% as a row if x is a row vector or as a column otherwise.

eye(2)
find (eye (2))



% If two inputs are given, n indicates the maximum number of elements to find
% from the beginning of the matrix or vector.

% If three inputs are given, direction should be one of "first" or "last", requesting only the first or last n indices, respectively.
% However, the indices are always returned in ascending order.

% If two outputs are requested, find returns the row and column indices of
% nonzero elements of a matrix. For example:

[i, j] = find (2 * eye (2))



% If three outputs are requested, find also returns a vector containing the
% nonzero values. For example:

[i, j, v] = find (3 * eye (2))


% Note that this function is particularly useful for sparse matrices,
% as it extracts the nonzero elements as vectors, which can then be
% used to create the original matrix. For example:
a = [ 1 2 4; 4 5 6; 7 8 9]
sz = size (a);
[i, j, v] = find (a);
b = sparse (i, j, v, sz(1), sz(2));
