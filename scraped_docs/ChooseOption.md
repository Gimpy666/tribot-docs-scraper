# ChooseOption (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/ChooseOption.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.ChooseOption

* ---

```
public class ChooseOption
extends java.lang.Object
```

Utilities for using the "ChooseOption" interface, which is the box of options that appears when right-clicking things
in the game.

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[ChooseOption](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static boolean` | `[close](#close())()` | Closes the ChooseOption interface |
| `static boolean` | `[ensureDeselected](#ensureDeselected())()` | Deselects a selected item/spell, if one is selected |
| `static boolean` | `[isOpen](#isOpen())()` | Determines if the interface is open. |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### ChooseOption

```
public ChooseOption()
```

+ ### Method Detail

- #### isOpen

```
public static boolean isOpen()
```

Determines if the interface is open.

Returns:
True if open. False otherwise.
- #### close

```
public static boolean close()
```

Closes the ChooseOption interface

Returns:
True if successfully closed. False if not and the interface is still up.
- #### ensureDeselected

```
public static boolean ensureDeselected()
```

Deselects a selected item/spell, if one is selected

Returns:
true if no spell or item is selected anymore, false if a spell or item is selected and it couldn't be deselected