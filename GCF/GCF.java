// Using java, have the function divide(num1,num2)
// take both parameters being passed and return the Greatest Common Factor.
// That is, return the greatest number that evenly goes into both numbers with no remainder.
// For example: 20 and 10 both are divisible by 1, 2, 5 and 10 so the output should be 10.
// The range for both parameters will be from 1 to 10^3.

// public class GCF {
//
//
//     public static void main(String [] args){
//
//       System.out.print(divide(54, 24));
//     }
//
//     private static int divide(int num1, int num2) {
//         //base case
//         if(num2 == 0){
//             return num1;
//         }
//         return divide(num2, num1%num2);
//     }
// }


public class GCF {
    public static void main(String [] args){

      System.out.print(divide(54, 24));
    }

    private static int divide(int num1, int num2) {
      //base case
      gcd =  1;

      for (int i = 0; i < (10^3); i++){
        if(num2%i == 0 && num1%i == 0){
          return i;
        gcd += i;
        }
      // return divide(num2, num1%num2);
      }
  }
}
