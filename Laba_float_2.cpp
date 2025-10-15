#include <iostream>
#include <cmath>
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
    cout << fixed;
    cout.precision(2);
    fu bits;
    float p = 1.0f;
    for (int i = 0; i < 39; i++) {
        p *= 10.0f;
        bits.f = p;
        cout <<"10^" << (i+1)<<"=" << p << endl;
        cout << "";
        bin(bits.u);
        cout << endl;
        if (isinf(p)) {
            cout << "!!!!!!!!!!" << endl;
            break;
        }
    }
    return 0;
}