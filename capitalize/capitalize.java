// Using java, have the function capitalize(str) take the str parameter being passed and capitalize
// the first letter of each word. Words will be separated by only one space.
// use the main method for testing and call the function from the main method
// it should take string input from a user



import java.util.Scanner;
import java.util.Arrays;

public class capitalize(str) {
	
	String[] token = str.split(" ");
	
	for(int i = 0; i < token.length; ++i) {
		if(token[i].length() > 0) {
        	char[] digit = token[i].toCharArray();
	        	digit[0] = Character.toUpperCase(digit[0]);
	        	token[i] = new String(digit);
		}
	    else {
	        System.out.print(" ");
		    }
    return token;
	}

	public static void main(String[] args) {

		
		System.out.print("Hi, type in your sentence: ");
		
		Scanner input = new Scanner(System.in);
		String token = input.nextLine();
		
		System.out.println(token);

	}

}
