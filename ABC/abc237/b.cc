#include <bits/stdc++.h>
using namespace std;

int main() {
  int h,w;
  cin >> h >> w;
  vector<vector<int>> a (h,vector<int>(w));
  for (int i = 0; i < h; i++){
    for (int j = 0; j < w; j++){
      int tmp;
      cin >> tmp;
      a.at(i).at(j) = tmp;
    }
  }
  vector<vector<int>> b (w,vector<int>(h));
  for (int i = 0; i < w; i ++){
    for (int j = 0; j < h; j++){
      b.at(i).at(j) = a.at(j).at(i);
    }
  }
  for (int i = 0; i < w; i++){
    for (int j = 0; j < h; j++){
      if (j != (h-1)){
        cout << b.at(i).at(j) << " ";
      }else{
        cout << b.at(i).at(j) << endl;
      }
    }
  }
}