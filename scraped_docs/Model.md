# Model (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/Model.html

**Package:** Packagenet.runelite.api

---

* All Superinterfaces:
`[Mesh](Mesh.html "interface in net.runelite.api")<[Model](Model.html "interface in net.runelite.api")>`, `[Node](Node.html "interface in net.runelite.api")`, `[Renderable](Renderable.html "interface in net.runelite.api")`

---

```
public interface Model
extends [Mesh](Mesh.html "interface in net.runelite.api")<[Model](Model.html "interface in net.runelite.api")>, [Renderable](Renderable.html "interface in net.runelite.api")
```

Represents the model of an object.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) [Deprecated Methods](javascript:show(32);) | Modifier and Type | Method | Description |
| `void` | `[calculateBoundsCylinder](#calculateBoundsCylinder())()` | |
| `void` | `[calculateExtreme](#calculateExtreme(int))​(int orientation)` | Deprecated. |
| `void` | `[drawFrustum](#drawFrustum(int,int,int,int,int,int,int))​(int zero,
int xRotate,
int yRotate,
int zRotate,
int xCamera,
int yCamera,
int zCamera)` | |
| `void` | `[drawOrtho](#drawOrtho(int,int,int,int,int,int,int,int))​(int zero,
int xRotate,
int yRotate,
int zRotate,
int xCamera,
int yCamera,
int zCamera,
int zoom)` | |
| `[AABB](AABB.html "interface in net.runelite.api")` | `[getAABB](#getAABB(int))​(int orientation)` | |
| `int` | `[getBottomY](#getBottomY())()` | |
| `int` | `[getBufferOffset](#getBufferOffset())()` | |
| `int` | `[getDiameter](#getDiameter())()` | |
| `byte[]` | `[getFaceBias](#getFaceBias())()` | |
| `int[]` | `[getFaceColors1](#getFaceColors1())()` | |
| `int[]` | `[getFaceColors2](#getFaceColors2())()` | |
| `int[]` | `[getFaceColors3](#getFaceColors3())()` | |
| `byte[]` | `[getFaceRenderPriorities](#getFaceRenderPriorities())()` | |
| `byte` | `[getOverrideAmount](#getOverrideAmount())()` | |
| `byte` | `[getOverrideHue](#getOverrideHue())()` | |
| `byte` | `[getOverrideLuminance](#getOverrideLuminance())()` | |
| `byte` | `[getOverrideSaturation](#getOverrideSaturation())()` | |
| `int` | `[getRadius](#getRadius())()` | |
| `int` | `[getSceneId](#getSceneId())()` | |
| `int[]` | `[getTexIndices1](#getTexIndices1())()` | |
| `int[]` | `[getTexIndices2](#getTexIndices2())()` | |
| `int[]` | `[getTexIndices3](#getTexIndices3())()` | |
| `byte[]` | `[getTextureFaces](#getTextureFaces())()` | |
| `short[]` | `[getUnlitFaceColors](#getUnlitFaceColors())()` | |
| `[Model](Model.html "interface in net.runelite.api")` | `[getUnskewedModel](#getUnskewedModel())()` | |
| `int` | `[getUvBufferOffset](#getUvBufferOffset())()` | |
| `int[]` | `[getVertexNormalsX](#getVertexNormalsX())()` | |
| `int[]` | `[getVertexNormalsY](#getVertexNormalsY())()` | |
| `int[]` | `[getVertexNormalsZ](#getVertexNormalsZ())()` | |
| `int` | `[getXYZMag](#getXYZMag())()` | |
| `void` | `[setBufferOffset](#setBufferOffset(int))​(int bufferOffset)` | |
| `void` | `[setSceneId](#setSceneId(int))​(int sceneId)` | |
| `void` | `[setUvBufferOffset](#setUvBufferOffset(int))​(int bufferOffset)` | |
| `boolean` | `[useBoundingBox](#useBoundingBox())()` | |

- ### Methods inherited from interface net.runelite.api.[Mesh](Mesh.html "interface in net.runelite.api")

