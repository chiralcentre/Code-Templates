typedef long long ll;

ll modExp(ll x, ll y, ll p) {
    ll ans = 1;
    while (y > 0) {
        if (y % 2 == 1) ans *= x;
        ans %= p;
        y >>= 1;
        x *= x;
        x %= p;
    }
    return ans % p;
}


ll mulmod(ll a, ll b, ll mod) {
    ll res = 0; // Initialize result
    a %= mod;
    while (b > 0) {
        if (b % 2 == 1) res = (res + a) % mod;
        a = (a << 1) % mod;
        // Divide b by 2
        b >>= 1;
    }
    return res % mod;
}
