import java.util.*;
import java.util.concurrent.*;
import java.util.stream.*;

// ==========================================
// ADVANCED CONCEPT: INTERFACES & OOP
// ==========================================
interface Worker {
    void performDuty(); // Abstract method
    
    // Java 8+ Default method
    default void logStatus() {
        System.out.println("LOG: Worker status is stable.");
    }
}

// Parent Class (Inheritance & Encapsulation)
class Person {
    private final String name; // Encapsulation: private variable

    public Person(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    // Method to be overridden (Polymorphism)
    public void greet() {
        System.out.println("Hello, I am " + name);
    }
}

// Child Class implementing an Interface
class Engineer extends Person implements Worker {
    private final String specialization;

    public Engineer(String name, String specialization) {
        super(name); // Call parent constructor
        this.specialization = specialization;
    }

    // Polymorphism: Method Overriding
    @Override
    public void greet() {
        System.out.println("Hi, I am " + getName() + ", a " + specialization + " engineer.");
    }

    @Override
    public void performDuty() {
        System.out.println(getName() + " is currently writing clean Java code.");
    }
}

// ==========================================
// ADVANCED CONCEPT: GENERICS (Type Safety)
// ==========================================
class Box<T> {
    private T content;

    public void pack(T item) {
        this.content = item;
    }

    public T unpack() {
        return content;
    }
}

// ==========================================
// MAIN TUTORIAL EXECUTION
// ==========================================
public class JavaMasterclass {

    public static void main(String[] args) {
        System.out.println("=== STARTING JAVA ROADMAP DEMO ===");

        // ------------------------------------------
        // 1. BASIC CONCEPTS
        // ------------------------------------------
        System.out.println("\n--- 1. Basics & Control Flow ---");
        
        // Variables & Data Types
        int age = 25;
        double salary = 85000.50;
        boolean isJavaFun = true;
        char grade = 'A';

        // Conditional Statements (If-Else)
        if (age >= 18 && isJavaFun) {
            System.out.println("Adult learning Java! Grade: " + grade);
        }

        // Loops (For & While)
        System.out.print("Counting up to 3 using a loop: ");
        for (int i = 1; i <= 3; i++) {
            System.out.print(i + " ");
        }
        System.out.println();

        // ------------------------------------------
        // 2. DATA STRUCTURES (Collections Framework)
        // ------------------------------------------
        System.out.println("\n--- 2. Collections (Lists & Maps) ---");
        
        // List implementation
        List<String> frameworkList = new ArrayList<>();
        frameworkList.add("Spring Boot");
        frameworkList.add("Hibernate");
        frameworkList.add("Quarkus");
        System.out.println("Java Frameworks List: " + frameworkList);

        // Map implementation (Key-Value pairs)
        Map<String, String> capitalMap = new HashMap<>();
        capitalMap.put("USA", "Washington D.C.");
        capitalMap.put("UK", "London");
        System.out.println("Capital of USA: " + capitalMap.get("USA"));

        // ------------------------------------------
        // 3. OBJECT-ORIENTED PROGRAMMING (OOP)
        // ------------------------------------------
        System.out.println("\n--- 3. Object-Oriented Programming ---");
        
        Person genericPerson = new Person("Alex");
        genericPerson.greet(); // Parent behavior

        Engineer engineer = new Engineer("Sarah", "Software");
        engineer.greet();       // Polymorphism: Overridden method behavior
        engineer.performDuty(); // Interface method
        engineer.logStatus();   // Interface default method

        // ------------------------------------------
        // 4. EXCEPTIONS & ERROR HANDLING
        // ------------------------------------------
        System.out.println("\n--- 4. Exception Handling ---");
        try {
            int result = 10 / 0; // Will trigger ArithmeticException
        } catch (ArithmeticException e) {
            System.err.println("Caught an Exception safely: Cannot divide by zero.");
        } finally {
            System.out.println("Finally block: This always executes.");
        }

        // ------------------------------------------
        // 5. GENERICS
        // ------------------------------------------
        System.out.println("\n--- 5. Generics ---");
        Box<Integer> integerBox = new Box<>();
        integerBox.pack(42);
        System.out.println("Unpacked type-safe value from Box: " + integerBox.unpack());

        // ------------------------------------------
        // 6. LAMBDAS & THE STREAM API (Functional Java)
        // ------------------------------------------
        System.out.println("\n--- 6. Functional Features (Streams & Lambdas) ---");
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

        // Filter out odd numbers, multiply by 10, and collect into a list
        List<Integer> processedNumbers = numbers.stream()
                .filter(n -> n % 2 == 0)             // Lambda predicate
                .map(filteredNum -> filteredNum * 10) // Lambda mapper
                .collect(Collectors.toList());

        System.out.println("Original numbers: " + numbers);
        System.out.println("Processed even numbers (multiplied by 10): " + processedNumbers);

        // ------------------------------------------
        // 7. MULTITHREADING & CONCURRENCY
        // ------------------------------------------
        System.out.println("\n--- 7. Multithreading & Concurrency ---");
        
        // Creating a thread pool using Executors
        ExecutorService executorService = Executors.newFixedThreadPool(2);

        // Submit tasks using functional Lambdas
        executorService.submit(() -> {
            String threadName = Thread.currentThread().getName();
            System.out.println("Async Task A running smoothly on pool thread: " + threadName);
        });

        executorService.submit(() -> {
            String threadName = Thread.currentThread().getName();
            System.out.println("Async Task B running smoothly on pool thread: " + threadName);
        });

        // Gracefully shut down the thread pool
        executorService.shutdown();
        try {
            // Wait for existing tasks to terminate completely
            if (!executorService.awaitTermination(2, TimeUnit.SECONDS)) {
                executorService.shutdownNow();
            }
        } catch (InterruptedException e) {
            executorService.shutdownNow();
        }

        System.out.println("\n=== ROADMAP DEMO COMPLETE ===");
    }
}
