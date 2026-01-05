# GrandExchangeOfferState (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/GrandExchangeOfferState.html

**Package:** Packagenet.runelite.api

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + [java.lang.Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[GrandExchangeOfferState](GrandExchangeOfferState.html "enum in net.runelite.api")>
+ - net.runelite.api.GrandExchangeOfferState

* All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/Serializable.html?is-external=true "class or interface in java.io")`, `[Comparable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Comparable.html?is-external=true "class or interface in java.lang")<[GrandExchangeOfferState](GrandExchangeOfferState.html "enum in net.runelite.api")>`

---

```
public enum GrandExchangeOfferState
extends [Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[GrandExchangeOfferState](GrandExchangeOfferState.html "enum in net.runelite.api")>
```

Describes the state of a Grand Exchange offer.

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[BOUGHT](#BOUGHT)` | A buy offer that has completed. |
| `[BUYING](#BUYING)` | A buy offer that is currently in progress. |
| `[CANCELLED\_BUY](#CANCELLED_BUY)` | A cancelled buy offer. |
| `[CANCELLED\_SELL](#CANCELLED_SELL)` | A cancelled sell offer. |
| `[EMPTY](#EMPTY)` | An empty slot. |
| `[SELLING](#SELLING)` | A sell offer that is currently in progress. |
| `[SOLD](#SOLD)` | A sell offer that has completed. |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [GrandExchangeOfferState](GrandExchangeOfferState.html "enum in net.runelite.api")` | `[valueOf](#valueOf(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)` | Returns the enum constant of this type with the specified name. |
| `static [GrandExchangeOfferState](GrandExchangeOfferState.html "enum in net.runelite.api")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#clone() "class or interface in java.lang"), [compareTo](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#compareTo(E) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#finalize() "class or interface in java.lang"), [getDeclaringClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#getDeclaringClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#hashCode() "class or interface in java.lang"), [name](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#name() "class or interface in java.lang"), [ordinal](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#ordinal() "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#toString() "class or interface in java.lang"), [valueOf](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#valueOf(java.lang.Class,java.lang.String) "class or interface in java.lang")`
- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Enum Constant Detail

- #### EMPTY

```
public static final [GrandExchangeOfferState](GrandExchangeOfferState.html "enum in net.runelite.api") EMPTY
```

An empty slot.
- #### CANCELLED\_BUY

```
public static final [GrandExchangeOfferState](GrandExchangeOfferState.html "enum in net.runelite.api") CANCELLED_BUY
```

A cancelled buy offer.
- #### CANCELLED\_SELL

```
public static final [GrandExchangeOfferState](GrandExchangeOfferState.html "enum in net.runelite.api") CANCELLED_SELL
```

A cancelled sell offer.
- #### BUYING

```
public static final [GrandExchangeOfferState](GrandExchangeOfferState.html "enum in net.runelite.api") BUYING
```

A buy offer that is currently in progress.
- #### BOUGHT

```
public static final [GrandExchangeOfferState](GrandExchangeOfferState.html "enum in net.runelite.api") BOUGHT
```

A buy offer that has completed.
- #### SELLING

```
public static final [GrandExchangeOfferState](GrandExchangeOfferState.html "enum in net.runelite.api") SELLING
```

A sell offer that is currently in progress.
- #### SOLD

```
public static final [GrandExchangeOfferState](GrandExchangeOfferState.html "enum in net.runelite.api") SOLD
```

A sell offer that has completed.

+ ### Method Detail

- #### values

```
public static [GrandExchangeOfferState](GrandExchangeOfferState.html "enum in net.runelite.api")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (GrandExchangeOfferState c : GrandExchangeOfferState.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [GrandExchangeOfferState](GrandExchangeOfferState.html "enum in net.runelite.api") valueOf​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)
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