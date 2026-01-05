# Player (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/Player.html

**Package:** Packagenet.runelite.api

---

* All Superinterfaces:
`[Actor](Actor.html "interface in net.runelite.api")`, `[CameraFocusableEntity](CameraFocusableEntity.html "interface in net.runelite.api")`, `[Node](Node.html "interface in net.runelite.api")`, `[Renderable](Renderable.html "interface in net.runelite.api")`

---

```
public interface Player
extends [Actor](Actor.html "interface in net.runelite.api")
```

Represents a player entity in the game.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `int` | `[getCombatLevel](#getCombatLevel())()` | Gets the combat level of the actor. |
| `int` | `[getFootprintSize](#getFootprintSize())()` | Get the player footprint size |
| `int` | `[getId](#getId())()` | Get the ID of the player |
| `[HeadIcon](HeadIcon.html "enum in net.runelite.api")` | `[getOverheadIcon](#getOverheadIcon())()` | Gets the displayed overhead icon of the player. |
| `[PlayerComposition](PlayerComposition.html "interface in net.runelite.api")` | `[getPlayerComposition](#getPlayerComposition())()` | Gets the composition of this player. |
| `[Polygon](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Polygon.html?is-external=true "class or interface in java.awt")[]` | `[getPolygons](#getPolygons())()` | Gets the polygons that make up the players model. |
| `int` | `[getSkullIcon](#getSkullIcon())()` | Gets the displayed skull icon of the player. |
| `int` | `[getTeam](#getTeam())()` | Gets the current team cape team number the player is on. |
| `boolean` | `[isClanMember](#isClanMember())()` | Checks whether the player is a member of the same clan as the local player. |
| `boolean` | `[isFriend](#isFriend())()` | Checks whether this player is a friend of the local player. |
| `boolean` | `[isFriendsChatMember](#isFriendsChatMember())()` | Checks whether this player is a member of the same friends chat
the local player. |
| `void` | `[setSkullIcon](#setSkullIcon(int))​(int skullIcon)` | Sets the displayed skull icon of the player. |

- ### Methods inherited from interface net.runelite.api.[Actor](Actor.html "interface in net.runelite.api")

`[clearSpotAnims](Actor.html#clearSpotAnims()), [createSpotAnim](Actor.html#createSpotAnim(int,int,int,int)), [getAnimation](Actor.html#getAnimation()), [getAnimationFrame](Actor.html#getAnimationFrame()), [getAnimationHeightOffset](Actor.html#getAnimationHeightOffset()), [getCanvasImageLocation](Actor.html#getCanvasImageLocation(java.awt.image.BufferedImage,int)), [getCanvasSpriteLocation](Actor.html#getCanvasSpriteLocation(net.runelite.api.SpritePixels,int)), [getCanvasTextLocation](Actor.html#getCanvasTextLocation(java.awt.Graphics2D,java.lang.String,int)), [getCanvasTilePoly](Actor.html#getCanvasTilePoly()), [getConvexHull](Actor.html#getConvexHull()), [getCurrentOrientation](Actor.html#getCurrentOrientation()), [getGraphic](Actor.html#getGraphic()), [getGraphicHeight](Actor.html#getGraphicHeight()), [getHealthRatio](Actor.html#getHealthRatio()), [getHealthScale](Actor.html#getHealthScale()), [getIdlePoseAnimation](Actor.html#getIdlePoseAnimation()), [getIdleRotateLeft](Actor.html#getIdleRotateLeft()), [getIdleRotateRight](Actor.html#getIdleRotateRight()), [getInteracting](Actor.html#getInteracting()), [getLocalLocation](Actor.html#getLocalLocation()), [getLogicalHeight](Actor.html#getLogicalHeight()), [getMinimapLocation](Actor.html#getMinimapLocation()), [getName](Actor.html#getName()), [getOrientation](Actor.html#getOrientation()), [getOverheadCycle](Actor.html#getOverheadCycle()), [getOverheadText](Actor.html#getOverheadText()), [getPoseAnimation](Actor.html#getPoseAnimation()), [getPoseAnimationFrame](Actor.html#getPoseAnimationFrame()), [getRunAnimation](Actor.html#getRunAnimation()), [getSpotAnimFrame](Actor.html#getSpotAnimFrame()), [getSpotAnims](Actor.html#getSpotAnims()), [getWalkAnimation](Actor.html#getWalkAnimation()), [getWalkRotate180](Actor.html#getWalkRotate180()), [getWalkRotateLeft](Actor.html#getWalkRotateLeft()), [getWalkRotateRight](Actor.html#getWalkRotateRight()), [getWorldArea](Actor.html#getWorldArea()), [getWorldLocation](Actor.html#getWorldLocation()), [getWorldView](Actor.html#getWorldView()), [hasSpotAnim](Actor.html#hasSpotAnim(int)), [isDead](Actor.html#isDead()), [isInteracting](Actor.html#isInteracting()), [removeSpotAnim](Actor.html#removeSpotAnim(int)), [setActionFrame](Actor.html#setActionFrame(int)), [setAnimation](Actor.html#setAnimation(int)), [setAnimationFrame](Actor.html#setAnimationFrame(int)), [setDead](Actor.html#setDead(boolean)), [setGraphic](Actor.html#setGraphic(int)), [setGraphicHeight](Actor.html#setGraphicHeight(int)), [setIdlePoseAnimation](Actor.html#setIdlePoseAnimation(int)), [setIdleRotateLeft](Actor.html#setIdleRotateLeft(int)), [setIdleRotateRight](Actor.html#setIdleRotateRight(int)), [setOverheadCycle](Actor.html#setOverheadCycle(int)), [setOverheadText](Actor.html#setOverheadText(java.lang.String)), [setPoseAnimation](Actor.html#setPoseAnimation(int)), [setPoseAnimationFrame](Actor.html#setPoseAnimationFrame(int)), [setRunAnimation](Actor.html#setRunAnimation(int)), [setSpotAnimFrame](Actor.html#setSpotAnimFrame(int)), [setWalkAnimation](Actor.html#setWalkAnimation(int)), [setWalkRotate180](Actor.html#setWalkRotate180(int)), [setWalkRotateLeft](Actor.html#setWalkRotateLeft(int)), [setWalkRotateRight](Actor.html#setWalkRotateRight(int))`
- ### Methods inherited from interface net.runelite.api.[CameraFocusableEntity](CameraFocusableEntity.html "interface in net.runelite.api")

