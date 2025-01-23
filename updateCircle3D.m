function updateCircle3D(hCircle, xCenter, yCenter, radius)
    % Generate new circle points
    theta = linspace(0, 2 * pi, 100);
    x = xCenter + radius * cos(theta);
    y = yCenter + radius * sin(theta);
    z = zeros(size(x));
    % Update circle plot
    set(hCircle, 'XData', x, 'YData', y, 'ZData', z);
end