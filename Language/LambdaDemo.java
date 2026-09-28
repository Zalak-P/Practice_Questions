import java.util.*;
import java.util.stream.Collectors;
import java.util.function.*;

public class LambdaDemo {
    public static void main(String[] args) {
        System.out.println("=== PART 1: THE 4 MAIN BUILT-IN FUNCTIONS ===");

        // 1. Predicate<T>: Takes 1 input, returns a boolean (Used for testing/filtering) [4]
        Predicate<Integer> isEven = (num) -> num % 2 == 0;
        System.out.println("Is 8 even? " + isEven.test(8)); // Output: true

        // 2. Function<T, R>: Takes 1 input 'T', transforms it, returns a result 'R' [4]
        Function<String, Integer> stringLength = (str) -> str.length();
        System.out.println("Length of 'Java': " + stringLength.apply("Java")); // Output: 4

        // 3. Consumer<T>: Takes 1 input, performs an action, returns nothing (void) [4]
        Consumer<String> printGreeting = (name) -> System.out.println("Hello, " + name + "!");
        printGreeting.accept("Developer"); // Output: Hello, Developer!

        // 4. Supplier<T>: Takes NO inputs, returns a freshly generated value 'T' [4]
        Supplier<Double> randomValue = () -> Math.random();
        System.out.println("Random Supplier generated: " + randomValue.get());


        System.out.println("\n=== PART 2: LAMBDA SYNTAX VARIATIONS ===");

        // Variation A: Zero Parameters (Requires empty parentheses)
        Runnable zeroParam = () -> System.out.println("Zero parameter lambda running.");
        zeroParam.run();

        // Variation B: Single Parameter (Parentheses can be completely omitted!)
        Consumer<Integer> singleParam = x -> System.out.println("Single param squared: " + (x * x));
        singleParam.accept(5); // Output: 25

        // Variation C: Multiple Parameters (Requires parentheses around inputs)
        BiFunction<Integer, Integer, Integer> multiply = (a, b) -> a * b;
        System.out.println("Multi-param result: " + multiply.apply(4, 5)); // Output: 20

        // Variation D: Multi-line Body (Requires curly braces {} and an explicit 'return' statement)
        Function<String, String> multiLine = (input) -> {
            String cleared = input.trim();
            String upper = cleared.toUpperCase();
            return upper + "_PROCESSED";
        };
        System.out.println("Multi-line result: " + multiLine.apply("   lambda   ")); // Output: LAMBDA_PROCESSED


        System.out.println("\n=== PART 3: METHOD REFERENCES (THE LAMBDA SHORTCUT) ===");

        List<String> frameworkList = Arrays.asList("spring", "hibernate", "quarkus");

        // Standard Lambda Syntax:
        System.out.print("Standard Lambda Print: ");
        frameworkList.forEach(item -> System.out.print(item + " "));
        System.out.println();

        // Compressed Method Reference Syntax (Object::instanceMethod)
        System.out.print("Method Reference Print: ");
        frameworkList.forEach(System.out::print);
        System.out.println();
    }
}



record Employee(String name, String department, double salary, int age) {
}

public class CompleteStreamDemo {
    public static void main(String[] args) {
        List<Employee> employees = Arrays.asList(
                new Employee("Alice", "IT", 85000, 26),
                new Employee("Bob", "HR", 60000, 32),
                new Employee("Charlie", "IT", 95000, 41),
                new Employee("David", "Finance", 70000, 29),
                new Employee("Eva", "HR", 65000, 24),
                new Employee("Frank", "Finance", 110000, 35));

        System.out.println("=== 1. INTERMEDIATE OPERATIONS ===");

        // filter(): Keeps elements matching a condition
        System.out.print("IT Employees: ");
        employees.stream()
                .filter(emp -> emp.department().equals("IT"))
                .forEach(emp -> System.out.print(emp.name() + " "));
        System.out.println();

        // map(): Transforms objects into something else (Employee -> String)
        List<String> namesInUppercase = employees.stream()
                .map(emp -> emp.name().toUpperCase())
                .collect(Collectors.toList());
        System.out.println("Uppercase Names: " + namesInUppercase);

        // sorted(): Sorts elements (using a custom comparator by age)
        System.out.print("Sorted by Age: ");
        employees.stream()
                .sorted(Comparator.comparingInt(Employee::age))
                .forEach(emp -> System.out.print(emp.name() + "(" + emp.age() + ") "));
        System.out.println();

        // limit() & skip(): Truncates and skips data
        System.out.print("Skip 1st, show next 2: ");
        employees.stream()
                .skip(1)
                .limit(2)
                .forEach(emp -> System.out.print(emp.name() + " "));
        System.out.println("\n");

        System.out.println("=== 2. TERMINAL OPERATIONS ===");

        // collect(): Bundles stream back into a collection
        Set<String> departments = employees.stream()
                .map(Employee::department)
                .collect(Collectors.toSet()); // Removes duplicates
        System.out.println("Unique Departments: " + departments);

        // count(): Returns total elements matching criteria
        long highEarnersCount = employees.stream()
                .filter(emp -> emp.salary() > 80000)
                .count();
        System.out.println("Employees earning > 80k: " + highEarnersCount);

        // reduce(): Combines all elements into a single summary value
        double totalPayroll = employees.stream()
                .map(Employee::salary)
                .reduce(0.0, Double::sum);
        System.out.println("Total Payroll Expense: $" + totalPayroll);

        // min() & max(): Finds extreme boundary objects
        Optional<Employee> oldest = employees.stream()
                .max(Comparator.comparingInt(Employee::age));
        oldest.ifPresent(emp -> System.out.println("Oldest Employee: " + emp.name()));

        System.out.println("\n=== 3. MATCHING & FINDING ===");

        // anyMatch(): Returns true if AT LEAST ONE matches
        boolean hasYoungStaff = employees.stream().anyMatch(emp -> emp.age() < 25);
        System.out.println("Any staff under 25? " + hasYoungStaff);

        // allMatch(): Returns true if EVERY element matches
        boolean everyoneEarnsWell = employees.stream().allMatch(emp -> emp.salary() >= 50000);
        System.out.println("Does everyone earn >= 50k? " + everyoneEarnsWell);

        // findFirst(): Safely finds the first match in the sequence
        Optional<Employee> firstFinance = employees.stream()
                .filter(emp -> emp.department().equals("Finance"))
                .findFirst();
        firstFinance.ifPresent(emp -> System.out.println("First Finance employee: " + emp.name()));

        System.out.println("\n=== 4. ADVANCED COLLECTORS ===");

        // Collectors.groupingBy(): Groups items into a Map (Like SQL GROUP BY)
        Map<String, List<Employee>> employeesByDept = employees.stream()
                .collect(Collectors.groupingBy(Employee::department));
        System.out.println("Grouped by Dept: " + employeesByDept.keySet());
    }
}