`[getCameraFocus](CameraFocusableEntity.html#getCameraFocus())`
- ### Methods inherited from interface net.runelite.api.[Node](Node.html "interface in net.runelite.api")

`[getHash](Node.html#getHash()), [getNext](Node.html#getNext()), [getPrevious](Node.html#getPrevious())`
- ### Methods inherited from interface net.runelite.api.[Renderable](Renderable.html "interface in net.runelite.api")

`[getModel](Renderable.html#getModel()), [getModelHeight](Renderable.html#getModelHeight()), [setModelHeight](Renderable.html#setModelHeight(int))`

* + ### Method Detail

- #### getId

```
int getId()
```

Get the ID of the player

Returns:
- #### getCombatLevel

```
int getCombatLevel()
```

Description copied from interface: `[Actor](Actor.html#getCombatLevel())`
Gets the combat level of the actor.

Specified by:
`[getCombatLevel](Actor.html#getCombatLevel())` in interface `[Actor](Actor.html "interface in net.runelite.api")`
Returns:
the combat level
- #### getPlayerComposition

```
[PlayerComposition](PlayerComposition.html "interface in net.runelite.api") getPlayerComposition()
```

Gets the composition of this player.

Returns:
the composition
- #### getPolygons

```
[Polygon](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Polygon.html?is-external=true "class or interface in java.awt")[] getPolygons()
```

Gets the polygons that make up the players model.

Returns:
the model polygons
- #### getTeam

```
int getTeam()
```

Gets the current team cape team number the player is on.

Returns:
team number, or 0 if not on any team
- #### isFriendsChatMember

```
boolean isFriendsChatMember()
```

Checks whether this player is a member of the same friends chat
the local player.

Returns:
true if the player is a friends chat member, false otherwise
- #### isFriend

```
boolean isFriend()
```

Checks whether this player is a friend of the local player.

Returns:
true if the player is a friend, false otherwise
- #### isClanMember

```
boolean isClanMember()
```

Checks whether the player is a member of the same clan as the local player.

Returns:
- #### getOverheadIcon

```
[HeadIcon](HeadIcon.html "enum in net.runelite.api") getOverheadIcon()
```

Gets the displayed overhead icon of the player.

Returns:
the overhead icon
- #### getSkullIcon

```
int getSkullIcon()
```

Gets the displayed skull icon of the player.

Returns:
the id skull icon, or -1 if unskulled.
See Also:
[`SkullIcon`](SkullIcon.html "class in net.runelite.api")
- #### setSkullIcon

```
void setSkullIcon​(int skullIcon)
```

Sets the displayed skull icon of the player.

Parameters:
`skullIcon` - The id of the skull icon, or -1 to remove the skull icon.
See Also:
[`SkullIcon`](SkullIcon.html "class in net.runelite.api")
- #### getFootprintSize

```
int getFootprintSize()
```

Get the player footprint size

Returns: