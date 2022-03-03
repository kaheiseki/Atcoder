#include <bits/stdc++.h>
using namespace std;

int main(){
  int l,r;
  string s;
  cin >> l >> r;
  cin >> s;
  string answer = "";
  for (int i = 0;i < s.size();i++){
    if (i < l - 1){
      answer += s.at(i);
    }else if (l - 1 <= i && i <= r - 1){
      answer += s.at(r - 1 - i + l - 1);
    }else{
      answer += s.at(i);
    }
  }
  cout << answer << endl;
}
