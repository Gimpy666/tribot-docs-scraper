# DrawCallbacks (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/hooks/DrawCallbacks.html

**Package:** Packagenet.runelite.api.hooks

---

* ---

```
public interface DrawCallbacks
```

* + ### Field Summary

Fields | Modifier and Type | Field | Description |
| `static int` | `[GPU](#GPU)` | GPU mode on. |
| `static int` | `[HILLSKEW](#HILLSKEW)` | GPU hillskew support. |
| `static int` | `[NO\_VERTEX\_SNAPPING](#NO_VERTEX_SNAPPING)` | Disable vertex snapping for animations |
| `static int` | `[NORMALS](#NORMALS)` | Requests normals be computed for models. |
| `static int` | `[PASS\_ALPHA](#PASS_ALPHA)` | |
| `static int` | `[PASS\_OPAQUE](#PASS_OPAQUE)` | |
| `static int` | `[UNLIT\_FACE\_COLORS](#UNLIT_FACE_COLORS)` | Enable the [`Model.getUnlitFaceColors()`](../Model.html#getUnlitFaceColors()) method |
| `static int` | `[ZBUF](#ZBUF)` | Enable zbuf renderer. |
| `static int` | `[ZBUF\_ZONE\_FRUSTUM\_CHECK](#ZBUF_ZONE_FRUSTUM_CHECK)` | Enable the [`zoneInFrustum(int, int, int, int)`](#zoneInFrustum(int,int,int,int)) callback |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) [Default Methods](javascript:show(16);) | Modifier and Type | Method | Description |
| `default void` | `[animate](#animate(net.runelite.api.Texture,int))​([Texture](../Texture.html "interface in net.runelite.api") texture,
int diff)` | |
| `default void` | `[despawnWorldView](#despawnWorldView(net.runelite.api.WorldView))​([WorldView](../WorldView.html "interface in net.runelite.api") worldView)` | |
| `void` | `[draw](#draw(int))​(int overlayColor)` | Called when a frame should be drawn. |
| `default void` | `[draw](#draw(net.runelite.api.Projection,net.runelite.api.Scene,net.runelite.api.Renderable,int,int,int,int,long))​([Projection](../Projection.html "interface in net.runelite.api") projection,
[Scene](../Scene.html "interface in net.runelite.api") scene,
[Renderable](../Renderable.html "interface in net.runelite.api") renderable,
int orientation,
int x,
int y,
int z,
long hash)` | |
| `default void` | `[drawDynamic](#drawDynamic(net.runelite.api.Projection,net.runelite.api.Scene,net.runelite.api.TileObject,net.runelite.api.Renderable,net.runelite.api.Model,int,int,int,int))​([Projection](../Projection.html "interface in net.runelite.api") worldProjection,
[Scene](../Scene.html "interface in net.runelite.api") scene,
[TileObject](../TileObject.html "interface in net.runelite.api") tileObject,
[Renderable](../Renderable.html "interface in net.runelite.api") r,
[Model](../Model.html "interface in net.runelite.api") m,
int orient,
int x,
int y,
int z)` | |
| `default void` | `[drawPass](#drawPass(net.runelite.api.Projection,net.runelite.api.Scene,int))​([Projection](../Projection.html "interface in net.runelite.api") entityProjection,
[Scene](../Scene.html "interface in net.runelite.api") scene,
int pass)` | |
| `default void` | `[drawScene](#drawScene(double,double,double,double,double,int))​(double cameraX,
double cameraY,
double cameraZ,
double cameraPitch,
double cameraYaw,
int plane)` | Called before the scene is drawn |
| `default void` | `[drawScenePaint](#drawScenePaint(net.runelite.api.Scene,net.runelite.api.SceneTilePaint,int,int,int))​([Scene](../Scene.html "interface in net.runelite.api") scene,
[SceneTilePaint](../SceneTilePaint.html "interface in net.runelite.api") paint,
int plane,
int tileX,
int tileZ)` | |
| `default void` | `[drawSceneTileModel](#drawSceneTileModel(net.runelite.api.Scene,net.runelite.api.SceneTileModel,int,int))​([Scene](../Scene.html "interface in net.runelite.api") scene,
[SceneTileModel](../SceneTileModel.html "interface in net.runelite.api") model,
int tileX,
int tileZ)` | |
| `default void` | `[drawTemp](#drawTemp(net.runelite.api.Projection,net.runelite.api.Scene,net.runelite.api.GameObject,net.runelite.api.Model,int,int,int,int))​([Projection](../Projection.html "interface in net.runelite.api") worldProjection,
[Scene](../Scene.html "interface in net.runelite.api") scene,
[GameObject](../GameObject.html "interface in net.runelite.api") gameObject,
[Model](../Model.html "interface in net.runelite.api") m,
int orient,
int x,
int y,
int z)` | |
| `default void` | `[drawZoneAlpha](#drawZoneAlpha(net.runelite.api.Projection,net.runelite.api.Scene,int,int,int))​([Projection](../Projection.html "interface in net.runelite.api") entityProjection,
[Scene](../Scene.html "interface in net.runelite.api") scene,
int level,
int zx,
int zz)` | |
| `default void` | `[drawZoneOpaque](#drawZoneOpaque(net.runelite.api.Projection,net.runelite.api.Scene,int,int))​([Projection](../Projection.html "interface in net.runelite.api") entityProjection,
[Scene](../Scene.html "interface in net.runelite.api") scene,
int zx,
int zz)` | |
| `default void` | `[invalidateZone](#invalidateZone(net.runelite.api.Scene,int,int))​([Scene](../Scene.html "interface in net.runelite.api") scene,
int zx,
int zz)` | |
| `default void` | `[loadScene](#loadScene(net.runelite.api.Scene))​([Scene](../Scene.html "interface in net.runelite.api") scene)` | |
| `default void` | `[loadScene](#loadScene(net.runelite.api.WorldView,net.runelite.api.Scene))​([WorldView](../WorldView.html "interface in net.runelite.api") worldView,
[Scene](../Scene.html "interface in net.runelite.api") scene)` | |
| `default void` | `[postDrawScene](#postDrawScene())()` | Called after the scene has been drawn |
| `default void` | `[postSceneDraw](#postSceneDraw(net.runelite.api.Scene))​([Scene](../Scene.html "interface in net.runelite.api") scene)` | |
| `default void` | `[preSceneDraw](#preSceneDraw(net.runelite.api.Scene,float,float,float,float,float,int,int,int,java.util.Set))​([Scene](../Scene.html "interface in net.runelite.api") scene,
float cameraX,
float cameraY,
float cameraZ,
float cameraPitch,
float cameraYaw,
int minLevel,
int level,
int maxLevel,
[Set](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Set.html?is-external=true "class or interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Integer.html?is-external=true "class or interface in java.lang")> hideRoofIds)` | |
| `void` | `[swapScene](#swapScene(net.runelite.api.Scene))​([Scene](../Scene.html "interface in net.runelite.api") scene)` | |
| `default boolean` | `[tileInFrustum](#tileInFrustum(net.runelite.api.Scene,float,float,float,float,int,int,int,int,int,int))​([Scene](../Scene.html "interface in net.runelite.api") scene,
float pitchSin,
float pitchCos,
float yawSin,
float yawCos,
int cameraX,
int cameraY,
int cameraZ,
int plane,
int msx,
int msy)` | |
| `default boolean` | `[zoneInFrustum](#zoneInFrustum(int,int,int,int))​(int zoneX,
int zoneZ,
int maxY,
int minY)` | |

* + ### Field Detail

- #### GPU

```
static final int GPU
```

GPU mode on.

See Also:
[Constant Field Values](../../../../constant-values.html#net.runelite.api.hooks.DrawCallbacks.GPU)
- #### HILLSKEW

```
static final int HILLSKEW
```

GPU hillskew support. Enables the [`Model.getUnskewedModel()`](../Model.html#getUnskewedModel())
API to get the unskewed model.

See Also:
[Constant Field Values](../../../../constant-values.html#net.runelite.api.hooks.DrawCallbacks.HILLSKEW)
- #### NORMALS

```
static final int NORMALS
```

Requests normals be computed for models. Enables the [`Model.getVertexNormalsX()`](../Model.html#getVertexNormalsX())
[`Model.getVertexNormalsY()`](../Model.html#getVertexNormalsY()) [`Model.getVertexNormalsZ()`](../Model.html#getVertexNormalsZ()) API.

See Also:
[Constant Field Values](../../../../constant-values.html#net.runelite.api.hooks.DrawCallbacks.NORMALS)
- #### NO\_VERTEX\_SNAPPING

```
static final int NO_VERTEX_SNAPPING
```

Disable vertex snapping for animations

See Also:
[Constant Field Values](../../../../constant-values.html#net.runelite.api.hooks.DrawCallbacks.NO_VERTEX_SNAPPING)
- #### ZBUF

```
static final int ZBUF
```

Enable zbuf renderer.

See Also:
[Constant Field Values](../../../../constant-values.html#net.runelite.api.hooks.DrawCallbacks.ZBUF)
- #### ZBUF\_ZONE\_FRUSTUM\_CHECK

```
static final int ZBUF_ZONE_FRUSTUM_CHECK
```

Enable the [`zoneInFrustum(int, int, int, int)`](#zoneInFrustum(int,int,int,int)) callback

See Also:
[Constant Field Values](../../../../constant-values.html#net.runelite.api.hooks.DrawCallbacks.ZBUF_ZONE_FRUSTUM_CHECK)
- #### UNLIT\_FACE\_COLORS

```
static final int UNLIT_FACE_COLORS
```

Enable the [`Model.getUnlitFaceColors()`](../Model.html#getUnlitFaceColors()) method

See Also:
[Constant Field Values](../../../../constant-values.html#net.runelite.api.hooks.DrawCallbacks.UNLIT_FACE_COLORS)
- #### PASS\_OPAQUE

```
static final int PASS_OPAQUE
```

See Also:
[Constant Field Values](../../../../constant-values.html#net.runelite.api.hooks.DrawCallbacks.PASS_OPAQUE)
- #### PASS\_ALPHA

```
static final int PASS_ALPHA
```

See Also:
[Constant Field Values](../../../../constant-values.html#net.runelite.api.hooks.DrawCallbacks.PASS_ALPHA)

+ ### Method Detail

- #### draw

```
default void draw​([Projection](../Projection.html "interface in net.runelite.api") projection,
[Scene](../Scene.html "interface in net.runelite.api") scene,
[Renderable](../Renderable.html "interface in net.runelite.api") renderable,
int orientation,
int x,
int y,
int z,
long hash)
```
- #### drawScenePaint

```
default void drawScenePaint​([Scene](../Scene.html "interface in net.runelite.api") scene,
[SceneTilePaint](../SceneTilePaint.html "interface in net.runelite.api") paint,
int plane,
int tileX,
int tileZ)
```
- #### drawSceneTileModel

```
default void drawSceneTileModel​([Scene](../Scene.html "interface in net.runelite.api") scene,
[SceneTileModel](../SceneTileModel.html "interface in net.runelite.api") model,
int tileX,
int tileZ)
```
- #### draw

```
void draw​(int overlayColor)
```

Called when a frame should be drawn.

Parameters:
`overlayColor` - Color of full-viewport overlays, if any
- #### drawScene

```
default void drawScene​(double cameraX,
double cameraY,
double cameraZ,
double cameraPitch,
double cameraYaw,
int plane)
```

Called before the scene is drawn
- #### postDrawScene

```
default void postDrawScene()
```

Called after the scene has been drawn
- #### animate

```
default void animate​([Texture](../Texture.html "interface in net.runelite.api") texture,
int diff)
```
- #### loadScene

```
default void loadScene​([Scene](../Scene.html "interface in net.runelite.api") scene)
```
- #### swapScene

```
void swapScene​([Scene](../Scene.html "interface in net.runelite.api") scene)
```
- #### tileInFrustum

```
default boolean tileInFrustum​([Scene](../Scene.html "interface in net.runelite.api") scene,
float pitchSin,
float pitchCos,
float yawSin,
float yawCos,
int cameraX,
int cameraY,
int cameraZ,
int plane,
int msx,
int msy)
```
- #### zoneInFrustum

```
default boolean zoneInFrustum​(int zoneX,
int zoneZ,
int maxY,
int minY)
```
- #### loadScene

```
default void loadScene​([WorldView](../WorldView.html "interface in net.runelite.api") worldView,
[Scene](../Scene.html "interface in net.runelite.api") scene)
```
- #### despawnWorldView

```
default void despawnWorldView​([WorldView](../WorldView.html "interface in net.runelite.api") worldView)
```
- #### preSceneDraw

```
default void preSceneDraw​([Scene](../Scene.html "interface in net.runelite.api") scene,
float cameraX,
float cameraY,
float cameraZ,
float cameraPitch,
float cameraYaw,
int minLevel,
int level,
int maxLevel,
[Set](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Set.html?is-external=true "class or interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Integer.html?is-external=true "class or interface in java.lang")> hideRoofIds)
```
- #### postSceneDraw

```
default void postSceneDraw​([Scene](../Scene.html "interface in net.runelite.api") scene)
```
- #### drawPass

```
default void drawPass​([Projection](../Projection.html "interface in net.runelite.api") entityProjection,
[Scene](../Scene.html "interface in net.runelite.api") scene,
int pass)
```
- #### drawZoneOpaque

```
default void drawZoneOpaque​([Projection](../Projection.html "interface in net.runelite.api") entityProjection,
[Scene](../Scene.html "interface in net.runelite.api") scene,
int zx,
int zz)
```
- #### drawZoneAlpha

```
default void drawZoneAlpha​([Projection](../Projection.html "interface in net.runelite.api") entityProjection,
[Scene](../Scene.html "interface in net.runelite.api") scene,
int level,
int zx,
int zz)
```
- #### drawDynamic

```
default void drawDynamic​([Projection](../Projection.html "interface in net.runelite.api") worldProjection,
[Scene](../Scene.html "interface in net.runelite.api") scene,
[TileObject](../TileObject.html "interface in net.runelite.api") tileObject,
[Renderable](../Renderable.html "interface in net.runelite.api") r,
[Model](../Model.html "interface in net.runelite.api") m,
int orient,
int x,
int y,
int z)
```
- #### drawTemp

```
default void drawTemp​([Projection](../Projection.html "interface in net.runelite.api") worldProjection,
[Scene](../Scene.html "interface in net.runelite.api") scene,
[GameObject](../GameObject.html "interface in net.runelite.api") gameObject,
[Model](../Model.html "interface in net.runelite.api") m,
int orient,
int x,
int y,
int z)
```
- #### invalidateZone

```
default void invalidateZone​([Scene](../Scene.html "interface in net.runelite.api") scene,
int zx,
int zz)
```