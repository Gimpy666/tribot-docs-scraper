# Hitsplat (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/types/Hitsplat.html

**Package:** Packageorg.tribot.script.sdk.types

---

* java.lang.Object
* + org.tribot.script.sdk.types.Hitsplat

* All Implemented Interfaces:
`[Indexable](../interfaces/Indexable.html "interface in org.tribot.script.sdk.interfaces")`

---

```
public class Hitsplat
extends java.lang.Object
implements [Indexable](../interfaces/Indexable.html "interface in org.tribot.script.sdk.interfaces")
```

A hitsplat visible on a [`Character`](../interfaces/Character.html "interface in org.tribot.script.sdk.interfaces")

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[Hitsplat.Type](Hitsplat.Type.html "enum in org.tribot.script.sdk.types")` | An enumeration of hitsplat types. |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `boolean` | `[equals](#equals(java.lang.Object))​(java.lang.Object o)` | |
| `int` | `[getIndex](#getIndex())()` | Gets the index of the entity. |
| `[Hitsplat.Type](Hitsplat.Type.html "enum in org.tribot.script.sdk.types")` | `[getType](#getType())()` | Gets the type of hitsplat |
| `int` | `[getValue](#getValue())()` | The hitsplat value (the amount of damage) |
| `int` | `[hashCode](#hashCode())()` | |
| `boolean` | `[isMine](#isMine())()` | Checks if this hitsplat is from my player |
| `boolean` | `[isOthers](#isOthers())()` | Checks if this hitsplat is not from my player |
| `java.lang.String` | `[toString](#toString())()` | |

- ### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

* + ### Method Detail

- #### getIndex

```
public int getIndex()
```

Description copied from interface: `[Indexable](../interfaces/Indexable.html#getIndex())`
Gets the index of the entity.

Specified by:
`[getIndex](../interfaces/Indexable.html#getIndex())` in interface `[Indexable](../interfaces/Indexable.html "interface in org.tribot.script.sdk.interfaces")`
- #### getValue

```
public int getValue()
```

The hitsplat value (the amount of damage)

Returns:
the hitsplat value
- #### getType

```
public [Hitsplat.Type](Hitsplat.Type.html "enum in org.tribot.script.sdk.types") getType()
```

Gets the type of hitsplat

Returns:
the type of hitsplat
- #### isMine

```
public boolean isMine()
```

Checks if this hitsplat is from my player

Returns:
true if this is from my player, false otherwise
- #### isOthers

```
public boolean isOthers()
```

Checks if this hitsplat is not from my player

Returns:
true if this is from my player, false otherwise
- #### equals

```
public boolean equals​(java.lang.Object o)
```

Overrides:
`equals` in class `java.lang.Object`
- #### hashCode

```
public int hashCode()
```

Overrides:
`hashCode` in class `java.lang.Object`
- #### toString

```
public java.lang.String toString()
```

Overrides:
`toString` in class `java.lang.Object`