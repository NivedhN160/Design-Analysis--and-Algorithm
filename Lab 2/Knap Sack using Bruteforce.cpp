#include <iostream>
using namespace std;

int max(int a, int b) {
    return (a > b) ? a : b;
}

// Brute force recursive knapsack
int knapsack(int W, int wt[], int val[], int n) {
    // Base case
    if (n == 0 || W == 0)
        return 0;
    // If weight exceeds capacity, skip item
    if (wt[n - 1] > W)
        return knapsack(W, wt, val, n - 1);

    // Choose max of including or excluding item
    return max(
        val[n - 1] + knapsack(W - wt[n - 1], wt, val, n - 1),
        knapsack(W, wt, val, n - 1)
    );
}

int main() {
    int n, W;

    cout << "Enter number of items: ";
    cin >> n;

    int wt[n], val[n];

    cout << "Enter weights:\n";
    for (int i = 0; i < n; i++)
        cin >> wt[i];

    cout << "Enter values:\n";
    for (int i = 0; i < n; i++)
        cin >> val[i];

    cout << "Enter knapsack capacity: ";
    cin >> W;

    cout << "Maximum value: " << knapsack(W, wt, val, n);

    return 0;
}
