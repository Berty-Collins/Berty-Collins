function intersections = find_intersections(center1, center2, center3, r1, r2, r3)
    % Initialize storage for intersection points
    intersections = [];

    % Pairwise circle intersections
    pairs = {[center1, r1], [center2, r2]; [center1, r1], [center3, r3]; [center2, r2], [center3, r3]};
    
    for k = 1:size(pairs, 1)
        inters = compute_circle_intersection(pairs{k,1}(1:2), pairs{k,1}(3), pairs{k,2}(1:2), pairs{k,2}(3));
        if ~isempty(inters)
            intersections = [intersections; inters]; %#ok<AGROW>
        end
    end
end