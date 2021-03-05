## Obtaining CPI Stack for Programs using Hardware Performance Counters and Linear Regression

We have to obtain the CPI(Cycles per Instruction) stack for programs using hardware performance monitoring counters. CPI stack divides the total CPI of an application into components that reflect the time spent in various events, such L1-I Cache misses, L1-D cache misses, L2/L3 Cache misses, I-TLB and D- TLB misses, branch misprediction, etc. We have to obtain CPI using hardware performance monitoring counters. We can also extract the count of various miss events occurs using hardware monitoring counters using Perf tool. 

We have to develop a linear regression model (using simple linear terms) for CPI for each application. The miss events are additive in nature thatswhy it has always  non-negative coefficients. The regression model (with additive terms) essentially gives the CPI stack. For each program-input pair, there would be a separate regression model which gives the CPI stack for that program.

We have to develop linear regression for different Benchmarks programs. 3 Floating point Benchmark and 3 Integer type benchmarks.
