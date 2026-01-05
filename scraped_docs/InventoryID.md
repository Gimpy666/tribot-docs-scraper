# InventoryID (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/InventoryID.html

**Package:** Packagenet.runelite.api

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + [java.lang.Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[InventoryID](InventoryID.html "enum in net.runelite.api")>
+ - net.runelite.api.InventoryID

* All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/Serializable.html?is-external=true "class or interface in java.io")`, `[Comparable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Comparable.html?is-external=true "class or interface in java.lang")<[InventoryID](InventoryID.html "enum in net.runelite.api")>`

---

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public enum InventoryID
extends [Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[InventoryID](InventoryID.html "enum in net.runelite.api")>
```

Deprecated.
An enumeration of possible inventory types.

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[BANK](#BANK)` | Deprecated.
Bank inventory. |
| `[BARROWS\_REWARD](#BARROWS_REWARD)` | Deprecated.
Barrows reward chest inventory. |
| `[CHAMBERS\_OF\_XERIC\_CHEST](#CHAMBERS_OF_XERIC_CHEST)` | Deprecated.
Chambers of Xeric chest inventory. |
| `[DRIFT\_NET\_FISHING\_REWARD](#DRIFT_NET_FISHING_REWARD)` | Deprecated.
Drift net fishing reward |
| `[EQUIPMENT](#EQUIPMENT)` | Deprecated.
Equipment inventory. |
| `[FISHING\_TRAWLER\_REWARD](#FISHING_TRAWLER_REWARD)` | Deprecated.
Reward from fishing trawler |
| `[FORTIS\_COLOSSEUM\_REWARD\_CHEST](#FORTIS_COLOSSEUM_REWARD_CHEST)` | Deprecated.
Reward chest for the Fortis Colosseum |
| `[GROUP\_STORAGE](#GROUP_STORAGE)` | Deprecated.
Group ironman shared storage |
| `[GROUP\_STORAGE\_INV](#GROUP_STORAGE_INV)` | Deprecated.
Player inventory when accessing group ironman shared storage |
| `[INVENTORY](#INVENTORY)` | Deprecated.
Standard player inventory. |
| `[KINGDOM\_OF\_MISCELLANIA](#KINGDOM_OF_MISCELLANIA)` | Deprecated.
Kingdom Of Miscellania reward inventory. |
| `[LUNAR\_CHEST](#LUNAR_CHEST)` | Deprecated.
Reward chest for Moons of Peril |
| `[MONKEY\_MADNESS\_PUZZLE\_BOX](#MONKEY_MADNESS_PUZZLE_BOX)` | Deprecated.
Monkey madness puzzle box inventory. |
| `[PUZZLE\_BOX](#PUZZLE_BOX)` | Deprecated.
A puzzle box inventory. |
| `[SEED\_VAULT](#SEED_VAULT)` | Deprecated.
Seed vault located inside the Farming Guild |
| `[THEATRE\_OF\_BLOOD\_CHEST](#THEATRE_OF_BLOOD_CHEST)` | Deprecated.
Theater of Blood reward chest inventory (Raids 2) |
| `[TOA\_REWARD\_CHEST](#TOA_REWARD_CHEST)` | Deprecated.
TOA reward chest |
| `[TRADE](#TRADE)` | Deprecated.
The trade inventory. |
| `[TRADEOTHER](#TRADEOTHER)` | Deprecated.
The other trade inventory. |
| `[WILDERNESS\_LOOT\_CHEST](#WILDERNESS_LOOT_CHEST)` | Deprecated.
Wilderness loot chest |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);) | Modifier and Type | Method | Description |
| `int` | `[getId](#getId())()` | Deprecated.
Gets the raw inventory type ID. |
| `static [InventoryID](InventoryID.html "enum in net.runelite.api")` | `[valueOf](#valueOf(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)` | Deprecated.
Returns the enum constant of this type with the specified name. |
| `static [InventoryID](InventoryID.html "enum in net.runelite.api")[]` | `[values](#values())()` | Deprecated.
Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#clone() "class or interface in java.lang"), [compareTo](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#compareTo(E) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#finalize() "class or interface in java.lang"), [getDeclaringClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#getDeclaringClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#hashCode() "class or interface in java.lang"), [name](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#name() "class or interface in java.lang"), [ordinal](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#ordinal() "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#toString() "class or interface in java.lang"), [valueOf](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#valueOf(java.lang.Class,java.lang.String) "class or interface in java.lang")`
- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Enum Constant Detail

- #### FISHING\_TRAWLER\_REWARD

