// Types et E/S — base des ticks et ordres en C++
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <string>

int main() {
    // Pourquoi tailles fixes : alignement cache, messages binaires FIX/ITCH
    std::int64_t price_micros = 150'250'000;  // 150.25 * 1e6
    std::int32_t quantity = 100;
    std::string symbol = "AAPL";
    bool is_buy = true;

    double price = static_cast<double>(price_micros) / 1'000'000.0;

    std::cout << std::fixed << std::setprecision(4);
    std::cout << "Symbole: " << symbol
              << " | " << (is_buy ? "BUY" : "SELL")
              << " qty=" << quantity
              << " prix=" << price << '\n';
    return 0;
}
