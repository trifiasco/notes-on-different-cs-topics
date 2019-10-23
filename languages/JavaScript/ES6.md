### Topics
- [var vs let vs const](#var-vs-let-vs-const)
- [Anonymous Function](Anonymous-Function)
- [Arrow Function](Arrow-Function)
- [Generator Function](Generator-Function)


#### var vs let vs const
**Hoisting** - means to use something before decalring it. Can be variables, can be functions

```
The scope of a variable declared with var is its current execution context, which is either the enclosing function or, for variables declared outside any function, global. Variable hoisting allows the use of a variable in a JavaScript program, even before it is declared.
```

```
We can't use let or const-declared variables before we've defined them. In other words, they're not hoisted by the compiler, as var-declarations are.
```

```
You must assign a value to a const-declared variable when you create it. You can't create it first and assign it later.

You cannot change the vaue of a const-declared variable after you create it. If you try, you'll get a TypeError.
```

#### Anonymous Function
Functions that are not bound to an identifier (function name) are called as anonymous functions. These functions are dynamically declared at runtime. Anonymous functions can accept inputs and return outputs, just as standard functions do. An anonymous function is usually not accessible after its initial creation.

Variables can be assigned an anonymous function. Such an expression is called a function expression.

Following is the syntax for anonymous function.

```
var f = function(){ return "hello"} 
```

#### Arrow Function
Also called as `lambda functions` - 

```
([param1, parma2,…param n] )=>statement;
```