# Decorator Pattern — Mario Power-Up Example

## What is the Decorator Pattern?

The **Decorator Pattern** is used when we want to add new behavior to an object dynamically without modifying the original class.

In this example, we start with a basic `Mario` object and keep wrapping it with different power-ups.

```text
StarPowerUp(
    GunPowerUp(
        HeightUp(
            Mario
        )
    )
)
```

Each power-up adds extra behavior while still behaving like a `Character`.

---

## UML Structure

```text
                 Character
                    |
        -------------------------
        |                       |
      Mario             CharacterDecorator
                                |
                --------------------------------
                |              |               |
             HeightUp      GunPowerUp      StarPowerUp
```

---

## Design Flow

### 1. Character defines common behavior

`Character` is the common interface/base class.

```java
String getAbilities();
```

Every character and every decorator must follow this method.

---

### 2. Mario is the concrete base object

`Mario` is the original object.

```java
class Mario implements Character {
    public String getAbilities() {
        return "Mario";
    }
}
```

At this point:

```java
mario.getAbilities();
```

returns:

```text
Mario
```

---

### 3. CharacterDecorator stores a Character object

`CharacterDecorator` is the abstract wrapper.

It has two important responsibilities:

```text
is-a Character
has-a Character
```

That means:

- It behaves like a `Character`
- It also stores another `Character` inside it

```java
abstract class CharacterDecorator implements Character {
    protected Character character;

    public CharacterDecorator(Character c) {
        this.character = c;
    }
}
```

This is what allows one decorator to wrap another decorator.

---

### 4. HeightUp extends CharacterDecorator

`HeightUp` adds height ability.

```java
class HeightUp extends CharacterDecorator {
    public HeightUp(Character c) {
        super(c);
    }

    public String getAbilities() {
        return character.getAbilities() + " with HeightUp";
    }
}
```

Usage:

```java
mario = new HeightUp(mario);
```

Now Mario becomes:

```text
HeightUp(Mario)
```

---

### 5. GunPowerUp extends CharacterDecorator

`GunPowerUp` adds gun ability.

```java
class GunPowerUp extends CharacterDecorator {
    public GunPowerUp(Character c) {
        super(c);
    }

    public String getAbilities() {
        return character.getAbilities() + " with Gun";
    }
}
```

Usage:

```java
mario = new GunPowerUp(mario);
```

Now Mario becomes:

```text
GunPowerUp(HeightUp(Mario))
```

---

### 6. StarPowerUp extends CharacterDecorator

`StarPowerUp` adds temporary star power.

```java
class StarPowerUp extends CharacterDecorator {
    public StarPowerUp(Character c) {
        super(c);
    }

    public String getAbilities() {
        return character.getAbilities() + " with Star Power";
    }
}
```

Usage:

```java
mario = new StarPowerUp(mario);
```

Now Mario becomes:

```text
StarPowerUp(GunPowerUp(HeightUp(Mario)))
```

---

## Client Code Flow

```java
Character mario = new Mario();

mario = new HeightUp(mario);
mario = new GunPowerUp(mario);
mario = new StarPowerUp(mario);
```

The client keeps reassigning `mario` to the newly decorated object.

Final object structure:

```text
StarPowerUp(
    GunPowerUp(
        HeightUp(
            Mario
        )
    )
)
```

Final output:

```text
Mario with HeightUp with Gun with Star Power
```

---

## What changes if a new power-up is added later?

Suppose we want to add a new power-up called `FirePowerUp`.

We do **not** change these existing classes:

```text
Mario
Character
HeightUp
GunPowerUp
StarPowerUp
```

We only add one new class:

```java
class FirePowerUp extends CharacterDecorator {
    public FirePowerUp(Character c) {
        super(c);
    }

    public String getAbilities() {
        return character.getAbilities() + " with Fire";
    }
}
```

Then use it like this:

```java
mario = new FirePowerUp(mario);
```

Now the object can become:

```text
FirePowerUp(
    StarPowerUp(
        GunPowerUp(
            HeightUp(
                Mario
            )
        )
    )
)
```

---

## Why Decorator Pattern follows Open/Closed Principle

The **Open/Closed Principle** says:

> A class should be open for extension but closed for modification.

Decorator Pattern follows this because:

- We can add new power-ups by creating new decorator classes
- We do not need to modify existing working classes
- Existing code remains stable
- New behavior is added through composition

So instead of creating many subclasses like:

```text
TallMario
GunMario
FireMario
TallGunMario
TallGunFireMario
```

We create small reusable decorators:

```text
HeightUp
GunPowerUp
StarPowerUp
FirePowerUp
```

Then combine them dynamically.

---

## Key Takeaway

Use the Decorator Pattern when:

- You want to add behavior dynamically
- You want to avoid too many subclasses
- You want to follow Open/Closed Principle
- You want flexible object composition

In simple words:

> Decorator Pattern lets us wrap an object with extra features without changing the original object.
