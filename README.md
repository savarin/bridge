# bridge

Simple examples for Python-Rust interop via WebAssembly.

## Commands

To run benchmarks:
```
python run.py
```

To install `wasmtime` with `pip`:
```
pip install wasmtime
```

To recompile `primes.wasm`:
```
rustup target add wasm32-wasi
rustc primes.rs --codegen opt-level=3 --crate-type=cdylib --target=wasm32-wasi
```

## Context

Foreign function interfaces (FFI) allow programs written in one programming
language to call routines in another language, as per [Wikipedia](https://en.wikipedia.org/wiki/Foreign_function_interface).
This can be done through dynamic libraries i.e. `.dylib`/`.so`/`.dll` files for
Mac/Linux/Windows respectively, as discussed in the post [here](https://codeburst.io/how-to-use-rust-to-extend-python-360174ee5819)
re: using Python to call Rust.

WebAssembly is a way of taking code written in programming languages other than
JavaScript and running that code in the browser. Running the code in the browser
effectively means the compiled .wasm binary is agnostic to the choice of
processor and OS. Lin Clark has an excellent series on WebAssembly [here](https://hacks.mozilla.org/2017/02/a-cartoon-intro-to-webassembly/);
minimal  examples to compile and run WebAssembly can be found [here](https://github.com/savarin/minimal).

The WebAssembly project has expanded beyond the browser, with [wasmtime](https://wasmtime.dev)
as the independent runtime and [WASI](https://wasi.dev) as the unified systems
interface. This could also make the .wasm format the new standard in portable
binaries for cross-language bridges.

The example in this repo calculates the 10,000th prime number in pure Python and
in Python with Rust via WebAssembly, with local benchmarks as follows:

```
average time (out of 3) Python: 3.830613s
average time (out of 3) Rust: 0.324900s
```
