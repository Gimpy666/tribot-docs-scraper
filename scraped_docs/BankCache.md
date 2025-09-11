# BankCache (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/cache/BankCache.html

**Package:** Packageorg.tribot.script.sdk.cache

---

* java.lang.Object
* + org.tribot.script.sdk.cache.BankCache

* ---

```
public class BankCache
extends java.lang.Object
```

Provides a cache that keeps track of all the items in the bank. This updates when opening and closing the bank using
the standard Bank API. Can also be updated manually. Only stores item IDs and Stacks to minimize memory.

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[BankCache](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static java.util.Set<java.util.Map.Entry<java.lang.Integer,​java.lang.Integer>>` | `[entries](#entries())()` | Gets all the cache entries |
| `static int` | `[getStack](#getStack(int))​(int itemId)` | Gets the amount of the given itemID is contained in the bank cache. |
| `static boolean` | `[isInitialized](#isInitialized())()` | Determines if the cache has had its first successful update yet. |
| `static void` | `[update](#update())()` | Updates the cache with all the bank items. |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### BankCache

```
public BankCache()
```

+ ### Method Detail

- #### update

```
public static void update()
```

Updates the cache with all the bank items. Does nothing if the bank screen isn't open.
- #### isInitialized

```
public static boolean isInitialized()
```

Determines if the cache has had its first successful update yet.
- #### getStack

```
public static int getStack​(int itemId)
```

Gets the amount of the given itemID is contained in the bank cache.

Parameters:
`itemId` - The item to check
Returns:
The amount of the item in the bank cache
- #### entries

```
public static java.util.Set<java.util.Map.Entry<java.lang.Integer,​java.lang.Integer>> entries()
```

Gets all the cache entries

Returns:
An set of entries of ID to Amount