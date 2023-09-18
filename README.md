This is a collection of various code elements that either implement design principles or flat-out ignore them.
-


Either way, this is my personal little research tunnel.
-

  
Design Principles I enjoy:
SOLID Principle
Each letter in "SOLID" stands for a principle:

S: Single Responsibility Principle (SRP) - Each part of the code should do only one thing.
Single Responsibility Principle states that every class should have a single responsibility. There should never be more than one reason for a class to change.

Just because you can add everything you want into your class doesn’t mean that you should. Thinking in terms of responsibilities will help you design your application better. Ask yourself whether the logic you are introducing should live in this class or not. Using layers in your application helps a lot. Split big classes in smaller ones, and avoid huge classes. Last but not least, write straightforward comments. If you start writing comments such as in this case, but if, except when, or, then you are doing it wrong.

O: Open/Closed Principle (OCP) - Code should be open to adding new features but closed to changing existing ones.
Open/Closed Principle or OCP states that software entities should be open for extension, but closed for modification.

You should make all member variables private by default. Write getters and setters only when you need them. 

L: Liskov Substitution Principle (LSP) - Substituting one part of code with another shouldn't break anything.
Liskov Substitution Principle states that objects in a program should be replaceable with instances of their subtypes without altering the correctness of the program.

I: Interface Segregation Principle (ISP) - Code should use small and specific parts, rather than big and general ones.
Interface Segregation Principle states that many client-specific interfaces are better than one general-purpose interface. In other words, you should not have to implement methods that you don’t use. 

Note that this is similar to the Single Responsibility Principle. An interface is a contract that meets a need. It is ok to have a class that implements different interfaces, but be careful, don’t violate SRP.

D: Dependency Inversion Principle (DIP) - High-level parts of code shouldn't depend directly on low-level parts.
Dependency Inversion Principle has two key points:
 * Abstractions should not depend upon details;
 * Details should depend upon abstractions.
This principle could be rephrased as use the same level of abstraction at a given level. Interfaces should depend on other interfaces. Don’t add concrete classes to method signatures of an interface. However, use interfaces in your class methods.

