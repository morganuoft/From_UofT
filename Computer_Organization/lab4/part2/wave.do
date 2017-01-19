
# Set the working dir, where all compiled Verilog goes.
vlib work

# Compile all verilog modules in mux.v to working dir;
# could also have multiple verilog files.
vlog lab4part2.v

# Load simulation using mux as the top level simulation module.
vsim lab4part2

# Log all signals and add some signals to waveform window.
log {/*}

# add wave {/*} would add all items in top level simulation module.
add wave {/*}

force {CLOCK_50} 0 0ns, 1 10ns -r 20ns

force {SW[1]} 0
force {SW[2]} 1
force {SW[3]} 0
force {SW[0]} 0 
 
run 20 ns

force {SW[1]} 1
force {SW[2]} 1
force {SW[3]} 1
force {SW[0]} 0


run 20 ns

force {SW[1]} 0
force {SW[2]} 1
force {SW[3]} 0
force {SW[0]} 1 

run 20 ns

force {SW[1]} 1
force {SW[2]} 1
force {SW[3]} 1
force {SW[0]} 1 

run 20 ns


force {SW[1]} 1
force {SW[2]} 1
force {SW[3]} 1
force {SW[0]} 1 
force {SW[4]} 1 
force {SW[5]} 1 
force {SW[6]} 1 
force {SW[7]} 1 
run 2000 ns
