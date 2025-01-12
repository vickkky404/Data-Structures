#include<bits/stdc++.h>
using namespace std;
int cnt = 0;

void print(){

    // base condition
    if(cnt == 3) return;
    cout<<cnt<<endl;

    // cout Incriment
    cnt++;
    print();
}
int main(){
    print();
    return 0;
}
