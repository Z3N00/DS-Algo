import java.util.Scanner;

public class exitPoint {
    public static void main(String[] args) {

        Scanner s = new Scanner(System.in);

        int n = s.nextInt();
        int m = s.nextInt();
        int[][] arr = new int[n][m];

        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                arr[i][j] = s.nextInt();
            }
        }

        int i = 0;
        int j = 0;
        int dir = 0; // 0 - e, 1 - s, 2 - w, 3 - n

        while(true){
            dir = (dir + arr[i][j]) % 4;
            if(dir == 0){
                j++;
            }
            if(dir == 1){
                i++;
            }
            if(dir == 2){
                j--;
            }
            if(dir == 3){
                i--;
            }

            if(i<0){
                i++;
                break;
            }
            if(j<0){
                j++;
                break;
            }
            if(i == arr.length){
                i--;
                break;
            }
            if(j==arr[0].length){
                j--;
                break;
            }
        }

        System.out.println(i + "\n" + j);


    }
        
}