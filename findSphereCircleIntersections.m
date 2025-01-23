function [intX, intY, intZ] = findSphereCircleIntersections(xC, yC, zC, rC, xS, yS, zS, rS)
    % Translate circle center to sphere's origin
    dx = xC - xS;
    dy = yC - yS;
    dz = zC - zS;
    
    % Distance between sphere and circle center
    d = sqrt(dx^2 + dy^2 + dz^2);

    % Check for intersection
    if d > rC + rS || d < abs(rC - rS)
        % No intersection
        intX = [];
        intY = [];
        intZ = [];
        return;
    end

    % Find intersection points in parametric form
    a = (rS^2 - rC^2 + d^2) / (2 * d);
    h = sqrt(rS^2 - a^2);

    % Base point for intersections
    px = xS + a * dx / d;
    py = yS + a * dy / d;
    pz = zS + a * dz / d;

    % Intersection offsets
    rx = -h * dy / d;
    ry = h * dx / d;

    % Calculate intersection points
    intX = [px + rx, px - rx];
    intY = [py + ry, py - ry];
    intZ = [pz, pz];
end