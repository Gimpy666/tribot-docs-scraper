# LocalWalking.Map.MapBuilder (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/walking/LocalWalking.Map.MapBuilder.html

**Package:** Packageorg.tribot.script.sdk.walking

---

* java.lang.Object
* + org.tribot.script.sdk.walking.LocalWalking.Map.MapBuilder

* Enclosing class:
[LocalWalking.Map](LocalWalking.Map.html "class in org.tribot.script.sdk.walking")

---

```
public static class LocalWalking.Map.MapBuilder
extends java.lang.Object
```

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `[LocalWalking.Map.MapBuilder](LocalWalking.Map.MapBuilder.html "class in org.tribot.script.sdk.walking")` | `[bidirectionalLink](#bidirectionalLink(org.tribot.script.sdk.interfaces.Positionable,org.tribot.script.sdk.interfaces.Positionable))​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") start,
[Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") end)` | |
| `[LocalWalking.Map](LocalWalking.Map.html "class in org.tribot.script.sdk.walking")` | `[build](#build())()` | |
| `[LocalWalking.Map.MapBuilder](LocalWalking.Map.MapBuilder.html "class in org.tribot.script.sdk.walking")` | `[clearIgnoreTiles](#clearIgnoreTiles())()` | |
| `[LocalWalking.Map.MapBuilder](LocalWalking.Map.MapBuilder.html "class in org.tribot.script.sdk.walking")` | `[ignoreTile](#ignoreTile(org.tribot.script.sdk.types.LocalTile))​([LocalTile](../types/LocalTile.html "class in org.tribot.script.sdk.types") ignoreTile)` | |
| `[LocalWalking.Map.MapBuilder](LocalWalking.Map.MapBuilder.html "class in org.tribot.script.sdk.walking")` | `[ignoreTiles](#ignoreTiles(java.util.Collection))​(java.util.Collection<? extends [LocalTile](../types/LocalTile.html "class in org.tribot.script.sdk.types")> ignoreTiles)` | |
| `[LocalWalking.Map.MapBuilder](LocalWalking.Map.MapBuilder.html "class in org.tribot.script.sdk.walking")` | `[link](#link(org.tribot.script.sdk.interfaces.Positionable,org.tribot.script.sdk.interfaces.Positionable))​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") start,
[Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") destination)` | |
| `[LocalWalking.Map.MapBuilder](LocalWalking.Map.MapBuilder.html "class in org.tribot.script.sdk.walking")` | `[links](#links(org.tribot.script.sdk.interfaces.Positionable,java.util.Collection))​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") start,
java.util.Collection<[Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces")> end)` | |
| `[LocalWalking.Map.MapBuilder](LocalWalking.Map.MapBuilder.html "class in org.tribot.script.sdk.walking")` | `[source](#source(org.tribot.script.sdk.interfaces.Positionable))​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") source)` | |
| `java.lang.String` | `[toString](#toString())()` | |
| `[LocalWalking.Map.MapBuilder](LocalWalking.Map.MapBuilder.html "class in org.tribot.script.sdk.walking")` | `[travelThroughDoors](#travelThroughDoors(boolean))​(boolean travelThroughDoors)` | |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

* + ### Method Detail

- #### bidirectionalLink

```
public [LocalWalking.Map.MapBuilder](LocalWalking.Map.MapBuilder.html "class in org.tribot.script.sdk.walking") bidirectionalLink​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") start,
[Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") end)
```
- #### link

```
public [LocalWalking.Map.MapBuilder](LocalWalking.Map.MapBuilder.html "class in org.tribot.script.sdk.walking") link​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") start,
[Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") destination)
```
- #### links

```
public [LocalWalking.Map.MapBuilder](LocalWalking.Map.MapBuilder.html "class in org.tribot.script.sdk.walking") links​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") start,
java.util.Collection<[Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces")> end)
```
- #### source

```
public [LocalWalking.Map.MapBuilder](LocalWalking.Map.MapBuilder.html "class in org.tribot.script.sdk.walking") source​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") source)
```
- #### ignoreTile

```
public [LocalWalking.Map.MapBuilder](LocalWalking.Map.MapBuilder.html "class in org.tribot.script.sdk.walking") ignoreTile​([LocalTile](../types/LocalTile.html "class in org.tribot.script.sdk.types") ignoreTile)
```
- #### ignoreTiles

```
public [LocalWalking.Map.MapBuilder](LocalWalking.Map.MapBuilder.html "class in org.tribot.script.sdk.walking") ignoreTiles​(java.util.Collection<? extends [LocalTile](../types/LocalTile.html "class in org.tribot.script.sdk.types")> ignoreTiles)
```
- #### clearIgnoreTiles

```
public [LocalWalking.Map.MapBuilder](LocalWalking.Map.MapBuilder.html "class in org.tribot.script.sdk.walking") clearIgnoreTiles()
```
- #### travelThroughDoors

```
public [LocalWalking.Map.MapBuilder](LocalWalking.Map.MapBuilder.html "class in org.tribot.script.sdk.walking") travelThroughDoors​(boolean travelThroughDoors)
```
- #### build

```
public [LocalWalking.Map](LocalWalking.Map.html "class in org.tribot.script.sdk.walking") build()
```
- #### toString

```
public java.lang.String toString()
```

Overrides:
`toString` in class `java.lang.Object`