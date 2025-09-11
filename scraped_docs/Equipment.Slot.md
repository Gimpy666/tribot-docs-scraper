# Equipment.Slot (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/Equipment.Slot.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + java.lang.Enum<[Equipment.Slot](Equipment.Slot.html "enum in org.tribot.script.sdk")>
+ - org.tribot.script.sdk.Equipment.Slot

* All Implemented Interfaces:
`java.io.Serializable`, `java.lang.Comparable<[Equipment.Slot](Equipment.Slot.html "enum in org.tribot.script.sdk")>`

Enclosing class:
[Equipment](Equipment.html "class in org.tribot.script.sdk")

---

```
public static enum Equipment.Slot
extends java.lang.Enum<[Equipment.Slot](Equipment.Slot.html "enum in org.tribot.script.sdk")>
```

Represents an equipment slot in the equipment tab

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[AMMO](#AMMO)` | |
| `[BODY](#BODY)` | |
| `[CAPE](#CAPE)` | |
| `[FEET](#FEET)` | |
| `[HANDS](#HANDS)` | |
| `[HEAD](#HEAD)` | |
| `[LEGS](#LEGS)` | |
| `[NECK](#NECK)` | |
| `[RING](#RING)` | |
| `[SHIELD](#SHIELD)` | |
| `[WEAPON](#WEAPON)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `java.util.Optional<[EquipmentItem](types/EquipmentItem.html "class in org.tribot.script.sdk.types")>` | `[getItem](#getItem())()` | Gets the Item in the slot |
| `int` | `[getSlotIndex](#getSlotIndex())()` | |
| `static [Equipment.Slot](Equipment.Slot.html "enum in org.tribot.script.sdk")` | `[valueOf](#valueOf(java.lang.String))​(java.lang.String name)` | Returns the enum constant of this type with the specified name. |
| `static [Equipment.Slot](Equipment.Slot.html "enum in org.tribot.script.sdk")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
- ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

- #### HEAD

```
public static final [Equipment.Slot](Equipment.Slot.html "enum in org.tribot.script.sdk") HEAD
```
- #### CAPE

```
public static final [Equipment.Slot](Equipment.Slot.html "enum in org.tribot.script.sdk") CAPE
```
- #### NECK

```
public static final [Equipment.Slot](Equipment.Slot.html "enum in org.tribot.script.sdk") NECK
```
- #### WEAPON

```
public static final [Equipment.Slot](Equipment.Slot.html "enum in org.tribot.script.sdk") WEAPON
```
- #### BODY

```
public static final [Equipment.Slot](Equipment.Slot.html "enum in org.tribot.script.sdk") BODY
```
- #### SHIELD

```
public static final [Equipment.Slot](Equipment.Slot.html "enum in org.tribot.script.sdk") SHIELD
```
- #### LEGS

```
public static final [Equipment.Slot](Equipment.Slot.html "enum in org.tribot.script.sdk") LEGS
```
- #### HANDS

```
public static final [Equipment.Slot](Equipment.Slot.html "enum in org.tribot.script.sdk") HANDS
```
- #### FEET

```
public static final [Equipment.Slot](Equipment.Slot.html "enum in org.tribot.script.sdk") FEET
```
- #### RING

```
public static final [Equipment.Slot](Equipment.Slot.html "enum in org.tribot.script.sdk") RING
```
- #### AMMO

```
public static final [Equipment.Slot](Equipment.Slot.html "enum in org.tribot.script.sdk") AMMO
```

+ ### Method Detail

- #### values

```
public static [Equipment.Slot](Equipment.Slot.html "enum in org.tribot.script.sdk")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (Equipment.Slot c : Equipment.Slot.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [Equipment.Slot](Equipment.Slot.html "enum in org.tribot.script.sdk") valueOf​(java.lang.String name)
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
- #### getSlotIndex

```
public int getSlotIndex()
```
- #### getItem

```
public java.util.Optional<[EquipmentItem](types/EquipmentItem.html "class in org.tribot.script.sdk.types")> getItem()
```

Gets the Item in the slot