#include <bits/stdc++.h>
using namespace std;

int main() {
  int x,y;
  cin >> x >> y ;
  int answer = 0;
  int dif = y - x;
  if (dif <= 0){
    cout << 0 << endl;
  }else{
    while(dif > 0){
      dif -= 10;
      answer ++;
    }
    cout << answer << endl;
  }
}
