#include <iostream>
#include <climits>
using namespace std;
int n;
int dist[10][10];
int dp[1 << 10][10];
int tsp(int mask, int pos) {
    if(mask == (1 << n) - 1)
        return dist[pos][0];
    if(dp[mask][pos] != -1)
        return dp[mask][pos];
    int ans = INT_MAX;
    for(int city = 0; city < n; city++) {
        if((mask & (1 << city)) == 0) {

            int newAns = dist[pos][city] +
                         tsp(mask | (1 << city), city);

            ans = min(ans, newAns);
        }
    }
    dp[mask][pos] = ans;
    return ans;
}
int main() {
    cout << "Enter Number of Cities: ";
    cin >> n;
    cout << "Enter Distance matrix:\n";
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cin >> dist[i][j];
        }
    }
    for(int i = 0; i < (1 << n); i++) {
        for(int j = 0; j < n; j++) {
            dp[i][j] = -1;
        }
    }
    cout << "Minimum Travel Cost: " << tsp(1, 0);
    return 0;
}