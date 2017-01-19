# Set the working dir, where all compiled Verilog goes.
vlib work

# Compile all verilog modules in mux.v to working dir;
# could also have multiple verilog files.
vlog lab5part2.v

# Load simulation using mux as the top level simulation module.
vsim lab5part2

# Log all signals and add some signals to waveform window.
log {/*}
# add wave {/*} would add all items in top level simulation module.
add wave {/*}

# Repetition
force {CLOCK_50} 1 0ns, 0 1ns -repeat 2ns

force {KEY[0]} 0
run 2ns
# Reset
force {KEY[0]} 1
force {KEY[1]} 1
force {SW[0]} 0
force {SW[1]} 1
force {SW[2]} 0
force {SW[3]} 0
force {SW[4]} 0
force {SW[5]} 0
force {SW[6]} 0
force {SW[7]} 0
run 2ns
force {KEY[0]} 0
run 2ns
force {KEY[0]} 1
run 2ns
# A = 2, B = 2, C = 2, x = 2
# A*x^2 + B*x + C = 14 (E)
force {KEY[1]} 0
run 2ns
force {KEY[1]} 1
run 2ns

force {KEY[1]} 0
run 2ns
force {KEY[1]} 1
run 2ns

force {KEY[1]} 0
run 2ns
force {KEY[1]} 1
run 2ns

force {KEY[1]} 0
run 2ns
force {KEY[1]} 1
run 2ns

force {KEY[1]} 0
run 2ns
force {KEY[1]} 1
run 2ns

force {KEY[1]} 0
run 2ns
force {KEY[1]} 1
run 2ns

force {KEY[1]} 0
run 2ns
force {KEY[1]} 1
run 2ns

# Reset 1
# A = 1, B = 1, C = 1, x = 1
# A*x^2 + B*x + C = 3
force {KEY[0]} 0
run 2ns
force {KEY[0]} 1
run 2ns

# A
force {SW[0]} 1
force {SW[1]} 0

force {KEY[1]} 0
run 2ns
force {KEY[1]} 1
run 2ns

# B
force {KEY[1]} 0
run 2ns
force {KEY[1]} 1
run 2ns

# C

force {KEY[1]} 0
run 2ns
force {KEY[1]} 1
run 2ns

# x
force {KEY[1]} 0
run 2ns
force {KEY[1]} 1
run 2ns

# Cycles
force {KEY[1]} 0
run 2ns
force {KEY[1]} 1
run 2ns
force {KEY[1]} 0
run 2ns
force {KEY[1]} 1
run 2ns
force {KEY[1]} 0
run 2ns
force {KEY[1]} 1
run 2ns

# Reset 2
# A = 3, B = 0, C = 0, x = 2
# A*x^2 + B*x + C = 12 (C)
force {KEY[0]} 0
run 2ns
force {KEY[0]} 1
run 2ns

# A
force {SW[0]} 1
force {SW[1]} 0

force {KEY[1]} 0
run 2ns
force {KEY[1]} 1
run 2ns

# B
force {KEY[1]} 0
run 2ns
force {KEY[1]} 1
run 2ns

# C

force {KEY[1]} 0
run 2ns
force {KEY[1]} 1
run 2ns

# x
force {KEY[1]} 0
run 2ns
force {KEY[1]} 1
run 2ns

# Cycles
force {KEY[1]} 0
run 2ns
force {KEY[1]} 1
run 2ns
force {KEY[1]} 0
run 2ns
force {KEY[1]} 1
run 2ns
force {KEY[1]} 0
run 2ns
force {KEY[1]} 1
run 2ns

