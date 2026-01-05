# VarbitChanged (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/events/VarbitChanged.html

**Package:** Packagenet.runelite.api.events

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + net.runelite.api.events.VarbitChanged

* ---

```
public class VarbitChanged
extends [Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
```

An event when a varbit or varplayer has changed.

If the client preemptively changes a varp and the server agrees
the next tick, VarbitChanged will only be posted when the client
changes the value, not the server. This can cause unintended effects
if the VarPlayer has special engine behavior assigned to it.

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[VarbitChanged](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);) | Modifier and Type | Method | Description |
| `protected boolean` | `[canEqual](#canEqual(java.lang.Object))​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang") other)` | |
| `boolean` | `[equals](#equals(java.lang.Object))​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang") o)` | |
| `int` | `[getIndex](#getIndex())()` | Deprecated. |
| `int` | `[getValue](#getValue())()` | The new value of the varp or varbit |
| `int` | `[getVarbitId](#getVarbitId())()` | The id of the varbit that was changed. |
| `int` | `[getVarpId](#getVarpId())()` | The id of the varp that was changed. |
| `int` | `[hashCode](#hashCode())()` | |
| `void` | `[setValue](#setValue(int))​(int value)` | The new value of the varp or varbit |
| `void` | `[setVarbitId](#setVarbitId(int))​(int varbitId)` | The id of the varbit that was changed. |
| `void` | `[setVarpId](#setVarpId(int))​(int varpId)` | The id of the varp that was changed. |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[toString](#toString())()` | |

- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#clone() "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#finalize() "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Constructor Detail

- #### VarbitChanged

```
public VarbitChanged()
```

+ ### Method Detail

- #### getIndex

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public int getIndex()
```

Deprecated.
- #### getVarpId

```
public int getVarpId()
```

The id of the varp that was changed.
For a varplayer, this is the varplayer id.
- #### getVarbitId

```
public int getVarbitId()
```

The id of the varbit that was changed.
For a varplayer, this is -1.
- #### getValue

```
public int getValue()
```

The new value of the varp or varbit
- #### setVarpId

```
public void setVarpId​(int varpId)
```

The id of the varp that was changed.
For a varplayer, this is the varplayer id.
- #### setVarbitId

```
public void setVarbitId​(int varbitId)
```

The id of the varbit that was changed.
For a varplayer, this is -1.
- #### setValue

```
public void setValue​(int value)
```

The new value of the varp or varbit
- #### equals

```
public boolean equals​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang") o)
```

Overrides:
`[equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang")` in class `[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")`
- #### canEqual

```
protected boolean canEqual​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang") other)
```
- #### hashCode

```
public int hashCode()
```

Overrides:
`[hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#hashCode() "class or interface in java.lang")` in class `[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")`
- #### toString

```
public [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") toString()
```

Overrides:
`[toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#toString() "class or interface in java.lang")` in class `[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")`