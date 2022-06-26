import java.util.Scanner;

public class prime {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int t = s.nextInt();
        
        for (int i = 1; i<=t; i++){
            int n = s.nextInt();
            boolean flag = false;
            int j = 2;
            while(j*j<=n){
                if(n%j==0){
                    flag = true;
                    break;
                }
                j++;
            }
            if (flag == true){
                System.out.println("not prime");
            }else{
                System.out.println("prime");
            }
        } 
    }
    
}