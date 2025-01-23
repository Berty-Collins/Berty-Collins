% (xCircle1,yCircle1), radiusCircle1 & (xCircle2,yCircle2), radiusCircle2 - centre & radii of 2 circles
% (xPoint,yPoint) - point
% (xOnCircle,yOnCircle) - closest point on one of the circles
% select - which circle is closest (1 or 2)

function [xOnCircle, yOnCircle, select] = closestPointsOnCircle(xCircle1,yCircle1,radiusCircle1,xCircle2,yCircle2,radiusCircle2,xPoint,yPoint)
    distCircle1 = sqrt((xCircle1-xPoint)^2 + (yCircle1-yPoint)^2) - radiusCircle1;
    distCircle2 = sqrt((xCircle2-xPoint)^2 + (yCircle2-yPoint)^2) - radiusCircle2;
    
    if distCircle1 <= distCircle2
        slope = (yCircle1 - yPoint)/(xCircle1 - xPoint);
        intercept = yCircle1 - slope*xCircle1;
        [xOnCircle,yOnCircle] = linecirc(slope,intercept,xCircle1,yCircle1,radiusCircle1);
        x1 = xOnCircle(1);
        x2 = xOnCircle(2);
        y1 = yOnCircle(1);
        y2 = yOnCircle(2);
        dist1 = sqrt((x1-xPoint)^2 + (y1-yPoint)^2);
        dist2 = sqrt((x2-xPoint)^2 + (y2-yPoint)^2);
        if dist1 <= dist2
            xOnCircle = x1;
            yOnCircle = y1;
        else
            xOnCircle = x2;
            yOnCircle = y2;
        end
        select = 1;
    else
        slope = (yCircle2 - yPoint)/(xCircle2 - xPoint);
        intercept = yCircle2 - slope*xCircle2;
        [xOnCircle,yOnCircle] = linecirc(slope,intercept,xCircle2,yCircle2,radiusCircle2);
        select = 2;
        x1 = xOnCircle(1);
        x2 = xOnCircle(2);
        y1 = yOnCircle(1);
        y2 = yOnCircle(2);
        dist1 = sqrt((x1-xPoint)^2 + (y1-yPoint)^2);
        dist2 = sqrt((x2-xPoint)^2 + (y2-yPoint)^2);
        if dist1 <= dist2
            xOnCircle = x1;
            yOnCircle = y1;
        else
            xOnCircle = x2;
            yOnCircle = y2;
        end
    end
end
