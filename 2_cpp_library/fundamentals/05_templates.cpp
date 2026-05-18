// Templates — code générique réutilisable (prix, quantités, types fixes)
#include <iostream>
#include <type_traits>
#include <vector>

template <typename T>
T clamp(T value, T lo, T hi) {
    return (value < lo) ? lo : (value > hi) ? hi : value;
}

template <typename Iter, typename T>
T accumulate_sum(Iter begin, Iter end, T init) {
    for (Iter it = begin; it != end; ++it) init += *it;
    return init;
}

int main() {
    double price = clamp(150.99, 100.0, 150.5);
    std::vector<int> sizes = {10, 20, 5};
    int total_qty = accumulate_sum(sizes.begin(), sizes.end(), 0);

    std::cout << "Prix clampé: " << price << '\n';
    std::cout << "Quantité totale: " << total_qty << '\n';
    std::cout << "sizeof(int): " << sizeof(int) << " bytes\n";
    return 0;
}
