/// Calculates the nth prime number.
#[no_mangle]
pub extern fn prime(n: u32) -> u32 {
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


/// Calculates pi, as per https://github.com/JuliaLang/Microbenchmarks.
#[no_mangle]
pub extern fn pi() -> f64 {
    let mut sum = 0.;

    for _ in 0..500 {
        sum = (1..10001)
            .map(|k| {
                let k = k as f64;
                1. / (k * k)
            })
            .sum();
    }

    sum
}


/// Calculates the nth Fibonacci number, as per https://github.com/JuliaLang/Microbenchmarks.
#[no_mangle]
pub extern fn fibonacci(n: i32) -> i32 {
    if n < 2 {
        n
    } else {
        fibonacci(n - 1) + fibonacci(n - 2)
    }
}
