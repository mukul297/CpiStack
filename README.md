## Obtaining CPI Stack for Programs using Hardware Performance Counters and Linear Regression

We have to obtain the CPI(Cycles per Instruction) stack for programs using hardware performance monitoring counters. CPI stack divides the total CPI of an application into components that reflect the time spent in various events, such L1-I Cache misses, L1-D cache misses, L2/L3 Cache misses, I-TLB and D- TLB misses, branch misprediction, etc. We have to obtain CPI using hardware performance monitoring counters. We can also extract the count of various miss events occurs using hardware monitoring counters using Perf tool. 

We have to develop a linear regression model (using simple linear terms) for CPI for each application. The miss events are additive in nature thatswhy it has always  non-negative coefficients. The regression model (with additive terms) essentially gives the CPI stack. For each program-input pair, there would be a separate regression model which gives the CPI stack for that program.

We have to develop linear regression for different Benchmarks programs. 3 Floating point Benchmark and 3 Integer type benchmarks.

Below are some of the predicted CPI stack:
1. 557. xz_r SPEC INT Benchmark
![alt text](https://lh5.googleusercontent.com/J158_aMlxRKqd0VHNygUg-APXy0lwox7X1lVzzjaIZRyW9l9fHL5u8Xo9pMzh4RkO8k=w1200-h630-p)

2. 526. blender_r SPEC FP Benchmark
![alt text](https://lh6.googleusercontent.com/2CyOlK6nELzLyCkMT-iCY4On-0xrymMxHWSbrOSKJa9uyXitSvG3gUCTLJ3EVxfviXE=w1200-h630-p)
