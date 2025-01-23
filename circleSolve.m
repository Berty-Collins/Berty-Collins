% (xCircle,yCircle), radiusCircle - centre & radius of circle
% (xPoint1,yPoint1), (xPoint2,yPoint2), (xPoint3,yPoint3) - points on the circumference of the circle

function [xCircle, yCircle, radiusCircle] = circleSolve(p1,p2,p3)
    x1 = p1(1);
    y1 = p1(2);
    x2 = p2(1);
    y2 = p2(2);
    x3 = p3(1);
    y3 = p3(2);
    
    mid_AB = [(x1 + x2) / 2, (y1 + y2) / 2];
    mid_BC = [(x2 + x3) / 2, (y2 + y3) / 2];
    
    slope_AB = (y2 - y1) / (x2 - x1);
    slope_BC = (y3 - y2) / (x3 - x2);

    perp_slope_AB = -1 / slope_AB;
    perp_slope_BC = -1 / slope_BC;

    syms x y
    eq1 = y - mid_AB(2) == perp_slope_AB * (x - mid_AB(1));
    eq2 = y - mid_BC(2) == perp_slope_BC * (x - mid_BC(1));
    solution = solve([eq1, eq2], [x, y]);
    xCircle = double(solution.x);
    yCircle = double(solution.y);

    radiusCircle = sqrt((xCircle - x1)^2 + (yCircle - y1)^2);
end
