# OOP Concepts in C++
### Topics
- Classes & Objects
  - [Class Access Modifier](#class-Access-Modifier)
  - [Constructors & Desctructors](#constructors-&-destructors)
  - [Copy Constructors](#copy-constructors)
  - [Friend Function](#friend-function)
- [Inheritance](#inheritance)
- Overloading
  - function
  - operator
- [Polymorphism](#polymorphism)
- Abstraction
- Encapsulation
- [Virtual Function](#virtual-function)
- [Pure Virtual Function](#pure-virtual-function)
- [Abstract Class](#abstract-class)
- [Interface](#interface)


### Class Access Modifier

|Access	         |public	|protected	|private|
| ---------------|----------|-----------|-------|
|Same class	     |yes	    |yes	    |yes    |
|Derived classes |yes	    |yes	    |no     |
|Outside classes |yes	    |no	        |no     |

### Constructors & Destructors

```
A destructor will have exact same name as the class prefixed with a tilde (~) and it can neither return a value nor can it take any parameters. Destructor can be very useful for releasing resources before coming out of the program like closing files, releasing memories etc.
```

### Copy Constructors

```
The copy constructor is a constructor which creates an object by initializing it with an object of the same class, which has been created previously. The copy constructor is used to −

1. Initialize one object from another of the same type.
2. Copy an object to pass it as an argument to a function.
3. Copy an object to return it from a function.

If a copy constructor is not defined in a class, the compiler itself defines one.If the class has pointer variables and has some dynamic memory allocations, then it is a must to have a copy constructor. The most common form of copy constructor is shown here
```

```
classname (const classname &obj) {
   // body of constructor
}
```

Example -

```
#include <iostream>

using namespace std;

class Line {
   public:
      int getLength( void );
      Line( int len );             // simple constructor
      Line( const Line &obj);  // copy constructor
      ~Line();                     // destructor

   private:
      int *ptr;
};

// Member functions definitions including constructor
Line::Line(int len) {
   cout << "Normal constructor allocating ptr" << endl;
   
   // allocate memory for the pointer;
   ptr = new int;
   *ptr = len;
}

Line::Line(const Line &obj) {
   cout << "Copy constructor allocating ptr." << endl;
   ptr = new int;
   *ptr = *obj.ptr; // copy the value
}

Line::~Line(void) {
   cout << "Freeing memory!" << endl;
   delete ptr;
}

int Line::getLength( void ) {
   return *ptr;
}

void display(Line obj) {
   cout << "Length of line : " << obj.getLength() <<endl;
}

// Main function for the program
int main() {

   Line line1(10);

   Line line2 = line1; // This also calls copy constructor

   display(line1);
   display(line2);

   return 0;
}
```

Above code will have following output - 

```
Normal constructor allocating ptr
Copy constructor allocating ptr.
Copy constructor allocating ptr.
Length of line : 10
Freeing memory!
Copy constructor allocating ptr.
Length of line : 10
Freeing memory!
Freeing memory!
Freeing memory!
```

### Friend Function

```
A friend function of a class is defined outside that class' scope but it has the right to access all private and protected members of the class. Even though the prototypes for friend functions appear in the class definition, friends are not member functions.

A friend can be a function, function template, or member function, or a class or class template, in which case the entire class and all of its members are friends.
```

Example - 

```
class Box {
   double width;
   
   public:
      friend void printWidth( Box box );
      void setWidth( double wid );
};

// Member function definition
void Box::setWidth( double wid ) {
   width = wid;
}

// Note: printWidth() is not a member function of any class.
void printWidth( Box box ) {
   /* Because printWidth() is a friend of Box, it can
   directly access any member of this class */
   cout << "Width of box : " << box.width <<endl;

```

### Inheritance

**The idea of inheritance implements the is a relationship. For example, mammal IS-A animal, dog IS-A mammal hence dog IS-A animal as well and so on**

```
class derived-class: access-specifier base-class
```

### Polymorphism

**C++ polymorphism means that a call to a member function will cause a different function to be executed depending on the type of object that invokes the function**

Consider the following example - 

```
class Shape {
   protected:
      int width, height;
      
   public:
      Shape( int a = 0, int b = 0){
         width = a;
         height = b;
      }
      int area() {
         cout << "Parent class area :" <<endl;
         return 0;
      }
};
class Rectangle: public Shape {
   public:
      Rectangle( int a = 0, int b = 0):Shape(a, b) { }
      
      int area () { 
         cout << "Rectangle class area :" <<endl;
         return (width * height); 
      }
};

class Triangle: public Shape {
   public:
      Triangle( int a = 0, int b = 0):Shape(a, b) { }
      
      int area () { 
         cout << "Triangle class area :" <<endl;
         return (width * height / 2); 
      }
};

// Main function for the program
int main() {
   Shape *shape;
   Rectangle rec(10,7);
   Triangle  tri(10,5);

   // store the address of Rectangle
   shape = &rec;
   
   // call rectangle area.
   shape->area();

   // store the address of Triangle
   shape = &tri;
   
   // call triangle area.
   shape->area();
   
   return 0;
}
```

This code won't return anything. **The reason for the incorrect output is that the call of the function `area()` is being set once by the compiler as the version defined in the base class. This is called `static resolution` of the function call, or `static linkage` - the function call is fixed before the program is executed. This is also sometimes called `early binding` because the area() function is set during the compilation of the program.**

Solution - `virtual` - Dynamic linkage.

```
class Shape {
   protected:
      int width, height;
      
   public:
      Shape( int a = 0, int b = 0) {
         width = a;
         height = b;
      }
      virtual int area() {
         cout << "Parent class area :" <<endl;
         return 0;
      }
};
```

### Virtual Function

A virtual function is a function in a base class that is declared using the keyword virtual. Defining in a base class a virtual function, with another version in a derived class, signals to the compiler that we don't want static linkage for this function.

What we do want is the selection of the function to be called at any given point in the program to be based on the kind of object for which it is called. This sort of operation is referred to as dynamic linkage, or late binding.

### Pure Virtual Function

It is possible that you want to include a virtual function in a base class so that it may be redefined in a derived class to suit the objects of that class, but that there is no meaningful definition you could give for the function in the base class.

```
class Shape {
   protected:
      int width, height;

   public:
      Shape(int a = 0, int b = 0) {
         width = a;
         height = b;
      }
      
      // pure virtual function
      virtual int area() = 0;
};
```

### Abstract Class

```
Abstract class is used when you know partial implementation, where say out of 5 methods, you know implementation of 3 methods and don't know implemenatation of 2 methods in that case 2 methods will be abstract and you need to rely on implementer as a contract to must provide body of abstract methods to accomplish the task.
```

```
by abstract class you mean a C++ class with virtual methods that can be overridden, and some code, but at least one pure virtual method that makes the class not instantiable.
```

```
class MyAbstractClass
{
public:
  virtual ~MyAbstractClass();

  virtual void Method1();
  virtual void Method2();
  void Method3();

  virtual void Method4() = 0; // make MyAbstractClass not instantiable
};
```

### Interface

**Describes the behavior or capabilities without committing to a particular implementation. Kind of like API Declaration.**

[Tutorials Point Tutorial](https://www.tutorialspoint.com/cplusplus/cpp_interfaces.htm)

```
by interface you mean a C++ class with only pure virtual methods (i.e. without any code)
```

```
Interface is used when you don't know anything about implementation but know the contract that implementer should have to accomplish the task.
```

```
class MyInterface
{
public:
  // Empty virtual destructor for proper cleanup
  virtual ~MyInterface() {}

  virtual void Method1() = 0;
  virtual void Method2() = 0;
};
```

[A nice C++ doc](http://www.stroustrup.com/bs_faq2.html)

