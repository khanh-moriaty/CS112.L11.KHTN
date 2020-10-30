#include <iostream>
using namespace std;
int main(){
    int n,k;
    freopen("test.inp","w",stdout);
    for (int seed = 1; seed <= 100000000; seed++){
        srand(seed);
        n = rand()%20+1;
        k = rand()% n+1;
        printf("%d %d\n",n,k);
        for (int i = 1; i <= n; i++){
            printf("%d ",rand()%4097);
        }
    }
}
