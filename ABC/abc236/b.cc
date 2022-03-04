#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;
  int sum = ((1 + n) * n /2 ) * 4;
  int get = 0;
  for (int i = 0; i < 4 * n  -1 ; i++){
    int h;
    cin >> h;
    get += h;
  }
  cout << sum - get << endl;
}