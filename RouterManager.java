import java.util.*;

public class RouterManager {
    private Map<String, List<String>> connections = new HashMap<>();

    public void addDevice(NetworkDevice device) {
        connections.putIfAbsent(device.getId(), new ArrayList<>());
    }

    public void addRoute(NetworkDevice source, NetworkDevice destination, int weight) {
        if (connections.containsKey(source.getId()) && connections.containsKey(destination.getId())) {
            connections.get(source.getId()).add(destination.getId());
            connections.get(destination.getId()).add(source.getId());
        } else {
            throw new IllegalArgumentException(
                    "One or both devices not found in RouterManager: " + source.getId() + ", " + destination.getId());
        }
    }

    public List<String> getOptimalRoute(String sourceId, String destinationId) {
        Queue<String> queue = new LinkedList<>();
        Map<String, String> previous = new HashMap<>();
        Set<String> visited = new HashSet<>();

        queue.add(sourceId);
        visited.add(sourceId);

        while (!queue.isEmpty()) {
            String current = queue.poll();
            if (current.equals(destinationId)) {
                return constructPath(previous, sourceId, destinationId);
            }

            for (String neighbor : connections.getOrDefault(current, new ArrayList<>())) {
                if (!visited.contains(neighbor)) {
                    visited.add(neighbor);
                    queue.add(neighbor);
                    previous.put(neighbor, current);
                }
            }
        }

        return Collections.emptyList(); // No path found
    }

    private List<String> constructPath(Map<String, String> previous, String start, String end) {
        List<String> path = new LinkedList<>();
        for (String at = end; at != null; at = previous.get(at)) {
            path.add(0, at);
        }
        return path;
    }
}
