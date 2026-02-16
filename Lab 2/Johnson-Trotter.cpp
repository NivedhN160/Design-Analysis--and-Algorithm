#include <iostream>
#include <vector>
using namespace std;

// Print current permutation
void printPermutation(vector<int>& perm) {
    for (int x : perm)
        cout << x << " ";
    cout << endl;
}

int getMobile(vector<int>& perm, vector<int>& dir, int n) {
    int mobile = 0, mobileIndex = -1;

    for (int i = 0; i < n; i++) {
        int next = i + dir[perm[i] - 1];

        if (next >= 0 && next < n && perm[i] > perm[next]) {
            if (perm[i] > mobile) {
                mobile = perm[i];
                mobileIndex = i;
            }
        }
    }
    return mobileIndex;
}

void johnsonTrotter(int n) {
    vector<int> perm(n);
    vector<int> dir(n, -1); // -1 = left, +1 = right

    for (int i = 0; i < n; i++)
        perm[i] = i + 1;

    printPermutation(perm);

    while (true) {
        int mobileIndex = getMobile(perm, dir, n);
        if (mobileIndex == -1)
            break;

        int mobile = perm[mobileIndex];
        int swapIndex = mobileIndex + dir[mobile - 1];

        swap(perm[mobileIndex], perm[swapIndex]);
        mobileIndex = swapIndex;

        // Reverse directions of elements greater than mobile
        for (int i = 0; i < n; i++) {
            if (perm[i] > mobile)
                dir[perm[i] - 1] *= -1;
        }

        printPermutation(perm);
    }
}

int main() {
    int n;
    cout << "Enter n: ";
    cin >> n;

    johnsonTrotter(n);
    return 0;
}
