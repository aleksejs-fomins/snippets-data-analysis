% Generate cell array of random reals ints with random length and sublength

randDim0 = [1 100];
randDim1 = [1 100];
randRange = [0 1];

myArray = [];
L0 = randi(randDim0);

TotRand = 0;
for i = 1:L0 
  L1 = randi(randDim1);
  myArray{i} = randRange(1) + randRange(2) * rand(1, L1);
  TotRand = TotRand + L1;
end

fprintf("There are %d cells and total of %d random numbers \n", L0, TotRand);

% Create a new cell array that only has random numbers from first array, if
% larger than 0.5

TotRand2 = 0;
myArray2 = []
for i = 1:L0 
  myArray2{i} = myArray{i}(myArray{i} > 0.5);
  tmp = size(myArray2{i});
  TotRand2 = TotRand2 + tmp(2);
end

fprintf("There are %d cells and total of %d random numbers \n", L0, TotRand);

% A = [];
% 
% for i = 0:99
%   if (mod(i, 2))
%     A(end + 1) = i;
%   end
% end
% 
% A