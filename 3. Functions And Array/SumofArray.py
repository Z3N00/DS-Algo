arr1 = [1,2,5,4]
arr2 = [2,5,7,8]
new = []
i,j = 0,0
while(i<len(arr1) or j<len(arr2)):

    new.append(arr1[i] + arr2[j])
    i+=1
    j+=1


print(new)

    #     Scanner s = new Scanner(System.in);
    #     int n1 = s.nextInt();
    #     int[] a1 = new int[n1];
    #     for(int i=0; i<a1.length; i++){
    #         a1[i] = s.nextInt();
    #     }
        
    #     int n2 = s.nextInt();
    #     int[] a2 = new int[n2];
    #     for(int i=0; i<a2.length; i++){
    #         a2[i] = s.nextInt();
    #     }
        
    #     int [] sum = new int[n1>n2?n1:n2];
    #     int i = a1.length-1;
    #     int j = a2.length-1;
    #     int k = sum.length-1;
    #     int c = 0;
    #     while(k>=0){
    #         int d = c;
            
    #         if(i>=0){
    #             d+=a1[i];
    #         }
    #         if(j>=0){
    #             d+=a2[j];
    #         }
            
    #         c = d/10;
    #         d = d%10;
           
    #         sum[k] = d;
            
    #         i--;
    #         j--;
    #         k--;
            
    #     }
    #     if(c>0){
    #         System.out.println(c);
    #     }
        
    #     for(int val:sum){
    #         System.out.println(val);
    #     }
    # }