import com.tinkerforge.BrickletCurrent12;
import com.tinkerforge.IPConnection;

public class ExampleCallback {
	private static final String host = "localhost";
	private static final int port = 4223;
	private static final String UID = "ABC"; // Change to your UID
	
	// Note: To make the example code cleaner we do not handle exceptions. Exceptions you
	//       might normally want to catch are described in the documentation
	public static void main(String args[]) throws Exception {
		IPConnection ipcon = new IPConnection(); // Create IP connection
		BrickletCurrent12 c12 = new BrickletCurrent12(UID, ipcon); // Create device object

		ipcon.connect(host, port); // Connect to brickd
		// Don't use device before ipcon is connected

		// Set Period for current callback to 1s (1000ms)
		// Note: The current callback is only called every second if the 
		//       current has changed since the last call!
		c12.setCurrentCallbackPeriod(1000);

		// Add and implement current listener (called if current changes)
		c12.addCurrentListener(new BrickletCurrent12.CurrentListener() {
			public void current(short current) {
				System.out.println("Current: " + current/1000.0 + " A");
			}
		});

		System.console().readLine("Press key to exit\n");
		ipcon.disconnect();
	}
}
