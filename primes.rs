/// Calculates the nth prime number.
#[no_mangle]
pub extern fn nth(n: u32) -> u32 {
    if n == 0 {
        return 2
    }

    let m = n as usize;

    let mut primes = vec![3];
    let mut recent = 3;
    let mut count = 1;

    while count < m {
        recent += 2;
        let mut is_prime = true;

        for item in &primes {
            if recent % item == 0 {
                is_prime = false;
                break;
            }
        }

        if is_prime {
            primes.push(recent);
            count += 1;
        }
    }

    primes[m - 1]
}
