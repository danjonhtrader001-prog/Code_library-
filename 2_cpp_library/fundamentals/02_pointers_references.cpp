// Pointeurs et références — passer carnets d'ordres sans copie
#include <iostream>
#include <vector>

void apply_spread(double& mid, double half_spread) {
    mid += half_spread;  // modification in-place via référence
}

int main() {
    std::vector<double> bids = {99.9, 99.8, 99.7};
    double* best_bid_ptr = &bids[0];  // pointeur vers meilleur bid
    double& best_bid_ref = bids[0];   // référence (alias)

    std::cout << "Best bid (ptr): " << *best_bid_ptr << '\n';
    apply_spread(best_bid_ref, 0.05);
    std::cout << "Après ajustement: " << bids[0] << '\n';
    return 0;
}
