function points = compute_circle_intersection(c1, r1, c2, r2)
    % Calculate distance between centers
    d = norm(c2 - c1);

    % Check for no intersection
    if d > r1 + r2 || d < abs(r1 - r2) || d == 0
        points = [];
        return;
    end

    % Calculate intersection points
    a = (r1^2 - r2^2 + d^2) / (2 * d);
    h = sqrt(r1^2 - a^2);
    p = c1 + a * (c2 - c1) / d;

    % Two intersection points
    offset = h * [-(c2(2) - c1(2)) / d, (c2(1) - c1(1)) / d];
    points = [p + offset; p - offset];
end