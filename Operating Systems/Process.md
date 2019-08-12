# Process

Process is `program in execution`.

### Attributes
- process id
- process state - new, ready, running, wait(or block), complete, suspended ready, suspended block
- CPU registers - like program counter
- scheduling info

Attributes of a process is also called `Context of a process`.

Each process has it's own `PCB(Program-Control-Block)` - pointer, process state, process number, program counter, registers, status data etc.

### Process Scheduler

- Long Term or job scheduler - brings new process to ready stat. Controls degree of multi-programming.

- Short Term or CPU scheduler - selects one process from ready state for scheduling it one running state.
  dispatcher is responsible for loading the selected process and context switching.

- Medium Term - responsible for suspending and resuming the process. mainly does the swapping.

### Process synchronization

A process can be 1. Independent or 2. Co-operative

Synchronization problem arises for #2.

#### Race Condition

#### Critical Section problem

Critical section is a code segment that can be accessed by only one process at a time. Critical section contains shared variables which need to be synchronized to maintain consistency of data variables.

```
do{
    //entry section

        //critical section
    
    //exit section
    
        //remainder section
}
```

Any solution must satisfy the following three:
- Mutual exclusion: only one process is allowed to be in critical section at a time.
- Progress: a process outside the critical section does not block other processes from entering the critical section
- Bounded waiting: everyone gets a fair chance.

### [Mutex & Sempaphores](https://www.geeksforgeeks.org/mutex-vs-semaphore/)
mutex and semaphore are kernel resources that provide synchronization services (also called as synchronization primitives)

- `mutext` - a mutex provides mutual exclusion. It's a locking mechanism.
- `semaphore` - a semaphore is a generalized mutex. It's a signaling mechanism.
  a. binary semaphore.
  b. counting semaphore.

#### [Semaphore Implementation](https://www.geeksforgeeks.org/semaphores-operating-system/)
A sempaphore is simply a variable, used to solve the critical section problem.

```
Wait(semaphore s)
{
    while(s == 0); // wait until s=0

    s--;
}

Release(semaphore s){
    s++;
}


run()
{
    // initially semaphore s = 1
    //something
    wait(s)

    // critical section

    release(s)

    //remainder
}

```

### DeadLock

#### Necessary conditions
- Mutual exclusion: resources are non-sharable
- Hold & wait: a process is holding one resource and requesting for others.
- No Preemption: a resource can't be taken from a process unless the process releases it on it's own.
- circular wait: self explanatory.


