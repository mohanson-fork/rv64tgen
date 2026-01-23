import subprocess

import common
import convention


def main_b():
    for _ in range(1 << 32):
        tester = common.Tester()
        tester.tgen()
        expect = subprocess.run([
            '/home/ubuntu/src/ckb-vm/target/release/examples/ckb_vm_runner',
            convention.conf_fbin,
        ]).returncode
        result = subprocess.run([
            '/home/ubuntu/app/riscv/bin/qemu-riscv64',
            '-L',
            '/home/ubuntu/app/riscv/sysroot',
            '/home/ubuntu/src/ckb-vm/target/riscv64gc-unknown-linux-gnu/release/examples/ckb_vm_runner',
            convention.conf_fbin,
        ]).returncode
        assert result == expect


if __name__ == '__main__':
    main_b()
