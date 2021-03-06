`timescale 1ns / 1ns // `timescale time_unit/time_precision

module lab4part2(SW, CLOCK_50, HEX0);
	input [7:0] SW;
	input CLOCK_50;
	output [6:0] HEX0;

	wire RDtoHD;
	wire [3:0]to;


	RateDivider RD( .a(SW[0]), .b(SW[1]), .Clear_b(SW[3]), .clock(CLOCK_50), .load1(RDtoHD), .Enable(SW[2]));
	DisplayCounter DC(.a(SW[0]),.b(SW[1]), .clear_b(SW[3]), .Enable(RDtoHD), .clock(CLOCK_50), .load(to));
	hex_decoder h0(.a(to[3]),.b(to[2]),.c(to[1]),.d(to[0]), .out0(HEX0[0]),.out1(HEX0[1]),.out2(HEX0[2]),.out3(HEX0[3]),.out4(HEX0[4]),.out5(HEX0[5]),.out6(HEX0[6]));

endmodule

module DisplayCounter(a,b, clear_b, Enable, clock, load);
	input a,b, clear_b, Enable, clock;
	output  reg [3:0] load;
	always @(posedge clock) 
		begin
			if (clear_b ==1'b0) 
				load <= 0; // reset
			else if (Enable ==1'b1) 
				load <= load + 1'b1; // increment by 1
		end


endmodule

module RateDivider( a, b, Clear_b, clock, Enable, load1);
	input a,b, Clear_b, clock, Enable;
	output reg load1;
	
	wire [1:0]toRD;

	assign toRD[1:0] = {a,b};
	
	reg[28:0] count;
	always @ (posedge clock) //positive edge trigger
	begin 
		if (Clear_b == 1'b0) // reset all
			load1 <= 0;
			
		else if (count == 28'b0000000000000000000000000000) // if count is zero 
			begin		
					load1 <= 1; //every time count down to zero, loading to display	
/*		
					case (toRD[1:0]) // four speed from 00 to 11
						2'b00 : count <= 1'b1; // this is full speed
						2'b01 : count <= 28'b0010111110101111000001111111; // this is 50 m
						2'b10 : count <= 28'b0101111101011110000011111111; // this is 100 m
						2'b11 : count <= 28'b1011111010111100000111111111; // this is 200 m
						default: count<= 28'b0000000000000000000000000000;
					endcase
*/

					case (toRD[1:0]) // four speed from 00 to 11
						2'b00 : count <= 1'b1; // this is full speed
						2'b01 : count <= 2'b10; // this is 50 m
						2'b10 : count <= 3'b100; // this is 100 m
						2'b11 : count <= 4'b1000; // this is 200 m
						default: count<= 28'b0000000000000000000000000000;
					endcase
			end
	
		else if (Enable == 1'b1) // if enabled 
			begin
				load1 <= 0;
				count <= count - 28'b0000000000000000000000000001; // decrement count by 1
			end
	end	
endmodule


module hex_decoder(a,b,c,d,out0,out1,out2,out3,out4,out5,out6);
	input a,b,c,d;
	output out0,out1,out2,out3,out4,out5,out6;
	assign out0 = ~a&~b&~c&d | ~a&b&~c&~d | a&~b&c&d | a&b&~c&d;
	assign out1 = a&b&c | b&c&~d | a&c&d | a&b&~c&~d | ~a&b&~c&d;
	assign out2 = a&b&c | ~a&~b&c&~d | a&b&~c&~d;
	assign out3 = ~a&~b&~c&d | ~a&b&~c&~d | b&c&d | a&~b&c&~d;
	assign out4 = ~a&d | ~a&b&~c | ~b&~c&d;
	assign out5 = ~a&~b&d | ~a&~b&c | ~a&c&d | a&b&~c&d;
	assign out6 = ~a&~b&~c | ~a&b&c&d | a&b&~c&~d;
endmodule
