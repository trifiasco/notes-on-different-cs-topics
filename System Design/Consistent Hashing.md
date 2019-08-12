# Consistent Hashing

### Motivation
Suppose you have a distributed system - 

|Key|Value|
|---|-----|
|1  |     |
|2  |     |
|3  |     |
|4  |     |
|5  |     |
|6  |     |
|7  |     |

Where 1-5 is stored in Computer1 and 6-7 is stored in Computer2.

So Table size is 7. If computer2 fails, then your table size is 5. But at this time rest of the hashes in computer1 is invalid. because you were doing a mod by table size. Consistent hashing to the rescue.

### Basic Idea

Your keys will be randomly generated numbers(preferably from a hash function).

|Key|Value|
|---|-----|
|1234  |     |
|2134  |     |
|3451  |     |
|4378  |     |
|5982  |     |
|6487  |     |
|7059  |     |

Now when you try to insert a value, and your hash function gives you to 3000, then you try to find a key which is next greater number than 3000. So you end up inserting at 3451.

if it's greater than 7059(the greatest number as key), then you insert it in the first bucket having 1234, which would make your hash table into a hashring.


### Further reading
1. [An Youtube Video](https://www.youtube.com/watch?v=zaRkONvyGr8)
2. [Improving load balancing with a new consistent-hashing algorithm](https://medium.com/vimeo-engineering-blog/improving-load-balancing-with-a-new-consistent-hashing-algorithm-9f1bd75709ed)
3. [Uber ring-pop](https://eng.uber.com/intro-to-ringpop/)
4. [Implement efficient consistent hashring](https://www.ably.io/blog/implementing-efficient-consistent-hashing)