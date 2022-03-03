#include <bits/stdc++.h>
using namespace std;

int main() {
 int n;
 vector<vector<int>> vec(n,vector<int>(2));
 for (int i = 0; i < n; i++){
   int x,y;
   cin >> x >> y;
   vec.at(i).at(0) = x;
   vec.at(i).at(1) = y;
 }
 cout << vec << endl; 
 float m = 0.0;
 for (int i = 0;i < n - 1; i++){
   for (int j = i + 1; j < n; j++){
     float a;
     a = sqrt((vec.at(j).at(0) - vec.at(i).at(0)) ^ 2 + (vec.at(j).at(1) - vec.at(i).at(1)) ^2);
     cout << a << endl;
     m = max(a,m);
   }
 }
 cout << m << endl;
}