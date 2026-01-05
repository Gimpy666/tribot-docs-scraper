# ParamHolder (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/ParamHolder.html

**Package:** Packagenet.runelite.api

---

* All Known Subinterfaces:
`[ItemComposition](ItemComposition.html "interface in net.runelite.api")`, `[NPCComposition](NPCComposition.html "interface in net.runelite.api")`, `[ObjectComposition](ObjectComposition.html "interface in net.runelite.api")`, `[StructComposition](StructComposition.html "interface in net.runelite.api")`

---

```
public interface ParamHolder
```

A composition that can hold `param` keys. This lets Jagex attach arbitrary constant
data to certain items, objects, npcs, or structs for use in cs2

See Also:
[`ParamID`](ParamID.html "class in net.runelite.api")

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `int` | `[getIntValue](#getIntValue(int))​(int paramID)` | Gets the value of a given [`ParamID`](ParamID.html "class in net.runelite.api"), or its default if it is unset |
| `[IterableHashTable](IterableHashTable.html "interface in net.runelite.api")<[Node](Node.html "interface in net.runelite.api")>` | `[getParams](#getParams())()` | |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getStringValue](#getStringValue(int))​(int paramID)` | Gets the value of a given [`ParamID`](ParamID.html "class in net.runelite.api"), or its default if it is unset |
| `void` | `[setParams](#setParams(net.runelite.api.IterableHashTable))​([IterableHashTable](IterableHashTable.html "interface in net.runelite.api")<[Node](Node.html "interface in net.runelite.api")> params)` | |
| `void` | `[setValue](#setValue(int,int))​(int paramID,
int value)` | Sets the value of a given [`ParamID`](ParamID.html "class in net.runelite.api") |
| `void` | `[setValue](#setValue(int,java.lang.String))​(int paramID,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") value)` | Sets the value of a given [`ParamID`](ParamID.html "class in net.runelite.api") |

* + ### Method Detail

- #### getParams

```
[IterableHashTable](IterableHashTable.html "interface in net.runelite.api")<[Node](Node.html "interface in net.runelite.api")> getParams()
```
- #### setParams

```
void setParams​([IterableHashTable](IterableHashTable.html "interface in net.runelite.api")<[Node](Node.html "interface in net.runelite.api")> params)
```
- #### getIntValue

```
int getIntValue​(int paramID)
```

Gets the value of a given [`ParamID`](ParamID.html "class in net.runelite.api"), or its default if it is unset
- #### setValue

```
void setValue​(int paramID,
int value)
```

Sets the value of a given [`ParamID`](ParamID.html "class in net.runelite.api")
- #### getStringValue

```
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getStringValue​(int paramID)
```

Gets the value of a given [`ParamID`](ParamID.html "class in net.runelite.api"), or its default if it is unset
- #### setValue

```
void setValue​(int paramID,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") value)
```

Sets the value of a given [`ParamID`](ParamID.html "class in net.runelite.api")