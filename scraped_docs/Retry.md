# Retry (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/util/Retry.html

**Package:** Packageorg.tribot.script.sdk.util

---

* java.lang.Object
* + org.tribot.script.sdk.util.Retry

* ---

```
public class Retry
extends java.lang.Object
```

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[Retry](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static boolean` | `[retry](#retry(int,java.util.function.BooleanSupplier))​(int maxRetries,
java.util.function.BooleanSupplier action)` | Helper function for performing a given action multiple times to achieve the desired result |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### Retry

```
public Retry()
```

+ ### Method Detail

- #### retry

```
public static boolean retry​(int maxRetries,
java.util.function.BooleanSupplier action)
```

Helper function for performing a given action multiple times to achieve the desired result

Parameters:
`maxRetries` - Max number of times to run the action
`action` - The action to run. Must return true for success and false for failure
Returns:
If the action returns true for any attempt