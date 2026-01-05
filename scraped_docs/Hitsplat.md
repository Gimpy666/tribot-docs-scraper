# Hitsplat (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/Hitsplat.html

**Package:** Packagenet.runelite.api

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + net.runelite.api.Hitsplat

* ---

```
public class Hitsplat
extends [Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
```

A hitsplat that has been applied to an [`Actor`](Actor.html "interface in net.runelite.api").

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[Hitsplat](#%3Cinit%3E(int,int,int))​(int hitsplatType,
int amount,
int disappearsOnGameCycle)` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `int` | `[getAmount](#getAmount())()` | The value displayed by the hitsplat. |
| `int` | `[getDisappearsOnGameCycle](#getDisappearsOnGameCycle())()` | When the hitsplat will disappear. |
| `int` | `[getHitsplatType](#getHitsplatType())()` | The type of hitsplat. |
| `boolean` | `[isMine](#isMine())()` | |
| `boolean` | `[isOthers](#isOthers())()` | |

- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#clone() "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#finalize() "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#hashCode() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#toString() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Constructor Detail

- #### Hitsplat

```
public Hitsplat​([@HitsplatType](annotations/HitsplatType.html "annotation in net.runelite.api.annotations")
int hitsplatType,
int amount,
int disappearsOnGameCycle)
```

+ ### Method Detail

- #### isMine

```
public boolean isMine()
```
- #### isOthers

```
public boolean isOthers()
```
- #### getHitsplatType

```
[@HitsplatType](annotations/HitsplatType.html "annotation in net.runelite.api.annotations")
public int getHitsplatType()
```

The type of hitsplat.
- #### getAmount

```
public int getAmount()
```

The value displayed by the hitsplat.
- #### getDisappearsOnGameCycle

```
public int getDisappearsOnGameCycle()
```

When the hitsplat will disappear.