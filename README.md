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
rustc primes.rs --codegen opt-level=3 --crate-type=cdylib --target=wasm32-wasi
```
