# EquipmentInventorySlot (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/EquipmentInventorySlot.html

**Package:** Packagenet.runelite.api

**Description:** These values are intended for use with the local players equipmentItemContainercorresponding. For obtaining information about equipment
 in thePlayerComposition, useKitType....

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + [java.lang.Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[EquipmentInventorySlot](EquipmentInventorySlot.html "enum in net.runelite.api")>
+ - net.runelite.api.EquipmentInventorySlot

* All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/Serializable.html?is-external=true "class or interface in java.io")`, `[Comparable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Comparable.html?is-external=true "class or interface in java.lang")<[EquipmentInventorySlot](EquipmentInventorySlot.html "enum in net.runelite.api")>`

---

```
public enum EquipmentInventorySlot
extends [Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[EquipmentInventorySlot](EquipmentInventorySlot.html "enum in net.runelite.api")>
```

An enumeration of equipment slots in the inventory [`ItemContainer`](ItemContainer.html "interface in net.runelite.api").

These values are intended for use with the local players equipment
[`ItemContainer`](ItemContainer.html "interface in net.runelite.api") corresponding. For obtaining information about equipment
in the [`PlayerComposition`](PlayerComposition.html "interface in net.runelite.api"), use [`KitType`](kit/KitType.html "enum in net.runelite.api.kit").

See Also:
[`Client.getItemContainer(int)`](Client.html#getItemContainer(int)),
`InventoryID.WORN`

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[AMMO](#AMMO)` | |
| `[AMULET](#AMULET)` | |
| `[ARMS](#ARMS)` | |
| `[BODY](#BODY)` | |
| `[BOOTS](#BOOTS)` | |
| `[CAPE](#CAPE)` | |
| `[GLOVES](#GLOVES)` | |
| `[HAIR](#HAIR)` | |
| `[HEAD](#HEAD)` | |
| `[JAW](#JAW)` | |
| `[LEGS](#LEGS)` | |
| `[RING](#RING)` | |
| `[SHIELD](#SHIELD)` | |
| `[WEAPON](#WEAPON)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `int` | `[getSlotIdx](#getSlotIdx())()` | Gets the index into the item array obtained from
[`ItemContainer.getItems()`](ItemContainer.html#getItems()). |
| `static [EquipmentInventorySlot](EquipmentInventorySlot.html "enum in net.runelite.api")` | `[valueOf](#valueOf(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)` | Returns the enum constant of this type with the specified name. |
| `static [EquipmentInventorySlot](EquipmentInventorySlot.html "enum in net.runelite.api")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#clone() "class or interface in java.lang"), [compareTo](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#compareTo(E) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#finalize() "class or interface in java.lang"), [getDeclaringClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#getDeclaringClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#hashCode() "class or interface in java.lang"), [name](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#name() "class or interface in java.lang"), [ordinal](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#ordinal() "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#toString() "class or interface in java.lang"), [valueOf](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#valueOf(java.lang.Class,java.lang.String) "class or interface in java.lang")`
- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Enum Constant Detail

- #### HEAD

```
public static final [EquipmentInventorySlot](EquipmentInventorySlot.html "enum in net.runelite.api") HEAD
```
- #### CAPE

```
public static final [EquipmentInventorySlot](EquipmentInventorySlot.html "enum in net.runelite.api") CAPE
```
- #### AMULET

```
public static final [EquipmentInventorySlot](EquipmentInventorySlot.html "enum in net.runelite.api") AMULET
```
- #### WEAPON

```
public static final [EquipmentInventorySlot](EquipmentInventorySlot.html "enum in net.runelite.api") WEAPON
```
- #### BODY

```
public static final [EquipmentInventorySlot](EquipmentInventorySlot.html "enum in net.runelite.api") BODY
```
- #### SHIELD

```
public static final [EquipmentInventorySlot](EquipmentInventorySlot.html "enum in net.runelite.api") SHIELD
```
- #### ARMS

```
public static final [EquipmentInventorySlot](EquipmentInventorySlot.html "enum in net.runelite.api") ARMS
```
- #### LEGS

```
public static final [EquipmentInventorySlot](EquipmentInventorySlot.html "enum in net.runelite.api") LEGS
```
- #### HAIR

```
public static final [EquipmentInventorySlot](EquipmentInventorySlot.html "enum in net.runelite.api") HAIR
```
- #### GLOVES

```
public static final [EquipmentInventorySlot](EquipmentInventorySlot.html "enum in net.runelite.api") GLOVES
```
- #### BOOTS

```
public static final [EquipmentInventorySlot](EquipmentInventorySlot.html "enum in net.runelite.api") BOOTS
```
- #### JAW

```
public static final [EquipmentInventorySlot](EquipmentInventorySlot.html "enum in net.runelite.api") JAW
```
- #### RING

```
public static final [EquipmentInventorySlot](EquipmentInventorySlot.html "enum in net.runelite.api") RING
```
- #### AMMO

```
public static final [EquipmentInventorySlot](EquipmentInventorySlot.html "enum in net.runelite.api") AMMO
```

+ ### Method Detail

- #### values

```
public static [EquipmentInventorySlot](EquipmentInventorySlot.html "enum in net.runelite.api")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (EquipmentInventorySlot c : EquipmentInventorySlot.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [EquipmentInventorySlot](EquipmentInventorySlot.html "enum in net.runelite.api") valueOf​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)
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
- #### getSlotIdx

```
public int getSlotIdx()
```

Gets the index into the item array obtained from
[`ItemContainer.getItems()`](ItemContainer.html#getItems()).

Returns:
the raw index