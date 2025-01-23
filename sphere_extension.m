function sphere_extension(xCircle1, yCircle1, radius1, xCircle2, yCircle2, radius2, xCircle3, yCircle3, radius3)
    % Sphere parameters
    sphere_center = [xCircle3, yCircle3, 0]; % Center at xCircle3, yCircle3
    sphere_radius = radius3; % Radius of the sphere

    % Create figure
    figure;
    hold on;
    axis equal;
    xlim([-100, 100]);
    ylim([-100, 100]);
    zlim([-100, 100]);
    grid on;

    % Plot circles
    theta = linspace(0, 2*pi, 500);
    plot3(xCircle1 + radius1*cos(theta), ...
          yCircle1 + radius1*sin(theta), ...
          zeros(1, numel(theta)), 'r', 'LineWidth', 1.5);
    plot3(xCircle2 + radius2*cos(theta), ...
          yCircle2 + radius2*sin(theta), ...
          zeros(1, numel(theta)), 'g', 'LineWidth', 1.5);

    % Plot sphere
    [X, Y, Z] = sphere(50);
    X = X * sphere_radius + sphere_center(1);
    Y = Y * sphere_radius + sphere_center(2);
    Z = Z * sphere_radius + sphere_center(3);
    surf(X, Y, Z, 'FaceAlpha', 0.3, 'EdgeColor', 'none', 'FaceColor', 'b');

    % Find and plot intersections
    intersection1 = circle_sphere_intersection([xCircle1, yCircle1], radius1, sphere_center, sphere_radius);
    intersection2 = circle_sphere_intersection([xCircle2, yCircle2], radius2, sphere_center, sphere_radius);

    % Plot intersection points if they exist
    if ~isempty(intersection1)
        plot3(intersection1(:,1), intersection1(:,2), intersection1(:,3), 'ko', 'MarkerSize', 5, 'MarkerFaceColor', 'k');
    end
    if ~isempty(intersection2)
        plot3(intersection2(:,1), intersection2(:,2), intersection2(:,3), 'ko', 'MarkerSize', 5, 'MarkerFaceColor', 'k');
    end

    title('Circles and Sphere Intersections');
    xlabel('X');
    ylabel('Y');
    zlabel('Z');
end