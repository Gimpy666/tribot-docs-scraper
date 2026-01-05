# DecorativeObjectSpawned (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/events/DecorativeObjectSpawned.html

**Package:** Packagenet.runelite.api.events

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + net.runelite.api.events.DecorativeObjectSpawned

* ---

```
public class DecorativeObjectSpawned
extends [Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
```

An event where a [`DecorativeObject`](../DecorativeObject.html "interface in net.runelite.api") is attached to a [`Tile`](../Tile.html "interface in net.runelite.api").

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[DecorativeObjectSpawned](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `protected boolean` | `[canEqual](#canEqual(java.lang.Object))​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang") other)` | |
| `boolean` | `[equals](#equals(java.lang.Object))​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang") o)` | |
| `[DecorativeObject](../DecorativeObject.html "interface in net.runelite.api")` | `[getDecorativeObject](#getDecorativeObject())()` | The newly spawned decorative object. |
| `[Tile](../Tile.html "interface in net.runelite.api")` | `[getTile](#getTile())()` | The affected tile. |
| `int` | `[hashCode](#hashCode())()` | |
| `void` | `[setDecorativeObject](#setDecorativeObject(net.runelite.api.DecorativeObject))​([DecorativeObject](../DecorativeObject.html "interface in net.runelite.api") decorativeObject)` | The newly spawned decorative object. |
| `void` | `[setTile](#setTile(net.runelite.api.Tile))​([Tile](../Tile.html "interface in net.runelite.api") tile)` | The affected tile. |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[toString](#toString())()` | |

- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#clone() "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#finalize() "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Constructor Detail

- #### DecorativeObjectSpawned

```
public DecorativeObjectSpawned()
```

+ ### Method Detail

- #### getTile

```
public [Tile](../Tile.html "interface in net.runelite.api") getTile()
```

The affected tile.
- #### getDecorativeObject

```
public [DecorativeObject](../DecorativeObject.html "interface in net.runelite.api") getDecorativeObject()
```

The newly spawned decorative object.
- #### setTile

```
public void setTile​([Tile](../Tile.html "interface in net.runelite.api") tile)
```

The affected tile.
- #### setDecorativeObject

```
public void setDecorativeObject​([DecorativeObject](../DecorativeObject.html "interface in net.runelite.api") decorativeObject)
```

The newly spawned decorative object.
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