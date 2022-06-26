/*

1												1	
1	2										2	1	
1	2	3								3	2	1	
1	2	3	4						4	3	2	1	
1	2	3	4	5				5	4	3	2	1	
1	2	3	4	5	6		6	5	4	3	2	1	
1	2	3	4	5	6	7	6	5	4	3	2	1	

*/



public class Pattern16 {
    public static void main(String[] args) {
        int n = 7;
        int st = 1;
        int space = 2*n-3;
        
        for(int i=1; i<=n; i++){
            int val = 1;
            for(int j=1; j<=st; j++){
                System.out.print(val + "\t");
                val++;
            }

            for(int k=1; k<=space; k++){
                System.out.print("\t");
            }
            if(i==n){
                st--;
                val--;
            }
            for(int j=1; j<=st; j++){
                val--;
                System.out.print(val + "\t");
                
            }
            st++;
            space-=2;
            System.out.println();

            
        }
        
    }
}

