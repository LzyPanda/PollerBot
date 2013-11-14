package truck;

import com.tinkerforge.BrickMaster;
import com.tinkerforge.IPConnection;

public class ExampleStackStatus {
	private static final String host = "localhost";
	private static final int port = 4223;
	private static final String UID = "";

	
	public static void main(String args[]) throws Exception {
		IPConnection ipcon = new IPConnection();
		BrickMaster master = new BrickMaster(UID, ipcon);
		
		ipcon.connect(host, port);
		
		int voltage = master.getStackVoltage();
		int current = master.getStackCurrent();

		System.out.println("Stack Voltage: " + voltage/1000.0 + " V");
		System.out.println("Stack Current: " + current/1000.0 + " A");

		ipcon.disconnect();
	}
}
