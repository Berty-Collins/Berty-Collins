function animate_circles(xCircle1,yCircle1,radius1,xCircle2,yCircle2,radius2,xCircle3,yCircle3,radius3)
    % Circle properties
    circle1_center = [xCircle1, yCircle1];
    circle2_center = [xCircle2, yCircle2];
    circle3_center = [xCircle3, yCircle3];

    % Create figure
    figure;
    axis equal;
    hold on;
    xlim([-100, 100]);
    ylim([-100, 100]);

    % Plot initial circles
    theta = linspace(0, 2*pi, 500);
    circle1_plot = plot(circle1_center(1) + radius1*cos(theta), circle1_center(2) + radius1*sin(theta), 'r');
    circle2_plot = plot(circle2_center(1) + radius2*cos(theta), circle2_center(2) + radius2*sin(theta), 'g');
    circle3_plot = plot(circle3_center(1) + radius3*cos(theta), circle3_center(2) + radius3*sin(theta), 'b');
    
    % Intersection markers
    intersection_plot = plot(0, 0, 'ko', 'MarkerSize', 5, 'MarkerFaceColor', 'k');
    
    % Animation parameters
    total_steps = 300; % Total number of steps
    steps_per_cycle = 150; % Steps for each in-and-out motion
    
    % Animation loop
    for t = 1:total_steps
        % Calculate the "phase" for the current step
        phase = mod(t, steps_per_cycle) / steps_per_cycle; % From 0 to 1

        % Calculate the center positions based on the phase
        if phase <= 0.5
            % Moving towards the origin
            factor = 1 - 2 * phase; % Linearly decrease from 1 to 0
        else
            % Moving apart from the origin
            factor = -1 + 2 * (phase - 0.5); % Linearly increase from 0 to 1
        end

        circle1_center_current = circle1_center * factor;
        circle2_center_current = circle2_center * factor;
        circle3_center_current = circle3_center * factor;

        % Update circle plots
        set(circle1_plot, 'XData', circle1_center_current(1) + radius1*cos(theta), 'YData', circle1_center_current(2) + radius1*sin(theta));
        set(circle2_plot, 'XData', circle2_center_current(1) + radius2*cos(theta), 'YData', circle2_center_current(2) + radius2*sin(theta));
        set(circle3_plot, 'XData', circle3_center_current(1) + radius3*cos(theta), 'YData', circle3_center_current(2) + radius3*sin(theta));

        % Find and plot intersections
        intersections = find_intersections(circle1_center_current, circle2_center_current, ...
                                           circle3_center_current, radius1, radius2, radius3);
        if ~isempty(intersections)
            set(intersection_plot, 'XData', intersections(:,1), 'YData', intersections(:,2));
        else
            set(intersection_plot, 'XData', [], 'YData', []);
        end

        % Pause for animation
        pause(0.02);
    end
end
