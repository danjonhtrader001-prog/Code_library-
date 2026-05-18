// Conteneurs STL — carnets, lookup symboles
#include <iostream>
#include <map>
#include <unordered_map>
#include <vector>

int main() {
    std::vector<double> ticks = {100.0, 100.1, 100.05};
    std::unordered_map<std::string, double> last_price;
    last_price["AAPL"] = 150.0;
    last_price["MSFT"] = 300.0;

    std::map<int, double> depth_bids = {{1, 99.9}, {2, 99.8}};  // niveau → prix

    double sum = 0.0;
    for (double t : ticks) sum += t;

    std::cout << "Moyenne ticks: " << sum / ticks.size() << '\n';
    std::cout << "AAPL: " << last_price["AAPL"] << '\n';
    std::cout << "Bid niveau 1: " << depth_bids[1] << '\n';
    return 0;
}
