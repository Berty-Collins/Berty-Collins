% m,c - parameters of bisector line y = mx + c
% (xOffBisector,yOffBisector) - point not on the bisector line
% (xOnBisector,yOnBisector) - point on the bisector line

function [xOnBisector, yOnBisector] = closestPointBisector(m,c,xOffBisector,yOffBisector)
    c2 = yOffBisector - (-1/m)*xOffBisector;
    xOnBisector = (c2 - c)/(m - (-1/m));
    yOnBisector = m*xOnBisector + c;
end
