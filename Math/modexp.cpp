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
