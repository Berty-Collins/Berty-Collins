function animateSphereAndCircles(xCircle1, yCircle1, r1, xCircle2, yCircle2, r2, xSphere, ySphere, rSphere)
    % Parameters
    numFrames = 100;
    theta = linspace(0, 2 * pi, 200); % For precise circle plotting
    sphereScaling = linspace(0.5, 1.5, numFrames); % Sphere scaling factors
    
    % Generate figure and plot handles
    figure;
    hold on;
    axis equal;
    xlim([-100, 100]);
    ylim([-100, 100]);
    zlim([-100, 100]);
    grid on;

    % Initial 3D view setup
    viewAngleAzimuth = 45; % Starting azimuth
    viewAngleElevation = 30; % Starting elevation
    view(viewAngleAzimuth, viewAngleElevation);

    % Plot circles and sphere
    hCircle1 = plot3(xCircle1 + r1 * cos(theta), yCircle1 + r1 * sin(theta), zeros(size(theta)), 'b', 'LineWidth', 1.5);
    hCircle2 = plot3(xCircle2 + r2 * cos(theta), yCircle2 + r2 * sin(theta), zeros(size(theta)), 'r', 'LineWidth', 1.5);
    [X, Y, Z] = sphere(50);
    hSphere = surf(rSphere * X, rSphere * Y, rSphere * Z, 'FaceAlpha', 0.3, 'EdgeColor', 'none');

    % Intersection markers
    hIntersections1 = scatter3([], [], [], 20, 'g', 'filled');
    hIntersections2 = scatter3([], [], [], 20, 'm', 'filled');

    % Animation loop
    for frame = 1:numFrames
        % Update circle positions (sinusoidal motion)
        angleOffset = 2 * pi * frame / numFrames;
        x1 = xCircle1 + 10 * cos(angleOffset);
        y1 = yCircle1 + 10 * sin(angleOffset);
        x2 = xCircle2 + 10 * sin(angleOffset);
        y2 = yCircle2 + 10 * cos(angleOffset);

        % Update circles
        set(hCircle1, 'XData', x1 + r1 * cos(theta), 'YData', y1 + r1 * sin(theta), 'ZData', zeros(size(theta)));
        set(hCircle2, 'XData', x2 + r2 * cos(theta), 'YData', y2 + r2 * sin(theta), 'ZData', zeros(size(theta)));

        % Update sphere size
        scaleFactor = sphereScaling(frame)*2;
        set(hSphere, 'XData', scaleFactor * rSphere * X, 'YData', scaleFactor * rSphere * Y, 'ZData', scaleFactor * rSphere * Z);

        % Calculate intersections for circle 1
        [intX1, intY1, intZ1] = findSphereCircleIntersections(x1, y1, 0, r1, 0, 0, 0, scaleFactor * rSphere);
        % Update intersection markers for circle 1
        set(hIntersections1, 'XData', intX1, 'YData', intY1, 'ZData', intZ1);

        % Calculate intersections for circle 2
        [intX2, intY2, intZ2] = findSphereCircleIntersections(x2, y2, 0, r2, 0, 0, 0, scaleFactor * rSphere);
        % Update intersection markers for circle 2
        set(hIntersections2, 'XData', intX2, 'YData', intY2, 'ZData', intZ2);

        % Update the view to rotate around the sphere
        viewAngleAzimuth = mod(viewAngleAzimuth + 1, 360); % Increment azimuth
        view(viewAngleAzimuth, viewAngleElevation);

        % Pause for animation effect
        pause(0.05);
    end
end