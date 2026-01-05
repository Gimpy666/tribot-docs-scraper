# World (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/World.html

**Package:** Packagenet.runelite.api

**Description:** For example, world 2 would return "Trade - Members"....

---

* ---

```
public interface World
```

Holds data of a RuneScape world.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getActivity](#getActivity())()` | Gets the world activity description. |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getAddress](#getAddress())()` | Gets the address of the world. |
| `int` | `[getId](#getId())()` | Gets the world number. |
| `int` | `[getIndex](#getIndex())()` | Gets the worlds index. |
| `int` | `[getLocation](#getLocation())()` | Gets the world location value. |
| `int` | `[getPlayerCount](#getPlayerCount())()` | Gets the current number of players logged in the world. |
| `[EnumSet](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/EnumSet.html?is-external=true "class or interface in java.util")<[WorldType](WorldType.html "enum in net.runelite.api")>` | `[getTypes](#getTypes())()` | Gets all applicable world types for this world. |
| `void` | `[setActivity](#setActivity(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") activity)` | Sets the world activity description. |
| `void` | `[setAddress](#setAddress(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") address)` | Sets the address of the world. |
| `void` | `[setId](#setId(int))​(int id)` | Sets the world number. |
| `void` | `[setIndex](#setIndex(int))​(int index)` | Sets the worlds index. |
| `void` | `[setLocation](#setLocation(int))​(int location)` | Sets the world location value. |
| `void` | `[setPlayerCount](#setPlayerCount(int))​(int playerCount)` | Sets the player count of the world. |
| `void` | `[setTypes](#setTypes(java.util.EnumSet))​([EnumSet](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/EnumSet.html?is-external=true "class or interface in java.util")<[WorldType](WorldType.html "enum in net.runelite.api")> types)` | Sets world types. |

* + ### Method Detail

- #### getTypes

```
[EnumSet](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/EnumSet.html?is-external=true "class or interface in java.util")<[WorldType](WorldType.html "enum in net.runelite.api")> getTypes()
```

Gets all applicable world types for this world.

Returns:
the world types
- #### setTypes

```
void setTypes​([EnumSet](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/EnumSet.html?is-external=true "class or interface in java.util")<[WorldType](WorldType.html "enum in net.runelite.api")> types)
```

Sets world types.

Parameters:
`types` - the types
- #### getPlayerCount

```
int getPlayerCount()
```

Gets the current number of players logged in the world.

Returns:
the player count
- #### setPlayerCount

```
void setPlayerCount​(int playerCount)
```

Sets the player count of the world.

Parameters:
`playerCount` - the new player count
- #### getLocation

```
int getLocation()
```

Gets the world location value.

Returns:
the world location
- #### setLocation

```
void setLocation​(int location)
```

Sets the world location value.

Parameters:
`location` - the location
- #### getIndex

```
int getIndex()
```

Gets the worlds index.

Returns:
the index
- #### setIndex

```
void setIndex​(int index)
```

Sets the worlds index.

Parameters:
`index` - the index
- #### getId

```
int getId()
```

Gets the world number.

Returns:
the world number
- #### setId

```
void setId​(int id)
```

Sets the world number.

Parameters:
`id` - the world number
- #### getActivity

```
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getActivity()
```

Gets the world activity description.

For example, world 2 would return "Trade - Members".

Returns:
the world activity
- #### setActivity

```
void setActivity​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") activity)
```

Sets the world activity description.

Parameters:
`activity` - the activity
- #### getAddress

```
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getAddress()
```

Gets the address of the world.

Returns:
the world address
- #### setAddress

```
void setAddress​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") address)
```

Sets the address of the world.

Parameters:
`address` - the address