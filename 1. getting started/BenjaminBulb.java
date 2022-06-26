import java.util.*;

public class BenjaminBulb {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();

        for(int i=1; i*i<=n; i++){
            System.out.println(i*i);
        }
    }
    
}
