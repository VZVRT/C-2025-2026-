#include <iostream>
using namespace std;
void bin(unsigned int n) {
    int bit = sizeof(unsigned int) * 8;
    for (int i = bit - 1; i >= 0; i--) {
        cout << ((n >> i) & 1);
    }
    cout << endl;
}
int main() {
    unsigned int num;
    cin >> num;
    bin(num);
    return 0;
}