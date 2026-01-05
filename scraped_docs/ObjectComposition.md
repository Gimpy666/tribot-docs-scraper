# ObjectComposition (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/ObjectComposition.html

**Package:** Packagenet.runelite.api

---

* All Superinterfaces:
`[ParamHolder](ParamHolder.html "interface in net.runelite.api")`

---

```
public interface ObjectComposition
extends [ParamHolder](ParamHolder.html "interface in net.runelite.api")
```

Information about a specific `ObjectID`

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")[]` | `[getActions](#getActions())()` | The 5 menuops this object has when in world. |
| `int` | `[getId](#getId())()` | Gets ID for the object. |
| `[ObjectComposition](ObjectComposition.html "interface in net.runelite.api")` | `[getImpostor](#getImpostor())()` | Get the object composition the player's state says this object should
transmogrify into. |
| `int[]` | `[getImpostorIds](#getImpostorIds())()` | Get the `ObjectID`s of objects this can transform into, depending
on a `VarbitID` or `VarPlayerID` |
| `int` | `[getMapIconId](#getMapIconId())()` | Gets the index of this object in the [`Client.getMapIcons()`](Client.html#getMapIcons())
array, or -1 if it has no full map icon |
| `int` | `[getMapSceneId](#getMapSceneId())()` | Gets the index of this object in the [`Client.getMapScene()`](Client.html#getMapScene())
array, or -1 if it has no map scene icon |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getName](#getName())()` | Gets the name of the object. |
| `int` | `[getSizeX](#getSizeX())()` | Get the size of the object on the X-axis in tiles |
| `int` | `[getSizeY](#getSizeY())()` | Get the size of the object on the Y-axis in tiles |
| `int` | `[getVarbitId](#getVarbitId())()` | Gets the `VarbitID` used to switch this multiloc, or `-1` if this is not switched by a Varbit |
| `int` | `[getVarPlayerId](#getVarPlayerId())()` | Gets the `VarPlayerID` used to switch this multiloc, or `-1` if this is not switched by a VarPlayer |
| `void` | `[setMapIconId](#setMapIconId(int))​(int mapIconId)` | Set the index of the object in the [`Client.getMapIcons()`](Client.html#getMapIcons())
array, or -1 if it has no map icon |
| `void` | `[setMapSceneId](#setMapSceneId(int))​(int mapSceneId)` | Set the map scene index into the [`Client.getMapScene()`](Client.html#getMapScene())
array, or -1 if it has no map scene icon |

- ### Methods inherited from interface net.runelite.api.[ParamHolder](ParamHolder.html "interface in net.runelite.api")

`[getIntValue](ParamHolder.html#getIntValue(int)), [getParams](ParamHolder.html#getParams()), [getStringValue](ParamHolder.html#getStringValue(int)), [setParams](ParamHolder.html#setParams(net.runelite.api.IterableHashTable)), [setValue](ParamHolder.html#setValue(int,int)), [setValue](ParamHolder.html#setValue(int,java.lang.String))`

* + ### Method Detail

- #### getId

```
int getId()
```

Gets ID for the object.

See Also:
`ObjectID`
- #### getName

```
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getName()
```

Gets the name of the object.
- #### getActions

```
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")[] getActions()
```

The 5 menuops this object has when in world. Index 0 corresponds to
[`MenuAction.GAME_OBJECT_FIRST_OPTION`](MenuAction.html#GAME_OBJECT_FIRST_OPTION), Index 2 to
[`MenuAction.GAME_OBJECT_SECOND_OPTION`](MenuAction.html#GAME_OBJECT_SECOND_OPTION) and so on.
- #### getMapSceneId

```
int getMapSceneId()
```

Gets the index of this object in the [`Client.getMapScene()`](Client.html#getMapScene())
array, or -1 if it has no map scene icon
- #### setMapSceneId

```
void setMapSceneId​(int mapSceneId)
```

Set the map scene index into the [`Client.getMapScene()`](Client.html#getMapScene())
array, or -1 if it has no map scene icon

Parameters:
`mapSceneId` -
- #### getMapIconId

```
int getMapIconId()
```

Gets the index of this object in the [`Client.getMapIcons()`](Client.html#getMapIcons())
array, or -1 if it has no full map icon
- #### setMapIconId

```
void setMapIconId​(int mapIconId)
```

Set the index of the object in the [`Client.getMapIcons()`](Client.html#getMapIcons())
array, or -1 if it has no map icon

Parameters:
`mapIconId` -
- #### getImpostorIds

```
int[] getImpostorIds()
```

Get the `ObjectID`s of objects this can transform into, depending
on a `VarbitID` or `VarPlayerID`
- #### getImpostor

```
[ObjectComposition](ObjectComposition.html "interface in net.runelite.api") getImpostor()
```

Get the object composition the player's state says this object should
transmogrify into.

Throws:
`[NullPointerException](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/NullPointerException.html?is-external=true "class or interface in java.lang")` - if [`getImpostorIds()`](#getImpostorIds()) is null
- #### getVarbitId

```
[@Varbit](annotations/Varbit.html "annotation in net.runelite.api.annotations")
int getVarbitId()
```

Gets the `VarbitID` used to switch this multiloc, or `-1` if this is not switched by a Varbit

See Also:
[`getImpostor()`](#getImpostor()),
[`getImpostorIds()`](#getImpostorIds())
- #### getVarPlayerId

```
[@Varp](annotations/Varp.html "annotation in net.runelite.api.annotations")
int getVarPlayerId()
```

Gets the `VarPlayerID` used to switch this multiloc, or `-1` if this is not switched by a VarPlayer

See Also:
[`getImpostor()`](#getImpostor()),
[`getImpostorIds()`](#getImpostorIds())
- #### getSizeX

```
int getSizeX()
```

Get the size of the object on the X-axis in tiles

Returns:
- #### getSizeY

```
int getSizeY()
```

Get the size of the object on the Y-axis in tiles

Returns: