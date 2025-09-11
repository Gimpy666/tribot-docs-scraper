# Tribot (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/Tribot.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.Tribot

* ---

```
public class Tribot
extends java.lang.Object
```

Contains methods to obtain information about the tribot environment

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[Tribot](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static int` | `[getCurrentUserId](#getCurrentUserId())()` | |
| `static java.io.File` | `[getDirectory](#getDirectory())()` | Gets the TRiBot directory (for example, on windows this will be %appdata%/.tribot). |
| `static java.lang.String` | `[getUsername](#getUsername())()` | Determines the username of the user running the script. |
| `static boolean` | `[isTribotEcho](#isTribotEcho())()` | |
| `static boolean` | `[isTribotX](#isTribotX())()` | |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### Tribot

```
public Tribot()
```

+ ### Method Detail

- #### getUsername

```
public static java.lang.String getUsername()
```

Determines the username of the user running the script.
If for some reason the logged in user does not have a username, this will be an empty string.
- #### getCurrentUserId

```
public static int getCurrentUserId()
```
- #### getDirectory

```
public static java.io.File getDirectory()
```

Gets the TRiBot directory (for example, on windows this will be %appdata%/.tribot).
Scripts can access this directory.

Returns:
the TRiBot directory
- #### isTribotX

```
public static boolean isTribotX()
```
- #### isTribotEcho

```
public static boolean isTribotEcho()
```