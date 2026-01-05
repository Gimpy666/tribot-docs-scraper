# AccountType (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/vars/AccountType.html

**Package:** Packagenet.runelite.api.vars

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + [java.lang.Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[AccountType](AccountType.html "enum in net.runelite.api.vars")>
+ - net.runelite.api.vars.AccountType

* All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/Serializable.html?is-external=true "class or interface in java.io")`, `[Comparable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Comparable.html?is-external=true "class or interface in java.lang")<[AccountType](AccountType.html "enum in net.runelite.api.vars")>`

---

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public enum AccountType
extends [Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[AccountType](AccountType.html "enum in net.runelite.api.vars")>
```

Deprecated.
An enumeration of possible account types.

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[GROUP\_IRONMAN](#GROUP_IRONMAN)` | Deprecated.
Group ironman account type |
| `[HARDCORE\_GROUP\_IRONMAN](#HARDCORE_GROUP_IRONMAN)` | Deprecated.
Hardcore group ironman account type |
| `[HARDCORE\_IRONMAN](#HARDCORE_IRONMAN)` | Deprecated.
Hardcore ironman account type. |
| `[IRONMAN](#IRONMAN)` | Deprecated.
Ironman account type. |
| `[NORMAL](#NORMAL)` | Deprecated.
Normal account type. |
| `[ULTIMATE\_IRONMAN](#ULTIMATE_IRONMAN)` | Deprecated.
Ultimate ironman account type. |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);) | Modifier and Type | Method | Description |
| `boolean` | `[isGroupIronman](#isGroupIronman())()` | Deprecated.
Checks whether this type is a group ironman. |
| `boolean` | `[isIronman](#isIronman())()` | Deprecated.
Checks whether this type is a non-group ironman. |
| `static [AccountType](AccountType.html "enum in net.runelite.api.vars")` | `[valueOf](#valueOf(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)` | Deprecated.
Returns the enum constant of this type with the specified name. |
| `static [AccountType](AccountType.html "enum in net.runelite.api.vars")[]` | `[values](#values())()` | Deprecated.
Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#clone() "class or interface in java.lang"), [compareTo](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#compareTo(E) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#finalize() "class or interface in java.lang"), [getDeclaringClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#getDeclaringClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#hashCode() "class or interface in java.lang"), [name](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#name() "class or interface in java.lang"), [ordinal](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#ordinal() "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#toString() "class or interface in java.lang"), [valueOf](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#valueOf(java.lang.Class,java.lang.String) "class or interface in java.lang")`
- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Enum Constant Detail

- #### NORMAL

```
public static final [AccountType](AccountType.html "enum in net.runelite.api.vars") NORMAL
```

Deprecated.
Normal account type.
- #### IRONMAN

```
public static final [AccountType](AccountType.html "enum in net.runelite.api.vars") IRONMAN
```

Deprecated.
Ironman account type.
- #### ULTIMATE\_IRONMAN

```
public static final [AccountType](AccountType.html "enum in net.runelite.api.vars") ULTIMATE_IRONMAN
```

Deprecated.
Ultimate ironman account type.
- #### HARDCORE\_IRONMAN

```
public static final [AccountType](AccountType.html "enum in net.runelite.api.vars") HARDCORE_IRONMAN
```

Deprecated.
Hardcore ironman account type.
- #### GROUP\_IRONMAN

```
public static final [AccountType](AccountType.html "enum in net.runelite.api.vars") GROUP_IRONMAN
```

Deprecated.
Group ironman account type
- #### HARDCORE\_GROUP\_IRONMAN

```
public static final [AccountType](AccountType.html "enum in net.runelite.api.vars") HARDCORE_GROUP_IRONMAN
```

Deprecated.
Hardcore group ironman account type

+ ### Method Detail

- #### values

```
public static [AccountType](AccountType.html "enum in net.runelite.api.vars")[] values()
```

Deprecated.
Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (AccountType c : AccountType.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [AccountType](AccountType.html "enum in net.runelite.api.vars") valueOf​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)
```

Deprecated.
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
- #### isIronman

```
public boolean isIronman()
```

Deprecated.
Checks whether this type is a non-group ironman.

Returns:
`true` if the type is any of the non-group ironman types.
- #### isGroupIronman

```
public boolean isGroupIronman()
```

Deprecated.
Checks whether this type is a group ironman.

Returns:
`true` if the type is either of the group ironman types.