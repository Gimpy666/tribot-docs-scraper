# Client (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/Client.html

**Package:** Packagenet.runelite.api

**Description:** This value is a local coordinate value similar togetLocalDestinationLocation()....

---

* All Superinterfaces:
`[GameEngine](GameEngine.html "interface in net.runelite.api")`, `[OAuthApi](../../../com/jagex/oldscape/pub/OAuthApi.html "interface in com.jagex.oldscape.pub")`

---

```
public interface Client
extends [OAuthApi](../../../com/jagex/oldscape/pub/OAuthApi.html "interface in com.jagex.oldscape.pub"), [GameEngine](GameEngine.html "interface in net.runelite.api")
```

Represents the RuneScape client.

* + ### Field Summary

Fields | Modifier and Type | Field | Description |
| `static int` | `[DRAW\_2D\_ALL](#DRAW_2D_ALL)` | Draw all 2D extras. |
| `static int` | `[DRAW\_2D\_NONE](#DRAW_2D_NONE)` | Hide all 2D extras. |
| `static int` | `[DRAW\_2D\_OTHERS](#DRAW_2D_OTHERS)` | Render elements not otherwise specified in this bitflag. |
| `static int` | `[DRAW\_2D\_OVERHEAD\_TEXT](#DRAW_2D_OVERHEAD_TEXT)` | Render overhead text. |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) [Default Methods](javascript:show(16);) [Deprecated Methods](javascript:show(32);) | Modifier and Type | Method | Description |
| `[MessageNode](MessageNode.html "interface in net.runelite.api")` | `[addChatMessage](#addChatMessage(net.runelite.api.ChatMessageType,java.lang.String,java.lang.String,java.lang.String))​([ChatMessageType](ChatMessageType.html "enum in net.runelite.api") type,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") message,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") sender)` | Adds a new chat message to the chatbox. |
| `[MessageNode](MessageNode.html "interface in net.runelite.api")` | `[addChatMessage](#addChatMessage(net.runelite.api.ChatMessageType,java.lang.String,java.lang.String,java.lang.String,boolean))​([ChatMessageType](ChatMessageType.html "enum in net.runelite.api") type,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") message,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") sender,
boolean postEvent)` | Adds a new chat message to the chatbox. |
| `[Model](Model.html "interface in net.runelite.api")` | `[applyTransformations](#applyTransformations(net.runelite.api.Model,net.runelite.api.Animation,int,net.runelite.api.Animation,int))​([Model](Model.html "interface in net.runelite.api") model,
[Animation](Animation.html "interface in net.runelite.api") animA,
int frameA,
[Animation](Animation.html "interface in net.runelite.api") animB,
int frameB)` | Applies an animation to a Model. |
| `void` | `[changeMemoryMode](#changeMemoryMode(boolean))​(boolean lowMemory)` | Changes how game behaves based on memory mode. |
| `void` | `[changeWorld](#changeWorld(net.runelite.api.World))​([World](World.html "interface in net.runelite.api") world)` | Changes the selected world to log in to. |
| `void` | `[checkClickbox](#checkClickbox(net.runelite.api.Projection,net.runelite.api.Model,int,int,int,int,long))​([Projection](Projection.html "interface in net.runelite.api") projection,
[Model](Model.html "interface in net.runelite.api") model,
int orientation,
int x,
int y,
int z,
long hash)` | |
| `void` | `[clearHintArrow](#clearHintArrow())()` | Clears the current hint arrow. |
| `void` | `[closeInterface](#closeInterface(net.runelite.api.WidgetNode,boolean))​([WidgetNode](WidgetNode.html "interface in net.runelite.api") interfaceNode,
boolean unload)` | Close an interface |
| `[IndexedSprite](IndexedSprite.html "interface in net.runelite.api")` | `[createIndexedSprite](#createIndexedSprite())()` | Creates an empty indexed sprite. |
| `[SpritePixels](SpritePixels.html "interface in net.runelite.api")` | `[createItemSprite](#createItemSprite(int,int,int,int,int,boolean,int))​(int itemId,
int quantity,
int border,
int shadowColor,
int stackable,
boolean noted,
int scale)` | Creates an item icon sprite with passed variables. |
| `[MenuEntry](MenuEntry.html "interface in net.runelite.api")` | `[createMenuEntry](#createMenuEntry(int))​(int idx)` | Deprecated. |
| `[Projectile](Projectile.html "interface in net.runelite.api")` | `[createProjectile](#createProjectile(int,int,int,int,int,int,int,int,int,int,net.runelite.api.Actor,int,int))​(int id,
int plane,
int startX,
int startY,
int startZ,
int startCycle,
int endCycle,
int slope,
int startHeight,
int endHeight,
[Actor](Actor.html "interface in net.runelite.api") target,
int targetX,
int targetY)` | Deprecated. |
| `[Projectile](Projectile.html "interface in net.runelite.api")` | `[createProjectile](#createProjectile(int,net.runelite.api.coords.WorldPoint,int,net.runelite.api.Actor,net.runelite.api.coords.WorldPoint,int,net.runelite.api.Actor,int,int,int,int))​(int spotanimId,
[WorldPoint](coords/WorldPoint.html "class in net.runelite.api.coords") source,
int sourceHeightOffset,
[Actor](Actor.html "interface in net.runelite.api") sourceActor,
[WorldPoint](coords/WorldPoint.html "class in net.runelite.api.coords") target,
int targetHeightOffset,
[Actor](Actor.html "interface in net.runelite.api") targetActor,
int startCycle,
int endCycle,
int slope,
int startPos)` | Create a projectile. |
| `[RuneLiteObject](RuneLiteObject.html "class in net.runelite.api")` | `[createRuneLiteObject](#createRuneLiteObject())()` | Creates a RuneLiteObject, which is a modified [`GraphicsObject`](GraphicsObject.html "interface in net.runelite.api") |
| `[SceneTilePaint](SceneTilePaint.html "interface in net.runelite.api")` | `[createSceneTilePaint](#createSceneTilePaint(int,int,int,int,int,int,boolean))​(int swColor,
int seColor,
int neColor,
int nwColor,
int texture,
int minimapRgb,
boolean flatShade)` | Creates a SceneTilePaint instance, which can be attached to a Tile to control its appearance. |
| `[ScriptEvent](ScriptEvent.html "interface in net.runelite.api")` | `[createScriptEvent](#createScriptEvent(java.lang.Object...))​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")... args)` | Creates a blank ScriptEvent for executing a ClientScript2 script |
| `[SpritePixels](SpritePixels.html "interface in net.runelite.api")` | `[createSpritePixels](#createSpritePixels(int%5B%5D,int,int))​(int[] pixels,
int width,
int height)` | Creates a sprite image with given width and height containing the
pixels. |
| `[World](World.html "interface in net.runelite.api")` | `[createWorld](#createWorld())()` | Creates a new instance of a world. |
| `void` | `[draw2010Menu](#draw2010Menu(int))​(int alpha)` | Draws a menu in the 2010 interface style. |
| `[SpritePixels](SpritePixels.html "interface in net.runelite.api")` | `[drawInstanceMap](#drawInstanceMap(int))​(int z)` | Draws an instance map for the current viewed plane. |
| `void` | `[drawOriginalMenu](#drawOriginalMenu(int))​(int alpha)` | Draws a menu in the OSRS interface style. |
| `[WorldView](WorldView.html "interface in net.runelite.api")` | `[findWorldViewFromWorldPoint](#findWorldViewFromWorldPoint(net.runelite.api.coords.WorldPoint))​([WorldPoint](coords/WorldPoint.html "class in net.runelite.api.coords") point)` | Find the worldview a given worldpoint belongs in |
| `int` | `[get3dZoom](#get3dZoom())()` | |
| `[AccountType](vars/AccountType.html "enum in net.runelite.api.vars")` | `[getAccountType](#getAccountType())()` | Deprecated.
see Varbits#ACCOUNT\_TYPE
|
| `[List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html?is-external=true "class or interface in java.util")<[MidiRequest](MidiRequest.html "interface in net.runelite.api")>` | `[getActiveMidiRequests](#getActiveMidiRequests())()` | Get the currently playing midi requests. |
| `[Deque](Deque.html "interface in net.runelite.api")<[AmbientSoundEffect](AmbientSoundEffect.html "interface in net.runelite.api")>` | `[getAmbientSoundEffects](#getAmbientSoundEffects())()` | Deprecated. |
| `[NodeCache](NodeCache.html "interface in net.runelite.api")` | `[getAnimationCache](#getAnimationCache())()` | Returns the client [`Animation`](Animation.html "interface in net.runelite.api") cache |
| `[IntPredicate](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/function/IntPredicate.html?is-external=true "class or interface in java.util.function")` | `[getAnimationInterpolationFilter](#getAnimationInterpolationFilter())()` | |
| `int[]` | `[getArray](#getArray(int))​(int arrayId)` | Get one of the cs2 vm's arrays. |
| `int` | `[getArraySizes](#getArraySizes(int))​(int arrayId)` | Get the size of one of the cs2 vm's arrays. |
| `default int` | `[getBaseX](#getBaseX())()` | Deprecated. |
| `default int` | `[getBaseY](#getBaseY())()` | Deprecated. |
| `int` | `[getBoostedSkillLevel](#getBoostedSkillLevel(net.runelite.api.Skill))​([Skill](Skill.html "enum in net.runelite.api") skill)` | Gets the current modified level of a skill. |
| `int[]` | `[getBoostedSkillLevels](#getBoostedSkillLevels())()` | |
| `[BufferProvider](BufferProvider.html "interface in net.runelite.api")` | `[getBufferProvider](#getBufferProvider())()` | Gets the clients graphic buffer provider. |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getBuildID](#getBuildID())()` | |
| `[Callbacks](hooks/Callbacks.html "interface in net.runelite.api.hooks")` | `[getCallbacks](#getCallbacks())()` | The injected client invokes these callbacks to send events to us |
| `double` | `[getCameraFocalPointX](#getCameraFocalPointX())()` | Get the camera focus point x
Typically this is the player position, but can be other points in cutscenes or in free camera mode. |
| `double` | `[getCameraFocalPointY](#getCameraFocalPointY())()` | Get the camera focus point y
Typically this is the player position, but can be other points in cutscenes or in free camera mode. |
| `double` | `[getCameraFocalPointZ](#getCameraFocalPointZ())()` | Get the camera focus point z
Typically this is the player position, but can be other points in cutscenes or in free camera mode. |
| `[CameraFocusableEntity](CameraFocusableEntity.html "interface in net.runelite.api")` | `[getCameraFocusEntity](#getCameraFocusEntity())()` | Get the entity that the camera is focused on |
| `double` | `[getCameraFpPitch](#getCameraFpPitch())()` | Floating point camera pitch. |
| `double` | `[getCameraFpX](#getCameraFpX())()` | Floating point camera position, x-axis |
| `double` | `[getCameraFpY](#getCameraFpY())()` | Floating point camera position, y-axis |
| `double` | `[getCameraFpYaw](#getCameraFpYaw())()` | Floating point camera yaw |
| `double` | `[getCameraFpZ](#getCameraFpZ())()` | Floating point camera position, z-axis |
| `int` | `[getCameraMode](#getCameraMode())()` | Get the camera mode |
| `int` | `[getCameraPitch](#getCameraPitch())()` | Gets the pitch of the camera. |
| `int` | `[getCameraPitchTarget](#getCameraPitchTarget())()` | Get the target camera pitch
The target pitch is the pitch the camera should use based on player input. |
| `int` | `[getCameraX](#getCameraX())()` | Gets the x-axis coordinate of the camera. |
| `int` | `[getCameraY](#getCameraY())()` | Gets the y-axis coordinate of the camera. |
| `int` | `[getCameraYaw](#getCameraYaw())()` | Gets the yaw of the camera. |
| `int` | `[getCameraYawTarget](#getCameraYawTarget())()` | Get the target camera yaw. |
| `int` | `[getCameraZ](#getCameraZ())()` | Gets the z-axis coordinate of the camera. |
| `[Canvas](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Canvas.html?is-external=true "class or interface in java.awt")` | `[getCanvas](#getCanvas())()` | Gets the canvas that contains everything. |
| `int` | `[getCanvasHeight](#getCanvasHeight())()` | Gets the canvas height |
| `int` | `[getCanvasWidth](#getCanvasWidth())()` | Gets the canvas width |
| `int` | `[getCenterX](#getCenterX())()` | |
| `int` | `[getCenterY](#getCenterY())()` | |
| `[Map](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Map.html?is-external=true "class or interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Integer.html?is-external=true "class or interface in java.lang"),​[ChatLineBuffer](ChatLineBuffer.html "interface in net.runelite.api")>` | `[getChatLineMap](#getChatLineMap())()` | Gets the map of chat buffers. |
| `[ClanChannel](clan/ClanChannel.html "interface in net.runelite.api.clan")` | `[getClanChannel](#getClanChannel())()` | Get the primary clan channel the player is in. |
| `[ClanChannel](clan/ClanChannel.html "interface in net.runelite.api.clan")` | `[getClanChannel](#getClanChannel(int))​(int clanId)` | Get clan channel by id. |
| `[ClanSettings](clan/ClanSettings.html "interface in net.runelite.api.clan")` | `[getClanSettings](#getClanSettings())()` | Get clan settings for the clan the user is in. |
| `[ClanSettings](clan/ClanSettings.html "interface in net.runelite.api.clan")` | `[getClanSettings](#getClanSettings(int))​(int clanId)` | Get clan settings by id |
| `default [CollisionData](CollisionData.html "interface in net.runelite.api")[]` | `[getCollisionMaps](#getCollisionMaps())()` | Deprecated. |
| `[HashTable](HashTable.html "interface in net.runelite.api")<[WidgetNode](WidgetNode.html "interface in net.runelite.api")>` | `[getComponentTable](#getComponentTable())()` | Gets the widget node component table. |
| `[SpritePixels](SpritePixels.html "interface in net.runelite.api")[]` | `[getCrossSprites](#getCrossSprites())()` | Returns the array of cross sprites that appear and animate when left-clicking |
| `long[]` | `[getCrossWorldMessageIds](#getCrossWorldMessageIds())()` | Get the list of message ids for the recently received cross-world messages. |
| `int` | `[getCrossWorldMessageIdsIndex](#getCrossWorldMessageIdsIndex())()` | Get the index of the next message to be inserted in the cross world message id list |
| `int` | `[getCurrentLoginField](#getCurrentLoginField())()` | Gets currently selected login field. |
| `[DBRowConfig](dbtable/DBRowConfig.html "interface in net.runelite.api.dbtable")` | `[getDBRowConfig](#getDBRowConfig(int))​(int rowID)` | |
| `[List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html?is-external=true "class or interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Integer.html?is-external=true "class or interface in java.lang")>` | `[getDBRowsByValue](#getDBRowsByValue(int,int,int,java.lang.Object))​(int table,
int column,
int tupleIndex,
[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang") value)` | Uses an index to find rows containing a certain value in a column. |
| `[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")[]` | `[getDBTableField](#getDBTableField(int,int,int))​(int rowID,
int column,
int tupleIndex)` | Gets a entry out of a DBTable Row |
| `[List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html?is-external=true "class or interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Integer.html?is-external=true "class or interface in java.lang")>` | `[getDBTableRows](#getDBTableRows(int))​(int table)` | Gets all rows in a DBTable |
| `[Widget](widgets/Widget.html "interface in net.runelite.api.widgets")` | `[getDraggedOnWidget](#getDraggedOnWidget())()` | Gets the widget that is being dragged on. |
| `[Widget](widgets/Widget.html "interface in net.runelite.api.widgets")` | `[getDraggedWidget](#getDraggedWidget())()` | Gets the widget currently being dragged. |
| `int` | `[getDragTime](#getDragTime())()` | Get the number of client cycles the current dragged widget
has been dragged for. |
| `int` | `[getDraw2DMask](#getDraw2DMask())()` | Gets the current draw2D mask. |
| `[DrawCallbacks](hooks/DrawCallbacks.html "interface in net.runelite.api.hooks")` | `[getDrawCallbacks](#getDrawCallbacks())()` | The injected client invokes these callbacks for scene drawing, which is
used by the gpu plugin to override the client's normal scene drawing code |
| `int` | `[getEnergy](#getEnergy())()` | Gets the current run energy of the logged in player. |
| `[EnumComposition](EnumComposition.html "interface in net.runelite.api")` | `[getEnum](#getEnum(int))​(int id)` | |
| `int` | `[getEnvironment](#getEnvironment())()` | |
| `int` | `[getExpandedMapLoading](#getExpandedMapLoading())()` | |
| `[Widget](widgets/Widget.html "interface in net.runelite.api.widgets")` | `[getFocusedInputFieldWidget](#getFocusedInputFieldWidget())()` | Gets the current active [`WidgetType.INPUT_FIELD`](widgets/WidgetType.html#INPUT_FIELD) Widget |
| `[NPC](NPC.html "interface in net.runelite.api")` | `[getFollower](#getFollower())()` | Get the local player's follower, such as a pet |
| `int` | `[getFPS](#getFPS())()` | Gets the current FPS (frames per second). |
| `[FriendContainer](FriendContainer.html "interface in net.runelite.api")` | `[getFriendContainer](#getFriendContainer())()` | Retrieve the nameable container containing friends |
| `[FriendsChatManager](FriendsChatManager.html "interface in net.runelite.api")` | `[getFriendsChatManager](#getFriendsChatManager())()` | Retrieve the friends chat manager |
| `int` | `[getGameCycle](#getGameCycle())()` | Gets the local clients game cycle. |
| `[GameState](GameState.html "enum in net.runelite.api")` | `[getGameState](#getGameState())()` | Gets the current game state. |
| `[GrandExchangeOffer](GrandExchangeOffer.html "interface in net.runelite.api")[]` | `[getGrandExchangeOffers](#getGrandExchangeOffers())()` | Gets an array of current grand exchange offers. |
| `default [Deque](Deque.html "interface in net.runelite.api")<[GraphicsObject](GraphicsObject.html "interface in net.runelite.api")>` | `[getGraphicsObjects](#getGraphicsObjects())()` | Deprecated. |
| `[ClanChannel](clan/ClanChannel.html "interface in net.runelite.api.clan")` | `[getGuestClanChannel](#getGuestClanChannel())()` | Get the guest clan channel the player is in. |
| `[ClanSettings](clan/ClanSettings.html "interface in net.runelite.api.clan")` | `[getGuestClanSettings](#getGuestClanSettings())()` | Get the guest clan's settings. |
| `[NPC](NPC.html "interface in net.runelite.api")` | `[getHintArrowNpc](#getHintArrowNpc())()` | Gets the NPC that the hint arrow is directed at. |
| `[Player](Player.html "interface in net.runelite.api")` | `[getHintArrowPlayer](#getHintArrowPlayer())()` | Gets the player that the hint arrow is directed at. |
| `[WorldPoint](coords/WorldPoint.html "class in net.runelite.api.coords")` | `[getHintArrowPoint](#getHintArrowPoint())()` | Gets the world point that the hint arrow is directed at. |
| `int` | `[getHintArrowType](#getHintArrowType())()` | Gets the type of hint arrow currently displayed. |
| `int` | `[getIdleTimeout](#getIdleTimeout())()` | Get the amount of time until the client automatically logs out due to idle input. |
| `[NameableContainer](NameableContainer.html "interface in net.runelite.api")<[Ignore](Ignore.html "interface in net.runelite.api")>` | `[getIgnoreContainer](#getIgnoreContainer())()` | Retrieve the nameable container containing ignores |
| `[IndexDataBase](IndexDataBase.html "interface in net.runelite.api")` | `[getIndex](#getIndex(int))​(int id)` | Gets an index by id |
| `[IndexDataBase](IndexDataBase.html "interface in net.runelite.api")` | `[getIndexConfig](#getIndexConfig())()` | Gets the config index. |
| `[IndexDataBase](IndexDataBase.html "interface in net.runelite.api")` | `[getIndexScripts](#getIndexScripts())()` | Gets the script index. |
| `[IndexDataBase](IndexDataBase.html "interface in net.runelite.api")` | `[getIndexSprites](#getIndexSprites())()` | Gets the sprite index. |
| `int[][][]` | `[getInstanceTemplateChunks](#getInstanceTemplateChunks())()` | Deprecated. |
| `int[]` | `[getIntStack](#getIntStack())()` | Gets the cs2 vm's int stack |
| `int` | `[getIntStackSize](#getIntStackSize())()` | Gets the length of the cs2 vm's int stack |
| `[NodeCache](NodeCache.html "interface in net.runelite.api")` | `[getItemCompositionCache](#getItemCompositionCache())()` | Returns client item composition cache |
| `[ItemContainer](ItemContainer.html "interface in net.runelite.api")` | `[getItemContainer](#getItemContainer(int))​(int id)` | Get an item container by id |
| `[ItemContainer](ItemContainer.html "interface in net.runelite.api")` | `[getItemContainer](#getItemContainer(net.runelite.api.InventoryID))​([InventoryID](InventoryID.html "enum in net.runelite.api") inventory)` | Get the item container for an inventory. |
| `[HashTable](HashTable.html "interface in net.runelite.api")<[ItemContainer](ItemContainer.html "interface in net.runelite.api")>` | `[getItemContainers](#getItemContainers())()` | Get all item containers |
| `int` | `[getItemCount](#getItemCount())()` | Returns the max item index + 1 from cache |
| `[ItemComposition](ItemComposition.html "interface in net.runelite.api")` | `[getItemDefinition](#getItemDefinition(int))​(int id)` | Gets the item composition corresponding to an items ID. |
| `[NodeCache](NodeCache.html "interface in net.runelite.api")` | `[getItemModelCache](#getItemModelCache())()` | Get the item model cache. |
| `[NodeCache](NodeCache.html "interface in net.runelite.api")` | `[getItemSpriteCache](#getItemSpriteCache())()` | Get the item sprite cache. |
| `int` | `[getKeyboardIdleTicks](#getKeyboardIdleTicks())()` | Gets the amount of client ticks since the last keyboard press occurred. |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getLauncherDisplayName](#getLauncherDisplayName())()` | Gets the display name of the active account when launched from the Jagex launcher. |
| `[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords")` | `[getLocalDestinationLocation](#getLocalDestinationLocation())()` | Gets the location of the local player. |
| `[Player](Player.html "interface in net.runelite.api")` | `[getLocalPlayer](#getLocalPlayer())()` | Gets the logged in player instance. |
| `int` | `[getLoginIndex](#getLoginIndex())()` | Gets index of current login state. |
| `int` | `[getMapAngle](#getMapAngle())()` | Deprecated. |
| `[SpritePixels](SpritePixels.html "interface in net.runelite.api")[]` | `[getMapDots](#getMapDots())()` | Gets an array of currently drawn mini-map dots. |
| `[MapElementConfig](worldmap/MapElementConfig.html "interface in net.runelite.api.worldmap")` | `[getMapElementConfig](#getMapElementConfig(int))​(int id)` | Get a map element config by id |
| `[SpritePixels](SpritePixels.html "interface in net.runelite.api")[]` | `[getMapIcons](#getMapIcons())()` | Gets an array of current map icon sprites. |
| `int[]` | `[getMapRegions](#getMapRegions())()` | Deprecated. |
| `[IndexedSprite](IndexedSprite.html "interface in net.runelite.api")[]` | `[getMapScene](#getMapScene())()` | Gets a sprite of the map scene |
| `[Menu](Menu.html "interface in net.runelite.api")` | `[getMenu](#getMenu())()` | Get the client menu. |
| `[MenuEntry](MenuEntry.html "interface in net.runelite.api")[]` | `[getMenuEntries](#getMenuEntries())()` | Deprecated. |
| `int` | `[getMenuHeight](#getMenuHeight())()` | Deprecated. |
| `int` | `[getMenuScroll](#getMenuScroll())()` | Get the number of entries the currently open menu has been scrolled down. |
| `int` | `[getMenuWidth](#getMenuWidth())()` | Deprecated. |
| `int` | `[getMenuX](#getMenuX())()` | Deprecated. |
| `int` | `[getMenuY](#getMenuY())()` | Deprecated. |
| `[IterableHashTable](IterableHashTable.html "interface in net.runelite.api")<[MessageNode](MessageNode.html "interface in net.runelite.api")>` | `[getMessages](#getMessages())()` | Map of message node id to message node |
| `double` | `[getMinimapZoom](#getMinimapZoom())()` | Gets the number of pixels per tile on the minimap. |
| `[IndexedSprite](IndexedSprite.html "interface in net.runelite.api")[]` | `[getModIcons](#getModIcons())()` | Gets an array of mod icon sprites. |
| `[Point](Point.html "class in net.runelite.api")` | `[getMouseCanvasPosition](#getMouseCanvasPosition())()` | Gets the current position of the mouse on the canvas. |
| `int` | `[getMouseCurrentButton](#getMouseCurrentButton())()` | Gets the current mouse button that is pressed. |
| `int` | `[getMouseIdleTicks](#getMouseIdleTicks())()` | Gets the amount of client ticks since the last mouse movement occurred. |
| `long` | `[getMouseLastPressedMillis](#getMouseLastPressedMillis())()` | Gets the time at which the last mouse press occurred in milliseconds since
the UNIX epoch. |
| `int` | `[getMusicVolume](#getMusicVolume())()` | Gets the music volume |
| `[NPCComposition](NPCComposition.html "interface in net.runelite.api")` | `[getNpcDefinition](#getNpcDefinition(int))​(int npcId)` | Gets the NPC composition corresponding to an NPCs ID. |
| `default [List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html?is-external=true "class or interface in java.util")<[NPC](NPC.html "interface in net.runelite.api")>` | `[getNpcs](#getNpcs())()` | Deprecated. |
| `[NodeCache](NodeCache.html "interface in net.runelite.api")` | `[getObjectCompositionCache](#getObjectCompositionCache())()` | Returns client object composition cache |
| `[ObjectComposition](ObjectComposition.html "interface in net.runelite.api")` | `[getObjectDefinition](#getObjectDefinition(int))​(int objectId)` | Gets the object composition corresponding to an objects ID. |
| `[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")[]` | `[getObjectStack](#getObjectStack())()` | Gets the cs2 vm's object stack |
| `int` | `[getObjectStackSize](#getObjectStackSize())()` | Gets the length of the cs2 vm's object stack |
| `int` | `[getOculusOrbFocalPointX](#getOculusOrbFocalPointX())()` | Deprecated. |
| `int` | `[getOculusOrbFocalPointY](#getOculusOrbFocalPointY())()` | Deprecated. |
| `int` | `[getOculusOrbState](#getOculusOrbState())()` | Deprecated. |
| `long` | `[getOverallExperience](#getOverallExperience())()` | Get the total experience of the player |
| `default int` | `[getPlane](#getPlane())()` | Deprecated. |
| `int[]` | `[getPlayerMenuTypes](#getPlayerMenuTypes())()` | Gets an array of player menu types. |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")[]` | `[getPlayerOptions](#getPlayerOptions())()` | Gets an array of options that can currently be used on other players. |
| `boolean[]` | `[getPlayerOptionsPriorities](#getPlayerOptionsPriorities())()` | Gets an array of whether an option is enabled or not. |
| `default [List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html?is-external=true "class or interface in java.util")<[Player](Player.html "interface in net.runelite.api")>` | `[getPlayers](#getPlayers())()` | Deprecated. |
| `[Preferences](Preferences.html "interface in net.runelite.api")` | `[getPreferences](#getPreferences())()` | Gets the clients saved preferences. |
| `[Deque](Deque.html "interface in net.runelite.api")<[Projectile](Projectile.html "interface in net.runelite.api")>` | `[getProjectiles](#getProjectiles())()` | Gets a list of all projectiles currently spawned. |
| `[Rasterizer](Rasterizer.html "interface in net.runelite.api")` | `[getRasterizer](#getRasterizer())()` | |
| `int` | `[getRasterizer3D\_clipMidX2](#getRasterizer3D_clipMidX2())()` | |
| `int` | `[getRasterizer3D\_clipMidY2](#getRasterizer3D_clipMidY2())()` | |
| `int` | `[getRasterizer3D\_clipNegativeMidX](#getRasterizer3D_clipNegativeMidX())()` | |
| `int` | `[getRasterizer3D\_clipNegativeMidY](#getRasterizer3D_clipNegativeMidY())()` | |
| `[Dimension](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Dimension.html?is-external=true "class or interface in java.awt")` | `[getRealDimensions](#getRealDimensions())()` | Gets the real dimensions of the client before being stretched. |
| `int` | `[getRealSkillLevel](#getRealSkillLevel(net.runelite.api.Skill))​([Skill](Skill.html "enum in net.runelite.api") skill)` | Gets the real level of a skill. |
| `int[]` | `[getRealSkillLevels](#getRealSkillLevels())()` | |
| `[RenderOverview](RenderOverview.html "interface in net.runelite.api")` | `[getRenderOverview](#getRenderOverview())()` | Deprecated. |
| `int` | `[getRevision](#getRevision())()` | Gets the client revision number. |
| `int` | `[getScale](#getScale())()` | Gets the scale of the world (zoom value). |
| `default [Scene](Scene.html "interface in net.runelite.api")` | `[getScene](#getScene())()` | Deprecated. |
| `[Widget](widgets/Widget.html "interface in net.runelite.api.widgets")` | `[getScriptActiveWidget](#getScriptActiveWidget())()` | Gets the cs2 vm's active widget

This is used for all `cc_*` operations with a `0` operand |
| `[Widget](widgets/Widget.html "interface in net.runelite.api.widgets")` | `[getScriptDotWidget](#getScriptDotWidget())()` | Gets the cs2 vm's "dot" widget

This is used for all `.cc_*` operations with a `1` operand |
| `default [Tile](Tile.html "interface in net.runelite.api")` | `[getSelectedSceneTile](#getSelectedSceneTile())()` | Deprecated. |
| `[Widget](widgets/Widget.html "interface in net.runelite.api.widgets")` | `[getSelectedWidget](#getSelectedWidget())()` | Get the selected widget, such as a selected spell or selected item (eg. |
| `int` | `[getServerVarbitValue](#getServerVarbitValue(int))​(int varbit)` | Gets the value of the given varbit. |
| `int[]` | `[getServerVarps](#getServerVarps())()` | Get an array of all server varplayers. |
| `int` | `[getServerVarpValue](#getServerVarpValue(int))​(int varpId)` | Gets the value of a given VarPlayer. |
| `int` | `[getSkillExperience](#getSkillExperience(net.runelite.api.Skill))​([Skill](Skill.html "enum in net.runelite.api") skill)` | Gets the current experience towards a skill. |
| `int[]` | `[getSkillExperiences](#getSkillExperiences())()` | |
| `int` | `[getSkyboxColor](#getSkyboxColor())()` | Gets the RGB color of the skybox |
| `[Map](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Map.html?is-external=true "class or interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Integer.html?is-external=true "class or interface in java.lang"),​[SpritePixels](SpritePixels.html "interface in net.runelite.api")>` | `[getSpriteOverrides](#getSpriteOverrides())()` | Gets a mapping of sprites to override. |
| `[SpritePixels](SpritePixels.html "interface in net.runelite.api")[]` | `[getSprites](#getSprites(net.runelite.api.IndexDataBase,int,int))​([IndexDataBase](IndexDataBase.html "interface in net.runelite.api") source,
int archiveId,
int fileId)` | Loads and creates the sprite images of the passed archive and file IDs. |
| `[Dimension](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Dimension.html?is-external=true "class or interface in java.awt")` | `[getStretchedDimensions](#getStretchedDimensions())()` | Gets the current stretched dimensions of the client. |
| `[StructComposition](StructComposition.html "interface in net.runelite.api")` | `[getStructComposition](#getStructComposition(int))​(int structID)` | Gets the [`StructComposition`](StructComposition.html "interface in net.runelite.api") for a given struct ID |
| `[NodeCache](NodeCache.html "interface in net.runelite.api")` | `[getStructCompositionCache](#getStructCompositionCache())()` | Gets the client's cache of in memory struct compositions |
| `[TextureProvider](TextureProvider.html "interface in net.runelite.api")` | `[getTextureProvider](#getTextureProvider())()` | |
| `int` | `[getTickCount](#getTickCount())()` | Gets the current server tick count. |
| `default int[][][]` | `[getTileHeights](#getTileHeights())()` | Deprecated. |
| `default byte[][][]` | `[getTileSettings](#getTileSettings())()` | Deprecated. |
| `int` | `[getTopLevelInterfaceId](#getTopLevelInterfaceId())()` | Gets Interface ID of the root widget |
| `[WorldView](WorldView.html "interface in net.runelite.api")` | `[getTopLevelWorldView](#getTopLevelWorldView())()` | Get the top level world view |
| `int` | `[getTotalLevel](#getTotalLevel())()` | Calculates the total level from real skill levels. |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getUsername](#getUsername())()` | Deprecated. |
| `int` | `[getVar](#getVar(int))​(int varbit)` | Deprecated. |
| `[VarbitComposition](VarbitComposition.html "interface in net.runelite.api")` | `[getVarbit](#getVarbit(int))​(int id)` | Gets the varbit composition for a given varbit id |
| `int` | `[getVarbitValue](#getVarbitValue(int))​(int varbit)` | Gets the value of the given varbit. |
| `int` | `[getVarbitValue](#getVarbitValue(int%5B%5D,int))​(int[] varps,
int varbitId)` | Gets the value of a given variable. |
| `int` | `[getVarcIntValue](#getVarcIntValue(int))​(int var)` | Gets the value of a given VarClientInt |
| `[Map](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Map.html?is-external=true "class or interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Integer.html?is-external=true "class or interface in java.lang"),​[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")>` | `[getVarcMap](#getVarcMap())()` | Gets an array of all client variables. |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getVarcStrValue](#getVarcStrValue(int))​(int var)` | Gets the value of a given VarClientStr |
| `int[]` | `[getVarps](#getVarps())()` | Gets an array of all client varplayers. |
| `int` | `[getVarpValue](#getVarpValue(int))​(int varpId)` | Gets the value of a given VarPlayer. |
| `int` | `[getViewportHeight](#getViewportHeight())()` | Gets the height of the viewport. |
| `int` | `[getViewportWidth](#getViewportWidth())()` | Gets the width of the viewport. |
| `int` | `[getViewportXOffset](#getViewportXOffset())()` | Gets the x-axis offset of the viewport. |
| `int` | `[getViewportYOffset](#getViewportYOffset())()` | Gets the y-axis offset of the viewport. |
| `int` | `[getWeight](#getWeight())()` | Gets the current weight of the logged in player. |
| `[Widget](widgets/Widget.html "interface in net.runelite.api.widgets")` | `[getWidget](#getWidget(int))​(int componentId)` | Gets a widget by its component id. |
| `[Widget](widgets/Widget.html "interface in net.runelite.api.widgets")` | `[getWidget](#getWidget(int,int))​(int groupId,
int childId)` | Gets a widget by its raw group ID and child ID. |
| `[Widget](widgets/Widget.html "interface in net.runelite.api.widgets")` | `[getWidget](#getWidget(net.runelite.api.widgets.WidgetInfo))​([WidgetInfo](widgets/WidgetInfo.html "enum in net.runelite.api.widgets") widget)` | Deprecated. |
| `[WidgetConfigNode](widgets/WidgetConfigNode.html "interface in net.runelite.api.widgets")` | `[getWidgetConfig](#getWidgetConfig(net.runelite.api.widgets.Widget))​([Widget](widgets/Widget.html "interface in net.runelite.api.widgets") w)` | Get the widget config for a given widget |
| `[HashTable](HashTable.html "interface in net.runelite.api")<[WidgetConfigNode](widgets/WidgetConfigNode.html "interface in net.runelite.api.widgets")>` | `[getWidgetFlags](#getWidgetFlags())()` | Gets the widget flags table. |
| `int[]` | `[getWidgetPositionsX](#getWidgetPositionsX())()` | Gets an array containing the x-axis canvas positions
of all widgets. |
| `int[]` | `[getWidgetPositionsY](#getWidgetPositionsY())()` | Gets an array containing the y-axis canvas positions
of all widgets. |
| `[Widget](widgets/Widget.html "interface in net.runelite.api.widgets")[]` | `[getWidgetRoots](#getWidgetRoots())()` | Gets the root widgets. |
| `[NodeCache](NodeCache.html "interface in net.runelite.api")` | `[getWidgetSpriteCache](#getWidgetSpriteCache())()` | Returns widget sprite cache, to be used with [`getSpriteOverrides()`](#getSpriteOverrides()) |
| `[Map](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Map.html?is-external=true "class or interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Integer.html?is-external=true "class or interface in java.lang"),​[SpritePixels](SpritePixels.html "interface in net.runelite.api")>` | `[getWidgetSpriteOverrides](#getWidgetSpriteOverrides())()` | Gets a mapping of widget sprites to override. |
| `int` | `[getWorld](#getWorld())()` | Gets the current world number of the logged in player. |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getWorldHost](#getWorldHost())()` | Get the hostname of the current world |
| `[World](World.html "interface in net.runelite.api")[]` | `[getWorldList](#getWorldList())()` | Gets a list of all RuneScape worlds. |
| `[WorldMap](worldmap/WorldMap.html "interface in net.runelite.api.worldmap")` | `[getWorldMap](#getWorldMap())()` | Get the world map |
| `[EnumSet](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/EnumSet.html?is-external=true "class or interface in java.util")<[WorldType](WorldType.html "enum in net.runelite.api")>` | `[getWorldType](#getWorldType())()` | Gets a set of current world types that apply to the logged in world. |
| `[WorldView](WorldView.html "interface in net.runelite.api")` | `[getWorldView](#getWorldView(int))​(int id)` | Get worldview by id |
| `int[][]` | `[getXteaKeys](#getXteaKeys())()` | Deprecated. |
| `boolean` | `[hasHintArrow](#hasHintArrow())()` | Checks whether or not there is any active hint arrow. |
| `void` | `[hopToWorld](#hopToWorld(net.runelite.api.World))​([World](World.html "interface in net.runelite.api") world)` | Hops using in-game world hopper widget to another world |
| `void` | `[invalidateStretching](#invalidateStretching(boolean))​(boolean resize)` | Invalidates cached dimensions that are
used for stretching and scaling. |
| `boolean` | `[isCameraShakeDisabled](#isCameraShakeDisabled())()` | Whether camera shaking effects are disabled at e.g. |
| `boolean` | `[isDraggingWidget](#isDraggingWidget())()` | Checks whether a widget is currently being dragged. |
| `boolean` | `[isFriended](#isFriended(java.lang.String,boolean))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name,
boolean mustBeLoggedIn)` | Checks whether a player is on the friends list. |
| `boolean` | `[isGpu](#isGpu())()` | |
| `boolean` | `[isInInstancedRegion](#isInInstancedRegion())()` | Deprecated. |
| `boolean` | `[isKeyPressed](#isKeyPressed(int))​(int keycode)` | Test if a key is pressed |
| `boolean` | `[isMenuOpen](#isMenuOpen())()` | Checks whether a right-click menu is currently open. |
| `boolean` | `[isMenuScrollable](#isMenuScrollable())()` | Returns whether the currently open menu is scrollable. |
| `boolean` | `[isMinimapZoom](#isMinimapZoom())()` | Get whether minimap zoom is enabled |
| `boolean` | `[isPrayerActive](#isPrayerActive(net.runelite.api.Prayer))​([Prayer](Prayer.html "enum in net.runelite.api") prayer)` | Deprecated.
this method does not properly handle deadeye/eagle eye or mystic vigour/might
|
| `boolean` | `[isResized](#isResized())()` | Checks whether the client window is currently resized. |
| `boolean` | `[isRuneLiteObjectRegistered](#isRuneLiteObjectRegistered(net.runelite.api.RuneLiteObjectController))​([RuneLiteObjectController](RuneLiteObjectController.html "class in net.runelite.api") controller)` | Checks whether a [`RuneLiteObjectController`](RuneLiteObjectController.html "class in net.runelite.api") is registered to any [`WorldView`](WorldView.html "interface in net.runelite.api"). |
| `boolean` | `[isStretchedEnabled](#isStretchedEnabled())()` | Checks whether the client is in stretched mode. |
| `boolean` | `[isStretchedFast](#isStretchedFast())()` | Checks whether the client is using fast
rendering techniques when stretching the canvas. |
| `boolean` | `[isWidgetSelected](#isWidgetSelected())()` | Is a widget is in target mode? |
| `[Animation](Animation.html "interface in net.runelite.api")` | `[loadAnimation](#loadAnimation(int))​(int id)` | Loads an animation from the cache |
| `[Model](Model.html "interface in net.runelite.api")` | `[loadModel](#loadModel(int))​(int id)` | Loads and lights a model from the cache

This is equivalent to `loadModelData(id).light()` |
| `[Model](Model.html "interface in net.runelite.api")` | `[loadModel](#loadModel(int,short%5B%5D,short%5B%5D))​(int id,
short[] colorToFind,
short[] colorToReplace)` | Loads a model from the cache and also recolors it |
| `[ModelData](ModelData.html "interface in net.runelite.api")` | `[loadModelData](#loadModelData(int))​(int id)` | Loads an unlit model from the cache. |
| `void` | `[menuAction](#menuAction(int,int,net.runelite.api.MenuAction,int,int,java.lang.String,java.lang.String))​(int p0,
int p1,
[MenuAction](MenuAction.html "enum in net.runelite.api") action,
int id,
int itemId,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") option,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") target)` | |
| `[Model](Model.html "interface in net.runelite.api")` | `[mergeModels](#mergeModels(net.runelite.api.Model...))​([Model](Model.html "interface in net.runelite.api")... models)` | |
| `[Model](Model.html "interface in net.runelite.api")` | `[mergeModels](#mergeModels(net.runelite.api.Model%5B%5D,int))​([Model](Model.html "interface in net.runelite.api")[] models,
int length)` | |
| `[ModelData](ModelData.html "interface in net.runelite.api")` | `[mergeModels](#mergeModels(net.runelite.api.ModelData...))​([ModelData](ModelData.html "interface in net.runelite.api")... models)` | |
| `[ModelData](ModelData.html "interface in net.runelite.api")` | `[mergeModels](#mergeModels(net.runelite.api.ModelData%5B%5D,int))​([ModelData](ModelData.html "interface in net.runelite.api")[] models,
int length)` | |
| `[WidgetNode](WidgetNode.html "interface in net.runelite.api")` | `[openInterface](#openInterface(int,int,int))​(int componentId,
int interfaceId,
int modalMode)` | Open an interface. |
| `void` | `[openWorldHopper](#openWorldHopper())()` | Opens in-game world hopper interface |
| `void` | `[playSoundEffect](#playSoundEffect(int))​(int id)` | Play a sound effect at the player's current location. |
| `void` | `[playSoundEffect](#playSoundEffect(int,int))​(int id,
int volume)` | Plays a sound effect, even if the player's sound effect volume is muted. |
| `void` | `[playSoundEffect](#playSoundEffect(int,int,int,int))​(int id,
int x,
int y,
int range)` | Play a sound effect from some point in the world. |
| `void` | `[playSoundEffect](#playSoundEffect(int,int,int,int,int))​(int id,
int x,
int y,
int range,
int delay)` | Play a sound effect from some point in the world. |
| `void` | `[queueChangedSkill](#queueChangedSkill(net.runelite.api.Skill))​([Skill](Skill.html "enum in net.runelite.api") skill)` | |
| `void` | `[queueChangedVarp](#queueChangedVarp(int))​(int varp)` | Mark the given varp as changed, causing var listeners to be
triggered next tick |
| `void` | `[refreshChat](#refreshChat())()` | Refreshes the chat. |
| `void` | `[registerRuneLiteObject](#registerRuneLiteObject(net.runelite.api.RuneLiteObjectController))​([RuneLiteObjectController](RuneLiteObjectController.html "class in net.runelite.api") controller)` | Registers a new [`RuneLiteObjectController`](RuneLiteObjectController.html "class in net.runelite.api") to its corresponding [`WorldView`](WorldView.html "interface in net.runelite.api"). |
| `void` | `[removeRuneLiteObject](#removeRuneLiteObject(net.runelite.api.RuneLiteObjectController))​([RuneLiteObjectController](RuneLiteObjectController.html "class in net.runelite.api") controller)` | Removes a new [`RuneLiteObjectController`](RuneLiteObjectController.html "class in net.runelite.api") from its corresponding [`WorldView`](WorldView.html "interface in net.runelite.api"). |
| `void` | `[resetHealthBarCaches](#resetHealthBarCaches())()` | |
| `void` | `[runScript](#runScript(java.lang.Object...))​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")... args)` | Executes a client script from the cache

This method must be ran on the client thread and is not reentrant

This method is shorthand for `client.createScriptEvent(args).run()` |
| `void` | `[setAllWidgetsAreOpTargetable](#setAllWidgetsAreOpTargetable(boolean))​(boolean value)` | Makes all widgets behave as if they are [`WidgetConfig.WIDGET_USE_TARGET`](widgets/WidgetConfig.html#WIDGET_USE_TARGET) |
| `void` | `[setAnimationInterpolationFilter](#setAnimationInterpolationFilter(java.util.function.IntPredicate))​([IntPredicate](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/function/IntPredicate.html?is-external=true "class or interface in java.util.function") filter)` | |
| `void` | `[setCameraFocalPointX](#setCameraFocalPointX(double))​(double x)` | Sets the camera focus point x. |
| `void` | `[setCameraFocalPointY](#setCameraFocalPointY(double))​(double y)` | Sets the camera focus point y. |
| `void` | `[setCameraFocalPointZ](#setCameraFocalPointZ(double))​(double z)` | Sets the camera focus point z. |
| `void` | `[setCameraMode](#setCameraMode(int))​(int mode)` | Set the camera mode |
| `void` | `[setCameraMouseButtonMask](#setCameraMouseButtonMask(int))​(int mask)` | Sets the mask for which mouse buttons control the camera. |
| `void` | `[setCameraPitchRelaxerEnabled](#setCameraPitchRelaxerEnabled(boolean))​(boolean enabled)` | Sets whether the camera pitch can exceed the normal limits set
by the RuneScape client. |
| `void` | `[setCameraPitchTarget](#setCameraPitchTarget(int))​(int cameraPitchTarget)` | Set the target camera pitch |
| `void` | `[setCameraShakeDisabled](#setCameraShakeDisabled(boolean))​(boolean disabled)` | Set whether to disable camera shaking effects at e.g. |
| `void` | `[setCameraSpeed](#setCameraSpeed(float))​(float speed)` | Sets the camera speed |
| `void` | `[setCameraYawTarget](#setCameraYawTarget(int))​(int cameraYawTarget)` | Set the target camera yaw |
| `void` | `[setCompass](#setCompass(net.runelite.api.SpritePixels))​([SpritePixels](SpritePixels.html "interface in net.runelite.api") spritePixels)` | Sets the compass sprite. |
| `void` | `[setDraggedOnWidget](#setDraggedOnWidget(net.runelite.api.widgets.Widget))​([Widget](widgets/Widget.html "interface in net.runelite.api.widgets") widget)` | Sets the widget that is being dragged on. |
| `void` | `[setDraw2DMask](#setDraw2DMask(int))​(int mask)` | Sets the current draw2D mask. |
| `void` | `[setDrawCallbacks](#setDrawCallbacks(net.runelite.api.hooks.DrawCallbacks))​([DrawCallbacks](hooks/DrawCallbacks.html "interface in net.runelite.api.hooks") drawCallbacks)` | |
| `void` | `[setExpandedMapLoading](#setExpandedMapLoading(int))​(int chunks)` | |
| `void` | `[setFreeCameraSpeed](#setFreeCameraSpeed(int))​(int speed)` | Sets the normal moving speed when using oculus orb (default value is 12) |
| `void` | `[setGameState](#setGameState(net.runelite.api.GameState))​([GameState](GameState.html "enum in net.runelite.api") gameState)` | Sets the current game state |
| `void` | `[setGeSearchResultCount](#setGeSearchResultCount(int))​(int count)` | Sets the result count for GE search |
| `void` | `[setGeSearchResultIds](#setGeSearchResultIds(short%5B%5D))​(short[] ids)` | Sets the array of item ids for GE search |
| `void` | `[setGeSearchResultIndex](#setGeSearchResultIndex(int))​(int index)` | Sets the starting index in the item id array for GE search |
| `void` | `[setGpuFlags](#setGpuFlags(int))​(int gpuflags)` | |
| `void` | `[setHintArrow](#setHintArrow(net.runelite.api.coords.LocalPoint))​([LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") point)` | Sets the hint arrow to the passsed point |
| `void` | `[setHintArrow](#setHintArrow(net.runelite.api.coords.WorldPoint))​([WorldPoint](coords/WorldPoint.html "class in net.runelite.api.coords") point)` | Sets a hint arrow to point to the passed location. |
| `void` | `[setHintArrow](#setHintArrow(net.runelite.api.NPC))​([NPC](NPC.html "interface in net.runelite.api") npc)` | Sets a hint arrow to point to the passed NPC. |
| `void` | `[setHintArrow](#setHintArrow(net.runelite.api.Player))​([Player](Player.html "interface in net.runelite.api") player)` | Sets a hint arrow to point to the passed player. |
| `void` | `[setIdleTimeout](#setIdleTimeout(int))​(int ticks)` | Set the amount of time until the client automatically logs out due to idle input. |
| `void` | `[setIntStackSize](#setIntStackSize(int))​(int stackSize)` | Sets the length of the cs2 vm's int stack |
| `void` | `[setInventoryDragDelay](#setInventoryDragDelay(int))​(int delay)` | Deprecated. |
| `void` | `[setInvertPitch](#setInvertPitch(boolean))​(boolean invertPitch)` | Sets if the moving the camera vertically should be backwards |
| `void` | `[setInvertYaw](#setInvertYaw(boolean))​(boolean invertYaw)` | Sets if the moving the camera horizontally should be backwards |
| `void` | `[setLoginScreen](#setLoginScreen(net.runelite.api.SpritePixels))​([SpritePixels](SpritePixels.html "interface in net.runelite.api") pixels)` | Sets the image to be used for the login screen, provided as SpritePixels
If the image is larger than half the width of fixed mode,
it won't get mirrored to the other side of the screen |
| `void` | `[setMenuEntries](#setMenuEntries(net.runelite.api.MenuEntry%5B%5D))​([MenuEntry](MenuEntry.html "interface in net.runelite.api")[] entries)` | Deprecated. |
| `void` | `[setMenuScroll](#setMenuScroll(int))​(int scroll)` | Set the number of entries the currently open menu has been scrolled down. |
| `void` | `[setMinimapTileDrawer](#setMinimapTileDrawer(net.runelite.api.TileFunction))​([TileFunction](TileFunction.html "interface in net.runelite.api") drawTile)` | Sets a callback to override the drawing of tiles on the minimap. |
| `void` | `[setMinimapZoom](#setMinimapZoom(boolean))​(boolean minimapZoom)` | Set whether minimap zoom is enabled |
| `void` | `[setMinimapZoom](#setMinimapZoom(double))​(double zoom)` | Set the number of pixels per tile on the minimap. |
| `void` | `[setModIcons](#setModIcons(net.runelite.api.IndexedSprite%5B%5D))​([IndexedSprite](IndexedSprite.html "interface in net.runelite.api")[] modIcons)` | Replaces the current mod icons with a new array. |
| `void` | `[setMusicVolume](#setMusicVolume(int))​(int volume)` | Sets the music volume |
| `void` | `[setObjectStackSize](#setObjectStackSize(int))​(int stackSize)` | Sets the length of the cs2 vm's object stack |
| `void` | `[setOculusOrbNormalSpeed](#setOculusOrbNormalSpeed(int))​(int speed)` | Deprecated. |
| `void` | `[setOculusOrbState](#setOculusOrbState(int))​(int state)` | Deprecated. |
| `void` | `[setOtp](#setOtp(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") otp)` | Sets the 6 digit pin used for authenticator on login screen. |
| `void` | `[setPassword](#setPassword(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") password)` | Sets the password on login screen. |
| `void` | `[setScalingFactor](#setScalingFactor(int))​(int factor)` | Sets the scaling factor when scaling resizable mode. |
| `void` | `[setShouldRenderLoginScreenFire](#setShouldRenderLoginScreenFire(boolean))​(boolean val)` | Sets whether the flames on the login screen should be rendered |
| `void` | `[setSkyboxColor](#setSkyboxColor(int))​(int skyboxColor)` | Sets the RGB color of the skybox |
| `void` | `[setStretchedEnabled](#setStretchedEnabled(boolean))​(boolean state)` | Sets the client stretched mode state. |
| `void` | `[setStretchedFast](#setStretchedFast(boolean))​(boolean state)` | Sets whether to use fast rendering techniques
when stretching the canvas. |
| `void` | `[setStretchedIntegerScaling](#setStretchedIntegerScaling(boolean))​(boolean state)` | Sets whether to force integer scale factor by rounding scale
factors towards `zero` when stretching. |
| `void` | `[setStretchedKeepAspectRatio](#setStretchedKeepAspectRatio(boolean))​(boolean state)` | Sets whether to keep aspect ratio when stretching. |
| `void` | `[setTickCount](#setTickCount(int))​(int tickCount)` | Sets the current server tick count. |
| `void` | `[setUnlockedFps](#setUnlockedFps(boolean))​(boolean unlock)` | |
| `void` | `[setUnlockedFpsTarget](#setUnlockedFpsTarget(int))​(int fps)` | |
| `void` | `[setUsername](#setUsername(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)` | Sets the current logged in username. |
| `void` | `[setVarbit](#setVarbit(int,int))​(int varbit,
int value)` | Sets the value of a varbit |
| `void` | `[setVarbitValue](#setVarbitValue(int%5B%5D,int,int))​(int[] varps,
int varbit,
int value)` | Sets the value of a given variable. |
| `void` | `[setVarcIntValue](#setVarcIntValue(int,int))​(int var,
int value)` | Sets a VarClientInt to the passed value |
| `void` | `[setVarcStrValue](#setVarcStrValue(int,java.lang.String))​(int var,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") value)` | Sets a VarClientString to the passed value |
| `void` | `[setWidgetSelected](#setWidgetSelected(boolean))​(boolean selected)` | Sets if a widget is in target mode |
| `void` | `[stopNow](#stopNow())()` | Causes the client to shutdown. |

- ### Methods inherited from interface net.runelite.api.[GameEngine](GameEngine.html "interface in net.runelite.api")

`[getClientThread](GameEngine.html#getClientThread()), [isClientThread](GameEngine.html#isClientThread()), [resizeCanvas](GameEngine.html#resizeCanvas())`
- ### Methods inherited from interface com.jagex.oldscape.pub.[OAuthApi](../../../com/jagex/oldscape/pub/OAuthApi.html "interface in com.jagex.oldscape.pub")

`[getAccountHash](../../../com/jagex/oldscape/pub/OAuthApi.html#getAccountHash())`

* + ### Field Detail

- #### DRAW\_2D\_ALL

```
static final int DRAW_2D_ALL
```

Draw all 2D extras. This is the default.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Client.DRAW_2D_ALL)
- #### DRAW\_2D\_NONE

```
static final int DRAW_2D_NONE
```

Hide all 2D extras.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Client.DRAW_2D_NONE)
- #### DRAW\_2D\_OVERHEAD\_TEXT

```
static final int DRAW_2D_OVERHEAD_TEXT
```

Render overhead text.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Client.DRAW_2D_OVERHEAD_TEXT)
- #### DRAW\_2D\_OTHERS

```
static final int DRAW_2D_OTHERS
```

Render elements not otherwise specified in this bitflag.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Client.DRAW_2D_OTHERS)

+ ### Method Detail

- #### getCallbacks

```
[Callbacks](hooks/Callbacks.html "interface in net.runelite.api.hooks") getCallbacks()
```

The injected client invokes these callbacks to send events to us
- #### getDrawCallbacks

```
[DrawCallbacks](hooks/DrawCallbacks.html "interface in net.runelite.api.hooks") getDrawCallbacks()
```

The injected client invokes these callbacks for scene drawing, which is
used by the gpu plugin to override the client's normal scene drawing code
- #### setDrawCallbacks

```
void setDrawCallbacks​([DrawCallbacks](hooks/DrawCallbacks.html "interface in net.runelite.api.hooks") drawCallbacks)
```
- #### getBuildID

```
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getBuildID()
```
- #### getEnvironment

```
int getEnvironment()
```
- #### getBoostedSkillLevel

```
int getBoostedSkillLevel​([Skill](Skill.html "enum in net.runelite.api") skill)
```

Gets the current modified level of a skill.

Parameters:
`skill` - the skill
Returns:
the modified skill level
- #### getRealSkillLevel

```
int getRealSkillLevel​([Skill](Skill.html "enum in net.runelite.api") skill)
```

Gets the real level of a skill.

Parameters:
`skill` - the skill
Returns:
the skill level
- #### getTotalLevel

```
int getTotalLevel()
```

Calculates the total level from real skill levels.

Returns:
the total level
- #### addChatMessage

```
[MessageNode](MessageNode.html "interface in net.runelite.api") addChatMessage​([ChatMessageType](ChatMessageType.html "enum in net.runelite.api") type,
@Nonnull
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") message,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") sender)
```

Adds a new chat message to the chatbox.

Parameters:
`type` - the type of message
`name` - the name of the player that sent the message
`message` - the message contents
`sender` - the sender/channel name
Returns:
the message node for the message
- #### addChatMessage

```
[MessageNode](MessageNode.html "interface in net.runelite.api") addChatMessage​([ChatMessageType](ChatMessageType.html "enum in net.runelite.api") type,
@Nonnull
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") message,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") sender,
boolean postEvent)
```

Adds a new chat message to the chatbox.

Parameters:
`type` - the type of message
`name` - the name of the player that sent the message
`message` - the message contents
`sender` - the sender/channel name
`postEvent` - whether to post the chat message event
Returns:
the message node for the message
- #### getGameState

```
[GameState](GameState.html "enum in net.runelite.api") getGameState()
```

Gets the current game state.

Returns:
the game state
- #### setGameState

```
void setGameState​([GameState](GameState.html "enum in net.runelite.api") gameState)
```

Sets the current game state

Parameters:
`gameState` -
- #### stopNow

```
void stopNow()
```

Causes the client to shutdown. It is faster than
[`Applet.stop()`](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/applet/Applet.html?is-external=true#stop() "class or interface in java.applet") because it doesn't wait for 4000ms.
This will call [`System.exit(int)`](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/System.html?is-external=true#exit(int) "class or interface in java.lang") when it is done
- #### getLauncherDisplayName

```
@Nullable
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getLauncherDisplayName()
```

Gets the display name of the active account when launched from the Jagex launcher.

Returns:
The active account's display name, or `null` if not launched from the Jagex launcher
- #### getUsername

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getUsername()
```

Deprecated.
DEPRECATED. See getAccountHash instead.
Gets the current logged in username.

Returns:
the logged in username
See Also:
[`OAuthApi.getAccountHash()`](../../../com/jagex/oldscape/pub/OAuthApi.html#getAccountHash())
- #### setUsername

```
void setUsername​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)
```

Sets the current logged in username.

Parameters:
`name` - the logged in username
- #### setPassword

```
void setPassword​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") password)
```

Sets the password on login screen.

Parameters:
`password` - the login screen password
- #### setOtp

```
void setOtp​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") otp)
```

Sets the 6 digit pin used for authenticator on login screen.

Parameters:
`otp` - one time password
- #### getCurrentLoginField

```
int getCurrentLoginField()
```

Gets currently selected login field. 0 is username, and 1 is password.

Returns:
currently selected login field
- #### getLoginIndex

```
int getLoginIndex()
```

Gets index of current login state. 2 is username/password form, 4 is authenticator form

Returns:
current login state index
- #### getAccountType

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
[AccountType](vars/AccountType.html "enum in net.runelite.api.vars") getAccountType()
```

Deprecated.
see Varbits#ACCOUNT\_TYPE

Gets the account type of the logged in player.

Returns:
the account type
- #### getCanvas

```
[Canvas](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Canvas.html?is-external=true "class or interface in java.awt") getCanvas()
```

Description copied from interface: `[GameEngine](GameEngine.html#getCanvas())`
Gets the canvas that contains everything.

Specified by:
`[getCanvas](GameEngine.html#getCanvas())` in interface `[GameEngine](GameEngine.html "interface in net.runelite.api")`
Returns:
the game canvas
- #### getFPS

```
int getFPS()
```

Gets the current FPS (frames per second).

Returns:
the FPS
- #### getCameraX

```
int getCameraX()
```

Gets the x-axis coordinate of the camera.

This value is a local coordinate value similar to
[`getLocalDestinationLocation()`](#getLocalDestinationLocation()).

Returns:
the camera x coordinate
- #### getCameraFpX

```
double getCameraFpX()
```

Floating point camera position, x-axis

Returns:
See Also:
[`getCameraX()`](#getCameraX())
- #### getCameraY

```
int getCameraY()
```

Gets the y-axis coordinate of the camera.

This value is a local coordinate value similar to
[`getLocalDestinationLocation()`](#getLocalDestinationLocation()).

Returns:
the camera y coordinate
- #### getCameraFpY

```
double getCameraFpY()
```

Floating point camera position, y-axis

Returns:
See Also:
[`getCameraY()`](#getCameraY())
- #### getCameraZ

```
int getCameraZ()
```

Gets the z-axis coordinate of the camera.

This value is a local coordinate value similar to
[`getLocalDestinationLocation()`](#getLocalDestinationLocation()).

Returns:
the camera z coordinate
- #### getCameraFpZ

```
double getCameraFpZ()
```

Floating point camera position, z-axis

Returns:
See Also:
[`getCameraZ()`](#getCameraZ())
- #### getCameraPitch

```
int getCameraPitch()
```

Gets the pitch of the camera.

The value returned by this method is measured in JAU, or Jagex
Angle Unit, which is 1/1024 of a revolution.

Returns:
the camera pitch
- #### getCameraFpPitch

```
double getCameraFpPitch()
```

Floating point camera pitch.

Returns:
See Also:
[`getCameraPitch()`](#getCameraPitch())
- #### getCameraYaw

```
int getCameraYaw()
```

Gets the yaw of the camera.

Returns:
the camera yaw
- #### getCameraFpYaw

```
double getCameraFpYaw()
```

Floating point camera yaw

Returns:
See Also:
[`getCameraYaw()`](#getCameraYaw())
- #### getWorld

```
int getWorld()
```

Gets the current world number of the logged in player.

Returns:
the logged in world number
- #### getCanvasHeight

```
int getCanvasHeight()
```

Gets the canvas height

Returns:
- #### getCanvasWidth

```
int getCanvasWidth()
```

Gets the canvas width

Returns:
- #### getViewportHeight

```
int getViewportHeight()
```

Gets the height of the viewport.

Returns:
the viewport height
- #### getViewportWidth

```
int getViewportWidth()
```

Gets the width of the viewport.

Returns:
the viewport width
- #### getViewportXOffset

```
int getViewportXOffset()
```

Gets the x-axis offset of the viewport.

Returns:
the x-axis offset
- #### getViewportYOffset

```
int getViewportYOffset()
```

Gets the y-axis offset of the viewport.

Returns:
the y-axis offset
- #### getScale

```
int getScale()
```

Gets the scale of the world (zoom value).

Returns:
the world scale
- #### getMouseCanvasPosition

```
[Point](Point.html "class in net.runelite.api") getMouseCanvasPosition()
```

Gets the current position of the mouse on the canvas.

Returns:
the mouse canvas position
- #### getLocalPlayer

```
[Player](Player.html "interface in net.runelite.api") getLocalPlayer()
```

Gets the logged in player instance.

Returns:
the logged in player
- #### getFollower

```
@Nullable
[NPC](NPC.html "interface in net.runelite.api") getFollower()
```

Get the local player's follower, such as a pet

Returns:
- #### getItemDefinition

```
@Nonnull
[ItemComposition](ItemComposition.html "interface in net.runelite.api") getItemDefinition​(int id)
```

Gets the item composition corresponding to an items ID.

Parameters:
`id` - the item ID
Returns:
the corresponding item composition
See Also:
`ItemID`
- #### createItemSprite

```
@Nullable
[SpritePixels](SpritePixels.html "interface in net.runelite.api") createItemSprite​(int itemId,
int quantity,
int border,
int shadowColor,
int stackable,
boolean noted,
int scale)
```

Creates an item icon sprite with passed variables.

Parameters:
`itemId` - the item ID
`quantity` - the item quantity
`border` - whether to draw a border
`shadowColor` - the shadow color
`stackable` - whether the item is stackable
`noted` - whether the item is noted
`scale` - the scale of the sprite
Returns:
the created sprite
- #### getItemModelCache

```
[NodeCache](NodeCache.html "interface in net.runelite.api") getItemModelCache()
```

Get the item model cache. These models are used for drawing widgets of type [`WidgetType.MODEL`](widgets/WidgetType.html#MODEL)
and inventory item icons

Returns:
- #### getItemSpriteCache

```
[NodeCache](NodeCache.html "interface in net.runelite.api") getItemSpriteCache()
```

Get the item sprite cache. These are 2d SpritePixels which are used to raster item images on the inventory and
on widgets of type [`WidgetType.GRAPHIC`](widgets/WidgetType.html#GRAPHIC)

Returns:
- #### getSprites

```
@Nullable
[SpritePixels](SpritePixels.html "interface in net.runelite.api")[] getSprites​([IndexDataBase](IndexDataBase.html "interface in net.runelite.api") source,
int archiveId,
int fileId)
```

Loads and creates the sprite images of the passed archive and file IDs.

Parameters:
`source` - the sprite index
`archiveId` - the sprites archive ID
`fileId` - the sprites file ID
Returns:
the sprite image of the file
- #### getIndexSprites

```
[IndexDataBase](IndexDataBase.html "interface in net.runelite.api") getIndexSprites()
```

Gets the sprite index.
- #### getIndexScripts

```
[IndexDataBase](IndexDataBase.html "interface in net.runelite.api") getIndexScripts()
```

Gets the script index.
- #### getIndexConfig

```
[IndexDataBase](IndexDataBase.html "interface in net.runelite.api") getIndexConfig()
```

Gets the config index.
- #### getIndex

```
[IndexDataBase](IndexDataBase.html "interface in net.runelite.api") getIndex​(int id)
```

Gets an index by id
- #### getMouseCurrentButton

```
int getMouseCurrentButton()
```

Gets the current mouse button that is pressed.

Returns:
the pressed mouse button
- #### isDraggingWidget

```
boolean isDraggingWidget()
```

Checks whether a widget is currently being dragged.

Returns:
true if dragging a widget, false otherwise
- #### getDraggedWidget

```
@Nullable
[Widget](widgets/Widget.html "interface in net.runelite.api.widgets") getDraggedWidget()
```

Gets the widget currently being dragged.

Returns:
the dragged widget, null if not dragging any widget
- #### getDraggedOnWidget

```
@Nullable
[Widget](widgets/Widget.html "interface in net.runelite.api.widgets") getDraggedOnWidget()
```

Gets the widget that is being dragged on.

The widget being dragged has the [`WidgetConfig.DRAG`](widgets/WidgetConfig.html#DRAG)
flag set, and is the widget currently under the dragged widget.

Returns:
the dragged on widget, null if not dragging any widget
- #### setDraggedOnWidget

```
void setDraggedOnWidget​([Widget](widgets/Widget.html "interface in net.runelite.api.widgets") widget)
```

Sets the widget that is being dragged on.

Parameters:
`widget` - the new dragged on widget
- #### getDragTime

```
int getDragTime()
```

Get the number of client cycles the current dragged widget
has been dragged for.

Returns:
- #### getTopLevelInterfaceId

```
[@Interface](annotations/Interface.html "annotation in net.runelite.api.annotations")
int getTopLevelInterfaceId()
```

Gets Interface ID of the root widget
- #### getWidgetRoots

```
[Widget](widgets/Widget.html "interface in net.runelite.api.widgets")[] getWidgetRoots()
```

Gets the root widgets.

Returns:
the root widgets
- #### getWidget

```
@Nullable
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
[Widget](widgets/Widget.html "interface in net.runelite.api.widgets") getWidget​([WidgetInfo](widgets/WidgetInfo.html "enum in net.runelite.api.widgets") widget)
```

Deprecated.
Gets a widget corresponding to the passed widget info.

Parameters:
`widget` - the widget info
Returns:
the widget
- #### getWidget

```
@Nullable
[Widget](widgets/Widget.html "interface in net.runelite.api.widgets") getWidget​([@Interface](annotations/Interface.html "annotation in net.runelite.api.annotations")
int groupId,
int childId)
```

Gets a widget by its raw group ID and child ID.

Parameters:
`groupId` - the group ID
`childId` - the child widget ID
Returns:
the widget corresponding to the group and child pair
- #### getWidget

```
@Nullable
[Widget](widgets/Widget.html "interface in net.runelite.api.widgets") getWidget​([@Component](annotations/Component.html "annotation in net.runelite.api.annotations")
int componentId)
```

Gets a widget by its component id.

Parameters:
`componentId` - the component id
- #### getWidgetPositionsX

```
int[] getWidgetPositionsX()
```

Gets an array containing the x-axis canvas positions
of all widgets.

Returns:
array of x-axis widget coordinates
- #### getWidgetPositionsY

```
int[] getWidgetPositionsY()
```

Gets an array containing the y-axis canvas positions
of all widgets.

Returns:
array of y-axis widget coordinates
- #### getEnergy

```
int getEnergy()
```

Gets the current run energy of the logged in player.

Returns:
the run energy in units of 1/100th of an percentage
- #### getWeight

```
int getWeight()
```

Gets the current weight of the logged in player.

Returns:
the weight
- #### getPlayerOptions

```
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")[] getPlayerOptions()
```

Gets an array of options that can currently be used on other players.

For example, if the player is in a PVP area the "Attack" option
will become available in the array. Otherwise, it won't be there.

Returns:
an array of options
- #### getPlayerOptionsPriorities

```
boolean[] getPlayerOptionsPriorities()
```

Gets an array of whether an option is enabled or not.

Returns:
the option priorities
- #### getPlayerMenuTypes

```
int[] getPlayerMenuTypes()
```

Gets an array of player menu types.

Returns:
the player menu types
- #### getWorldList

```
[World](World.html "interface in net.runelite.api")[] getWorldList()
```

Gets a list of all RuneScape worlds.

Returns:
world list
- #### getMenu

```
@Nonnull
[Menu](Menu.html "interface in net.runelite.api") getMenu()
```

Get the client menu.
- #### createMenuEntry

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
[MenuEntry](MenuEntry.html "interface in net.runelite.api") createMenuEntry​(int idx)
```

Deprecated.
Create a new menu entry

Parameters:
`idx` - the index to create the menu entry at. Accepts negative indexes eg. -1 inserts at the end.
Returns:
the newly created menu entry
See Also:
[`getMenu()`](#getMenu()),
[`Menu.createMenuEntry(int)`](Menu.html#createMenuEntry(int))
- #### getMenuEntries

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
[MenuEntry](MenuEntry.html "interface in net.runelite.api")[] getMenuEntries()
```

Deprecated.
Gets an array of currently open right-click menu entries that can be
clicked and activated.

Returns:
array of open menu entries
See Also:
[`getMenu()`](#getMenu()),
[`Menu.getMenuEntries()`](Menu.html#getMenuEntries())
- #### setMenuEntries

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
void setMenuEntries​([MenuEntry](MenuEntry.html "interface in net.runelite.api")[] entries)
```

Deprecated.
Sets the array of open menu entries.

This method should typically be used in the context of the [`MenuOpened`](events/MenuOpened.html "class in net.runelite.api.events")
event, since setting the menu entries will be overwritten the next frame

Parameters:
`entries` - new array of open menu entries
See Also:
[`getMenu()`](#getMenu()),
[`Menu.setMenuEntries(MenuEntry[])`](Menu.html#setMenuEntries(net.runelite.api.MenuEntry%5B%5D))
- #### isMenuOpen

```
boolean isMenuOpen()
```

Checks whether a right-click menu is currently open.

Returns:
true if a menu is open, false otherwise
- #### isMenuScrollable

```
boolean isMenuScrollable()
```

Returns whether the currently open menu is scrollable.

Returns:
- #### getMenuScroll

```
int getMenuScroll()
```

Get the number of entries the currently open menu has been scrolled down.

Returns:
- #### setMenuScroll

```
void setMenuScroll​(int scroll)
```

Set the number of entries the currently open menu has been scrolled down.

Parameters:
`scroll` -
- #### getMenuX

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
int getMenuX()
```

Deprecated.
Get the menu x location. Only valid if the menu is open.

Returns:
the menu x location
See Also:
[`Menu.getMenuX()`](Menu.html#getMenuX())
- #### getMenuY

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
int getMenuY()
```

Deprecated.
Get the menu y location. Only valid if the menu is open.

Returns:
the menu y location
See Also:
[`Menu.getMenuY()`](Menu.html#getMenuY())
- #### getMenuHeight

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
int getMenuHeight()
```

Deprecated.
Get the menu height. Only valid if the menu is open.

Returns:
the menu height
See Also:
[`Menu.getMenuHeight()`](Menu.html#getMenuHeight())
- #### getMenuWidth

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
int getMenuWidth()
```

Deprecated.
Get the menu width. Only valid if the menu is open.

Returns:
the menu width
See Also:
[`Menu.getMenuWidth()`](Menu.html#getMenuWidth())
- #### getMapAngle

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
int getMapAngle()
```

Deprecated.
Gets the angle of the map, or target camera yaw.

Returns:
the map angle
See Also:
[`getCameraYawTarget()`](#getCameraYawTarget())
- #### isResized

```
boolean isResized()
```

Checks whether the client window is currently resized.

Returns:
true if resized, false otherwise
- #### getRevision

```
int getRevision()
```

Gets the client revision number.

Returns:
the revision
- #### getVarps

```
[@VisibleForDevtools](annotations/VisibleForDevtools.html "annotation in net.runelite.api.annotations")
int[] getVarps()
```

Gets an array of all client varplayers.

Returns:
local player variables
- #### getServerVarps

```
[@VisibleForDevtools](annotations/VisibleForDevtools.html "annotation in net.runelite.api.annotations")
int[] getServerVarps()
```

Get an array of all server varplayers. These vars are only
modified by the server, and so represent the server's idea of
the varp values.

Returns:
the server varps
- #### getVarcMap

```
[@VisibleForDevtools](annotations/VisibleForDevtools.html "annotation in net.runelite.api.annotations")
[Map](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Map.html?is-external=true "class or interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Integer.html?is-external=true "class or interface in java.lang"),​[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")> getVarcMap()
```

Gets an array of all client variables.
- #### getVar

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
int getVar​([@Varbit](annotations/Varbit.html "annotation in net.runelite.api.annotations")
int varbit)
```

Deprecated.
Gets a value corresponding to the passed varbit.

Parameters:
`varbit` - the varbit id
Returns:
the value
See Also:
[`getVarbitValue(int)`](#getVarbitValue(int))
- #### getVarbitValue

```
int getVarbitValue​([@Varbit](annotations/Varbit.html "annotation in net.runelite.api.annotations")
int varbit)
```

Gets the value of the given varbit.

Parameters:
`varbit` - the varbit id
Returns:
the value
- #### getServerVarbitValue

```
int getServerVarbitValue​([@Varbit](annotations/Varbit.html "annotation in net.runelite.api.annotations")
int varbit)
```

Gets the value of the given varbit.
This returns the server's idea of the value, not the client's. This is
specifically the last value set by the server regardless of changes to
the var by the client.

Parameters:
`varbit` - the varbit id
Returns:
the value
- #### getVarpValue

```
int getVarpValue​([@Varp](annotations/Varp.html "annotation in net.runelite.api.annotations")
int varpId)
```

Gets the value of a given VarPlayer.

Parameters:
`varpId` - the VarPlayer id
Returns:
the value
- #### getServerVarpValue

```
int getServerVarpValue​([@Varp](annotations/Varp.html "annotation in net.runelite.api.annotations")
int varpId)
```

Gets the value of a given VarPlayer.
This returns the server's idea of the value, not the client's. This is
specifically the last value set by the server regardless of changes to
the var by the client.

Parameters:
`varpId` - the VarPlayer id
Returns:
the value
- #### getVarcIntValue

```
int getVarcIntValue​([@VarCInt](annotations/VarCInt.html "annotation in net.runelite.api.annotations")
int var)
```

Gets the value of a given VarClientInt

Parameters:
`var` - the `VarClientID`
Returns:
the value
- #### getVarcStrValue

```
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getVarcStrValue​([@VarCStr](annotations/VarCStr.html "annotation in net.runelite.api.annotations")
int var)
```

Gets the value of a given VarClientStr

Parameters:
`var` - the `VarClientID`
Returns:
the value
- #### setVarcStrValue

```
void setVarcStrValue​([@VarCStr](annotations/VarCStr.html "annotation in net.runelite.api.annotations")
int var,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") value)
```

Sets a VarClientString to the passed value

Parameters:
`var` - the `VarClientID`
`value` - the new value
- #### setVarcIntValue

```
void setVarcIntValue​([@VarCInt](annotations/VarCInt.html "annotation in net.runelite.api.annotations")
int var,
int value)
```

Sets a VarClientInt to the passed value

Parameters:
`var` - the `VarClientID`
`value` - the new value
- #### setVarbit

```
void setVarbit​([@Varbit](annotations/Varbit.html "annotation in net.runelite.api.annotations")
int varbit,
int value)
```

Sets the value of a varbit

Parameters:
`varbit` - the varbit id
`value` - the new value
- #### getVarbit

```
[@VisibleForDevtools](annotations/VisibleForDevtools.html "annotation in net.runelite.api.annotations")
@Nullable
[VarbitComposition](VarbitComposition.html "interface in net.runelite.api") getVarbit​(int id)
```

Gets the varbit composition for a given varbit id

Parameters:
`id` -
Returns:
- #### getVarbitValue

```
[@VisibleForDevtools](annotations/VisibleForDevtools.html "annotation in net.runelite.api.annotations")
int getVarbitValue​(int[] varps,
[@Varbit](annotations/Varbit.html "annotation in net.runelite.api.annotations")
int varbitId)
```

Gets the value of a given variable.

Parameters:
`varps` - passed varbits
`varbitId` - the variable ID
Returns:
the value
See Also:
`VarbitID`
- #### setVarbitValue

```
[@VisibleForDevtools](annotations/VisibleForDevtools.html "annotation in net.runelite.api.annotations")
void setVarbitValue​(int[] varps,
[@Varbit](annotations/Varbit.html "annotation in net.runelite.api.annotations")
int varbit,
int value)
```

Sets the value of a given variable.

Parameters:
`varps` - passed varbits
`varbit` - the variable
`value` - the value
See Also:
`VarbitID`
- #### queueChangedVarp

```
void queueChangedVarp​([@Varp](annotations/Varp.html "annotation in net.runelite.api.annotations")
int varp)
```

Mark the given varp as changed, causing var listeners to be
triggered next tick

Parameters:
`varp` -
- #### openInterface

```
[WidgetNode](WidgetNode.html "interface in net.runelite.api") openInterface​(int componentId,
int interfaceId,
int modalMode)
```

Open an interface.

Parameters:
`componentId` - component id to open the interface at
`interfaceId` - the interface to open
`modalMode` - see [`WidgetModalMode`](widgets/WidgetModalMode.html "class in net.runelite.api.widgets")
Returns:
the [`WidgetNode`](WidgetNode.html "interface in net.runelite.api") for the interface. This should be closed later by calling
{[`closeInterface(WidgetNode, boolean)`](#closeInterface(net.runelite.api.WidgetNode,boolean)).
Throws:
`[IllegalStateException](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/IllegalStateException.html?is-external=true "class or interface in java.lang")` - if the component does not exist or it not a layer, or the interface is already
open on a different component
- #### closeInterface

```
void closeInterface​([WidgetNode](WidgetNode.html "interface in net.runelite.api") interfaceNode,
boolean unload)
```

Close an interface

Parameters:
`interfaceNode` - the [`WidgetNode`](WidgetNode.html "interface in net.runelite.api") linking the interface into the component tree
`unload` - whether to null the client's widget table
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/IllegalArgumentException.html?is-external=true "class or interface in java.lang")` - if the interfaceNode is not linked into the component tree
- #### getWidgetFlags

```
[HashTable](HashTable.html "interface in net.runelite.api")<[WidgetConfigNode](widgets/WidgetConfigNode.html "interface in net.runelite.api.widgets")> getWidgetFlags()
```

Gets the widget flags table.

Returns:
the widget flags table
- #### getWidgetConfig

```
@Nullable
[WidgetConfigNode](widgets/WidgetConfigNode.html "interface in net.runelite.api.widgets") getWidgetConfig​([Widget](widgets/Widget.html "interface in net.runelite.api.widgets") w)
```

Get the widget config for a given widget

Parameters:
`w` -
Returns:
- #### getComponentTable

```
[HashTable](HashTable.html "interface in net.runelite.api")<[WidgetNode](WidgetNode.html "interface in net.runelite.api")> getComponentTable()
```

Gets the widget node component table.

Returns:
the widget node component table
See Also:
[`WidgetNode`](WidgetNode.html "interface in net.runelite.api")
- #### getGrandExchangeOffers

```
[GrandExchangeOffer](GrandExchangeOffer.html "interface in net.runelite.api")[] getGrandExchangeOffers()
```

Gets an array of current grand exchange offers.

Returns:
all grand exchange offers
- #### isPrayerActive

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
boolean isPrayerActive​([Prayer](Prayer.html "enum in net.runelite.api") prayer)
```

Deprecated.
this method does not properly handle deadeye/eagle eye or mystic vigour/might

Checks whether or not a prayer is currently active.

Parameters:
`prayer` - the prayer
Returns:
true if the prayer is active, false otherwise
- #### getSkillExperience

```
int getSkillExperience​([Skill](Skill.html "enum in net.runelite.api") skill)
```

Gets the current experience towards a skill.

Parameters:
`skill` - the skill
Returns:
the experience
- #### getOverallExperience

```
long getOverallExperience()
```

Get the total experience of the player

Returns:
- #### refreshChat

```
void refreshChat()
```

Refreshes the chat.
- #### getChatLineMap

```
[Map](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Map.html?is-external=true "class or interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Integer.html?is-external=true "class or interface in java.lang"),​[ChatLineBuffer](ChatLineBuffer.html "interface in net.runelite.api")> getChatLineMap()
```

Gets the map of chat buffers.

Returns:
the chat buffers
- #### getMessages

```
[IterableHashTable](IterableHashTable.html "interface in net.runelite.api")<[MessageNode](MessageNode.html "interface in net.runelite.api")> getMessages()
```

Map of message node id to message node

Returns:
the map
- #### getObjectDefinition

```
[ObjectComposition](ObjectComposition.html "interface in net.runelite.api") getObjectDefinition​(int objectId)
```

Gets the object composition corresponding to an objects ID.

Parameters:
`objectId` - the object ID
Returns:
the corresponding object composition
See Also:
`ObjectID`
- #### getNpcDefinition

```
[NPCComposition](NPCComposition.html "interface in net.runelite.api") getNpcDefinition​(int npcId)
```

Gets the NPC composition corresponding to an NPCs ID.

Parameters:
`npcId` - the npc ID
Returns:
the corresponding NPC composition
See Also:
`NpcID`
- #### getStructComposition

```
[StructComposition](StructComposition.html "interface in net.runelite.api") getStructComposition​(int structID)
```

Gets the [`StructComposition`](StructComposition.html "interface in net.runelite.api") for a given struct ID

See Also:
[`StructID`](StructID.html "class in net.runelite.api")
- #### getStructCompositionCache

```
[NodeCache](NodeCache.html "interface in net.runelite.api") getStructCompositionCache()
```

Gets the client's cache of in memory struct compositions
- #### getDBTableField

```
[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")[] getDBTableField​(int rowID,
int column,
int tupleIndex)
```

Gets a entry out of a DBTable Row
- #### getDBRowConfig

```
[DBRowConfig](dbtable/DBRowConfig.html "interface in net.runelite.api.dbtable") getDBRowConfig​(int rowID)
```
- #### getDBRowsByValue

```
[List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html?is-external=true "class or interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Integer.html?is-external=true "class or interface in java.lang")> getDBRowsByValue​(int table,
int column,
int tupleIndex,
[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang") value)
```

Uses an index to find rows containing a certain value in a column.
An index must exist for this column.
- #### getDBTableRows

```
[List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html?is-external=true "class or interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Integer.html?is-external=true "class or interface in java.lang")> getDBTableRows​(int table)
```

Gets all rows in a DBTable
- #### getMapElementConfig

```
[MapElementConfig](worldmap/MapElementConfig.html "interface in net.runelite.api.worldmap") getMapElementConfig​(int id)
```

Get a map element config by id

Parameters:
`id` - the id
- #### getMapScene

```
[IndexedSprite](IndexedSprite.html "interface in net.runelite.api")[] getMapScene()
```

Gets a sprite of the map scene

Returns:
the sprite
- #### getMapDots

```
[SpritePixels](SpritePixels.html "interface in net.runelite.api")[] getMapDots()
```

Gets an array of currently drawn mini-map dots.

Returns:
all mini-map dots
- #### getGameCycle

```
int getGameCycle()
```

Gets the local clients game cycle.

Note: This value is incremented every 20ms.

Returns:
the game cycle
- #### getMapIcons

```
[SpritePixels](SpritePixels.html "interface in net.runelite.api")[] getMapIcons()
```

Gets an array of current map icon sprites.

Returns:
the map icons
- #### getModIcons

```
[IndexedSprite](IndexedSprite.html "interface in net.runelite.api")[] getModIcons()
```

Gets an array of mod icon sprites.

Returns:
the mod icons
- #### setModIcons

```
void setModIcons​([IndexedSprite](IndexedSprite.html "interface in net.runelite.api")[] modIcons)
```

Replaces the current mod icons with a new array.

Parameters:
`modIcons` - the new mod icons
- #### createIndexedSprite

```
[IndexedSprite](IndexedSprite.html "interface in net.runelite.api") createIndexedSprite()
```

Creates an empty indexed sprite.

Returns:
the sprite
- #### createSpritePixels

```
[SpritePixels](SpritePixels.html "interface in net.runelite.api") createSpritePixels​(int[] pixels,
int width,
int height)
```

Creates a sprite image with given width and height containing the
pixels.

Parameters:
`pixels` - the pixels
`width` - the width
`height` - the height
Returns:
the sprite image
- #### getLocalDestinationLocation

```
@Nullable
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") getLocalDestinationLocation()
```

Gets the location of the local player.

Returns:
the local player location
- #### createRuneLiteObject

```
[RuneLiteObject](RuneLiteObject.html "class in net.runelite.api") createRuneLiteObject()
```

Creates a RuneLiteObject, which is a modified [`GraphicsObject`](GraphicsObject.html "interface in net.runelite.api")
- #### registerRuneLiteObject

```
void registerRuneLiteObject​([RuneLiteObjectController](RuneLiteObjectController.html "class in net.runelite.api") controller)
```

Registers a new [`RuneLiteObjectController`](RuneLiteObjectController.html "class in net.runelite.api") to its corresponding [`WorldView`](WorldView.html "interface in net.runelite.api").
- #### removeRuneLiteObject

```
void removeRuneLiteObject​([RuneLiteObjectController](RuneLiteObjectController.html "class in net.runelite.api") controller)
```

Removes a new [`RuneLiteObjectController`](RuneLiteObjectController.html "class in net.runelite.api") from its corresponding [`WorldView`](WorldView.html "interface in net.runelite.api").
- #### isRuneLiteObjectRegistered

```
boolean isRuneLiteObjectRegistered​([RuneLiteObjectController](RuneLiteObjectController.html "class in net.runelite.api") controller)
```

Checks whether a [`RuneLiteObjectController`](RuneLiteObjectController.html "class in net.runelite.api") is registered to any [`WorldView`](WorldView.html "interface in net.runelite.api").
- #### loadModelData

```
@Nullable
[ModelData](ModelData.html "interface in net.runelite.api") loadModelData​(int id)
```

Loads an unlit model from the cache. The returned model shares
data such as faces, face colors, face transparencies, and vertex points with
other models. If you want to mutate these you MUST call the relevant `cloneX`
method.

Parameters:
`id` - the ID of the model
Returns:
the model or null if it is loading or nonexistent
See Also:
[`ModelData.cloneColors()`](ModelData.html#cloneColors())
- #### mergeModels

```
[ModelData](ModelData.html "interface in net.runelite.api") mergeModels​([ModelData](ModelData.html "interface in net.runelite.api")[] models,
int length)
```
- #### mergeModels

```
[ModelData](ModelData.html "interface in net.runelite.api") mergeModels​([ModelData](ModelData.html "interface in net.runelite.api")... models)
```
- #### mergeModels

```
[Model](Model.html "interface in net.runelite.api") mergeModels​([Model](Model.html "interface in net.runelite.api")[] models,
int length)
```
- #### mergeModels

```
[Model](Model.html "interface in net.runelite.api") mergeModels​([Model](Model.html "interface in net.runelite.api")... models)
```
- #### loadModel

```
@Nullable
[Model](Model.html "interface in net.runelite.api") loadModel​(int id)
```

Loads and lights a model from the cache

This is equivalent to `loadModelData(id).light()`

Parameters:
`id` - the ID of the model
Returns:
the model or null if it is loading or nonexistent
- #### loadModel

```
@Nullable
[Model](Model.html "interface in net.runelite.api") loadModel​(int id,
short[] colorToFind,
short[] colorToReplace)
```

Loads a model from the cache and also recolors it

Parameters:
`id` - the ID of the model
`colorToFind` - array of hsl color values to find in the model to replace
`colorToReplace` - array of hsl color values to replace in the model
Returns:
the model or null if it is loading or nonexistent
- #### loadAnimation

```
[Animation](Animation.html "interface in net.runelite.api") loadAnimation​(int id)
```

Loads an animation from the cache

Parameters:
`id` - the ID of the animation. Any int is allowed, but implementations in the client
should be defined in `AnimationID`
- #### getMusicVolume

```
int getMusicVolume()
```

Gets the music volume

Returns:
volume 0-255 inclusive
- #### setMusicVolume

```
void setMusicVolume​(int volume)
```

Sets the music volume

Parameters:
`volume` - 0-255 inclusive
- #### playSoundEffect

```
void playSoundEffect​(int id)
```

Play a sound effect at the player's current location. This is how UI,
and player-generated (e.g. mining, woodcutting) sound effects are
normally played.

Parameters:
`id` - the ID of the sound to play. Any int is allowed, but see
[`SoundEffectID`](SoundEffectID.html "class in net.runelite.api") for some common ones
- #### playSoundEffect

```
void playSoundEffect​(int id,
int x,
int y,
int range)
```

Play a sound effect from some point in the world.

Parameters:
`id` - the ID of the sound to play. Any int is allowed, but see
[`SoundEffectID`](SoundEffectID.html "class in net.runelite.api") for some common ones
`x` - the ground coordinate on the x axis
`y` - the ground coordinate on the y axis
`range` - the number of tiles away that the sound can be heard
from
- #### playSoundEffect

```
void playSoundEffect​(int id,
int x,
int y,
int range,
int delay)
```

Play a sound effect from some point in the world.

Parameters:
`id` - the ID of the sound to play. Any int is allowed, but see
[`SoundEffectID`](SoundEffectID.html "class in net.runelite.api") for some common ones
`x` - the ground coordinate on the x axis
`y` - the ground coordinate on the y axis
`range` - the number of tiles away that the sound can be heard
from
`delay` - the amount of frames before the sound starts playing
- #### playSoundEffect

```
void playSoundEffect​(int id,
int volume)
```

Plays a sound effect, even if the player's sound effect volume is muted.

Parameters:
`id` - the ID of the sound effect - [`SoundEffectID`](SoundEffectID.html "class in net.runelite.api")
`volume` - the volume to play the sound effect at, see [`SoundEffectVolume`](SoundEffectVolume.html "class in net.runelite.api") for values used
in the settings interface. if the sound effect volume is not muted, uses the set volume
- #### getActiveMidiRequests

```
[List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html?is-external=true "class or interface in java.util")<[MidiRequest](MidiRequest.html "interface in net.runelite.api")> getActiveMidiRequests()
```

Get the currently playing midi requests.

Returns:
- #### getBufferProvider

```
[BufferProvider](BufferProvider.html "interface in net.runelite.api") getBufferProvider()
```

Gets the clients graphic buffer provider.

Returns:
the buffer provider
- #### getMouseIdleTicks

```
int getMouseIdleTicks()
```

Gets the amount of client ticks since the last mouse movement occurred.

Returns:
amount of idle mouse ticks
See Also:
[`Constants.CLIENT_TICK_LENGTH`](Constants.html#CLIENT_TICK_LENGTH)
- #### getMouseLastPressedMillis

```
long getMouseLastPressedMillis()
```

Gets the time at which the last mouse press occurred in milliseconds since
the UNIX epoch.
- #### getKeyboardIdleTicks

```
int getKeyboardIdleTicks()
```

Gets the amount of client ticks since the last keyboard press occurred.

Returns:
amount of idle keyboard ticks
See Also:
[`Constants.CLIENT_TICK_LENGTH`](Constants.html#CLIENT_TICK_LENGTH)
- #### changeMemoryMode

```
void changeMemoryMode​(boolean lowMemory)
```

Changes how game behaves based on memory mode. Low memory mode skips
drawing of all floors and renders ground textures in low quality.

Parameters:
`lowMemory` - if we are running in low memory mode or not
- #### getItemContainer

```
@Nullable
[ItemContainer](ItemContainer.html "interface in net.runelite.api") getItemContainer​([InventoryID](InventoryID.html "enum in net.runelite.api") inventory)
```

Get the item container for an inventory.

Parameters:
`inventory` - the inventory type
Returns:
the item container
See Also:
`InventoryID`
- #### getItemContainer

```
@Nullable
[ItemContainer](ItemContainer.html "interface in net.runelite.api") getItemContainer​(int id)
```

Get an item container by id

Parameters:
`id` - the inventory id
Returns:
the item container
See Also:
`InventoryID`
- #### getItemContainers

```
[HashTable](HashTable.html "interface in net.runelite.api")<[ItemContainer](ItemContainer.html "interface in net.runelite.api")> getItemContainers()
```

Get all item containers

Returns:
- #### getIntStackSize

```
int getIntStackSize()
```

Gets the length of the cs2 vm's int stack
- #### setIntStackSize

```
void setIntStackSize​(int stackSize)
```

Sets the length of the cs2 vm's int stack
- #### getIntStack

```
int[] getIntStack()
```

Gets the cs2 vm's int stack
- #### getObjectStackSize

```
int getObjectStackSize()
```

Gets the length of the cs2 vm's object stack
- #### setObjectStackSize

```
void setObjectStackSize​(int stackSize)
```

Sets the length of the cs2 vm's object stack
- #### getObjectStack

```
[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")[] getObjectStack()
```

Gets the cs2 vm's object stack
- #### getArraySizes

```
int getArraySizes​(int arrayId)
```

Get the size of one of the cs2 vm's arrays.

Parameters:
`arrayId` - the array id
Returns:
- #### getArray

```
int[] getArray​(int arrayId)
```

Get one of the cs2 vm's arrays. Use [`getArraySizes(int)`](#getArraySizes(int)) to get
the array length.

Parameters:
`arrayId` - the array id
Returns:
- #### getScriptActiveWidget

```
[Widget](widgets/Widget.html "interface in net.runelite.api.widgets") getScriptActiveWidget()
```

Gets the cs2 vm's active widget

This is used for all `cc_*` operations with a `0` operand
- #### getScriptDotWidget

```
[Widget](widgets/Widget.html "interface in net.runelite.api.widgets") getScriptDotWidget()
```

Gets the cs2 vm's "dot" widget

This is used for all `.cc_*` operations with a `1` operand
- #### isFriended

```
boolean isFriended​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name,
boolean mustBeLoggedIn)
```

Checks whether a player is on the friends list.

Parameters:
`name` - the name of the player
`mustBeLoggedIn` - if they player is online
Returns:
true if the player is friends
- #### getFriendsChatManager

```
@Nullable
[FriendsChatManager](FriendsChatManager.html "interface in net.runelite.api") getFriendsChatManager()
```

Retrieve the friends chat manager

Returns:
- #### getFriendContainer

```
[FriendContainer](FriendContainer.html "interface in net.runelite.api") getFriendContainer()
```

Retrieve the nameable container containing friends

Returns:
- #### getIgnoreContainer

```
[NameableContainer](NameableContainer.html "interface in net.runelite.api")<[Ignore](Ignore.html "interface in net.runelite.api")> getIgnoreContainer()
```

Retrieve the nameable container containing ignores

Returns:
- #### getPreferences

```
[Preferences](Preferences.html "interface in net.runelite.api") getPreferences()
```

Gets the clients saved preferences.

Returns:
the client preferences
- #### getCameraYawTarget

```
int getCameraYawTarget()
```

Get the target camera yaw.
The target yaw is the yaw the camera should use based on player input.
The actual camera yaw, from [`getCameraYaw()`](#getCameraYaw()), is what the camera
is actually using, which can be overridden by eg. cutscenes.

Returns:
the target camera yaw
- #### getCameraPitchTarget

```
int getCameraPitchTarget()
```

Get the target camera pitch
The target pitch is the pitch the camera should use based on player input.
The actual camera pitch, from [`getCameraPitch()`](#getCameraPitch()) ()}, is what the camera
is actually using, which can be overridden by eg. cutscenes.

Returns:
the target camera pitch
- #### setCameraYawTarget

```
void setCameraYawTarget​(int cameraYawTarget)
```

Set the target camera yaw

Parameters:
`cameraYawTarget` - target camera yaw
- #### setCameraPitchTarget

```
void setCameraPitchTarget​(int cameraPitchTarget)
```

Set the target camera pitch

Parameters:
`cameraPitchTarget` - target camera pitch
- #### setCameraSpeed

```
void setCameraSpeed​(float speed)
```

Sets the camera speed

Parameters:
`speed` -
- #### setCameraMouseButtonMask

```
void setCameraMouseButtonMask​(int mask)
```

Sets the mask for which mouse buttons control the camera.
Use 0 for the default behavior of mouse button 4 if "middle mouse moves camera" is on.

Parameters:
`mask` -
- #### setCameraPitchRelaxerEnabled

```
void setCameraPitchRelaxerEnabled​(boolean enabled)
```

Sets whether the camera pitch can exceed the normal limits set
by the RuneScape client.

Parameters:
`enabled` - new camera pitch relaxer value
- #### setInvertYaw

```
void setInvertYaw​(boolean invertYaw)
```

Sets if the moving the camera horizontally should be backwards
- #### setInvertPitch

```
void setInvertPitch​(boolean invertPitch)
```

Sets if the moving the camera vertically should be backwards
- #### getRenderOverview

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
[RenderOverview](RenderOverview.html "interface in net.runelite.api") getRenderOverview()
```

Deprecated.
Gets the world map overview.

Returns:
the world map overview
See Also:
[`getWorldMap()`](#getWorldMap())
- #### getWorldMap

```
[WorldMap](worldmap/WorldMap.html "interface in net.runelite.api.worldmap") getWorldMap()
```

Get the world map
- #### isStretchedEnabled

```
boolean isStretchedEnabled()
```

Checks whether the client is in stretched mode.

Returns:
true if the client is in stretched mode, false otherwise
- #### setStretchedEnabled

```
void setStretchedEnabled​(boolean state)
```

Sets the client stretched mode state.

Parameters:
`state` - new stretched mode state
- #### isStretchedFast

```
boolean isStretchedFast()
```

Checks whether the client is using fast
rendering techniques when stretching the canvas.

Returns:
true if stretching is fast rendering, false otherwise
- #### setStretchedFast

```
void setStretchedFast​(boolean state)
```

Sets whether to use fast rendering techniques
when stretching the canvas.

Parameters:
`state` - new fast rendering state
- #### setStretchedIntegerScaling

```
void setStretchedIntegerScaling​(boolean state)
```

Sets whether to force integer scale factor by rounding scale
factors towards `zero` when stretching.

Parameters:
`state` - new integer scaling state
- #### setStretchedKeepAspectRatio

```
void setStretchedKeepAspectRatio​(boolean state)
```

Sets whether to keep aspect ratio when stretching.

Parameters:
`state` - new keep aspect ratio state
- #### setScalingFactor

```
void setScalingFactor​(int factor)
```

Sets the scaling factor when scaling resizable mode.

Parameters:
`factor` - new scaling factor
- #### invalidateStretching

```
void invalidateStretching​(boolean resize)
```

Invalidates cached dimensions that are
used for stretching and scaling.

Parameters:
`resize` - true to tell the game to
resize the canvas on the next frame,
false otherwise.
- #### getStretchedDimensions

```
[Dimension](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Dimension.html?is-external=true "class or interface in java.awt") getStretchedDimensions()
```

Gets the current stretched dimensions of the client.

Returns:
the stretched dimensions
- #### getRealDimensions

```
[Dimension](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Dimension.html?is-external=true "class or interface in java.awt") getRealDimensions()
```

Gets the real dimensions of the client before being stretched.

Returns:
the real dimensions
- #### changeWorld

```
void changeWorld​([World](World.html "interface in net.runelite.api") world)
```

Changes the selected world to log in to.

Note: this method will have no effect unless [`GameState`](GameState.html "enum in net.runelite.api")
is [`GameState.LOGIN_SCREEN`](GameState.html#LOGIN_SCREEN).

Parameters:
`world` - the world to switch to
- #### createWorld

```
[World](World.html "interface in net.runelite.api") createWorld()
```

Creates a new instance of a world.
- #### drawInstanceMap

```
[SpritePixels](SpritePixels.html "interface in net.runelite.api") drawInstanceMap​(int z)
```

Draws an instance map for the current viewed plane.

Parameters:
`z` - the plane
Returns:
the map sprite
- #### runScript

```
void runScript​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")... args)
```

Executes a client script from the cache

This method must be ran on the client thread and is not reentrant

This method is shorthand for `client.createScriptEvent(args).run()`

Parameters:
`args` - the script id, then any additional arguments to execute the script with
See Also:
[`ScriptID`](ScriptID.html "class in net.runelite.api")
- #### createScriptEvent

```
[ScriptEvent](ScriptEvent.html "interface in net.runelite.api") createScriptEvent​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")... args)
```

Creates a blank ScriptEvent for executing a ClientScript2 script

Parameters:
`args` - the script id, then any additional arguments to execute the script with
See Also:
[`ScriptID`](ScriptID.html "class in net.runelite.api")
- #### hasHintArrow

```
boolean hasHintArrow()
```

Checks whether or not there is any active hint arrow.

Returns:
true if there is a hint arrow, false otherwise
- #### getHintArrowType

```
int getHintArrowType()
```

Gets the type of hint arrow currently displayed.

Returns:
the hint arrow type
- #### clearHintArrow

```
void clearHintArrow()
```

Clears the current hint arrow.
- #### setHintArrow

```
void setHintArrow​([WorldPoint](coords/WorldPoint.html "class in net.runelite.api.coords") point)
```

Sets a hint arrow to point to the passed location.

Parameters:
`point` - the location
- #### setHintArrow

```
void setHintArrow​([LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") point)
```

Sets the hint arrow to the passsed point

Parameters:
`point` -
- #### setHintArrow

```
void setHintArrow​([Player](Player.html "interface in net.runelite.api") player)
```

Sets a hint arrow to point to the passed player.

Parameters:
`player` - the player
- #### setHintArrow

```
void setHintArrow​([NPC](NPC.html "interface in net.runelite.api") npc)
```

Sets a hint arrow to point to the passed NPC.

Parameters:
`npc` - the NPC
- #### getHintArrowPoint

```
[WorldPoint](coords/WorldPoint.html "class in net.runelite.api.coords") getHintArrowPoint()
```

Gets the world point that the hint arrow is directed at.

Returns:
hint arrow target
- #### getHintArrowPlayer

```
[Player](Player.html "interface in net.runelite.api") getHintArrowPlayer()
```

Gets the player that the hint arrow is directed at.

Returns:
hint arrow target
- #### getHintArrowNpc

```
[NPC](NPC.html "interface in net.runelite.api") getHintArrowNpc()
```

Gets the NPC that the hint arrow is directed at.

Returns:
hint arrow target
- #### getAnimationInterpolationFilter

```
[IntPredicate](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/function/IntPredicate.html?is-external=true "class or interface in java.util.function") getAnimationInterpolationFilter()
```
- #### setAnimationInterpolationFilter

```
void setAnimationInterpolationFilter​([IntPredicate](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/function/IntPredicate.html?is-external=true "class or interface in java.util.function") filter)
```
- #### getBoostedSkillLevels

```
[@VisibleForDevtools](annotations/VisibleForDevtools.html "annotation in net.runelite.api.annotations")
int[] getBoostedSkillLevels()
```
- #### getRealSkillLevels

```
[@VisibleForDevtools](annotations/VisibleForDevtools.html "annotation in net.runelite.api.annotations")
int[] getRealSkillLevels()
```
- #### getSkillExperiences

```
[@VisibleForDevtools](annotations/VisibleForDevtools.html "annotation in net.runelite.api.annotations")
int[] getSkillExperiences()
```
- #### queueChangedSkill

```
void queueChangedSkill​([Skill](Skill.html "enum in net.runelite.api") skill)
```
- #### getSpriteOverrides

```
[Map](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Map.html?is-external=true "class or interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Integer.html?is-external=true "class or interface in java.lang"),​[SpritePixels](SpritePixels.html "interface in net.runelite.api")> getSpriteOverrides()
```

Gets a mapping of sprites to override.

The key value in the map corresponds to the ID of the sprite,
and the value the sprite to replace it with.
- #### getWidgetSpriteOverrides

```
[Map](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Map.html?is-external=true "class or interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Integer.html?is-external=true "class or interface in java.lang"),​[SpritePixels](SpritePixels.html "interface in net.runelite.api")> getWidgetSpriteOverrides()
```

Gets a mapping of widget sprites to override.

The key value in the map corresponds to the packed widget ID,
and the value the sprite to replace the widgets sprite with.
- #### setCompass

```
void setCompass​([SpritePixels](SpritePixels.html "interface in net.runelite.api") spritePixels)
```

Sets the compass sprite.

Parameters:
`spritePixels` - the new sprite
- #### getWidgetSpriteCache

```
[NodeCache](NodeCache.html "interface in net.runelite.api") getWidgetSpriteCache()
```

Returns widget sprite cache, to be used with [`getSpriteOverrides()`](#getSpriteOverrides())

Returns:
the cache
- #### getTickCount

```
int getTickCount()
```

Gets the current server tick count.

Returns:
the tick count
- #### setTickCount

```
void setTickCount​(int tickCount)
```

Sets the current server tick count.

Parameters:
`tickCount` - the new tick count
- #### setInventoryDragDelay

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
void setInventoryDragDelay​(int delay)
```

Deprecated.
Sets the inventory drag delay in client game cycles (20ms).

Parameters:
`delay` - the number of game cycles to delay dragging
- #### getWorldHost

```
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getWorldHost()
```

Get the hostname of the current world

Returns:
- #### getWorldType

```
[EnumSet](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/EnumSet.html?is-external=true "class or interface in java.util")<[WorldType](WorldType.html "enum in net.runelite.api")> getWorldType()
```

Gets a set of current world types that apply to the logged in world.

Returns:
the types for current world
- #### getCameraMode

```
int getCameraMode()
```

Get the camera mode

Returns:
0 for normal, 1 for free camera
- #### setCameraMode

```
void setCameraMode​(int mode)
```

Set the camera mode

Parameters:
`mode` - 0 for normal, 1 for free camera
- #### getCameraFocalPointX

```
double getCameraFocalPointX()
```

Get the camera focus point x
Typically this is the player position, but can be other points in cutscenes or in free camera mode.

Returns:
- #### setCameraFocalPointX

```
void setCameraFocalPointX​(double x)
```

Sets the camera focus point x. Requires the [`getCameraMode()`](#getCameraMode()) to be free camera.

Parameters:
`x` -
- #### getCameraFocalPointY

```
double getCameraFocalPointY()
```

Get the camera focus point y
Typically this is the player position, but can be other points in cutscenes or in free camera mode.

Returns:
- #### setCameraFocalPointY

```
void setCameraFocalPointY​(double y)
```

Sets the camera focus point y. Requires the [`getCameraMode()`](#getCameraMode()) to be free camera.

Parameters:
`y` -
- #### getCameraFocalPointZ

```
double getCameraFocalPointZ()
```

Get the camera focus point z
Typically this is the player position, but can be other points in cutscenes or in free camera mode.

Returns:
- #### setCameraFocalPointZ

```
void setCameraFocalPointZ​(double z)
```

Sets the camera focus point z. Requires the [`getCameraMode()`](#getCameraMode()) to be free camera.

Parameters:
`z` -
- #### setFreeCameraSpeed

```
void setFreeCameraSpeed​(int speed)
```

Sets the normal moving speed when using oculus orb (default value is 12)
- #### getOculusOrbState

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
int getOculusOrbState()
```

Deprecated.
Gets the enabled state for the Oculus orb mode
- #### setOculusOrbState

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
void setOculusOrbState​(int state)
```

Deprecated.
Sets the enabled state for the Oculus orb state

Parameters:
`state` - boolean enabled value
- #### setOculusOrbNormalSpeed

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
void setOculusOrbNormalSpeed​(int speed)
```

Deprecated.
Sets the normal moving speed when using oculus orb (default value is 12)
- #### getOculusOrbFocalPointX

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
int getOculusOrbFocalPointX()
```

Deprecated.
Gets local X coord where the camera is pointing when the Oculus orb is active
- #### getOculusOrbFocalPointY

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
int getOculusOrbFocalPointY()
```

Deprecated.
Gets local Y coord where the camera is pointing when the Oculus orb is active
- #### openWorldHopper

```
void openWorldHopper()
```

Opens in-game world hopper interface
- #### hopToWorld

```
void hopToWorld​([World](World.html "interface in net.runelite.api") world)
```

Hops using in-game world hopper widget to another world

Parameters:
`world` - target world to hop to
- #### setSkyboxColor

```
void setSkyboxColor​(int skyboxColor)
```

Sets the RGB color of the skybox
- #### getSkyboxColor

```
int getSkyboxColor()
```

Gets the RGB color of the skybox
- #### isGpu

```
boolean isGpu()
```
- #### setGpuFlags

```
void setGpuFlags​(int gpuflags)
```
- #### setExpandedMapLoading

```
void setExpandedMapLoading​(int chunks)
```
- #### getExpandedMapLoading

```
int getExpandedMapLoading()
```
- #### get3dZoom

```
int get3dZoom()
```
- #### getCenterX

```
int getCenterX()
```
- #### getCenterY

```
int getCenterY()
```
- #### getTextureProvider

```
[TextureProvider](TextureProvider.html "interface in net.runelite.api") getTextureProvider()
```
- #### getRasterizer3D\_clipMidX2

```
int getRasterizer3D_clipMidX2()
```
- #### getRasterizer3D\_clipNegativeMidX

```
int getRasterizer3D_clipNegativeMidX()
```
- #### getRasterizer3D\_clipNegativeMidY

```
int getRasterizer3D_clipNegativeMidY()
```
- #### getRasterizer3D\_clipMidY2

```
int getRasterizer3D_clipMidY2()
```
- #### checkClickbox

```
void checkClickbox​([Projection](Projection.html "interface in net.runelite.api") projection,
[Model](Model.html "interface in net.runelite.api") model,
int orientation,
int x,
int y,
int z,
long hash)
```
- #### isWidgetSelected

```
boolean isWidgetSelected()
```

Is a widget is in target mode?
- #### setWidgetSelected

```
void setWidgetSelected​(boolean selected)
```

Sets if a widget is in target mode
- #### getSelectedWidget

```
@Nullable
[Widget](widgets/Widget.html "interface in net.runelite.api.widgets") getSelectedWidget()
```

Get the selected widget, such as a selected spell or selected item (eg. "Use")

Returns:
the selected widget
- #### getFocusedInputFieldWidget

```
@Nullable
[Widget](widgets/Widget.html "interface in net.runelite.api.widgets") getFocusedInputFieldWidget()
```

Gets the current active [`WidgetType.INPUT_FIELD`](widgets/WidgetType.html#INPUT_FIELD) Widget
- #### getItemCompositionCache

```
[NodeCache](NodeCache.html "interface in net.runelite.api") getItemCompositionCache()
```

Returns client item composition cache
- #### getObjectCompositionCache

```
[NodeCache](NodeCache.html "interface in net.runelite.api") getObjectCompositionCache()
```

Returns client object composition cache

Returns:
- #### getAnimationCache

```
[NodeCache](NodeCache.html "interface in net.runelite.api") getAnimationCache()
```

Returns the client [`Animation`](Animation.html "interface in net.runelite.api") cache
- #### getCrossSprites

```
[SpritePixels](SpritePixels.html "interface in net.runelite.api")[] getCrossSprites()
```

Returns the array of cross sprites that appear and animate when left-clicking
- #### getEnum

```
[EnumComposition](EnumComposition.html "interface in net.runelite.api") getEnum​(int id)
```
- #### draw2010Menu

```
void draw2010Menu​(int alpha)
```

Draws a menu in the 2010 interface style.

Parameters:
`alpha` - background transparency of the menu
- #### drawOriginalMenu

```
void drawOriginalMenu​(int alpha)
```

Draws a menu in the OSRS interface style.

Parameters:
`alpha` - background transparency of the menu
- #### resetHealthBarCaches

```
void resetHealthBarCaches()
```
- #### getItemCount

```
int getItemCount()
```

Returns the max item index + 1 from cache
- #### setAllWidgetsAreOpTargetable

```
void setAllWidgetsAreOpTargetable​(boolean value)
```

Makes all widgets behave as if they are [`WidgetConfig.WIDGET_USE_TARGET`](widgets/WidgetConfig.html#WIDGET_USE_TARGET)
- #### setGeSearchResultCount

```
void setGeSearchResultCount​(int count)
```

Sets the result count for GE search
- #### setGeSearchResultIds

```
void setGeSearchResultIds​(short[] ids)
```

Sets the array of item ids for GE search
- #### setGeSearchResultIndex

```
void setGeSearchResultIndex​(int index)
```

Sets the starting index in the item id array for GE search
- #### setLoginScreen

```
void setLoginScreen​([SpritePixels](SpritePixels.html "interface in net.runelite.api") pixels)
```

Sets the image to be used for the login screen, provided as SpritePixels
If the image is larger than half the width of fixed mode,
it won't get mirrored to the other side of the screen
- #### setShouldRenderLoginScreenFire

```
void setShouldRenderLoginScreenFire​(boolean val)
```

Sets whether the flames on the login screen should be rendered
- #### isKeyPressed

```
boolean isKeyPressed​(int keycode)
```

Test if a key is pressed

Parameters:
`keycode` - the keycode
Returns:
See Also:
[`KeyCode`](KeyCode.html "class in net.runelite.api")
- #### getCrossWorldMessageIds

```
long[] getCrossWorldMessageIds()
```

Get the list of message ids for the recently received cross-world messages. The upper 32 bits of the
id is the world id, the lower is a sequence number per-world.

Returns:
- #### getCrossWorldMessageIdsIndex

```
int getCrossWorldMessageIdsIndex()
```

Get the index of the next message to be inserted in the cross world message id list

Returns:
- #### getClanChannel

```
@Nullable
[ClanChannel](clan/ClanChannel.html "interface in net.runelite.api.clan") getClanChannel()
```

Get the primary clan channel the player is in.

Returns:
- #### getGuestClanChannel

```
@Nullable
[ClanChannel](clan/ClanChannel.html "interface in net.runelite.api.clan") getGuestClanChannel()
```

Get the guest clan channel the player is in.

Returns:
- #### getClanSettings

```
@Nullable
[ClanSettings](clan/ClanSettings.html "interface in net.runelite.api.clan") getClanSettings()
```

Get clan settings for the clan the user is in.

Returns:
- #### getGuestClanSettings

```
@Nullable
[ClanSettings](clan/ClanSettings.html "interface in net.runelite.api.clan") getGuestClanSettings()
```

Get the guest clan's settings.

Returns:
- #### getClanChannel

```
@Nullable
[ClanChannel](clan/ClanChannel.html "interface in net.runelite.api.clan") getClanChannel​(int clanId)
```

Get clan channel by id.

Parameters:
`clanId` - the clan id
Returns:
See Also:
[`ClanID`](clan/ClanID.html "class in net.runelite.api.clan")
- #### getClanSettings

```
@Nullable
[ClanSettings](clan/ClanSettings.html "interface in net.runelite.api.clan") getClanSettings​(int clanId)
```

Get clan settings by id

Parameters:
`clanId` - the clan id
Returns:
See Also:
[`ClanID`](clan/ClanID.html "class in net.runelite.api.clan")
- #### setUnlockedFps

```
void setUnlockedFps​(boolean unlock)
```
- #### setUnlockedFpsTarget

```
void setUnlockedFpsTarget​(int fps)
```
- #### getAmbientSoundEffects

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
[Deque](Deque.html "interface in net.runelite.api")<[AmbientSoundEffect](AmbientSoundEffect.html "interface in net.runelite.api")> getAmbientSoundEffects()
```

Deprecated.
Gets the ambient sound effects

Returns:
- #### setIdleTimeout

```
void setIdleTimeout​(int ticks)
```

Set the amount of time until the client automatically logs out due to idle input.

Parameters:
`ticks` - client ticks
- #### getIdleTimeout

```
int getIdleTimeout()
```

Get the amount of time until the client automatically logs out due to idle input.

Returns:
client ticks
- #### isMinimapZoom

```
boolean isMinimapZoom()
```

Get whether minimap zoom is enabled

Returns:
- #### setMinimapZoom

```
void setMinimapZoom​(boolean minimapZoom)
```

Set whether minimap zoom is enabled

Parameters:
`minimapZoom` -
- #### getMinimapZoom

```
double getMinimapZoom()
```

Gets the number of pixels per tile on the minimap. The default is 4.

Returns:
- #### setMinimapZoom

```
void setMinimapZoom​(double zoom)
```

Set the number of pixels per tile on the minimap. The default is 4.

Parameters:
`zoom` -
- #### setMinimapTileDrawer

```
void setMinimapTileDrawer​([TileFunction](TileFunction.html "interface in net.runelite.api") drawTile)
```

Sets a callback to override the drawing of tiles on the minimap.
Will be called per tile per frame.
- #### getRasterizer

```
[Rasterizer](Rasterizer.html "interface in net.runelite.api") getRasterizer()
```
- #### menuAction

```
void menuAction​(int p0,
int p1,
[MenuAction](MenuAction.html "enum in net.runelite.api") action,
int id,
int itemId,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") option,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") target)
```
- #### getWorldView

```
[WorldView](WorldView.html "interface in net.runelite.api") getWorldView​(int id)
```

Get worldview by id

Parameters:
`id` - id, or -1 for top level worldview
Returns:
- #### getTopLevelWorldView

```
[WorldView](WorldView.html "interface in net.runelite.api") getTopLevelWorldView()
```

Get the top level world view

Returns:
- #### isCameraShakeDisabled

```
boolean isCameraShakeDisabled()
```

Whether camera shaking effects are disabled at e.g. Barrows, ToA

Returns:
- #### setCameraShakeDisabled

```
void setCameraShakeDisabled​(boolean disabled)
```

Set whether to disable camera shaking effects at e.g. Barrows, ToA

Parameters:
`disabled` -
- #### getDraw2DMask

```
int getDraw2DMask()
```

Gets the current draw2D mask.

Returns:
the current mask
See Also:
[`setDraw2DMask(int)`](#setDraw2DMask(int))
- #### setDraw2DMask

```
void setDraw2DMask​(int mask)
```

Sets the current draw2D mask.
Use bit operations on the value returned by [`getDraw2DMask()`](#getDraw2DMask()) to modify specific features.

Parameters:
`mask` - The new mask.
- #### getInstanceTemplateChunks

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
int[][][] getInstanceTemplateChunks()
```

Deprecated.
Contains a 3D array of template chunks for instanced areas.

The array returned is of format [z][x][y], where z is the
plane, x and y the x-axis and y-axis coordinates of a tile
divided by the size of a chunk.

The bits of the int value held by the coordinates are -1 if there is no data,
structured in the following format:

```

0 1 2 3
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
| |rot| y chunk coord | x chunk coord |pln| |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

```

Returns:
the array of instance template chunks
See Also:
[`Constants.CHUNK_SIZE`](Constants.html#CHUNK_SIZE),
[`InstanceTemplates`](InstanceTemplates.html "enum in net.runelite.api"),
[`WorldView.getInstanceTemplateChunks()`](WorldView.html#getInstanceTemplateChunks())
- #### getXteaKeys

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
int[][] getXteaKeys()
```

Deprecated.
Returns a 2D array containing XTEA encryption keys used to decrypt
map region files.

The array maps the region keys at index `n` to the region
ID held in [`getMapRegions()`](#getMapRegions()) at `n`.

The array of keys for the region make up a 128-bit encryption key
spread across 4 integers.

Returns:
the XTEA encryption keys
- #### isInInstancedRegion

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
boolean isInInstancedRegion()
```

Deprecated.
Checks whether the scene is in an instanced region.

See Also:
[`WorldView.isInstance()`](WorldView.html#isInstance())
- #### getMapRegions

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
int[] getMapRegions()
```

Deprecated.
Gets an array of map region IDs that are currently loaded.

Returns:
the map regions
- #### getScene

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
default [Scene](Scene.html "interface in net.runelite.api") getScene()
```

Deprecated.
Gets the current scene

See Also:
[`WorldView.getScene()`](WorldView.html#getScene())
- #### getPlayers

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
default [List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html?is-external=true "class or interface in java.util")<[Player](Player.html "interface in net.runelite.api")> getPlayers()
```

Deprecated.
Gets a list of all valid players from the player cache.

Returns:
a list of all players
See Also:
[`WorldView.players()`](WorldView.html#players())
- #### getNpcs

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
default [List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html?is-external=true "class or interface in java.util")<[NPC](NPC.html "interface in net.runelite.api")> getNpcs()
```

Deprecated.
Gets a list of all valid NPCs from the NPC cache.

Returns:
a list of all NPCs
See Also:
[`WorldView.npcs()`](WorldView.html#npcs())
- #### getCollisionMaps

```
@Nullable
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
default [CollisionData](CollisionData.html "interface in net.runelite.api")[] getCollisionMaps()
```

Deprecated.
Gets an array of tile collision data.

The index into the array is the plane/z-axis coordinate.

Returns:
the collision data
See Also:
[`WorldView.getCollisionMaps()`](WorldView.html#getCollisionMaps())
- #### getPlane

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
default int getPlane()
```

Deprecated.
Gets the current plane the player is on.

This value indicates the current map level above ground level, where
ground level is 0. For example, going up a ladder in Lumbridge castle
will put the player on plane 1.

Note: This value will never be below 0. Basements and caves below ground
level use a tile offset and are still considered plane 0 by the game.

Returns:
the plane
See Also:
[`WorldView.getPlane()`](WorldView.html#getPlane())
- #### getTileHeights

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
default int[][][] getTileHeights()
```

Deprecated.
Gets a 3D array containing the heights of tiles in the
current scene.

Returns:
the tile heights
See Also:
[`WorldView.getTileHeights()`](WorldView.html#getTileHeights())
- #### getTileSettings

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
default byte[][][] getTileSettings()
```

Deprecated.
Gets a 3D array containing the settings of tiles in the
current scene.

Returns:
the tile settings
See Also:
[`WorldView.getTileSettings()`](WorldView.html#getTileSettings())
- #### getBaseX

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
default int getBaseX()
```

Deprecated.
Returns the x-axis base coordinate.

This value is the x-axis world coordinate of tile (0, 0) in
the current scene (ie. the bottom-left most coordinates in the scene).

Returns:
the base x-axis coordinate
See Also:
[`WorldView.getBaseX()`](WorldView.html#getBaseX())
- #### getBaseY

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
default int getBaseY()
```

Deprecated.
Returns the y-axis base coordinate.

This value is the y-axis world coordinate of tile (0, 0) in
the current scene (ie. the bottom-left most coordinates in the scene).

Returns:
the base y-axis coordinate
See Also:
[`WorldView.getBaseY()`](WorldView.html#getBaseY())
- #### createProjectile

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
[Projectile](Projectile.html "interface in net.runelite.api") createProjectile​(int id,
int plane,
int startX,
int startY,
int startZ,
int startCycle,
int endCycle,
int slope,
int startHeight,
int endHeight,
@Nullable
[Actor](Actor.html "interface in net.runelite.api") target,
int targetX,
int targetY)
```

Deprecated.
Create a projectile.

Parameters:
`id` - projectile/spotanim id
`plane` - plane the projectile is on
`startX` - local x coordinate the projectile starts at
`startY` - local y coordinate the projectile starts at
`startZ` - local z coordinate the projectile starts at - includes tile height
`startCycle` - cycle the project starts
`endCycle` - cycle the projectile ends
`slope` -
`startHeight` - start height of projectile - excludes tile height
`endHeight` - end height of projectile - excludes tile height
`target` - optional actor target
`targetX` - target x - if an actor target is supplied should be the target x
`targetY` - target y - if an actor target is supplied should be the target y
Returns:
the new projectile
- #### createProjectile

```
[Projectile](Projectile.html "interface in net.runelite.api") createProjectile​(int spotanimId,
[WorldPoint](coords/WorldPoint.html "class in net.runelite.api.coords") source,
int sourceHeightOffset,
@Nullable
[Actor](Actor.html "interface in net.runelite.api") sourceActor,
[WorldPoint](coords/WorldPoint.html "class in net.runelite.api.coords") target,
int targetHeightOffset,
@Nullable
[Actor](Actor.html "interface in net.runelite.api") targetActor,
int startCycle,
int endCycle,
int slope,
int startPos)
```

Create a projectile.

Parameters:
`spotanimId` - spotanim id
`source` - source position
`sourceHeightOffset` - source height offset
`sourceActor` - source actor
`target` - target position
`targetHeightOffset` - target height offset
`targetActor` - target actor
`startCycle` - start time
`endCycle` - end time
`slope` - slope
`startPos` - offset from the start where the projectile starts
Returns:
the new projectile
See Also:
`SpotanimID`
- #### getProjectiles

```
[Deque](Deque.html "interface in net.runelite.api")<[Projectile](Projectile.html "interface in net.runelite.api")> getProjectiles()
```

Gets a list of all projectiles currently spawned.

Returns:
all projectiles
- #### getGraphicsObjects

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
default [Deque](Deque.html "interface in net.runelite.api")<[GraphicsObject](GraphicsObject.html "interface in net.runelite.api")> getGraphicsObjects()
```

Deprecated.
Gets a list of all graphics objects currently drawn.

Returns:
all graphics objects
See Also:
[`WorldView.getGraphicsObjects()`](WorldView.html#getGraphicsObjects())
- #### getSelectedSceneTile

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
@Nullable
default [Tile](Tile.html "interface in net.runelite.api") getSelectedSceneTile()
```

Deprecated.
Gets the currently selected tile. (ie. last right clicked tile)

Returns:
the selected tile
See Also:
[`WorldView.getSelectedSceneTile()`](WorldView.html#getSelectedSceneTile())
- #### applyTransformations

```
[Model](Model.html "interface in net.runelite.api") applyTransformations​([Model](Model.html "interface in net.runelite.api") model,
@Nullable
[Animation](Animation.html "interface in net.runelite.api") animA,
int frameA,
@Nullable
[Animation](Animation.html "interface in net.runelite.api") animB,
int frameB)
```

Applies an animation to a Model. The returned model is shared and shouldn't be used
after any other call to applyTransformations, including calls made by the client internally.
Vertices are cloned from the source model. Face transparencies are copied if either animation
animates transparency, otherwise it will share a reference. All other fields share a reference.
- #### createSceneTilePaint

```
[SceneTilePaint](SceneTilePaint.html "interface in net.runelite.api") createSceneTilePaint​(int swColor,
int seColor,
int neColor,
int nwColor,
int texture,
int minimapRgb,
boolean flatShade)
```

Creates a SceneTilePaint instance, which can be attached to a Tile to control its appearance.

Parameters:
`swColor` - the color of the south-west corner of the tile
`seColor` - the color of the south-east corner of the tile
`neColor` - the color of the north-east corner of the tile
`nwColor` - the color of the north-west corner of the tile
`texture` - the texture to render for the tile, or -1 to use the colors
`minimapRgb` - the color to use when rendering the minimap
`flatShade` - whether the tile is flat
Returns:
the newly created SceneTilePaint
See Also:
[`Tile.setSceneTilePaint(SceneTilePaint)`](Tile.html#setSceneTilePaint(net.runelite.api.SceneTilePaint))
- #### getCameraFocusEntity

```
[CameraFocusableEntity](CameraFocusableEntity.html "interface in net.runelite.api") getCameraFocusEntity()
```

Get the entity that the camera is focused on

Returns:
- #### findWorldViewFromWorldPoint

```
@Nonnull
[WorldView](WorldView.html "interface in net.runelite.api") findWorldViewFromWorldPoint​([WorldPoint](coords/WorldPoint.html "class in net.runelite.api.coords") point)
```

Find the worldview a given worldpoint belongs in

Parameters:
`point` -
Returns: