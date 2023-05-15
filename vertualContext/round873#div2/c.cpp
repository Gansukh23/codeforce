#include<bits/stdc++.h>
#define REP(i,n) for (int i = 1; i <= n; i++)
#define mod 1000000007
#define pb push_back
#define ff first
#define ss second
#define ii pair<int,int>
#define vi vector<int>
#define vii vector<ii>
#define lli long long int
#define INF 1000000000
#define endl '\n'
const double PI = 3.141592653589793238460;
using namespace std;
 
void solve(){
    int n,d;
    string numb;
    cin >> n >> d;
    cin >> numb;
    if(d == 0){
        cout << numb + '0' << endl;
        return;
    }
    for(int i=0;i<n;i++){
        // cout << numb[i] << " ";
        if(numb[i] <= d + '0'){
            numb.insert(i,to_string(d),0);
            cout << numb << endl;
            return;
        }
    }
    cout << numb + to_string(d) << endl;
};
 
int main(){
    int q;
    cin>>q;
        while(q--){
            solve();
        }
}