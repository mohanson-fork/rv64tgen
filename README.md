# RV64 Test Generator

A random test generator for RV64 (RISC-V 64-bit) instruction correctness testing. It generates random assembly programs, compiles them, and cross-validates execution results between [ckb-vm](https://github.com/nervosnetwork/ckb-vm) and QEMU.

## Usage

```sh
$ python src/main.py
```

The generator runs in an infinite loop (up to $2^{32}$ iterations). Each iteration generates a fresh random test. The program exits with a non-zero status if the two runtimes disagree.
