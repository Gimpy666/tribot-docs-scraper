# Waiting (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/Waiting.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.Waiting

* ---

```
public class Waiting
extends java.lang.Object
```

Utilities for waiting (variable sleeps based on a condition and static waits). All numbers are milliseconds.

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[Waiting](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static void` | `[wait](#wait(int))​(int millis)` | Waits for the specified milliseconds |
| `static void` | `[waitNormal](#waitNormal(int,int))​(int mean,
int std)` | Waits for a random amount of time, using the mean/sd parameters in a normal distribution to pick a random value |
| `static void` | `[waitUniform](#waitUniform(int,int))​(int min,
int max)` | Waits for a random amount of time, using the min/max range in a uniform distribution to pick a random value |
| `static boolean` | `[waitUntil](#waitUntil(int,int,java.util.function.BooleanSupplier))​(int timeout,
int step,
java.util.function.BooleanSupplier condition)` | Waits until the specified condition is true, or the timeout limit is reached |
| `static boolean` | `[waitUntil](#waitUntil(int,java.util.function.BooleanSupplier))​(int timeout,
java.util.function.BooleanSupplier condition)` | Waits until the specified condition is true, or the timeout limit is reached |
| `static boolean` | `[waitUntil](#waitUntil(java.util.function.BooleanSupplier))​(java.util.function.BooleanSupplier condition)` | Waits until the specified condition is true, or times out after around 10 seconds |
| `static boolean` | `[waitUntilAnimating](#waitUntilAnimating(int))​(int timeout)` | Waits until my player is animating, or the timeout limit is reached |
| `static boolean` | `[waitUntilInArea](#waitUntilInArea(org.tribot.script.sdk.types.Area,int))​([Area](types/Area.html "class in org.tribot.script.sdk.types") area,
int timeout)` | Waits until my player is in the specified area, or the timeout limit is reached |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### Waiting

```
public Waiting()
```

+ ### Method Detail

- #### waitUniform

```
public static void waitUniform​(int min,
int max)
```

Waits for a random amount of time, using the min/max range in a uniform distribution to pick a random value

Parameters:
`min` - the min value
`max` - the max value
- #### waitNormal

```
public static void waitNormal​(int mean,
int std)
```

Waits for a random amount of time, using the mean/sd parameters in a normal distribution to pick a random value

Parameters:
`mean` - the mean
`std` - the standard deviation
- #### wait

```
public static void wait​(int millis)
```

Waits for the specified milliseconds

Parameters:
`millis` - the amount of milliseconds to wait for
- #### waitUntil

```
public static boolean waitUntil​(java.util.function.BooleanSupplier condition)
```

Waits until the specified condition is true, or times out after around 10 seconds

Parameters:
`condition` - the condition
Returns:
true if the condition was true, false if the timeout was reached
- #### waitUntil

```
public static boolean waitUntil​(int timeout,
java.util.function.BooleanSupplier condition)
```

Waits until the specified condition is true, or the timeout limit is reached

Parameters:
`timeout` - the timeout in milliseconds
`condition` - the condition to check
Returns:
true if the condition was true, false if the timeout was reached
- #### waitUntil

```
public static boolean waitUntil​(int timeout,
int step,
java.util.function.BooleanSupplier condition)
```

Waits until the specified condition is true, or the timeout limit is reached

Parameters:
`timeout` - the timeout in milliseconds
`step` - the amount of time inbetween each condition check
`condition` - the condition to check
Returns:
true if the condition was true, false if the timeout was reached
- #### waitUntilAnimating

```
public static boolean waitUntilAnimating​(int timeout)
```

Waits until my player is animating, or the timeout limit is reached

Parameters:
`timeout` - the timeout in milliseconds
Returns:
true if the player started animating, false if the timeout was reached
- #### waitUntilInArea

```
public static boolean waitUntilInArea​([Area](types/Area.html "class in org.tribot.script.sdk.types") area,
int timeout)
```

Waits until my player is in the specified area, or the timeout limit is reached

Parameters:
`area` - the area that the player will be in
`timeout` - the timeout in milliseconds
Returns:
true if the player reached the area, false if the timeout was reached