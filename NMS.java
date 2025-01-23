import java.io.*;
import java.util.logging.Level;

public class NMS {
    public static void main(String[] args) {
        if (args.length != 4) {
            System.out.println("Usage: java NMS <devices.txt> <connections.txt> <startDeviceId> <endDeviceId>");
            return;
        }

        String devicesFile = args[0];
        String connectionsFile = args[1];
        String startDeviceId = args[2];
        String endDeviceId = args[3];

        NetworkDeviceManager deviceManager = new NetworkDeviceManager();
        RouterManager routerManager = new RouterManager();
        LoggingManager logger = new LoggingManager();

        try (BufferedReader devicesReader = new BufferedReader(new FileReader(devicesFile))) {
            String line;
            while ((line = devicesReader.readLine()) != null) {
                String[] parts = line.split(",", 2);
                NetworkDevice device = new NetworkDevice(parts[0].trim(), parts[1].trim());
                deviceManager.addDevice(device);
                routerManager.addDevice(device);
            }
        } catch (IOException e) {
            logger.logError(Level.SEVERE, "Error reading devices file", e);
        }

        try (BufferedReader connectionsReader = new BufferedReader(new FileReader(connectionsFile))) {
            String line;
            while ((line = connectionsReader.readLine()) != null) {
                String[] parts = line.split(",");
                NetworkDevice source = deviceManager.getDevices().stream()
                        .filter(device -> device.getId().equals(parts[0].trim()))
                        .findFirst()
                        .orElse(null);

                NetworkDevice destination = deviceManager.getDevices().stream()
                        .filter(device -> device.getId().equals(parts[1].trim()))
                        .findFirst()
                        .orElse(null);

                if (source != null && destination != null) {
                    routerManager.addRoute(source, destination, 1);
                } else {
                    logger.logEvent(Level.WARNING, "Connection skipped: " + parts[0].trim() + " -> " + parts[1].trim());
                }
            }
        } catch (IOException e) {
            logger.logError(Level.SEVERE, "Error reading connections file", e);
        }

        System.out.println("Optimal route from " + startDeviceId + " to " + endDeviceId + ": " +
                routerManager.getOptimalRoute(startDeviceId, endDeviceId));
    }
}
