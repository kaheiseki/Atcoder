#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;
  int answer = 0;
  for (int i = 0; i< n; i++){
    int h;
    cin >> h;
    if (answer < h){
      answer = h;
    }else {
      break;
    }
  }
  cout << answer << endl;
}