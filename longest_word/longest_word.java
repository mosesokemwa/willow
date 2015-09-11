//  Using java, have the function LongestWord(sen) take the sen parameter
//  being passed and return the largest word in the string. If there are two or more 
//  words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty. 


import java.util.*; 
import java.io.*;

class Function {  
  String LongestWord(String sen) { 
  
    // code goes here
	  String[] wordsArray=sen.split(" ");

	  int maxsize = 0;
	  String maxWord = "";

	  	for (int=0; i<wordsArray.length; i++){
			if (wordsArray[i].length()>maxsize){
				maxWord=wordsArray[i];
				maxsize = wordsArray[i].length();
			}
		}
       
    return sen;
    
  } 
  
  public static void main (String[] args) {  
    // the function call should go here    
   
        //not sure at how to do this part
	    // I think i found a way
	  Strings[] food = {"Ugali", "beans", "Chapati" };
	  String sen = getsen(Chapati);
	  System.out.format("longest string: : '%s'\n", sen);

  }

  
}








  
