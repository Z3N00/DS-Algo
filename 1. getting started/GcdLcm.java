import java.util.*;

public class GcdLcm {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        int num1 =  s.nextInt();
        int num2 = s.nextInt();
        int n1=num1, n2=num2;
        while(num1 != num2){
            if(num1 > num2){
                num1 = num1 - num2;
            }else{
                num2 = num2 - num1;
            }
        }
        int gcd = num1;
        System.out.println(gcd);
        System.out.println((n1*n2)/gcd);
    }
}
