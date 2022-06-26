import java.util.*;
public class primeFactorsOfNum {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int p = 2;
        while(n!=1){
            if(n%p == 0){
                System.out.print(p+" ");
                n =  n / p;
            }
            else{
                p++;
            }
        }
    }
}
