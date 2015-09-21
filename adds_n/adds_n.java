//Using Java, have the function adds_n(num) add up all the numbers from 1 to num.
<<<<<<< HEAD
// num is a number entered in by a user(you) when prompted from the terminal 
//For the test cases, the parameter num will be any number from 1 to 1000. 


import java.util.scanner;
import java.io.*;

class Function {  
  static int adds_n(int num) { 
       if(num > 500){
    	   System.out.print("uknown number");
       }else{
    	   for(int i = 0; i <= num; i++){
    		   System.out.println(i);
    	   }
       }
    return num;
    
  } 
  
  public static void main (String[] args) {  
    // keep this function call here     
    Scanner  s = new Scanner(System.in);
    System.out.print(adds_n(s.nextLine())); 
  }   
  
}




=======
// num is a number entered in by a user(you) when prompted from the terminal
//For the test cases, the parameter num will be any number from 1 to 1000.

import java.util.Scanner;
public class User {
	static int sum = 0;
	static int adds_n(int num) {
		if(num > 1000){
			System.out.println("unknown number");
		}else{
	       for(int i = 0; i <= num; i++){
	    	   sum = sum + i;
	       }
		}
	    return sum;

	  }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner  s = new Scanner(System.in);
		System.out.println("enter an integer betwn 1 - 1000");
	    //Function c = new Function();
	    System.out.print(adds_n(s.nextInt()));
	}

}
>>>>>>> be7de606aeffec9408ed9ac9da88a5543913ebaf
