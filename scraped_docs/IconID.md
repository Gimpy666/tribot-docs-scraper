# IconID (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/IconID.html

**Package:** Packagenet.runelite.api

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + [java.lang.Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[IconID](IconID.html "enum in net.runelite.api")>
+ - net.runelite.api.IconID

* All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/Serializable.html?is-external=true "class or interface in java.io")`, `[Comparable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Comparable.html?is-external=true "class or interface in java.lang")<[IconID](IconID.html "enum in net.runelite.api")>`

---

```
public enum IconID
extends [Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[IconID](IconID.html "enum in net.runelite.api")>
```

Enum of all official icons that Jagex uses in chat.

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[BOUNTY\_HUNTER\_EMBLEM](#BOUNTY_HUNTER_EMBLEM)` | |
| `[CHAIN\_LINK](#CHAIN_LINK)` | |
| `[DMM\_SKULL\_1\_KEYS](#DMM_SKULL_1_KEYS)` | |
| `[DMM\_SKULL\_2\_KEYS](#DMM_SKULL_2_KEYS)` | |
| `[DMM\_SKULL\_3\_KEYS](#DMM_SKULL_3_KEYS)` | |
| `[DMM\_SKULL\_4\_KEYS](#DMM_SKULL_4_KEYS)` | |
| `[DMM\_SKULL\_5\_KEYS](#DMM_SKULL_5_KEYS)` | |
| `[HARDCORE\_IRONMAN](#HARDCORE_IRONMAN)` | |
| `[IRONMAN](#IRONMAN)` | |
| `[JAGEX\_MODERATOR](#JAGEX_MODERATOR)` | |
| `[LEAGUE](#LEAGUE)` | |
| `[NO\_ENTRY](#NO_ENTRY)` | |
| `[PLAYER\_MODERATOR](#PLAYER_MODERATOR)` | |
| `[SKULL](#SKULL)` | |
| `[ULTIMATE\_IRONMAN](#ULTIMATE_IRONMAN)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `int` | `[getIndex](#getIndex())()` | |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[toString](#toString())()` | |
| `static [IconID](IconID.html "enum in net.runelite.api")` | `[valueOf](#valueOf(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)` | Returns the enum constant of this type with the specified name. |
| `static [IconID](IconID.html "enum in net.runelite.api")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#clone() "class or interface in java.lang"), [compareTo](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#compareTo(E) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#finalize() "class or interface in java.lang"), [getDeclaringClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#getDeclaringClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#hashCode() "class or interface in java.lang"), [name](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#name() "class or interface in java.lang"), [ordinal](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#ordinal() "class or interface in java.lang"), [valueOf](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#valueOf(java.lang.Class,java.lang.String) "class or interface in java.lang")`
- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Enum Constant Detail

- #### PLAYER\_MODERATOR

```
public static final [IconID](IconID.html "enum in net.runelite.api") PLAYER_MODERATOR
```
- #### JAGEX\_MODERATOR

```
public static final [IconID](IconID.html "enum in net.runelite.api") JAGEX_MODERATOR
```
- #### IRONMAN

```
public static final [IconID](IconID.html "enum in net.runelite.api") IRONMAN
```
- #### ULTIMATE\_IRONMAN

```
public static final [IconID](IconID.html "enum in net.runelite.api") ULTIMATE_IRONMAN
```
- #### DMM\_SKULL\_5\_KEYS

```
public static final [IconID](IconID.html "enum in net.runelite.api") DMM_SKULL_5_KEYS
```
- #### DMM\_SKULL\_4\_KEYS

```
public static final [IconID](IconID.html "enum in net.runelite.api") DMM_SKULL_4_KEYS
```
- #### DMM\_SKULL\_3\_KEYS

```
public static final [IconID](IconID.html "enum in net.runelite.api") DMM_SKULL_3_KEYS
```
- #### DMM\_SKULL\_2\_KEYS

```
public static final [IconID](IconID.html "enum in net.runelite.api") DMM_SKULL_2_KEYS
```
- #### DMM\_SKULL\_1\_KEYS

```
public static final [IconID](IconID.html "enum in net.runelite.api") DMM_SKULL_1_KEYS
```
- #### SKULL

```
public static final [IconID](IconID.html "enum in net.runelite.api") SKULL
```
- #### HARDCORE\_IRONMAN

```
public static final [IconID](IconID.html "enum in net.runelite.api") HARDCORE_IRONMAN
```
- #### NO\_ENTRY

```
public static final [IconID](IconID.html "enum in net.runelite.api") NO_ENTRY
```
- #### CHAIN\_LINK

```
public static final [IconID](IconID.html "enum in net.runelite.api") CHAIN_LINK
```
- #### BOUNTY\_HUNTER\_EMBLEM

```
public static final [IconID](IconID.html "enum in net.runelite.api") BOUNTY_HUNTER_EMBLEM
```
- #### LEAGUE

```
public static final [IconID](IconID.html "enum in net.runelite.api") LEAGUE
```

+ ### Method Detail

- #### values

```
public static [IconID](IconID.html "enum in net.runelite.api")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (IconID c : IconID.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [IconID](IconID.html "enum in net.runelite.api") valueOf​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)
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
- #### toString

```
public [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") toString()
```

Overrides:
`[toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#toString() "class or interface in java.lang")` in class `[Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[IconID](IconID.html "enum in net.runelite.api")>`
- #### getIndex

```
public int getIndex()
```