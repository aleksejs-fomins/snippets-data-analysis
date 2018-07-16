close all;
clear all;

% define the network
N = 1000;
g = 2;
J = g*randn(N)/sqrt(N);

% run
x0 = randn(N,1);
f = @(t,x) -x +J*tanh(x);
trange = [0 200];
[t,y] = ode45(f,trange,x0);

%% plot the activity
figure(1)
plot(t,y(:,1:5))
title('network activity')

%% Euler integration (vs ode)

dt = 0.01;
tall = 0:dt:200;
xall = zeros(N,length(tall));
xall(:,1) = x0;
for i = 2:length(tall)
   dx =  -xall(:,i-1)+J*tanh(xall(:,i-1));
   xall(:,i) = xall(:,i-1)+dt*dx;
end
figure(6)
plot(tall,xall(1:5,:));
title('Activity (Euler integration)')

% to compare
f = @(t,x) -x +J*tanh(x);
[t,y] = ode45(f,tall,x0);
figure(7)
plot(t,y(:,1:5));
title('Activity (ODE (RK) integration)')

%% explore the activity as a function of g (strength of connections)
figure(2)
for i = 1:5
   g = i/2;
   J = g*randn(N)/sqrt(N);
   f = @(t,x) -x +J*tanh(x);
   [t,y] = ode45(f,trange,x0);
   subplot(1,5,i)
   plot(t,y(:,1:5))
   axis([0 200 -10 10])
   title(['g= ' num2str(g)])
end

%% explore the typical time scale as a function of the connection strengths 
figure(3)
trange = 0:0.1:400; % important for correct auto-correlation calculations
for i = 1:5
   g = i/2;
   J = g*randn(N)/sqrt(N);
   f = @(t,x) -x +J*tanh(x);
   [t,y] = ode45(f,trange,x0);
   subplot(2,5,i)
   plot(t,y(:,1:5))
   axis([0 200 -10 10])
   title(['g= ' num2str(g)])
   
   for j = 1:50
       ac(j,:) = xcorr(y(:,j),'unbiased');
   end
   ac = mean(ac);
   subplot(2,5,i+5)
   plot([-fliplr(trange), trange(2:end)],ac)
   axis([-100 100 -1 10])
   title('Average Autocorrelation')
   
end

%% explore different structures of the connectivity matrix

% different degrees of symmetry
figure(4)
for i = 1:10
    alpha = (i-1)/9;
    Jsym = (J+J')/2;
    Jas = J-Jsym;
    Jnew = (alpha)*Jsym + (1-alpha)*Jas;
    f = @(t,x) -x +Jnew*tanh(x);
    [t,y] = ode45(f,trange,x0);
    subplot(1,10,i)
    plot(t,y(:,1:5))
    title(['Symmetry Degree' num2str(alpha)])
end

%% different strength of diagonals (and lets catch fixed points)
figure(5)
for i = 1:5
    Jnew = J+diag(ones(N,1)*i);
    f = @(t,x) -x +Jnew*tanh(x);
    options = odeset('Events',@(t,y) myEvents(t,y,N,Jnew));
    [t,y,te,ye,ie] = ode45(f,t, x0,options);
    subplot(1,5,i)
    plot(t,y(:,1:5))
    if ~isempty(te)
        hold on
        plot(te(1)*ones(5,1),ye(1,1:5),'ro')
        hold off
    end
    title(['Diagonals strength ' num2str(i)])
end