```
public static final [InventoryID](InventoryID.html "enum in net.runelite.api") FISHING_TRAWLER_REWARD
```

Deprecated.
Reward from fishing trawler
- #### TRADE

```
public static final [InventoryID](InventoryID.html "enum in net.runelite.api") TRADE
```

Deprecated.
The trade inventory.
- #### TRADEOTHER

```
public static final [InventoryID](InventoryID.html "enum in net.runelite.api") TRADEOTHER
```

Deprecated.
The other trade inventory.
- #### INVENTORY

```
public static final [InventoryID](InventoryID.html "enum in net.runelite.api") INVENTORY
```

Deprecated.
Standard player inventory.
- #### EQUIPMENT

```
public static final [InventoryID](InventoryID.html "enum in net.runelite.api") EQUIPMENT
```

Deprecated.
Equipment inventory.
- #### BANK

```
public static final [InventoryID](InventoryID.html "enum in net.runelite.api") BANK
```

Deprecated.
Bank inventory.
- #### PUZZLE\_BOX

```
public static final [InventoryID](InventoryID.html "enum in net.runelite.api") PUZZLE_BOX
```

Deprecated.
A puzzle box inventory.
- #### BARROWS\_REWARD

```
public static final [InventoryID](InventoryID.html "enum in net.runelite.api") BARROWS_REWARD
```

Deprecated.
Barrows reward chest inventory.
- #### MONKEY\_MADNESS\_PUZZLE\_BOX

```
public static final [InventoryID](InventoryID.html "enum in net.runelite.api") MONKEY_MADNESS_PUZZLE_BOX
```

Deprecated.
Monkey madness puzzle box inventory.
- #### DRIFT\_NET\_FISHING\_REWARD

```
public static final [InventoryID](InventoryID.html "enum in net.runelite.api") DRIFT_NET_FISHING_REWARD
```

Deprecated.
Drift net fishing reward
- #### KINGDOM\_OF\_MISCELLANIA

```
public static final [InventoryID](InventoryID.html "enum in net.runelite.api") KINGDOM_OF_MISCELLANIA
```

Deprecated.
Kingdom Of Miscellania reward inventory.
- #### CHAMBERS\_OF\_XERIC\_CHEST

```
public static final [InventoryID](InventoryID.html "enum in net.runelite.api") CHAMBERS_OF_XERIC_CHEST
```

Deprecated.
Chambers of Xeric chest inventory.
- #### THEATRE\_OF\_BLOOD\_CHEST

```
public static final [InventoryID](InventoryID.html "enum in net.runelite.api") THEATRE_OF_BLOOD_CHEST
```

Deprecated.
Theater of Blood reward chest inventory (Raids 2)
- #### SEED\_VAULT

```
public static final [InventoryID](InventoryID.html "enum in net.runelite.api") SEED_VAULT
```

Deprecated.
Seed vault located inside the Farming Guild
- #### GROUP\_STORAGE

```
public static final [InventoryID](InventoryID.html "enum in net.runelite.api") GROUP_STORAGE
```

Deprecated.
Group ironman shared storage
- #### GROUP\_STORAGE\_INV

```
public static final [InventoryID](InventoryID.html "enum in net.runelite.api") GROUP_STORAGE_INV
```

Deprecated.
Player inventory when accessing group ironman shared storage
- #### WILDERNESS\_LOOT\_CHEST

```
public static final [InventoryID](InventoryID.html "enum in net.runelite.api") WILDERNESS_LOOT_CHEST
```

Deprecated.
Wilderness loot chest
- #### TOA\_REWARD\_CHEST

```
public static final [InventoryID](InventoryID.html "enum in net.runelite.api") TOA_REWARD_CHEST
```

Deprecated.
TOA reward chest
- #### LUNAR\_CHEST

```
public static final [InventoryID](InventoryID.html "enum in net.runelite.api") LUNAR_CHEST
```

Deprecated.
Reward chest for Moons of Peril
- #### FORTIS\_COLOSSEUM\_REWARD\_CHEST

```
public static final [InventoryID](InventoryID.html "enum in net.runelite.api") FORTIS_COLOSSEUM_REWARD_CHEST
```

Deprecated.
Reward chest for the Fortis Colosseum

+ ### Method Detail

- #### values

```
public static [InventoryID](InventoryID.html "enum in net.runelite.api")[] values()
```

Deprecated.
Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (InventoryID c : InventoryID.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [InventoryID](InventoryID.html "enum in net.runelite.api") valueOf​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)
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
- #### getId

```
public int getId()
```

Deprecated.
Gets the raw inventory type ID.

Returns:
inventory type