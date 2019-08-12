# Operating system
[Geeksforgeeks](https://www.geeksforgeeks.org/operating-systems/)

### Difference between multi-programming, multi-processing, multi-tasking, multi-threading:
- Multiprogramming – A computer running more than one program at a time (like running Excel and Firefox simultaneously).
- Multiprocessing – A computer using more than one CPU at a time.
- Multitasking – Tasks sharing a common resource (like 1 CPU).
- Multithreading is an extension of multitasking.

### Difference between 32bit and 64bit operating system:

32/64 bit refers to the memory addresses that can be accessed by the operating system.

32bit - 2^32, ie 4GB or RAM or physical memory access
64bit - 2^64

```
The CPU register stores memory addresses, which is how the processor accesses data from RAM. One bit in the register can reference an individual byte in memory, so a 32-bit system can address a maximum of 4 GB (4,294,967,296 bytes) of RAM. The actual limit is often less around 3.5 GB, since part of the register is used to store other temporary values besides memory addresses
```