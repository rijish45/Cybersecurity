//Rijish Ganguly
//rg239


import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.net.Socket;
import java.util.Scanner;
 
public class getbanner {
  

   
 
  public static void main(String[] args) throws IOException {

    //Create a Scanner
    Scanner read = new Scanner(System.in);
    Boolean error = false;

	String REMOTE_HOST;
	int PORT;
            
    //Take input from command line for host and port number
    //Make the server listen to the port using ns -l PORT


    System.out.println("Kindly Enter hostname: ");
    REMOTE_HOST = read.next();
			
	  System.out.println("Kindly Enter port: ");
	  PORT = read.nextInt();
		

    // Make a TCP connection to the remote process.
    Socket socket = new Socket(REMOTE_HOST, PORT);
    BufferedWriter socketOut = new BufferedWriter(
        new OutputStreamWriter(socket.getOutputStream()));
    BufferedReader socketIn = new BufferedReader(
        new InputStreamReader(socket.getInputStream()));
 
     
     //Send "QUIT\n to the remote host"

      String textString = "Quit\n";
      socketOut.write(textString, 0, textString.length());
      socketOut.newLine();
      socketOut.flush();
 


    for (;;) {
     
      //Read everything the client sends
      String response = socketIn.readLine();
      if (response == null) {
        System.out.println("Server disconnected.");
        break;
      }
      else
      {
      System.out.println("Got this as a response:");
      System.out.println(response);
      System.out.println();
	  }
    }
  }
}
