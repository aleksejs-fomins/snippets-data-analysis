function [ value,isterminal,direction ] = myEvents( t,x,N,J)
%EVENTS Summary of this function goes here
%   Detailed explanation goes here

value = 1/(N^2*var(J(:)))*(-x +J*tanh(x))'*(-x +J*tanh(x)) - (10^(-9));
isterminal = 0; %ones(100,1);
direction = 0; %zeros(100,1);

end

