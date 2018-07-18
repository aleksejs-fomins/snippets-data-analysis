Im = imread('../../Pictures/testrec.png');
bw = rgb2gray(Im);
figure
imshow(bw,'InitialMagnification','fit'), title('bw')

%Compute the distance transform of the complement of the binary image.
D = bwdist(~bw);
figure
imshow(D,[],'InitialMagnification','fit')
title('Distance transform of ~bw')

%Complement the distance transform, and force pixels that don't belong to the objects to be at Inf .
D = -D;
D(~bw) = Inf;

%Compute the watershed transform and display the resulting label matrix as an RGB image.
L = watershed(D);
L(~bw) = 0;
rgb = label2rgb(L,'jet',[.5 .5 .5]);
figure
imshow(rgb,'InitialMagnification','fit')
title('Watershed transform of D')