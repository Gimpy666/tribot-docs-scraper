# MyPlayer.AccountType (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/MyPlayer.AccountType.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + java.lang.Enum<[MyPlayer.AccountType](MyPlayer.AccountType.html "enum in org.tribot.script.sdk")>
+ - org.tribot.script.sdk.MyPlayer.AccountType

* All Implemented Interfaces:
`java.io.Serializable`, `java.lang.Comparable<[MyPlayer.AccountType](MyPlayer.AccountType.html "enum in org.tribot.script.sdk")>`

Enclosing class:
[MyPlayer](MyPlayer.html "class in org.tribot.script.sdk")

---

```
public static enum MyPlayer.AccountType
extends java.lang.Enum<[MyPlayer.AccountType](MyPlayer.AccountType.html "enum in org.tribot.script.sdk")>
```

An account type

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[GROUP\_IRONMAN](#GROUP_IRONMAN)` | |
| `[HARDCORE\_GROUP\_IRONMAN](#HARDCORE_GROUP_IRONMAN)` | |
| `[HARDCORE\_IRONMAN](#HARDCORE_IRONMAN)` | |
| `[IRONMAN](#IRONMAN)` | |
| `[NORMAL](#NORMAL)` | |
| `[ULTIMATE\_IRONMAN](#ULTIMATE_IRONMAN)` | |
| `[UNRANKED\_GROUP\_IRONMAN](#UNRANKED_GROUP_IRONMAN)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `boolean` | `[isGroupIronman](#isGroupIronman())()` | Checks if this account type is any group ironman type |
| `boolean` | `[isIronman](#isIronman())()` | Checks if this account is any ironman type (includes group ironman) |
| `static [MyPlayer.AccountType](MyPlayer.AccountType.html "enum in org.tribot.script.sdk")` | `[valueOf](#valueOf(java.lang.String))​(java.lang.String name)` | Returns the enum constant of this type with the specified name. |
| `static [MyPlayer.AccountType](MyPlayer.AccountType.html "enum in org.tribot.script.sdk")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
- ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

- #### NORMAL

```
public static final [MyPlayer.AccountType](MyPlayer.AccountType.html "enum in org.tribot.script.sdk") NORMAL
```
- #### IRONMAN

```
public static final [MyPlayer.AccountType](MyPlayer.AccountType.html "enum in org.tribot.script.sdk") IRONMAN
```
- #### ULTIMATE\_IRONMAN

```
public static final [MyPlayer.AccountType](MyPlayer.AccountType.html "enum in org.tribot.script.sdk") ULTIMATE_IRONMAN
```
- #### HARDCORE\_IRONMAN

```
public static final [MyPlayer.AccountType](MyPlayer.AccountType.html "enum in org.tribot.script.sdk") HARDCORE_IRONMAN
```
- #### GROUP\_IRONMAN

```
public static final [MyPlayer.AccountType](MyPlayer.AccountType.html "enum in org.tribot.script.sdk") GROUP_IRONMAN
```
- #### UNRANKED\_GROUP\_IRONMAN

```
public static final [MyPlayer.AccountType](MyPlayer.AccountType.html "enum in org.tribot.script.sdk") UNRANKED_GROUP_IRONMAN
```
- #### HARDCORE\_GROUP\_IRONMAN

```
public static final [MyPlayer.AccountType](MyPlayer.AccountType.html "enum in org.tribot.script.sdk") HARDCORE_GROUP_IRONMAN
```

+ ### Method Detail

- #### values

```
public static [MyPlayer.AccountType](MyPlayer.AccountType.html "enum in org.tribot.script.sdk")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (MyPlayer.AccountType c : MyPlayer.AccountType.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [MyPlayer.AccountType](MyPlayer.AccountType.html "enum in org.tribot.script.sdk") valueOf​(java.lang.String name)
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
- #### isIronman

```
public boolean isIronman()
```

Checks if this account is any ironman type (includes group ironman)

Returns:
true if this account type is an ironman, false otherwise
- #### isGroupIronman

```
public boolean isGroupIronman()
```

Checks if this account type is any group ironman type

Returns:
true if this is a group ironman type, false otherwise