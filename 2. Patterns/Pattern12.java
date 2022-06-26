/*
0	
1	1	
2	3	5	
8	13	21	34	
55	89	144	233	377

*/

public class Pattern12 {
    public static void main(String[] args) {
        int n = 5;
        int first = 0;
        int second = 1;
        int temp;

        for(int i=1; i<=n; i++){
            for(int j=1; j<=i; j++){
            System.out.print(first+"\t");
            temp = first;
            first = second;
            second = temp + first;
            }
            System.out.println();
        }
    }
}
