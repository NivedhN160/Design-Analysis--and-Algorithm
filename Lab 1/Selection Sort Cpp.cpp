#include<iostream>
using namespace std;
int main() {
    int n;
    cout << "Enter Number of Elements: ";
    cin >> n;
    int a[n];
    cout << "Enter Elements:\n";
    for(int i = 0; i < n; i++) {
        cin >> a[i];
    }
    for(int i = 0; i < n - 1; i++) {
        int MinIndex = i;

        for(int j = i + 1; j < n; j++) {
            if(a[j] < a[MinIndex]) {
                MinIndex = j;
            }
        }
        if(MinIndex != i) {
            int temp = a[i];
            a[i] = a[MinIndex];
            a[MinIndex] = temp;
        }
    }
    cout << "Sorted Array:\n";
    for(int i = 0; i < n; i++) {
        cout << a[i] << " ";
    }
    return 0;
}