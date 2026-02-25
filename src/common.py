import random
import subprocess

import convention


class Writer:

    def __init__(self, name: str) -> None:
        self.name = name
        self.head = ''
        self.f = open(self.name, 'w')

    def ml(self) -> None:
        self.head = self.head[:-2]

    def mr(self) -> None:
        self.head += '  '

    def line(self, line: str) -> None:
        self.f.write(self.head)
        self.f.write(line)
        self.f.write('\n')


class Tester:

    def __init__(self) -> None:
        self.writer = Writer(convention.conf_fasm)

    def rand_u64(self) -> int:
        if random.random() < convention.conf_probability_boundary_uint:
            return random.choice(convention.boundary_uint)
        return random.randint(0, (1 << 64) - 1)

    def rand_register(self) -> str:
        return random.choice(convention.register)

    def rand_instruction_i(self) -> None:
        choose_rule = random.choice(convention.instruction_rule_i)
        opcode = choose_rule[0]
        args = []
        for i in choose_rule[1]:
            match i:
                case 'r':
                    args.append(self.rand_register())
                case 'i12':
                    args.append(str((self.rand_u64() % (1 << 12)) - (1 << 11)))
                case 'u5':
                    args.append(str(self.rand_u64() % 32))
                case 'u6':
                    args.append(str(self.rand_u64() % 64))
                case 'u20':
                    args.append(str(self.rand_u64() % (1 << 20)))
                case _:
                    assert 0
        args_string = ', '.join(args)
        self.writer.line(f'{opcode:<9} {args_string}')
        self.writer.line(f'add       a0, a0, {args[0]}')

    def rand_instruction_m(self) -> None:
        choose_rule = random.choice(convention.instruction_rule_m)
        opcode = choose_rule[0]
        args = []
        for i in choose_rule[1]:
            match i:
                case 'r':
                    args.append(self.rand_register())
                case _:
                    assert 0
        args_string = ', '.join(args)
        self.writer.line(f'{opcode:<9} {args_string}')
        self.writer.line(f'add       a0, a0, {args[0]}')

    def rand_instruction_b(self) -> None:
        choose_rule = random.choice(convention.instruction_rule_b)
        opcode = choose_rule[0]
        args = []
        for i in choose_rule[1]:
            match i:
                case 'r':
                    args.append(self.rand_register())
                case 'u5':
                    args.append(str(self.rand_u64() % 32))
                case 'u6':
                    args.append(str(self.rand_u64() % 64))
                case _:
                    assert 0
        args_string = ', '.join(args)
        self.writer.line(f'{opcode:<9} {args_string}')
        self.writer.line(f'add       a0, a0, {args[0]}')

    def rand_instruction(self) -> None:
        return random.choice([
            self.rand_instruction_i,
            self.rand_instruction_m,
            self.rand_instruction_b,
        ])()

    def tgen(self) -> None:
        self.writer.line('.global _start')
        self.writer.line('.section .text')
        self.writer.line('_start:')
        self.writer.mr()

        for _ in range(convention.conf_loop_l1):
            for i in convention.register:
                self.writer.line(f'li        {i}, {self.rand_u64()}')
            for _ in range(convention.conf_loop_l2):
                self.rand_instruction()

        self.writer.line('')
        self.writer.line('li        a7, 93')
        self.writer.line('ecall')
        self.writer.ml()
        self.writer.f.close()

        subprocess.run([
            'clang-19',
            '--target=riscv64-unknown-elf',
            '-march=rv64imc_zba_zbb_zbc_zbs',
            '-nostdlib',
            '-o',
            convention.conf_fbin,
            convention.conf_fasm,
        ])
