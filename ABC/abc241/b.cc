#include <bits/stdc++.h>
using namespace std;

int main() {
  int n,m;
  cin >> n >> m;
  int a[n];
  int b[m];
  for (int i = 0; i < n; i++){
    cin >> a[i];
  }
  for (int i = 0; i < m; i++){
    cin >> b[i];
  }
   for (int i = 0; i < m; i++){
     bool c = false;
     for(int j = 0; j < n; j++){
       if (b[i] == a[j]){
         c = true;
         a[j] = 0;
         break;
       }
     }
     if (c == false){
       cout << "No" << endl;
       return 0;
     }
  }
  cout << "Yes" << endl;

}