/*
		1	
	2	3	2	
3	4	5	4	3	
	2	3	2	
		1	

*/


public class Pattern15 {
    public static void main(String[] args) {
        int n = 5;
        int space = n/2;
        int col = 1;
        int val;
        int c = 1;
        for(int i=1; i<=n; i++){
            for(int j=1; j<=space; j++){
                System.out.print("\t");
            }
            val = c;
            for(int j=1; j<=col; j++){
                System.out.print(val + "\t");
                if(j<=col/2){
                    val++;
                }
                else{
                    val--;
                }
            }
            if(i<=n/2){
                space--;
                col+= 2;
                c+=1;
            }else{
                space++;
                col-=2;
                c--;
            }
            System.out.println();
        }
    }
}
