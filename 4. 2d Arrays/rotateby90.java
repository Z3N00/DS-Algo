import java.util.*;

public class rotateby90 {
    

    public static void main(String[] args) {
        
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();

        int[][] arr = new int[n][n];
        int[][] newarr = new int[n][n];

        for(int i=0; i<n ; i++){
            for(int j=0; j<n; j++){
                arr[i][j] = s.nextInt();
            }
        }

        int a = 0;
        int b = 0;

        while(a<n && b<n){
            for(int j=0; j<n; j++){
                for(int i=n-1; i>=0; i--){
                    newarr[a][b] = arr[i][j];
                    b++;
                }
                b=0;
                a++;
            }
        }

        System.out.println("--------------------------------");
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                
                System.out.println(newarr[i][j]);

            }
        }

    }
}
