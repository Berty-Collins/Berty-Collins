import java.util.ArrayList;
import java.util.List;

public class NetworkDeviceManager {
    private List<NetworkDevice> devices = new ArrayList<>();

    public void addDevice(NetworkDevice device) {
        devices.add(device);
        System.out.println("Added device: " + device);
    }

    public void removeDevice(String deviceId) {
        devices.removeIf(device -> device.getId().equals(deviceId));
        System.out.println("Removed device with ID: " + deviceId);
    }

    public void configureDevice(String deviceId, DeviceConfiguration config) {
        for (NetworkDevice device : devices) {
            if (device.getId().equals(deviceId)) {
                device.setConfiguration(config);
                System.out.println("Configured device: " + device);
                return;
            }
        }
        System.out.println("Device with ID " + deviceId + " not found.");
    }

    public List<NetworkDevice> getDevices() {
        return devices;
    }
}
