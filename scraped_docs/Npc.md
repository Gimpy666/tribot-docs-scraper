# NPC (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/NPC.html

**Package:** Packagenet.runelite.api

---

* All Superinterfaces:
`[Actor](Actor.html "interface in net.runelite.api")`, `[CameraFocusableEntity](CameraFocusableEntity.html "interface in net.runelite.api")`, `[Node](Node.html "interface in net.runelite.api")`, `[Renderable](Renderable.html "interface in net.runelite.api")`

---

```
public interface NPC
extends [Actor](Actor.html "interface in net.runelite.api")
```

Represents a non-player character in the game.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `[NpcOverrides](NpcOverrides.html "interface in net.runelite.api")` | `[getChatheadOverrides](#getChatheadOverrides())()` | |
| `int` | `[getCombatLevel](#getCombatLevel())()` | Gets the combat level of the actor. |
| `[NPCComposition](NPCComposition.html "interface in net.runelite.api")` | `[getComposition](#getComposition())()` | Gets the composition of this NPC. |
| `int` | `[getId](#getId())()` | Gets the ID of the NPC. |
| `int` | `[getIndex](#getIndex())()` | Gets the index position of this NPC in the clients cached
NPC array. |
| `[NpcOverrides](NpcOverrides.html "interface in net.runelite.api")` | `[getModelOverrides](#getModelOverrides())()` | |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getName](#getName())()` | Gets the name of the actor. |
| `int[]` | `[getOverheadArchiveIds](#getOverheadArchiveIds())()` | Get the array of overhead icon archive ids. |
| `short[]` | `[getOverheadSpriteIds](#getOverheadSpriteIds())()` | Get the array of overhead icon sprite indexes. |
| `[NPCComposition](NPCComposition.html "interface in net.runelite.api")` | `[getTransformedComposition](#getTransformedComposition())()` | Get the composition for this NPC and transform it if required |

- ### Methods inherited from interface net.runelite.api.[Actor](Actor.html "interface in net.runelite.api")

`[clearSpotAnims](Actor.html#clearSpotAnims()), [createSpotAnim](Actor.html#createSpotAnim(int,int,int,int)), [getAnimation](Actor.html#getAnimation()), [getAnimationFrame](Actor.html#getAnimationFrame()), [getAnimationHeightOffset](Actor.html#getAnimationHeightOffset()), [getCanvasImageLocation](Actor.html#getCanvasImageLocation(java.awt.image.BufferedImage,int)), [getCanvasSpriteLocation](Actor.html#getCanvasSpriteLocation(net.runelite.api.SpritePixels,int)), [getCanvasTextLocation](Actor.html#getCanvasTextLocation(java.awt.Graphics2D,java.lang.String,int)), [getCanvasTilePoly](Actor.html#getCanvasTilePoly()), [getConvexHull](Actor.html#getConvexHull()), [getCurrentOrientation](Actor.html#getCurrentOrientation()), [getGraphic](Actor.html#getGraphic()), [getGraphicHeight](Actor.html#getGraphicHeight()), [getHealthRatio](Actor.html#getHealthRatio()), [getHealthScale](Actor.html#getHealthScale()), [getIdlePoseAnimation](Actor.html#getIdlePoseAnimation()), [getIdleRotateLeft](Actor.html#getIdleRotateLeft()), [getIdleRotateRight](Actor.html#getIdleRotateRight()), [getInteracting](Actor.html#getInteracting()), [getLocalLocation](Actor.html#getLocalLocation()), [getLogicalHeight](Actor.html#getLogicalHeight()), [getMinimapLocation](Actor.html#getMinimapLocation()), [getOrientation](Actor.html#getOrientation()), [getOverheadCycle](Actor.html#getOverheadCycle()), [getOverheadText](Actor.html#getOverheadText()), [getPoseAnimation](Actor.html#getPoseAnimation()), [getPoseAnimationFrame](Actor.html#getPoseAnimationFrame()), [getRunAnimation](Actor.html#getRunAnimation()), [getSpotAnimFrame](Actor.html#getSpotAnimFrame()), [getSpotAnims](Actor.html#getSpotAnims()), [getWalkAnimation](Actor.html#getWalkAnimation()), [getWalkRotate180](Actor.html#getWalkRotate180()), [getWalkRotateLeft](Actor.html#getWalkRotateLeft()), [getWalkRotateRight](Actor.html#getWalkRotateRight()), [getWorldArea](Actor.html#getWorldArea()), [getWorldLocation](Actor.html#getWorldLocation()), [getWorldView](Actor.html#getWorldView()), [hasSpotAnim](Actor.html#hasSpotAnim(int)), [isDead](Actor.html#isDead()), [isInteracting](Actor.html#isInteracting()), [removeSpotAnim](Actor.html#removeSpotAnim(int)), [setActionFrame](Actor.html#setActionFrame(int)), [setAnimation](Actor.html#setAnimation(int)), [setAnimationFrame](Actor.html#setAnimationFrame(int)), [setDead](Actor.html#setDead(boolean)), [setGraphic](Actor.html#setGraphic(int)), [setGraphicHeight](Actor.html#setGraphicHeight(int)), [setIdlePoseAnimation](Actor.html#setIdlePoseAnimation(int)), [setIdleRotateLeft](Actor.html#setIdleRotateLeft(int)), [setIdleRotateRight](Actor.html#setIdleRotateRight(int)), [setOverheadCycle](Actor.html#setOverheadCycle(int)), [setOverheadText](Actor.html#setOverheadText(java.lang.String)), [setPoseAnimation](Actor.html#setPoseAnimation(int)), [setPoseAnimationFrame](Actor.html#setPoseAnimationFrame(int)), [setRunAnimation](Actor.html#setRunAnimation(int)), [setSpotAnimFrame](Actor.html#setSpotAnimFrame(int)), [setWalkAnimation](Actor.html#setWalkAnimation(int)), [setWalkRotate180](Actor.html#setWalkRotate180(int)), [setWalkRotateLeft](Actor.html#setWalkRotateLeft(int)), [setWalkRotateRight](Actor.html#setWalkRotateRight(int))`
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

Gets the ID of the NPC.

Returns:
the ID of the NPC
See Also:
`NpcID`
- #### getName

```
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getName()
```

Description copied from interface: `[Actor](Actor.html#getName())`
Gets the name of the actor.

Specified by:
`[getName](Actor.html#getName())` in interface `[Actor](Actor.html "interface in net.runelite.api")`
Returns:
the name
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
- #### getIndex

```
int getIndex()
```

Gets the index position of this NPC in the clients cached
NPC array.

Returns:
the NPC index
- #### getComposition

```
[NPCComposition](NPCComposition.html "interface in net.runelite.api") getComposition()
```

Gets the composition of this NPC.

Returns:
the composition
- #### getTransformedComposition

```
@Nullable
[NPCComposition](NPCComposition.html "interface in net.runelite.api") getTransformedComposition()
```

Get the composition for this NPC and transform it if required

Returns:
the transformed NPC
- #### getModelOverrides

```
@Nullable
[NpcOverrides](NpcOverrides.html "interface in net.runelite.api") getModelOverrides()
```
- #### getChatheadOverrides

```
@Nullable
[NpcOverrides](NpcOverrides.html "interface in net.runelite.api") getChatheadOverrides()
```
- #### getOverheadArchiveIds

```
@Nullable
int[] getOverheadArchiveIds()
```

Get the array of overhead icon archive ids.
Used in conjunction with [`getOverheadSpriteIds()`](#getOverheadSpriteIds())
to determine which icons are being rendered overhead.

Returns:
A sparse array of archive ids. Values of -1 are not used.
See Also:
[`getOverheadSpriteIds()`](#getOverheadSpriteIds())
- #### getOverheadSpriteIds

```
@Nullable
short[] getOverheadSpriteIds()
```

Get the array of overhead icon sprite indexes.
Used in conjunction with [`getOverheadArchiveIds()`](#getOverheadArchiveIds())
to determine which icons are being rendered overhead.

Returns:
A sparse array of archive ids. Values of -1 are not used.
See Also:
[`getOverheadArchiveIds()`](#getOverheadArchiveIds())