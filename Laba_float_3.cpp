#include <iostream>
using namespace std;
int main() {
	cout << fixed;
	cout.precision(2);
	float n = 1664813248426.1f;
	int c = 0;
	while (n < 1664813248428.5){
		n += 1.0f;
		if (c % 1000000 == 0) {
			cout << n << endl;
		}
		c++;
	}
	return 0;
}