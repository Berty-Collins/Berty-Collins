function intersection = circle_sphere_intersection(circle_center, circle_radius, sphere_center, sphere_radius)
    % Calculate intersection of a circle in 3D with a sphere
    % Circle is in the XY plane, sphere is in 3D space

    % Translate sphere center relative to circle center
    relative_sphere_center = sphere_center - [circle_center, 0];

    % Check if intersection exists
    distance_to_center = norm(relative_sphere_center);
    if distance_to_center > sphere_radius + circle_radius || ...
       distance_to_center < abs(sphere_radius - circle_radius)
        intersection = [];
        return;
    end

    % Compute intersection circle in 3D
    d = norm(relative_sphere_center);
    a = (circle_radius^2 - sphere_radius^2 + d^2) / (2 * d);
    h = sqrt(circle_radius^2 - a^2);
    p = circle_center + a * (relative_sphere_center(1:2) / d);

    % Intersection points
    offset = h * [-relative_sphere_center(2) / d, relative_sphere_center(1) / d];
    intersection = [p + offset, 0; p - offset, 0];
end