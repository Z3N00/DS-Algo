public class rotate {
    public static void main(String[] args) {
        int n = 562984;
        int k = 2;
        int temp = n;
        int nod = 0;

        while(temp!=0){
            temp = temp/10;
            nod++;
        }

        k = k % nod;
        if(k<0){
            k = k + nod;
        }
        int d = 1;
        int m = 1;
        for(int i=1; i<=nod; i++){
            if(i<=k){
                d = d*10;
            }
            else{
                m = m*10;
            }
        }
        int q = n / d;
        int r = n % d;

        int res = r*m + q;
        System.out.println(res);
    }
}
