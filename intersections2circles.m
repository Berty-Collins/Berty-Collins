% (xCircle1,yCircle1), radiusCircle1 & (xCircle2,yCircle2), radiusCircle2 - centre & radii of 2 circles
% intersections - coordinates of intersections, one intersection per row; there will be 0, 1 or 2 rows

function [x_intersections, y_intersections] = intersections2circles(radiusCircle1,xCircle1,yCircle1,radiusCircle2,xCircle2,yCircle2)
    
    syms x y
    eq1 = (x - xCircle1)^2 + (y - yCircle1)^2 == radiusCircle1^2; % Circle 1 equation
    eq2 = (x - xCircle2)^2 + (y - yCircle2)^2 == radiusCircle2^2; % Circle 2 equation

    solutions = solve([eq1, eq2], [x, y]);

    x_intersections = double(solutions.x);
    y_intersections = double(solutions.y);

   
end
