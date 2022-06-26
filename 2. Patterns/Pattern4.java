 /*  *	*	*	*	*	
        *	*	*	*	
            *	*	*	
                *	*	
                    *
*/

public class Pattern4 {
    public static void main(String[] args) {
        int n = 5;
        for(int i=1; i<=n; i++){
            for(int j=n-i+1; j>=1; j--){
                System.out.print("*\t");
            }
            System.out.println("\n");
            for(int k=1; k<=i; k++){
                System.out.print("\t");
            }

        }
    }
}
