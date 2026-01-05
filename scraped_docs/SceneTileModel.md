# SceneTileModel (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/SceneTileModel.html

**Package:** Packagenet.runelite.api

---

* ---

```
public interface SceneTileModel
```

Represents the model of a tile in the current scene.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `int` | `[getBufferLen](#getBufferLen())()` | |
| `int` | `[getBufferOffset](#getBufferOffset())()` | |
| `int[]` | `[getFaceX](#getFaceX())()` | |
| `int[]` | `[getFaceY](#getFaceY())()` | |
| `int[]` | `[getFaceZ](#getFaceZ())()` | |
| `int` | `[getModelOverlay](#getModelOverlay())()` | Gets the overlay color of the tile. |
| `int` | `[getModelUnderlay](#getModelUnderlay())()` | Gets the underlay color of the tile. |
| `int` | `[getRotation](#getRotation())()` | Gets the rotation of the tile. |
| `int` | `[getShape](#getShape())()` | Gets the shape mask type. |
| `int[]` | `[getTriangleColorA](#getTriangleColorA())()` | |
| `int[]` | `[getTriangleColorB](#getTriangleColorB())()` | |
| `int[]` | `[getTriangleColorC](#getTriangleColorC())()` | |
| `int[]` | `[getTriangleTextureId](#getTriangleTextureId())()` | |
| `int` | `[getUvBufferOffset](#getUvBufferOffset())()` | |
| `int[]` | `[getVertexX](#getVertexX())()` | |
| `int[]` | `[getVertexY](#getVertexY())()` | |
| `int[]` | `[getVertexZ](#getVertexZ())()` | |
| `boolean` | `[isFlat](#isFlat())()` | |
| `void` | `[setBufferLen](#setBufferLen(int))​(int bufferLen)` | |
| `void` | `[setBufferOffset](#setBufferOffset(int))​(int bufferOffset)` | |
| `void` | `[setUvBufferOffset](#setUvBufferOffset(int))​(int bufferOffset)` | |

* + ### Method Detail

- #### getModelUnderlay

```
int getModelUnderlay()
```

Gets the underlay color of the tile.

Returns:
the underlay color
- #### getModelOverlay

```
int getModelOverlay()
```

Gets the overlay color of the tile.

Returns:
the overlay color
- #### getShape

```
int getShape()
```

Gets the shape mask type.

Returns:
the shape mask
- #### getRotation

```
int getRotation()
```

Gets the rotation of the tile.

Returns:
the rotation
- #### getFaceX

```
int[] getFaceX()
```
- #### getFaceY

```
int[] getFaceY()
```
- #### getFaceZ

```
int[] getFaceZ()
```
- #### getVertexX

```
int[] getVertexX()
```
- #### getVertexY

```
int[] getVertexY()
```
- #### getVertexZ

```
int[] getVertexZ()
```
- #### getTriangleColorA

```
int[] getTriangleColorA()
```
- #### getTriangleColorB

```
int[] getTriangleColorB()
```
- #### getTriangleColorC

```
int[] getTriangleColorC()
```
- #### getTriangleTextureId

```
int[] getTriangleTextureId()
```
- #### isFlat

```
boolean isFlat()
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
- #### getBufferLen

```
int getBufferLen()
```
- #### setBufferLen

```
void setBufferLen​(int bufferLen)
```