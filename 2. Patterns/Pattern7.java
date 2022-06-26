/*

*	
	*	
		*	
			*	
				*	


*/




public class Pattern7 {
    public static void main(String[] args) {
        int n = 5;
        int space = 1;

        for(int i=1; i<=n; i++){
            System.out.println("*");
            
            for(int j=1; j<=space; j++){
                System.out.print("\t");
            }
            space++;
        }
    }
}
