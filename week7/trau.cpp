#include <iostream>
using namespace std;
int n,m,s[105],tong,a[105];
void alibotto(int i){
    for (int j=0;j<=1;j++){
        s[i] = j;
        tong += j;
        if (tong == m && i == n){
            int tmp = 4095;
            for (int z = 1;z<= n; z++)
                if (s[z] == 1){
                    tmp = tmp & a[z];
                }
            if (tmp == 0) {
                cout<<"YES";
                exit(0);
            }
        }
        else if (i < n)
            alibotto(i+1);
        tong -= j ;
    }
}
int main()
{
    freopen("test.inp","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d%d",&n,&m);
    for (int i=1;i<=n;i++)
        scanf("%d",&a[i]);
    alibotto(1);
    cout<<"NO";
}