`[getFaceCount](Mesh.html#getFaceCount()), [getFaceIndices1](Mesh.html#getFaceIndices1()), [getFaceIndices2](Mesh.html#getFaceIndices2()), [getFaceIndices3](Mesh.html#getFaceIndices3()), [getFaceTextures](Mesh.html#getFaceTextures()), [getFaceTransparencies](Mesh.html#getFaceTransparencies()), [getVerticesCount](Mesh.html#getVerticesCount()), [getVerticesX](Mesh.html#getVerticesX()), [getVerticesY](Mesh.html#getVerticesY()), [getVerticesZ](Mesh.html#getVerticesZ()), [rotateY180Ccw](Mesh.html#rotateY180Ccw()), [rotateY270Ccw](Mesh.html#rotateY270Ccw()), [rotateY90Ccw](Mesh.html#rotateY90Ccw()), [scale](Mesh.html#scale(int,int,int)), [translate](Mesh.html#translate(int,int,int))`
- ### Methods inherited from interface net.runelite.api.[Node](Node.html "interface in net.runelite.api")

`[getHash](Node.html#getHash()), [getNext](Node.html#getNext()), [getPrevious](Node.html#getPrevious())`
- ### Methods inherited from interface net.runelite.api.[Renderable](Renderable.html "interface in net.runelite.api")

`[getAnimationHeightOffset](Renderable.html#getAnimationHeightOffset()), [getModel](Renderable.html#getModel()), [getModelHeight](Renderable.html#getModelHeight()), [setModelHeight](Renderable.html#setModelHeight(int))`

* + ### Method Detail

- #### getFaceColors1

```
int[] getFaceColors1()
```
- #### getFaceColors2

```
int[] getFaceColors2()
```
- #### getFaceColors3

```
int[] getFaceColors3()
```
- #### getUnlitFaceColors

```
short[] getUnlitFaceColors()
```
- #### getSceneId

```
int getSceneId()
```
- #### setSceneId

```
void setSceneId​(int sceneId)
```
- #### getBufferOffset

```
int getBufferOffset()
```
- #### setBufferOffset

```
void setBufferOffset​(int bufferOffset)
```
- #### getUvBufferOffset

```
int getUvBufferOffset()
```
- #### setUvBufferOffset

```
void setUvBufferOffset​(int bufferOffset)
```
- #### getBottomY

```
int getBottomY()
```
- #### calculateBoundsCylinder

```
void calculateBoundsCylinder()
```
- #### getFaceRenderPriorities

```
byte[] getFaceRenderPriorities()
```
- #### getFaceBias

```
byte[] getFaceBias()
```
- #### getRadius

```
int getRadius()
```
- #### getDiameter

```
int getDiameter()
```
- #### calculateExtreme

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
void calculateExtreme​(int orientation)
```

Deprecated.

See Also:
[`getAABB(int)`](#getAABB(int))
- #### getAABB

```
@Nonnull
[AABB](AABB.html "interface in net.runelite.api") getAABB​(int orientation)
```
- #### getXYZMag

```
int getXYZMag()
```
- #### useBoundingBox

```
boolean useBoundingBox()
```
- #### getVertexNormalsX

```
int[] getVertexNormalsX()
```
- #### getVertexNormalsY

```
int[] getVertexNormalsY()
```
- #### getVertexNormalsZ

```
int[] getVertexNormalsZ()
```
- #### getOverrideAmount

```
byte getOverrideAmount()
```
- #### getOverrideHue

```
byte getOverrideHue()
```
- #### getOverrideSaturation

```
byte getOverrideSaturation()
```
- #### getOverrideLuminance

```
byte getOverrideLuminance()
```
- #### getTextureFaces

```
byte[] getTextureFaces()
```
- #### getTexIndices1

```
int[] getTexIndices1()
```
- #### getTexIndices2

```
int[] getTexIndices2()
```
- #### getTexIndices3

```
int[] getTexIndices3()
```
- #### getUnskewedModel

```
[Model](Model.html "interface in net.runelite.api") getUnskewedModel()
```
- #### drawFrustum

```
void drawFrustum​(int zero,
int xRotate,
int yRotate,
int zRotate,
int xCamera,
int yCamera,
int zCamera)
```
- #### drawOrtho

```
void drawOrtho​(int zero,
int xRotate,
int yRotate,
int zRotate,
int xCamera,
int yCamera,
int zCamera,
int zoom)
```