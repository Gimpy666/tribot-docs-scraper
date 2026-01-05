# FriendsChatRank (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/FriendsChatRank.html

**Package:** Packagenet.runelite.api

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + [java.lang.Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[FriendsChatRank](FriendsChatRank.html "enum in net.runelite.api")>
+ - net.runelite.api.FriendsChatRank

* All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/Serializable.html?is-external=true "class or interface in java.io")`, `[Comparable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Comparable.html?is-external=true "class or interface in java.lang")<[FriendsChatRank](FriendsChatRank.html "enum in net.runelite.api")>`

---

```
public enum FriendsChatRank
extends [Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[FriendsChatRank](FriendsChatRank.html "enum in net.runelite.api")>
```

An enumeration of ranks of friends chat members.

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[CAPTAIN](#CAPTAIN)` | Captain rank. |
| `[CORPORAL](#CORPORAL)` | Corporal rank. |
| `[FRIEND](#FRIEND)` | Friend rank. |
| `[GENERAL](#GENERAL)` | General rank. |
| `[JMOD](#JMOD)` | JMod rank. |
| `[LIEUTENANT](#LIEUTENANT)` | Lieutenant rank. |
| `[OWNER](#OWNER)` | Channel owner rank. |
| `[RECRUIT](#RECRUIT)` | Recruit rank. |
| `[SERGEANT](#SERGEANT)` | Sergeant rank. |
| `[UNRANKED](#UNRANKED)` | Not ranked. |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `int` | `[getValue](#getValue())()` | The value of the rank. |
| `static [FriendsChatRank](FriendsChatRank.html "enum in net.runelite.api")` | `[valueOf](#valueOf(int))​(int rank)` | Utility method that maps the rank value to its respective
[`FriendsChatRank`](FriendsChatRank.html "enum in net.runelite.api") value. |
| `static [FriendsChatRank](FriendsChatRank.html "enum in net.runelite.api")` | `[valueOf](#valueOf(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)` | Returns the enum constant of this type with the specified name. |
| `static [FriendsChatRank](FriendsChatRank.html "enum in net.runelite.api")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#clone() "class or interface in java.lang"), [compareTo](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#compareTo(E) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#finalize() "class or interface in java.lang"), [getDeclaringClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#getDeclaringClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#hashCode() "class or interface in java.lang"), [name](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#name() "class or interface in java.lang"), [ordinal](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#ordinal() "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#toString() "class or interface in java.lang"), [valueOf](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#valueOf(java.lang.Class,java.lang.String) "class or interface in java.lang")`
- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Enum Constant Detail

- #### UNRANKED

```
public static final [FriendsChatRank](FriendsChatRank.html "enum in net.runelite.api") UNRANKED
```

Not ranked.
- #### FRIEND

```
public static final [FriendsChatRank](FriendsChatRank.html "enum in net.runelite.api") FRIEND
```

Friend rank.
- #### RECRUIT

```
public static final [FriendsChatRank](FriendsChatRank.html "enum in net.runelite.api") RECRUIT
```

Recruit rank.
- #### CORPORAL

```
public static final [FriendsChatRank](FriendsChatRank.html "enum in net.runelite.api") CORPORAL
```

Corporal rank.
- #### SERGEANT

```
public static final [FriendsChatRank](FriendsChatRank.html "enum in net.runelite.api") SERGEANT
```

Sergeant rank.
- #### LIEUTENANT

```
public static final [FriendsChatRank](FriendsChatRank.html "enum in net.runelite.api") LIEUTENANT
```

Lieutenant rank.
- #### CAPTAIN

```
public static final [FriendsChatRank](FriendsChatRank.html "enum in net.runelite.api") CAPTAIN
```

Captain rank.
- #### GENERAL

```
public static final [FriendsChatRank](FriendsChatRank.html "enum in net.runelite.api") GENERAL
```

General rank.
- #### OWNER

```
public static final [FriendsChatRank](FriendsChatRank.html "enum in net.runelite.api") OWNER
```

Channel owner rank.
- #### JMOD

```
public static final [FriendsChatRank](FriendsChatRank.html "enum in net.runelite.api") JMOD
```

JMod rank.

+ ### Method Detail

- #### values

```
public static [FriendsChatRank](FriendsChatRank.html "enum in net.runelite.api")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (FriendsChatRank c : FriendsChatRank.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [FriendsChatRank](FriendsChatRank.html "enum in net.runelite.api") valueOf​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)
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
- #### valueOf

```
public static [FriendsChatRank](FriendsChatRank.html "enum in net.runelite.api") valueOf​(int rank)
```

Utility method that maps the rank value to its respective
[`FriendsChatRank`](FriendsChatRank.html "enum in net.runelite.api") value.

Parameters:
`rank` - the rank value
Returns:
rank type
- #### getValue

```
public int getValue()
```

The value of the rank.