# KitType (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/kit/KitType.html

**Package:** Packagenet.runelite.api.kit

**Description:** These values are intended for use withPlayerCompositionequipment
 slots. For obtaining information about equipment in the local players
 equipmentItemContainer, useEquipmentInventorySlot....

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + [java.lang.Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[KitType](KitType.html "enum in net.runelite.api.kit")>
+ - net.runelite.api.kit.KitType

* All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/Serializable.html?is-external=true "class or interface in java.io")`, `[Comparable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Comparable.html?is-external=true "class or interface in java.lang")<[KitType](KitType.html "enum in net.runelite.api.kit")>`

---

```
public enum KitType
extends [Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[KitType](KitType.html "enum in net.runelite.api.kit")>
```

Represents an equipment slot in a players composition.

These values are intended for use with [`PlayerComposition`](../PlayerComposition.html "interface in net.runelite.api") equipment
slots. For obtaining information about equipment in the local players
equipment [`ItemContainer`](../ItemContainer.html "interface in net.runelite.api"), use
[`EquipmentInventorySlot`](../EquipmentInventorySlot.html "enum in net.runelite.api").

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[AMULET](#AMULET)` | |
| `[ARMS](#ARMS)` | |
| `[BOOTS](#BOOTS)` | |
| `[CAPE](#CAPE)` | |
| `[HAIR](#HAIR)` | |
| `[HANDS](#HANDS)` | |
| `[HEAD](#HEAD)` | |
| `[JAW](#JAW)` | |
| `[LEGS](#LEGS)` | |
| `[SHIELD](#SHIELD)` | |
| `[TORSO](#TORSO)` | |
| `[WEAPON](#WEAPON)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `int` | `[getIndex](#getIndex())()` | Gets the raw equipment index for use in [`PlayerComposition.getEquipmentIds()`](../PlayerComposition.html#getEquipmentIds()). |
| `static [KitType](KitType.html "enum in net.runelite.api.kit")` | `[valueOf](#valueOf(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)` | Returns the enum constant of this type with the specified name. |
| `static [KitType](KitType.html "enum in net.runelite.api.kit")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#clone() "class or interface in java.lang"), [compareTo](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#compareTo(E) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#finalize() "class or interface in java.lang"), [getDeclaringClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#getDeclaringClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#hashCode() "class or interface in java.lang"), [name](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#name() "class or interface in java.lang"), [ordinal](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#ordinal() "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#toString() "class or interface in java.lang"), [valueOf](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#valueOf(java.lang.Class,java.lang.String) "class or interface in java.lang")`
- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Enum Constant Detail

- #### HEAD

```
public static final [KitType](KitType.html "enum in net.runelite.api.kit") HEAD
```
- #### CAPE

```
public static final [KitType](KitType.html "enum in net.runelite.api.kit") CAPE
```
- #### AMULET

```
public static final [KitType](KitType.html "enum in net.runelite.api.kit") AMULET
```
- #### WEAPON

```
public static final [KitType](KitType.html "enum in net.runelite.api.kit") WEAPON
```
- #### TORSO

```
public static final [KitType](KitType.html "enum in net.runelite.api.kit") TORSO
```
- #### SHIELD

```
public static final [KitType](KitType.html "enum in net.runelite.api.kit") SHIELD
```
- #### ARMS

```
public static final [KitType](KitType.html "enum in net.runelite.api.kit") ARMS
```
- #### LEGS

```
public static final [KitType](KitType.html "enum in net.runelite.api.kit") LEGS
```
- #### HAIR

```
public static final [KitType](KitType.html "enum in net.runelite.api.kit") HAIR
```
- #### HANDS

```
public static final [KitType](KitType.html "enum in net.runelite.api.kit") HANDS
```
- #### BOOTS

```
public static final [KitType](KitType.html "enum in net.runelite.api.kit") BOOTS
```
- #### JAW

```
public static final [KitType](KitType.html "enum in net.runelite.api.kit") JAW
```

+ ### Method Detail

- #### values

```
public static [KitType](KitType.html "enum in net.runelite.api.kit")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (KitType c : KitType.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [KitType](KitType.html "enum in net.runelite.api.kit") valueOf​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)
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
- #### getIndex

```
public int getIndex()
```

Gets the raw equipment index for use in [`PlayerComposition.getEquipmentIds()`](../PlayerComposition.html#getEquipmentIds()).

Returns:
raw equipment index