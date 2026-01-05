# ProjectileMoved (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/events/ProjectileMoved.html

**Package:** Packagenet.runelite.api.events

**Description:** For projectiles that target the ground, this event is only triggered
 once (ie. AoE from Lizardman Shaman)....

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + net.runelite.api.events.ProjectileMoved

* ---

```
public class ProjectileMoved
extends [Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
```

An event called whenever a [`Projectile`](../Projectile.html "interface in net.runelite.api") has moved towards a point.

For projectiles that target the ground, this event is only triggered
once (ie. AoE from Lizardman Shaman).

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[ProjectileMoved](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `protected boolean` | `[canEqual](#canEqual(java.lang.Object))​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang") other)` | |
| `boolean` | `[equals](#equals(java.lang.Object))​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang") o)` | |
| `[LocalPoint](../coords/LocalPoint.html "class in net.runelite.api.coords")` | `[getPosition](#getPosition())()` | The target location of the projectile. |
| `[Projectile](../Projectile.html "interface in net.runelite.api")` | `[getProjectile](#getProjectile())()` | The projectile being moved. |
| `int` | `[getZ](#getZ())()` | The z-axis target location of the projectile. |
| `int` | `[hashCode](#hashCode())()` | |
| `void` | `[setPosition](#setPosition(net.runelite.api.coords.LocalPoint))​([LocalPoint](../coords/LocalPoint.html "class in net.runelite.api.coords") position)` | The target location of the projectile. |
| `void` | `[setProjectile](#setProjectile(net.runelite.api.Projectile))​([Projectile](../Projectile.html "interface in net.runelite.api") projectile)` | The projectile being moved. |
| `void` | `[setZ](#setZ(int))​(int z)` | The z-axis target location of the projectile. |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[toString](#toString())()` | |

- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#clone() "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#finalize() "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Constructor Detail

- #### ProjectileMoved

```
public ProjectileMoved()
```

+ ### Method Detail

- #### getProjectile

```
public [Projectile](../Projectile.html "interface in net.runelite.api") getProjectile()
```

The projectile being moved.
- #### getPosition

```
public [LocalPoint](../coords/LocalPoint.html "class in net.runelite.api.coords") getPosition()
```

The target location of the projectile.
- #### getZ

```
public int getZ()
```

The z-axis target location of the projectile.
- #### setProjectile

```
public void setProjectile​([Projectile](../Projectile.html "interface in net.runelite.api") projectile)
```

The projectile being moved.
- #### setPosition

```
public void setPosition​([LocalPoint](../coords/LocalPoint.html "class in net.runelite.api.coords") position)
```

The target location of the projectile.
- #### setZ

```
public void setZ​(int z)
```

The z-axis target location of the projectile.
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