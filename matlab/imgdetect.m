Im = imread('../../Pictures/testrec.png');
ImGray = rgb2gray(Im);
BW = imbinarize(Im); 
cc = bwconncomp(ImGray);
lmat = labelmatrix(cc);


lmat2 = watershed(BW);

%lrgb = label2rgb(lmat2);
figure, imshow(lmat2);