%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% define a function
%In your current working folder, create a function, findSqrRootIndex,
%to find the index of the first occurrence of the square root of a value
%within an array. If the square root isn't found, the function returns NaN.

function idx = findSqrRootIndex(target,arrayToSearch)

idx = NaN;
if target < 0
   return
end

for idx = 1:length(arrayToSearch)
    if arrayToSearch(idx) == sqrt(target)
        return
    end
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
