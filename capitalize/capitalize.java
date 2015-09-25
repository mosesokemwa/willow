// Using java, have the function capitalize(str) take the str parameter being passed and capitalize
// the first letter of each word. Words will be separated by only one space.
// the scanner object should be in the main method, from where we are going to call our function for testing
// it should take string input from a user
<<<<<<< HEAD


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
=======
>>>>>>> 7cccf75f5eeb839e84d646aac854e19e5f5c68c8
