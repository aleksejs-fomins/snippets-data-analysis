clear all;
close all;

%//Read in text and extract properties
BW = imread('../../Pictures/randpic.png');
s  = regionprops(BW, 'Centroid', 'PixelList');

%//Create an array that tells us whether or not we have visited this
%//centroid
centroidVisited = false(length(s),1);

%//Create an array that tells us which object belongs to what cluster
membershipList = zeros(length(s),1);

%//List of all centroids for each object
centroidList = reshape([s.Centroid], 2, length(s)).';

%//Initialize cluster count
clusterNumber = 1;

%//Threshold to figure out what is near
distThreshold = 30;

%//Map that gives us which pixel belongs to which cluster
map = zeros(size(BW));

%//If there are any objects we haven't visited...
while (any(centroidVisited == false))

    %//Find one object
    ind = find(centroidVisited == false, 1);

    %//Extract its centroid
    cent = s(ind).Centroid;

    %//Grab pixels where this object is valid
    pixelLocs = s(ind).PixelList;

    %//Find Euclidean distance squared between this centroid to all the
    %//other centroids
    distCentroids = sum(bsxfun(@minus, cent, centroidList).^2, 2);

    %//Find those locations that are lower than the centroid
    %//Also ensure that we filter out those locations that we have already visited
    belowThresh = find(distCentroids < distThreshold*distThreshold & ...
                       centroidVisited == false);

    %//Mark them as visited
    centroidVisited(belowThresh) = true;

    %//Assign their membership number
    membershipList(belowThresh) = clusterNumber;

    %//For each object that belongs to this cluster, mark them with this
    %//membership number
    for k = 1 : length(belowThresh)
        placesToMark = s(belowThresh(k)).PixelList;
        map(sub2ind(size(BW), placesToMark(:,2), placesToMark(:,1))) = ...
           clusterNumber;
    end

    %//For the next cluster 
   clusterNumber = clusterNumber + 1;    
end

%//Create a colour map that is the same size as the number of clusters
colourMap = jet(clusterNumber);

%//This colour map will contain what letters belong to what cluster (colour
%//coded)
colourMapRed = colourMap(:,1);
colourMapGreen = colourMap(:,2);
colourMapBlue = colourMap(:,3);

mapColumn = map(:) + 1;
redPlane = colourMapRed(mapColumn);
greenPlane = colourMapGreen(mapColumn);
bluePlane = colourMapBlue(mapColumn);

redPlane = reshape(redPlane, size(BW,1), size(BW,2));
greenPlane = reshape(greenPlane, size(BW,1), size(BW,2));
bluePlane = reshape(bluePlane, size(BW,1), size(BW,2));

clusterMapColour = cat(3,redPlane, greenPlane, bluePlane);

figure;
subplot(1,2,1);
imshow(BW);
title('Original Image');
subplot(1,2,2);
imshow(clusterMapColour);
title('Clustered Image');