#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pair_t;

int main() {
  int n;
  cin >> n;
  vector<pair_t> x(n);
 
  for (int i = 0; i < n; i++){
    cin >>x[i].first >> x[i].second;
  }
  string s;
  cin >> s;
  int count = 0;
  for (int i = 0; i < n; i++){
    if (int(s[i]) == 76){
      count ++;
    }
  }
  int l[count];
  int r[n-count];
  int li = 0;
  int ri = 0;
  for (int i = 0; i < n; i++){
    if (int(s[i]) == 76){
      l[li] = i;
      li ++;
    }else{
      r[ri] = i;
      ri ++;
    }
  }
  for (int i = 0; i < count; i++){
    for (int j = 0; j< (n - count); j++){
      if (x[l[i]].second == x[r[j]].second){
        if(x[l[i]].first > x[r[j]].first){
          cout << "Yes" << endl;
          return 0;
        }
      }
    }
  }
  cout << "No" << endl;
  
}