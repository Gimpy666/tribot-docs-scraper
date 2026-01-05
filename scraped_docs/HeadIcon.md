# HeadIcon (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/HeadIcon.html

**Package:** Packagenet.runelite.api

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + [java.lang.Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[HeadIcon](HeadIcon.html "enum in net.runelite.api")>
+ - net.runelite.api.HeadIcon

* All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/Serializable.html?is-external=true "class or interface in java.io")`, `[Comparable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Comparable.html?is-external=true "class or interface in java.lang")<[HeadIcon](HeadIcon.html "enum in net.runelite.api")>`

---

```
public enum HeadIcon
extends [Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[HeadIcon](HeadIcon.html "enum in net.runelite.api")>
```

An enumeration of prayer icons above the head.

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[DEFLECT\_MAGE](#DEFLECT_MAGE)` | Deflect magic curse |
| `[DEFLECT\_MELEE](#DEFLECT_MELEE)` | Deflect melee curse |
| `[DEFLECT\_RANGE](#DEFLECT_RANGE)` | Deflect range curse |
| `[MAGE\_MELEE](#MAGE_MELEE)` | Protect from mage and melee |
| `[MAGIC](#MAGIC)` | Protect from magic. |
| `[MELEE](#MELEE)` | Protect from melee. |
| `[RANGE\_MAGE](#RANGE_MAGE)` | Protect from range and mage. |
| `[RANGE\_MAGE\_MELEE](#RANGE_MAGE_MELEE)` | Protect from range, mage, and melee |
| `[RANGE\_MELEE](#RANGE_MELEE)` | Protect from range and melee |
| `[RANGED](#RANGED)` | Protect from ranged. |
| `[REDEMPTION](#REDEMPTION)` | Redemption prayer. |
| `[RETRIBUTION](#RETRIBUTION)` | Retribution prayer. |
| `[SMITE](#SMITE)` | Smite prayer. |
| `[SOUL\_SPLIT](#SOUL_SPLIT)` | Soult split curse |
| `[WRATH](#WRATH)` | Wrath curse |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [HeadIcon](HeadIcon.html "enum in net.runelite.api")` | `[valueOf](#valueOf(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)` | Returns the enum constant of this type with the specified name. |
| `static [HeadIcon](HeadIcon.html "enum in net.runelite.api")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#clone() "class or interface in java.lang"), [compareTo](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#compareTo(E) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#finalize() "class or interface in java.lang"), [getDeclaringClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#getDeclaringClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#hashCode() "class or interface in java.lang"), [name](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#name() "class or interface in java.lang"), [ordinal](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#ordinal() "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#toString() "class or interface in java.lang"), [valueOf](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#valueOf(java.lang.Class,java.lang.String) "class or interface in java.lang")`
- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Enum Constant Detail

- #### MELEE

```
public static final [HeadIcon](HeadIcon.html "enum in net.runelite.api") MELEE
```

Protect from melee.
- #### RANGED

```
public static final [HeadIcon](HeadIcon.html "enum in net.runelite.api") RANGED
```

Protect from ranged.
- #### MAGIC

```
public static final [HeadIcon](HeadIcon.html "enum in net.runelite.api") MAGIC
```

Protect from magic.
- #### RETRIBUTION

```
public static final [HeadIcon](HeadIcon.html "enum in net.runelite.api") RETRIBUTION
```

Retribution prayer.
- #### SMITE

```
public static final [HeadIcon](HeadIcon.html "enum in net.runelite.api") SMITE
```

Smite prayer.
- #### REDEMPTION

```
public static final [HeadIcon](HeadIcon.html "enum in net.runelite.api") REDEMPTION
```

Redemption prayer.
- #### RANGE\_MAGE

```
public static final [HeadIcon](HeadIcon.html "enum in net.runelite.api") RANGE_MAGE
```

Protect from range and mage. (ie. used by Kalphite Queen)
- #### RANGE\_MELEE

```
public static final [HeadIcon](HeadIcon.html "enum in net.runelite.api") RANGE_MELEE
```

Protect from range and melee
- #### MAGE\_MELEE

```
public static final [HeadIcon](HeadIcon.html "enum in net.runelite.api") MAGE_MELEE
```

Protect from mage and melee
- #### RANGE\_MAGE\_MELEE

```
public static final [HeadIcon](HeadIcon.html "enum in net.runelite.api") RANGE_MAGE_MELEE
```

Protect from range, mage, and melee
- #### WRATH

```
public static final [HeadIcon](HeadIcon.html "enum in net.runelite.api") WRATH
```

Wrath curse
- #### SOUL\_SPLIT

```
public static final [HeadIcon](HeadIcon.html "enum in net.runelite.api") SOUL_SPLIT
```

Soult split curse
- #### DEFLECT\_MELEE

```
public static final [HeadIcon](HeadIcon.html "enum in net.runelite.api") DEFLECT_MELEE
```

Deflect melee curse
- #### DEFLECT\_RANGE

```
public static final [HeadIcon](HeadIcon.html "enum in net.runelite.api") DEFLECT_RANGE
```

Deflect range curse
- #### DEFLECT\_MAGE

```
public static final [HeadIcon](HeadIcon.html "enum in net.runelite.api") DEFLECT_MAGE
```

Deflect magic curse

+ ### Method Detail

- #### values

```
public static [HeadIcon](HeadIcon.html "enum in net.runelite.api")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (HeadIcon c : HeadIcon.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [HeadIcon](HeadIcon.html "enum in net.runelite.api") valueOf​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)
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
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/IllegalArgumentException.html?is-external=true "class or interface in java.lang")` - if this enum type has no constant with the specified name
`[NullPointerException](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/NullPointerException.html?is-external=true "class or interface in java.lang")` - if the argument is null