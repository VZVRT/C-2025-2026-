#include <iostream>
using namespace std;
union fu {
    float f;
    unsigned int u;
};
void bin(unsigned int u) {
    for (int i = 31; i >= 0; i--) {
        cout << ((u >> i) & 1);
    }
    cout << endl;
}
int main() {
    fu a_lab_rat;
    cin >> a_lab_rat.f;
    bin(a_lab_rat.u);
}