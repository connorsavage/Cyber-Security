import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.util.Arrays;

public class PacketSniffer {
    public static void main(String[] args) throws IOException {
        // create a datagram socket that listens to all incoming traffic
        DatagramSocket sniffer = new DatagramSocket(0, InetAddress.getByName("0.0.0.0"));
        // specify which interface to listen on (leave blank to listen on all interfaces)
        // sniffer.bind(new InetSocketAddress("eth0", 0));

        // receive packets forever
        while (true) {
            // create a buffer to hold the packet data
            byte[] buffer = new byte[65565];
            // receive a packet
            DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
            sniffer.receive(packet);
            // get the packet data
            byte[] data = Arrays.copyOfRange(packet.getData(), packet.getOffset(), packet.getLength());
            // get the source and destination IP addresses
            InetAddress srcIp = packet.getAddress();
            InetAddress dstIp = InetAddress.getByAddress(Arrays.copyOfRange(data, 16, 20));
            // print the source and destination IP addresses
            System.out.println("Source IP: " + srcIp + "\tDestination IP: " + dstIp);
        }
    }
}