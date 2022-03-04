#include <bits/stdc++.h>
using namespace std;

int main() {
  string s;
  int a,b;
  cin >> s;
  cin >> a >> b;
  char tmp = s.at(a-1);
  s.at(a-1) = s.at(b-1);
  s.at(b-1) = tmp;
  cout << s << endl;
}