function hCircle = plotCircle3D(xCenter, yCenter, radius, color)
    % Generate circle points
    theta = linspace(0, 2 * pi, 100);
    x = xCenter + radius * cos(theta);
    y = yCenter + radius * sin(theta);
    z = zeros(size(x));
    hCircle = plot3(x, y, z, color, 'LineWidth', 2);
end