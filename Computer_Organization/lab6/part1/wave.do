
# Set the working dir, where all compiled Verilog goes.
vlib work

# Compile all verilog modules in mux.v to working dir;
# could also have multiple verilog files.
vlog lab6part1.v

# Load simulation using mux as the top level simulation module.
vsim -L  altera_mf_ver  -L  altera_mf lab6part1

# Log all signals and add some signals to waveform window.
log {/*}

# add wave {/*} would add all items in top level simulation module.
add wave {/*}



force {SW[0]} 0 
force {SW[1]} 0 
force {SW[2]} 0 
force {SW[3]} 1 

force {SW[4]} 0 
force {SW[5]} 0 
force {SW[6]} 0 
force {SW[7]} 0 
force {SW[8]} 1 

force {SW[9]} 0 
force {KEY[0]} 1
run 20 ns

force {KEY[0]} 0
run 20 ns


force {SW[0]} 0 
force {SW[1]} 0 
force {SW[2]} 1 
force {SW[3]} 0 

force {SW[4]} 0 
force {SW[5]} 0 
force {SW[6]} 0 
force {SW[7]} 1 
force {SW[8]} 0 

force {SW[9]} 1 

force {KEY[0]} 1
run 20 ns

force {KEY[0]} 0
run 20 ns

force {SW[0]} 0 
force {SW[1]} 0 
force {SW[2]} 1 
force {SW[3]} 1 

force {SW[4]} 0 
force {SW[5]} 0 
force {SW[6]} 0 
force {SW[7]} 1 
force {SW[8]} 1 

force {SW[9]} 1 

force {KEY[0]} 1
run 20 ns

force {KEY[0]} 0
run 20 ns

force {SW[0]} 0 
force {SW[1]} 0 
force {SW[2]} 1 
force {SW[3]} 0 

force {SW[4]} 0 
force {SW[5]} 0 
force {SW[6]} 0 
force {SW[7]} 1 
force {SW[8]} 0 

force {SW[9]} 1 

force {KEY[0]} 1
run 20 ns

force {KEY[0]} 0
run 20 ns

force {SW[0]} 0 
force {SW[1]} 0 
force {SW[2]} 1 
force {SW[3]} 0 

force {SW[4]} 0 
force {SW[5]} 0 
force {SW[6]} 0 
force {SW[7]} 1 
force {SW[8]} 0 

force {SW[9]} 0 

force {KEY[0]} 1
run 20 ns

force {KEY[0]} 0
run 20 ns

force {SW[0]} 0 
force {SW[1]} 1 
force {SW[2]} 1 
force {SW[3]} 0 

force {SW[4]} 0 
force {SW[5]} 0 
force {SW[6]} 0 
force {SW[7]} 1 
force {SW[8]} 0 

force {SW[9]} 0

force {KEY[0]} 1
run 20 ns

force {KEY[0]} 0
run 20 ns

force {SW[0]} 0 
force {SW[1]} 1 
force {SW[2]} 1 
force {SW[3]} 0 

force {SW[4]} 0 
force {SW[5]} 0 
force {SW[6]} 0 
force {SW[7]} 1 
force {SW[8]} 0 

force {SW[9]} 1

force {KEY[0]} 1
run 20 ns

force {KEY[0]} 0
run 20 ns