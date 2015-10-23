// Using java solve the problem below:
// Given an array of integers, find the maximum and minimum of this array.


public class maximum_and_minimum{

  public static void main(String args[]){
    int array[] = new int[]{10, 11, 88, 2, 12, 120};

    // Calling getMax() method for getting max value
    int max = getMax(array);
    System.out.println("Maximum Value is: " + max);

    // Calling getMin() method for getting min value
    int min = getMin(array);
    System.out.println("Minimum Value is: "+min);
  }

  // Method for getting the max value
  public static int getMax(int[] intArr){
    int maxValue = intArr[0];
    for(int i = 1; i < intArr.length; i++){
      if(intArr[i] > maxValue){
         maxValue = intArr[i];
      }
    }
    return maxValue;
  }

  // Method for getting the min value
  public static int getMin(int[] intArr){
    int minValue = intArr[0];
    for(int i = 1; i<intArr.length; i++){
      if(intArr[i] < minValue){
        minValue = intArr[i];
      }
    }
    return minValue;
  }

}

//in python

//def findSmallestInt(arr):
//    return min(arr)
//    return max(arr)

