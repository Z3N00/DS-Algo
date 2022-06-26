import java.util.*;
public class fibonaci {
    public static void main(String[] args) {
        
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int first=0, second=1, temp;
        for(int i=0; i<n; i++){
            System.out.println(first);
            temp = first + second;
            first = second;
            second = temp;
            
        }
        
    }
}
