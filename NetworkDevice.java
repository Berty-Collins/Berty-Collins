public class NetworkDevice {
    private String id;
    private String type;
    private DeviceConfiguration configuration;

    public NetworkDevice(String id, String type) {
        this.id = id;
        this.type = type;
    }

    public String getId() {
        return id;
    }

    public String getType() {
        return type;
    }

    public DeviceConfiguration getConfiguration() {
        return configuration;
    }

    public void setConfiguration(DeviceConfiguration configuration) {
        this.configuration = configuration;
    }

    @Override
    public String toString() {
        return "NetworkDevice{id='" + id + "', type='" + type + "', configuration=" + configuration + '}';
    }
}
