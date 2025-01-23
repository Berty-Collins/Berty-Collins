% (xCircle1,yCircle1) & (xCircle2,yCircle2) - centre of 2 circles
% (xPoint1,yPoint1) - point on the circumference of circle #1
% radiusCircle2 - radius of circle #2

function radiusCircle2 = radiusTangentialCircle(xCircle1,yCircle1,xPoint1,yPoint1,xCircle2,yCircle2)
        radius = sqrt((xCircle1-xPoint1)^2 + (yCircle1-yPoint1)^2);
        radiusCircle2 = sqrt((xCircle1-xCircle2)^2 + (yCircle1-yCircle2)^2) - radius;
end
