#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;
  int a[n];
  int b[n];
  for (int i = 0; i < n; i++){
    cin >> a[i];
  }
  for (int i = 0; i < n; i++){
    cin >> b[i];
  }
  int answer_1 = 0;
  for (int i = 0; i < n; i++){
    if(a[i] == b[i]){
      answer_1 ++;
    }
  }
  int count = 0;
  for (int i = 0; i < n; i++){
    for (int j = 0; j< n; j++){
      if(a[i] == b[j]){
        count++;
      }
    }
  }
  cout << answer_1 << endl;
  cout << count - answer_1 << endl;
}