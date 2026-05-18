// Classes et RAII — ressource acquise = ressource libérée (sockets, fichiers)
#include <iostream>
#include <string>
#include <utility>

class Order {
public:
    Order(std::string sym, int qty, double px)
        : symbol_(std::move(sym)), quantity_(qty), price_(px) {}

    double notional() const { return quantity_ * price_; }
    const std::string& symbol() const { return symbol_; }

private:
    std::string symbol_;
    int quantity_;
    double price_;
};

class ScopedTimer {
public:
    explicit ScopedTimer(const char* label) : label_(label) {
        std::cout << "[" << label_ << "] start\n";
    }
    ~ScopedTimer() { std::cout << "[" << label_ << "] end\n"; }  // RAII cleanup

    ScopedTimer(const ScopedTimer&) = delete;
    ScopedTimer& operator=(const ScopedTimer&) = delete;

private:
    const char* label_;
};

int main() {
    Order o("AAPL", 10, 150.0);
    std::cout << o.symbol() << " notional=" << o.notional() << '\n';
    {
        ScopedTimer t("latency_block");
    }
    return 0;
}
