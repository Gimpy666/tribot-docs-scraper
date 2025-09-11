# ItemDefinition (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/types/definitions/ItemDefinition.html

**Package:** Packageorg.tribot.script.sdk.types.definitions

---

* java.lang.Object
* + org.tribot.script.sdk.types.definitions.ItemDefinition

* All Implemented Interfaces:
`[Identifiable](../../interfaces/Identifiable.html "interface in org.tribot.script.sdk.interfaces")`, `[Named](../../interfaces/Named.html "interface in org.tribot.script.sdk.interfaces")`

---

```
public class ItemDefinition
extends java.lang.Object
implements [Identifiable](../../interfaces/Identifiable.html "interface in org.tribot.script.sdk.interfaces"), [Named](../../interfaces/Named.html "interface in org.tribot.script.sdk.interfaces")
```

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[ItemDefinition](#%3Cinit%3E(org.tribot.api2007.types.RSItemDefinition))​(org.tribot.api2007.types.RSItemDefinition itemDefinition)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);) | Modifier and Type | Method | Description |
| `static java.util.Optional<[ItemDefinition](ItemDefinition.html "class in org.tribot.script.sdk.types.definitions")>` | `[get](#get(int))​(int id)` | |
| `java.util.List<java.lang.String>` | `[getActions](#getActions())()` | Gets the inventory actions for this item |
| `int` | `[getBaseValue](#getBaseValue())()` | |
| `java.util.List<java.lang.String>` | `[getEquipmentActions](#getEquipmentActions())()` | Gets the equipment actions for this item |
| `java.util.List<java.lang.String>` | `[getGroundActions](#getGroundActions())()` | |
| `int` | `[getHighAlchValue](#getHighAlchValue())()` | |
| `int` | `[getId](#getId())()` | Gets the ID of the entity |
| `org.tribot.api2007.types.RSItemDefinition` | `[getLegacyDefinition](#getLegacyDefinition())()` | |
| `java.lang.String` | `[getName](#getName())()` | Determines the name of the entity of the object this method is called on. |
| `int` | `[getNotedItemId](#getNotedItemId())()` | |
| `int` | `[getPlaceholderId](#getPlaceholderId())()` | |
| `int` | `[getUnnotedItemId](#getUnnotedItemId())()` | |
| `boolean` | `[isBankable](#isBankable())()` | Deprecated. |
| `boolean` | `[isGrandExchangeTradeable](#isGrandExchangeTradeable())()` | |
| `boolean` | `[isMembersOnly](#isMembersOnly())()` | |
| `boolean` | `[isNoted](#isNoted())()` | |
| `boolean` | `[isPlaceholder](#isPlaceholder())()` | |
| `boolean` | `[isStackable](#isStackable())()` | |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### ItemDefinition

```
public ItemDefinition​(org.tribot.api2007.types.RSItemDefinition itemDefinition)
```

+ ### Method Detail

- #### getId

```
public int getId()
```

Description copied from interface: `[Identifiable](../../interfaces/Identifiable.html#getId())`
Gets the ID of the entity

Specified by:
`[getId](../../interfaces/Identifiable.html#getId())` in interface `[Identifiable](../../interfaces/Identifiable.html "interface in org.tribot.script.sdk.interfaces")`
- #### getName

```
public java.lang.String getName()
```

Description copied from interface: `[Named](../../interfaces/Named.html#getName())`
Determines the name of the entity of the object this method is called on.
This method cannot return null. Therefore, expect any problems in the determination of the name to force this
method to return a blank string.

Specified by:
`[getName](../../interfaces/Named.html#getName())` in interface `[Named](../../interfaces/Named.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
The name of the entity
- #### isMembersOnly

```
public boolean isMembersOnly()
```
- #### isStackable

```
public boolean isStackable()
```
- #### isNoted

```
public boolean isNoted()
```
- #### isBankable

```
@Deprecated
public boolean isBankable()
```

Deprecated.
- #### getHighAlchValue

```
public int getHighAlchValue()
```
- #### getBaseValue

```
public int getBaseValue()
```
- #### getUnnotedItemId

```
public int getUnnotedItemId()
```
- #### getNotedItemId

```
public int getNotedItemId()
```
- #### isGrandExchangeTradeable

```
public boolean isGrandExchangeTradeable()
```
- #### isPlaceholder

```
public boolean isPlaceholder()
```
- #### getPlaceholderId

```
public int getPlaceholderId()
```
- #### getActions

```
public java.util.List<java.lang.String> getActions()
```

Gets the inventory actions for this item

Returns:
the inventory actions for this item
- #### getEquipmentActions

```
public java.util.List<java.lang.String> getEquipmentActions()
```

Gets the equipment actions for this item

Returns:
the equipment actions for this item
- #### getGroundActions

```
public java.util.List<java.lang.String> getGroundActions()
```
- #### get

```
public static java.util.Optional<[ItemDefinition](ItemDefinition.html "class in org.tribot.script.sdk.types.definitions")> get​(int id)
```
- #### getLegacyDefinition

```
public org.tribot.api2007.types.RSItemDefinition getLegacyDefinition()
```