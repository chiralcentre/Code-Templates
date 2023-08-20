#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef unordered_map<ll,ll> umll;

umll PrimeFactor(ll n) {
    umll factors;
    while (n % 2 == 0){ 
        factors[2]++;
        n >>= 1;
    }
    for (ll i = 3; i < ll(sqrt(n)) + 1; i += 2) { 
        if (n < 2) break;
        while (n % i == 0) {
            factors[i]++;
            n /= i;
        }
    }
    if (n > 2) factors[n] = 1;
    return factors;
}
