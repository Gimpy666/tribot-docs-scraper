# Hitsplat.Type (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/types/Hitsplat.Type.html

**Package:** Packageorg.tribot.script.sdk.types

---

* java.lang.Object
* + java.lang.Enum<[Hitsplat.Type](Hitsplat.Type.html "enum in org.tribot.script.sdk.types")>
+ - org.tribot.script.sdk.types.Hitsplat.Type

* All Implemented Interfaces:
`java.io.Serializable`, `java.lang.Comparable<[Hitsplat.Type](Hitsplat.Type.html "enum in org.tribot.script.sdk.types")>`

Enclosing class:
[Hitsplat](Hitsplat.html "class in org.tribot.script.sdk.types")

---

```
public static enum Hitsplat.Type
extends java.lang.Enum<[Hitsplat.Type](Hitsplat.Type.html "enum in org.tribot.script.sdk.types")>
```

An enumeration of hitsplat types.

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[BLEED](#BLEED)` | Bleeding hit splat type (light red). |
| `[BLOCK\_ME](#BLOCK_ME)` | Blocking damage by me (blue). |
| `[BLOCK\_OTHER](#BLOCK_OTHER)` | Blocking damage by others (blue). |
| `[DAMAGE\_ME](#DAMAGE_ME)` | Taking damage by me (red). |
| `[DAMAGE\_ME\_CYAN](#DAMAGE_ME_CYAN)` | Taking damage by me (cyan). |
| `[DAMAGE\_ME\_ORANGE](#DAMAGE_ME_ORANGE)` | Taking damage by me (orange). |
| `[DAMAGE\_ME\_WHITE](#DAMAGE_ME_WHITE)` | Taking damage by me (white). |
| `[DAMAGE\_ME\_YELLOW](#DAMAGE_ME_YELLOW)` | Taking damage by me (yellow). |
| `[DAMAGE\_OTHER](#DAMAGE_OTHER)` | Taking damage by others (red). |
| `[DAMAGE\_OTHER\_CYAN](#DAMAGE_OTHER_CYAN)` | Taking damage by others (cyan). |
| `[DAMAGE\_OTHER\_ORANGE](#DAMAGE_OTHER_ORANGE)` | Taking damage by others (orange). |
| `[DAMAGE\_OTHER\_WHITE](#DAMAGE_OTHER_WHITE)` | Taking damage by others (white/black). |
| `[DAMAGE\_OTHER\_YELLOW](#DAMAGE_OTHER_YELLOW)` | Taking damage by others (yellow). |
| `[DISEASE](#DISEASE)` | Damage from disease (orange). |
| `[HEAL](#HEAL)` | Healing (purple). |
| `[POISON](#POISON)` | Damage from poison (green). |
| `[UNKNOWN](#UNKNOWN)` | Unknown hit splat type |
| `[VENOM](#VENOM)` | Damage from venom (teal). |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [Hitsplat.Type](Hitsplat.Type.html "enum in org.tribot.script.sdk.types")` | `[valueOf](#valueOf(java.lang.String))​(java.lang.String name)` | Returns the enum constant of this type with the specified name. |
| `static [Hitsplat.Type](Hitsplat.Type.html "enum in org.tribot.script.sdk.types")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
- ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

- #### BLOCK\_ME

```
public static final [Hitsplat.Type](Hitsplat.Type.html "enum in org.tribot.script.sdk.types") BLOCK_ME
```

Blocking damage by me (blue).
- #### BLOCK\_OTHER

```
public static final [Hitsplat.Type](Hitsplat.Type.html "enum in org.tribot.script.sdk.types") BLOCK_OTHER
```

Blocking damage by others (blue).
- #### DAMAGE\_ME

```
public static final [Hitsplat.Type](Hitsplat.Type.html "enum in org.tribot.script.sdk.types") DAMAGE_ME
```

Taking damage by me (red).
- #### DAMAGE\_OTHER

```
public static final [Hitsplat.Type](Hitsplat.Type.html "enum in org.tribot.script.sdk.types") DAMAGE_OTHER
```

Taking damage by others (red).
- #### DAMAGE\_ME\_CYAN

```
public static final [Hitsplat.Type](Hitsplat.Type.html "enum in org.tribot.script.sdk.types") DAMAGE_ME_CYAN
```

Taking damage by me (cyan).
- #### DAMAGE\_OTHER\_CYAN

```
public static final [Hitsplat.Type](Hitsplat.Type.html "enum in org.tribot.script.sdk.types") DAMAGE_OTHER_CYAN
```

Taking damage by others (cyan).
- #### DAMAGE\_ME\_ORANGE

```
public static final [Hitsplat.Type](Hitsplat.Type.html "enum in org.tribot.script.sdk.types") DAMAGE_ME_ORANGE
```

Taking damage by me (orange).
- #### DAMAGE\_OTHER\_ORANGE

```
public static final [Hitsplat.Type](Hitsplat.Type.html "enum in org.tribot.script.sdk.types") DAMAGE_OTHER_ORANGE
```

Taking damage by others (orange).
- #### DAMAGE\_ME\_YELLOW

```
public static final [Hitsplat.Type](Hitsplat.Type.html "enum in org.tribot.script.sdk.types") DAMAGE_ME_YELLOW
```

Taking damage by me (yellow).
- #### DAMAGE\_OTHER\_YELLOW

```
public static final [Hitsplat.Type](Hitsplat.Type.html "enum in org.tribot.script.sdk.types") DAMAGE_OTHER_YELLOW
```

Taking damage by others (yellow).
- #### DAMAGE\_ME\_WHITE

```
public static final [Hitsplat.Type](Hitsplat.Type.html "enum in org.tribot.script.sdk.types") DAMAGE_ME_WHITE
```

Taking damage by me (white).
- #### DAMAGE\_OTHER\_WHITE

```
public static final [Hitsplat.Type](Hitsplat.Type.html "enum in org.tribot.script.sdk.types") DAMAGE_OTHER_WHITE
```

Taking damage by others (white/black).
- #### POISON

```
public static final [Hitsplat.Type](Hitsplat.Type.html "enum in org.tribot.script.sdk.types") POISON
```

Damage from poison (green).
- #### VENOM

```
public static final [Hitsplat.Type](Hitsplat.Type.html "enum in org.tribot.script.sdk.types") VENOM
```

Damage from venom (teal).
- #### DISEASE

```
public static final [Hitsplat.Type](Hitsplat.Type.html "enum in org.tribot.script.sdk.types") DISEASE
```

Damage from disease (orange).
- #### HEAL

```
public static final [Hitsplat.Type](Hitsplat.Type.html "enum in org.tribot.script.sdk.types") HEAL
```

Healing (purple).
- #### BLEED

```
public static final [Hitsplat.Type](Hitsplat.Type.html "enum in org.tribot.script.sdk.types") BLEED
```

Bleeding hit splat type (light red).
- #### UNKNOWN

```
public static final [Hitsplat.Type](Hitsplat.Type.html "enum in org.tribot.script.sdk.types") UNKNOWN
```

Unknown hit splat type

+ ### Method Detail

- #### values

```
public static [Hitsplat.Type](Hitsplat.Type.html "enum in org.tribot.script.sdk.types")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (Hitsplat.Type c : Hitsplat.Type.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [Hitsplat.Type](Hitsplat.Type.html "enum in org.tribot.script.sdk.types") valueOf​(java.lang.String name)
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