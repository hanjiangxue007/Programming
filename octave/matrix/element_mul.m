#!/usr/bin/octave
% Author   : Bhishan Poudel
% Date     : May 23, 2016
# Ref      : https://stackoverflow.com/questions/7858589/element-wise-multiplication-of-a-matrix-and-a-vector

% element-wise matrix multiplication by a vector
A = [1 2; 3 4; 5 6]
B = [1; 2; 3] # 3*1

# using repmat (repeat matrix)
A .* repmat(B, 1, columns(A))

size(A,1) # number of rows
rows(A)
columns(A) # 2

%repmat(B,2)    # B,1 is same as B
%repmat(B,3)    # 3 times in a row, 3 times in a column (square matrix)
%repmat(B,3,1)  # m*n = 3*1 matrix using matrix block B
%repmat(B,1,3)  # m*n = 1*3 matrix using matrix block B
%repmat(B,1,2,2) # very large matrix
