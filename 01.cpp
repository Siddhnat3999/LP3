#include<bits/stdc++.h>
using namespace std;

int knapsack(vector<int>&weights,vector<int>&value,int n,int capacity){
   vector<vector<int>> dp(n+1,vector<int>(capacity+1,0));

   for(int i=1;i<=n;i++){
    for(int w=1;w<=capacity;w++){
        if(weights[i-1]<w){
            dp[i][w]=max(value[i-1]+dp[i-1][w-weights[i-1]],dp[i-1][w]);
        }
        else{
            dp[i][w]=dp[i-1][w];
        }
    }
   }
   return dp[n][capacity];
}


int main(){
    int n,capacity;
    cin>>n;
    cin>>capacity;
   vector<int> weights(n),value(n);
    for(int i=0;i<n;i++){
        cout<<"the weight and value of item"<<i+1;
        cin>>weights[i];
        cin>>value[i];
    }

    int maxVal=knapsack(weights,value,n,capacity);
    cout<<maxVal;
}