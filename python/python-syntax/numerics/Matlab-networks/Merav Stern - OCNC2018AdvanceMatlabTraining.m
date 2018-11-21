close all;
clear all;

%% Train by batch

N = 1000;
g = 2;
J = g*randn(N)/sqrt(N);
dt = 0.1;
tall = 0:dt:600;
xall = zeros(N,length(tall));

x0 = randn(N,1);
xall(:,1) = x0;
for i = 2:length(tall)
   dx =  -xall(:,i-1)+J*tanh(xall(:,i-1));
   xall(:,i) = xall(:,i-1)+dt*dx;
end

target = 2*sin(2*pi*0.03*tall)+2*cos(3*pi*0.03*tall+pi*0.1);
wout = target*pinv(xall);
z = wout*xall;

figure(1)
subplot(2,1,1)
plot(tall,xall(1:5,:))
title('activity')
subplot(2,1,2)
plot(tall,target)
hold on
plot(tall,z)
legend('target','readout')
hold off

%% look at PCs

% is x was not centered around zero:
for i = 1:N
   xall(i,:) = xall(i,:)-mean(xall(i,:)); 
end
 
C = xall*xall'/(N*length(tall));
[eig_vec,eig_val] = eig(C);
eig_val = flip(diag(eig_val));
new_x = flipud(eig_vec'*xall);
figure(2)
subplot(2,1,1)
plot(eig_val,'o')
title('Eigenvalues')
% or the cumulative variance
%subplot(2,1,1)
%title('Accumulating Sum Eig.')
%plot(cumsum(eig_val)/max(eig_val),'o')
subplot(2,1,2)
plot(tall,new_x(1:5,:))
title('First PCs Dynamics')

%% Train with feedback

wfb = randn(N,1);

for i = 2:length(tall)
   
    dx = dt*J*tanh(xall(:,i-1)) + dt*target(i-1)*wfb;
    xall(:,i) = (1-dt)*xall(:,i-1) + dx;

end

wout = target*pinv(xall);
z = wout*xall;

figure(3)
subplot(2,1,1)
plot(tall,xall(1:5,:))
title('activity')
subplot(2,1,2)
plot(tall,target)
hold on
plot(tall,z)
legend('target','readout')
hold off

%% look at PCs - once again

% is x was not centered around zero:
for i = 1:N
   xall(i,:) = xall(i,:)-mean(xall(i,:)); 
end
 
C = xall*xall'/(N*length(tall));
[eig_vec,eig_val] = eig(C);
eig_val = flip(diag(eig_val));
new_x = flipud(eig_vec'*xall);
figure(4)
subplot(2,1,1)
plot(eig_val,'o')
title('Eigenvalues')
% or the cumulative variance
%subplot(2,1,1)
%title('Accumulating Sum Eig.')
%plot(cumsum(eig_val)/max(eig_val),'o')
subplot(2,1,2)
plot(tall,new_x(1:5,:))
title('First PCs Dynamics')

%% Train with echo state

r = tanh(xall(:,1));
zall = zeros(1,length(tall));
learn_every = 0.773;
P = eye(N);
wout = zeros(1,N);

for i = 2:length(tall)
   
    dx = J*r*dt+target(i-1)*wfb*dt;
    xall(:,i) = (1-dt)*xall(:,i-1) + dx;
    r = tanh(xall(:,i));
    zall(1,i) = wout*r;
    
    if mod(tall(i),learn_every)<dt
        k = P*r;
        rPr = r'*k;
        c = 1/(1+rPr);
        P = P - k*(k'*c);
        e = target(i) - zall(1,i);
        dw = e*k*c;
        wout = wout + dw';
    end

end

figure(5)
subplot(2,1,1)
plot(tall,xall(1:5,:))
title('activity')
subplot(2,1,2)
plot(tall,target)
hold on
plot(tall,zall)
legend('target','readout')
hold off
%% Train with FORCE

r = tanh(xall(:,1));
zall = zeros(1,length(tall));
learn_every = 0.773;
P = eye(N);
wout = zeros(1,N);
zall(1,1) = wout*r;

for i = 2:length(tall)
   
    dx = J*r*dt+zall(1,i-1)*wfb*dt;
    xall(:,i) = (1-dt)*xall(:,i-1) + dx;
    r = tanh(xall(:,i));
    zall(1,i) = wout*r;
    
    %if mod(tall(i),learn_every)<dt
        k = P*r;
        rPr = r'*k;
        c = 1/(1+rPr);
        P = P - k*(k'*c);
        e = target(i) - zall(1,i);
        dw = e*k*c;
        wout = wout + dw';
    %end

end

figure(6)
subplot(2,1,1)
plot(tall,xall(1:5,:))
title('activity')
subplot(2,1,2)
plot(tall,target)
hold on
plot(tall,zall)
legend('target','readout')
hold off

%% keep runing

r = tanh(xall(:,end));
zall(1,1) = zall(1,end);

for i = 2:length(tall)
   
    dx = J*r*dt+zall(1,i-1)*wfb*dt;
    xall(:,i) = (1-dt)*xall(:,i-1) + dx;
    r = tanh(xall(:,i));
    zall(1,i) = wout*r;
    
end

figure(7)
subplot(2,1,1)
plot(tall,xall(1:5,:))
title('activity')
subplot(2,1,2)
%plot(tall,target)
hold on
plot(tall,zall)
legend('target','readout')
hold off

