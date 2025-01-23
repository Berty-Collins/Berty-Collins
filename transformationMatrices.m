% (xCircle1,yCircle1), (xCircle2,yCircle2), (xCircle3,yCircle3) - centres of 3 circles
% matrixT - translation matrix
% matrixR - rotation matrix
% matrixCombined - translation and rotation matrix
function [matrixT, matrixR, matrixCombined] = transformationMatrices(xCircle1, yCircle1, xCircle2, yCircle2, xCircle3, yCircle3)
    % Translate so the third circle is at the origin
    tX = -xCircle3;
    tY = -yCircle3;

    matrixT = [1, 0, tX;
               0, 1, tY;
               0, 0, 1];
    
    % Compute the angle of the line connecting centers
    deltaX = xCircle2 - xCircle1;
    deltaY = yCircle2 - yCircle1;
    theta = atan2(deltaY, deltaX); % Angle of the connecting line
    
    % Create a rotation matrix to rotate -theta about the origin
    matrixR = [cos(-theta), -sin(-theta), 0;
               sin(-theta), cos(-theta), 0;
               0, 0, 1];
    
    % Combine translation and rotation
    matrixCombined = matrixR * matrixT;
    
end
