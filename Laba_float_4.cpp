#include <iostream>
#include <cmath>
#include <chrono>
#include <iomanip>
using namespace std;

float Leibniz(int iter) {
    float π = 0.0f;
    for (int i = 0; i < iter; i++) {
        float curr = 1.0f / (2 * i + 1);
        if (i % 2 == 0) {
            π += curr;
        }
        else {
            π -= curr;
        }
    }
    return 4 * π;
}

float Madhava(int iter) {
    float π = 0.0f;
    for (int i = 0; i < iter; i++) {
        float curr = 1.0f / ((2 * i + 1) * pow(3.0f, i));
        if (i % 2 == 0) {
            π += curr;
        }
        else {
            π -= curr;
        }
    }
    return sqrt(12) * π;
}

float Nilakantha(int iter) {
    float π = 3.0f;
    for (int i = 1; i < iter; i++) {
        float curr = 4.0f / (2 * i * (2 * i + 1) * (2 * i + 2));
        if (i % 2 != 0) {
            π += curr;
        }
        else {
            π -= curr;
        }
    }
    return π;
}

float BBP(int iter) {
    float π = 0.0f;
    for (int i = 0; i < iter; i++) {
        float curr = ((4.0f / (8 * i + 1)) - (2.0f / (8 * i + 4)) - (1.0f / (8 * i + 5)) - (1.0f / (8 * i + 6))) / (pow(16.0f, i));
        π += curr;
    }
    return π;
}

float Wallis(int iter) {
    float π = 1.0f;
    for (int i = 1; i < iter; i++) {
        float curr = 4.0f * i * i / ((2 * i - 1) * (2 * i + 1));
        π *= curr;
    }
    return 2 * π;
}

double measure_time(int iterations, float (*function)(int)) {
    auto start = chrono::high_resolution_clock::now();
    function(iterations);
    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> duration = end - start;
    return duration.count();
}

int main() {
    const float π_true = 3.14159265358979323846f;
    setlocale(LC_ALL, "RU");

    int Leibniz_iter[] = { 9, 100, 1000, 9354, 69957, 227569, 293567, 295861 };
    int Wallis_iter[] = { 8, 78, 787, 2049, 2049, 2049, 2049, 2049 };
    int Nilakantha_iter[] = { 1, 2, 6, 13, 29, 58, 94, 115 };
    int Madhava_iter[] = { 1, 5, 9, 16, 20, 41, 50, 85 };
    int BBP_iter[] = { 1, 1, 1, 2, 3, 4, 5, 12 };

    int num_p = 8;
    float t[] = { 0.1f, 0.01f, 0.001f, 0.0001f, 0.00001f, 0.000001f, 0.0000001f, 0.00000001f };

    double time_Leibniz[8], time_Wallis[8], time_Nilakantha[8], time_Madhava[8], time_BBP[8];
    for (int i = 0; i < num_p; i++) {
        time_Leibniz[i] = measure_time(Leibniz_iter[i], Leibniz);
        time_Wallis[i] = measure_time(Wallis_iter[i], Wallis);
        time_Nilakantha[i] = measure_time(Nilakantha_iter[i], Nilakantha);
        time_Madhava[i] = measure_time(Madhava_iter[i], Madhava);
        time_BBP[i] = measure_time(BBP_iter[i], BBP);
    }

    cout << "Точное значение пи: " << setprecision(10) << π_true << "\n" << endl;
    cout << "Т\tЛейб\t\tОш\t\tВал\t\tОш\t\tНил\tОш\t\tМад\t\tОш\t\tBBP\t\tОш" << endl;
    cout << "-----------------------------------------------------------------------------------------------------------------" << endl;

    for (int i = 0; i < num_p; i++) {
        cout << fixed << setprecision(8) << t[i] << "\t";
        cout << fixed << setprecision(7);
        cout << Leibniz(Leibniz_iter[i]) << "\t" << fabs(Leibniz(Leibniz_iter[i]) - π_true) << "\t";
        cout << Wallis(Wallis_iter[i]) << "\t" << fabs(Wallis(Wallis_iter[i]) - π_true) << "\t";
        cout << Nilakantha(Nilakantha_iter[i]) << "\t" << fabs(Nilakantha(Nilakantha_iter[i]) - π_true) << "\t";
        cout << Madhava(Madhava_iter[i]) << "\t" << fabs(Madhava(Madhava_iter[i]) - π_true) << "\t";
        cout << BBP(BBP_iter[i]) << "\t" << fabs(BBP(BBP_iter[i]) - π_true) << endl;
    }

    cout << "\n\nВремя выполнения (секунды):" << endl;
    cout << "Т\tЛейбниц\t\tВаллис\t\tНилаканта\tМадхава\t\tBBP" << endl;
    cout << "-----------------------------------------------------------------------" << endl;

    for (int i = 0; i < num_p; i++) {
        cout << fixed << setprecision(8) << t[i] << "\t";
        cout << scientific << setprecision(6);
        cout << time_Leibniz[i] << "\t" << time_Wallis[i] << "\t" << time_Nilakantha[i] << "\t"
            << time_Madhava[i] << "\t" << time_BBP[i] << endl;
    }

    return 0;
}