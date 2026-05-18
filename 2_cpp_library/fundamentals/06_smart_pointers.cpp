// Smart pointers — propriété mémoire sans fuites en production
#include <iostream>
#include <memory>
#include <vector>

struct OrderBook {
    explicit OrderBook(std::string symbol) : symbol_(std::move(symbol)) {}
    void print() const { std::cout << "Book " << symbol_ << '\n'; }
    std::string symbol_;
};

int main() {
    // unique_ptr : propriété exclusive (un moteur par carnet)
    auto book = std::make_unique<OrderBook>("AAPL");
    book->print();

    // shared_ptr : partage (plusieurs stratégies lisent le même snapshot)
    std::shared_ptr<OrderBook> shared = std::make_shared<OrderBook>("MSFT");
    std::vector<std::shared_ptr<OrderBook>> readers = {shared, shared};
    std::cout << "use_count=" << shared.use_count() << '\n';

    book.reset();  // destruction automatique
    return 0;
}
