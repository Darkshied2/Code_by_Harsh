//  sort color solution in C (leetcode).

void sortColors(int* nums, int numsSize){
int count=0,flag=0,git=0;
    int k=0;
    // int x[100];y[100];z[100];
    for(int i=0;i<numsSize;i++)
    {
        if(nums[i]==0)
            count++;
        else if (nums[i]==1)
            flag++;
        else if (nums[i]==2)
            git++;
    }
       for (int i=0;i<count;i++)
       {
         nums[k]=0;
           k++;
       }
    for (int i=0;i<flag;i++)
       {
         nums[k]=1;
           k++;
       }
    for (int i=0;i<git;i++)
       {
         nums[k]=2;
           k++;
       }
    
}