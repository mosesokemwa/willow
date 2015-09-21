//Using Java, have the function adds_n(num) add up all the numbers from 1 to num.
// num is a number entered in by a user(you) when prompted from the terminal 
//For the test cases, the parameter num will be any number from 1 to 1000. 

import java.util.Scanner;
public class User {
	
	static int adds_n(int num) { 
		if(num > 1000){
			System.out.println("unknown number");
		}else{
	       for(int i = 0; i <= num; i++){
	    	   System.out.println(i);	
	       }
		}
	    return num;
	    
	  } 
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner  s = new Scanner(System.in);
	    	System.out.print(adds_n(s.nextInt()));
	}

}





