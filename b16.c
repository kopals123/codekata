#include <stdio.h>
int main()
{
    int low, high, z, flag;
    scanf("%d %d", &low, &high);
    while (low < high)
    {
        flag = 0;
        for(z = 2; z <= low/2; ++z)
        {
            if(low % z == 0)
            {
                flag = 1;
                break;
            }
        }
        if (flag == 0)
            printf("%d ", low);
        ++low;
    }
    return 0;
}
