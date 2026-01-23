conf_fasm = '/tmp/main.S'
conf_fbin = '/tmp/main'
conf_loop_l1 = 32
conf_loop_l2 = 1024
conf_probability_boundary_uint = 0.05

register = [
    'zero', 'ra', 'sp', 'gp',
    'tp', 't0', 't1', 't2',
    's0', 's1', 'a0', 'a1',
    'a2', 'a3', 'a4', 'a5',
    'a6', 'a7', 's2', 's3',
    's4', 's5', 's6', 's7',
    's8', 's9', 's10', 's11',
    't3', 't4', 't5', 't6',
]
register.remove('zero')
register.remove('a0')

boundary_uint = []

for i in range(0, 64):
    n = 1 << i
    boundary_uint.append(n - 1)
    boundary_uint.append(n)
    boundary_uint.append(n + 1)
    n = 0xffffffffffffffff >> i
    boundary_uint.append(n)
    boundary_uint.append(n << i)

instruction_rule_b = [
    ['add.uw', ['r', 'r', 'r']],
    ['andn', ['r', 'r', 'r']],
    ['clmul', ['r', 'r', 'r']],
    ['clmulh', ['r', 'r', 'r']],
    ['clmulr', ['r', 'r', 'r']],
    ['clz', ['r', 'r']],
    ['clzw', ['r', 'r']],
    ['cpop', ['r', 'r']],
    ['cpopw', ['r', 'r']],
    ['ctz', ['r', 'r']],
    ['ctzw', ['r', 'r']],
    ['max', ['r', 'r', 'r']],
    ['maxu', ['r', 'r', 'r']],
    ['min', ['r', 'r', 'r']],
    ['minu', ['r', 'r', 'r']],
    ['orc.b', ['r', 'r']],
    ['orn', ['r', 'r', 'r']],
    ['rev8', ['r', 'r']],
    ['rol', ['r', 'r', 'r']],
    ['rolw', ['r', 'r', 'r']],
    ['ror', ['r', 'r', 'r']],
    ['rori', ['r', 'r', 'u6']],
    ['roriw', ['r', 'r', 'u5']],
    ['rorw', ['r', 'r', 'r']],
    ['bclr', ['r', 'r', 'r']],
    ['bclri', ['r', 'r', 'u6']],
    ['bext', ['r', 'r', 'r']],
    ['bexti', ['r', 'r', 'u6']],
    ['binv', ['r', 'r', 'r']],
    ['binvi', ['r', 'r', 'u6']],
    ['bset', ['r', 'r', 'r']],
    ['bseti', ['r', 'r', 'u6']],
    ['sext.b', ['r', 'r']],
    ['sext.h', ['r', 'r']],
    ['sh1add', ['r', 'r', 'r']],
    ['sh1add.uw', ['r', 'r', 'r']],
    ['sh2add', ['r', 'r', 'r']],
    ['sh2add.uw', ['r', 'r', 'r']],
    ['sh3add', ['r', 'r', 'r']],
    ['sh3add.uw', ['r', 'r', 'r']],
    ['slli.uw', ['r', 'r', 'u6']],
    ['xnor', ['r', 'r', 'r']],
    ['zext.h', ['r', 'r']],
]
