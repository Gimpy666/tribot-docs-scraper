# WorldHopper (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/WorldHopper.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.WorldHopper

* ---

```
public class WorldHopper
extends java.lang.Object
```

Contains methods for using the world hopper

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[WorldHopper](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static int` | `[getCurrentWorld](#getCurrentWorld())()` | Gets the current world number |
| `static boolean` | `[hop](#hop(int))​(int world)` | Attempts to hop to the specified world, will short circuit if there is any reason we cannot hop |
| `static boolean` | `[isInMembersWorld](#isInMembersWorld())()` | Checks if we are currently in a members world |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### WorldHopper

```
public WorldHopper()
```

+ ### Method Detail

- #### getCurrentWorld

```
public static int getCurrentWorld()
```

Gets the current world number

Returns:
the current world number
- #### isInMembersWorld

```
public static boolean isInMembersWorld()
```

Checks if we are currently in a members world

Returns:
true if we are in a members world, false otherwise
- #### hop

```
public static boolean hop​(int world)
```

Attempts to hop to the specified world, will short circuit if there is any reason we cannot hop

Parameters:
`world` - the world to hop to
Returns:
true if hopped to the specified world, false otherwise