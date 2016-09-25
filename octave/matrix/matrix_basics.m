#!/usr/bin/octave -qf
% Author    : Bhishan Poudel
% Date      : May 24, 2016
% Ref       : http://wiki.octave.org/Tips_and_tricks

A = [ 1 2 3; 3 4 34; 5 66 87]  # 3*3 matrix
B = [1 2 1; 3 4 3; 33 55 7]        #   3*3 matrix
y = ones(3,1) # [1;1;1]

C = A + B; # matirx sum
C = A * B; # matrix prod
C = A.*B; # element multiplication
C = A./B; # element division
C = A' # transpose
C = A(3,2) # m,n element of matrix

# comparison to scalar
# A>2 A<2 A==2 A~=2 A>=2 A<=2

%matrix of zeros	A=zeros(m,n)	A.fill(0.0)
%matrix of ones	A=ones(m,n)	A.fill(1.0)
%identity matrix	eye(N)	identity_matrix(N,N)
%inverse of A	inv(A)	A.inverse()
%pseudoinverse of A	pinv(A)	A.pseudo_inverse()
%diagonal elements of A	diag(A)	A.diag()
%column vector	A(:)	ColumnVector(A.reshape (dim_vector(A.length())))
%row vector	A(:)'	RowVector(A.reshape (dim_vector(A.length())))

# add y to the first column of A
size(A)
rows(A) # number of rows = size(A,1)
columns(A)
A(1,:) # 1st row all columns
A(:)   # all elements in one column (transpose gives row)
A(:,1) # 1st clm all rows

#stack two matrices horizontally (; stacks vertically)
C=[y,A]

#sum squares of columns
A
A .^2
sumsq(A)

# sum along columns and rows
A
sum(A,1) # sum along columns gives rows
# cumsum along columns
A
cumsum(A,1) # similarly cumprod

# product along columns
A
prod(A,1)

# repetition of matrix
A
repmat(A,3,1)  # m*n = 3*1 matrix using matrix block A
repmat(A,1,3)  # m*n = 1*3 matrix using matrix block A


