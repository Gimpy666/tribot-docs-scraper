# Player.SkullIcon (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/types/Player.SkullIcon.html

**Package:** Packageorg.tribot.script.sdk.types

---

* java.lang.Object
* + java.lang.Enum<[Player.SkullIcon](Player.SkullIcon.html "enum in org.tribot.script.sdk.types")>
+ - org.tribot.script.sdk.types.Player.SkullIcon

* All Implemented Interfaces:
`java.io.Serializable`, `java.lang.Comparable<[Player.SkullIcon](Player.SkullIcon.html "enum in org.tribot.script.sdk.types")>`

Enclosing class:
[Player](Player.html "class in org.tribot.script.sdk.types")

---

```
public static enum Player.SkullIcon
extends java.lang.Enum<[Player.SkullIcon](Player.SkullIcon.html "enum in org.tribot.script.sdk.types")>
```

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[DEAD\_MAN](#DEAD_MAN)` | |
| `[DEAD\_MAN\_FIVE](#DEAD_MAN_FIVE)` | |
| `[DEAD\_MAN\_FOUR](#DEAD_MAN_FOUR)` | |
| `[DEAD\_MAN\_ONE](#DEAD_MAN_ONE)` | |
| `[DEAD\_MAN\_THREE](#DEAD_MAN_THREE)` | |
| `[DEAD\_MAN\_TWO](#DEAD_MAN_TWO)` | |
| `[FORINTHRY](#FORINTHRY)` | |
| `[FORINTHRY\_DEAD\_MAN](#FORINTHRY_DEAD_MAN)` | |
| `[FORINTHRY\_FIVE](#FORINTHRY_FIVE)` | |
| `[FORINTHRY\_FOUR](#FORINTHRY_FOUR)` | |
| `[FORINTHRY\_ONE](#FORINTHRY_ONE)` | |
| `[FORINTHRY\_THREE](#FORINTHRY_THREE)` | |
| `[FORINTHRY\_TWO](#FORINTHRY_TWO)` | |
| `[HIGH\_RISK](#HIGH_RISK)` | |
| `[SKULL](#SKULL)` | |
| `[SKULL\_FIGHT\_PIT](#SKULL_FIGHT_PIT)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [Player.SkullIcon](Player.SkullIcon.html "enum in org.tribot.script.sdk.types")` | `[valueOf](#valueOf(java.lang.String))​(java.lang.String name)` | Returns the enum constant of this type with the specified name. |
| `static [Player.SkullIcon](Player.SkullIcon.html "enum in org.tribot.script.sdk.types")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
- ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

- #### SKULL

```
public static final [Player.SkullIcon](Player.SkullIcon.html "enum in org.tribot.script.sdk.types") SKULL
```
- #### SKULL\_FIGHT\_PIT

```
public static final [Player.SkullIcon](Player.SkullIcon.html "enum in org.tribot.script.sdk.types") SKULL_FIGHT_PIT
```
- #### HIGH\_RISK

```
public static final [Player.SkullIcon](Player.SkullIcon.html "enum in org.tribot.script.sdk.types") HIGH_RISK
```
- #### FORINTHRY

```
public static final [Player.SkullIcon](Player.SkullIcon.html "enum in org.tribot.script.sdk.types") FORINTHRY
```
- #### FORINTHRY\_DEAD\_MAN

```
public static final [Player.SkullIcon](Player.SkullIcon.html "enum in org.tribot.script.sdk.types") FORINTHRY_DEAD_MAN
```
- #### FORINTHRY\_ONE

```
public static final [Player.SkullIcon](Player.SkullIcon.html "enum in org.tribot.script.sdk.types") FORINTHRY_ONE
```
- #### FORINTHRY\_TWO

```
public static final [Player.SkullIcon](Player.SkullIcon.html "enum in org.tribot.script.sdk.types") FORINTHRY_TWO
```
- #### FORINTHRY\_THREE

```
public static final [Player.SkullIcon](Player.SkullIcon.html "enum in org.tribot.script.sdk.types") FORINTHRY_THREE
```
- #### FORINTHRY\_FOUR

```
public static final [Player.SkullIcon](Player.SkullIcon.html "enum in org.tribot.script.sdk.types") FORINTHRY_FOUR
```
- #### FORINTHRY\_FIVE

```
public static final [Player.SkullIcon](Player.SkullIcon.html "enum in org.tribot.script.sdk.types") FORINTHRY_FIVE
```
- #### DEAD\_MAN

```
public static final [Player.SkullIcon](Player.SkullIcon.html "enum in org.tribot.script.sdk.types") DEAD_MAN
```
- #### DEAD\_MAN\_ONE

```
public static final [Player.SkullIcon](Player.SkullIcon.html "enum in org.tribot.script.sdk.types") DEAD_MAN_ONE
```
- #### DEAD\_MAN\_TWO

```
public static final [Player.SkullIcon](Player.SkullIcon.html "enum in org.tribot.script.sdk.types") DEAD_MAN_TWO
```
- #### DEAD\_MAN\_THREE

```
public static final [Player.SkullIcon](Player.SkullIcon.html "enum in org.tribot.script.sdk.types") DEAD_MAN_THREE
```
- #### DEAD\_MAN\_FOUR

```
public static final [Player.SkullIcon](Player.SkullIcon.html "enum in org.tribot.script.sdk.types") DEAD_MAN_FOUR
```
- #### DEAD\_MAN\_FIVE

```
public static final [Player.SkullIcon](Player.SkullIcon.html "enum in org.tribot.script.sdk.types") DEAD_MAN_FIVE
```

+ ### Method Detail

- #### values

```
public static [Player.SkullIcon](Player.SkullIcon.html "enum in org.tribot.script.sdk.types")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (Player.SkullIcon c : Player.SkullIcon.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [Player.SkullIcon](Player.SkullIcon.html "enum in org.tribot.script.sdk.types") valueOf​(java.lang.String name)
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