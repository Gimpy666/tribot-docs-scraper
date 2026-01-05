# StructComposition (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/StructComposition.html

**Package:** Packagenet.runelite.api

---

* All Superinterfaces:
`[ParamHolder](ParamHolder.html "interface in net.runelite.api")`

---

```
public interface StructComposition
extends [ParamHolder](ParamHolder.html "interface in net.runelite.api")
```

A config type dedicated to holding params.

Historically items were often used for this before structs were made
available, and there are many of these still around.

See Also:
[`ParamHolder`](ParamHolder.html "interface in net.runelite.api")

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `int` | `[getId](#getId())()` | |

- ### Methods inherited from interface net.runelite.api.[ParamHolder](ParamHolder.html "interface in net.runelite.api")

`[getIntValue](ParamHolder.html#getIntValue(int)), [getParams](ParamHolder.html#getParams()), [getStringValue](ParamHolder.html#getStringValue(int)), [setParams](ParamHolder.html#setParams(net.runelite.api.IterableHashTable)), [setValue](ParamHolder.html#setValue(int,int)), [setValue](ParamHolder.html#setValue(int,java.lang.String))`

* + ### Method Detail

- #### getId

```
int getId()
```