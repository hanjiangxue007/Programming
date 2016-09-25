#!/usr/bin/octave -qf
% Author    : Bhishan Poudel
% Date      : May 26, 2016
% Topic     : repmat (repetitions of matirx)

A = [ 1 2 3; 3 4 5; 6 7 8];  # 3*3 matrix

# repetition of matrix
A;
repmat_A_3_1 = repmat(A,3,1);  # m*n = 3*1 matrix using matrix block A
repmat_A_1_3 = repmat(A,1,3); # m*n = 1*3 matrix using matrix block A

X = [ ...
   2104      3; ...
   1600      3; ...
   2400      3; ...
   1416      2; ...
   3000      4; ...
   1985      4; ...
   1534      3; ...
   1427      3; ...
   1380      3; ...
   1494      3 ]

size_X = size(X) % 10*2

% we want to normalize each columns of X
X_norm = X;
mu = zeros(1, size(X, 2));    % size(X,2) = columns(X), [0 0] zero row vector 1*2
sigma = zeros(1, size(X, 2));

mu = mean(X_norm);   % 1834.0000      3.1000
sigma = std(X_norm); % 535.66760     0.56765


% general method %%
X_col1 = X(:,1);
X_col2 = X(:,2);

X_col1_mean = mean(X_col1);
X_col2_mean = mean(X_col2);
mu = [X_col1_mean X_col2_mean]

X_col1_std = std(X_col1);
X_col2_std = std(X_col2);
sigma = [X_col1_std X_col2_std];
%%%%%%%%%%%%%%%%%%%%%%
length_X_norm = length(X_norm)
repmat_mu_rows = repmat(mu,length(X_norm),1)
size_X_norm = size(X_norm)
size_repmat_mu_rows = size(repmat_mu_rows)

%% normalization of matrix columns
%% tf = transfer function
% we can write mu_sizeX and std_sizeA
tf_mu = X_norm - repmat(mu,length(X_norm),1);
tf_std = repmat(sigma,length(X_norm),1);

X_norm = tf_mu ./ tf_std;
