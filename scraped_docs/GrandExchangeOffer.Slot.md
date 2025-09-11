# GrandExchangeOffer.Slot (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/types/GrandExchangeOffer.Slot.html

**Package:** Packageorg.tribot.script.sdk.types

---

* java.lang.Object
* + java.lang.Enum<[GrandExchangeOffer.Slot](GrandExchangeOffer.Slot.html "enum in org.tribot.script.sdk.types")>
+ - org.tribot.script.sdk.types.GrandExchangeOffer.Slot

* All Implemented Interfaces:
`java.io.Serializable`, `java.lang.Comparable<[GrandExchangeOffer.Slot](GrandExchangeOffer.Slot.html "enum in org.tribot.script.sdk.types")>`

Enclosing class:
[GrandExchangeOffer](GrandExchangeOffer.html "class in org.tribot.script.sdk.types")

---

```
public static enum GrandExchangeOffer.Slot
extends java.lang.Enum<[GrandExchangeOffer.Slot](GrandExchangeOffer.Slot.html "enum in org.tribot.script.sdk.types")>
```

The grand exchange offer slots, starting from the top left to the top right, then the bottom left to the bottom right

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[EIGHT](#EIGHT)` | |
| `[FIVE](#FIVE)` | |
| `[FOUR](#FOUR)` | |
| `[ONE](#ONE)` | |
| `[SEVEN](#SEVEN)` | |
| `[SIX](#SIX)` | |
| `[THREE](#THREE)` | |
| `[TWO](#TWO)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `boolean` | `[isEnabled](#isEnabled())()` | Checks if this slot is enabled - non-members cannot trade more than the first 3 slots |
| `static [GrandExchangeOffer.Slot](GrandExchangeOffer.Slot.html "enum in org.tribot.script.sdk.types")` | `[valueOf](#valueOf(java.lang.String))​(java.lang.String name)` | Returns the enum constant of this type with the specified name. |
| `static [GrandExchangeOffer.Slot](GrandExchangeOffer.Slot.html "enum in org.tribot.script.sdk.types")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
- ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

- #### ONE

```
public static final [GrandExchangeOffer.Slot](GrandExchangeOffer.Slot.html "enum in org.tribot.script.sdk.types") ONE
```
- #### TWO

```
public static final [GrandExchangeOffer.Slot](GrandExchangeOffer.Slot.html "enum in org.tribot.script.sdk.types") TWO
```
- #### THREE

```
public static final [GrandExchangeOffer.Slot](GrandExchangeOffer.Slot.html "enum in org.tribot.script.sdk.types") THREE
```
- #### FOUR

```
public static final [GrandExchangeOffer.Slot](GrandExchangeOffer.Slot.html "enum in org.tribot.script.sdk.types") FOUR
```
- #### FIVE

```
public static final [GrandExchangeOffer.Slot](GrandExchangeOffer.Slot.html "enum in org.tribot.script.sdk.types") FIVE
```
- #### SIX

```
public static final [GrandExchangeOffer.Slot](GrandExchangeOffer.Slot.html "enum in org.tribot.script.sdk.types") SIX
```
- #### SEVEN

```
public static final [GrandExchangeOffer.Slot](GrandExchangeOffer.Slot.html "enum in org.tribot.script.sdk.types") SEVEN
```
- #### EIGHT

```
public static final [GrandExchangeOffer.Slot](GrandExchangeOffer.Slot.html "enum in org.tribot.script.sdk.types") EIGHT
```

+ ### Method Detail

- #### values

```
public static [GrandExchangeOffer.Slot](GrandExchangeOffer.Slot.html "enum in org.tribot.script.sdk.types")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (GrandExchangeOffer.Slot c : GrandExchangeOffer.Slot.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [GrandExchangeOffer.Slot](GrandExchangeOffer.Slot.html "enum in org.tribot.script.sdk.types") valueOf​(java.lang.String name)
```

Returns the enum constant of this type with the specified name.
The string must match *exactly* an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

Parameters:
`name` - the name of the enum constant to be returned.
Returns:
the enum constant with the specified name
Throws:
`java.lang.IllegalArgumentException` - if this enum type has no constant with the specified name
`java.lang.NullPointerException` - if the argument is null
- #### isEnabled

```
public boolean isEnabled()
```

Checks if this slot is enabled - non-members cannot trade more than the first 3 slots

Returns:
true if this slot is enabled, false otherwise