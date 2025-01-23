public class DeviceConfiguration {
    private String interfaceType;
    private String macAddress;
    private String ipv4Address;
    private String subnet;

    public DeviceConfiguration(String interfaceType, String macAddress, String ipv4Address, String subnet) {
        this.interfaceType = interfaceType;
        this.macAddress = macAddress;
        this.ipv4Address = ipv4Address;
        this.subnet = subnet;
    }

    @Override
    public String toString() {
        return "DeviceConfiguration{interfaceType='" + interfaceType + "', macAddress='" + macAddress +
                "', ipv4Address='" + ipv4Address + "', subnet='" + subnet + "'}";
    }
}
