# Mesh (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/Mesh.html

**Package:** Packagenet.runelite.api

---

* All Known Subinterfaces:
`[Model](Model.html "interface in net.runelite.api")`, `[ModelData](ModelData.html "interface in net.runelite.api")`

---

```
public interface Mesh<T extends Mesh<T>>
```

A [`Model`](Model.html "interface in net.runelite.api") or [`ModelData`](ModelData.html "interface in net.runelite.api")

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `int` | `[getFaceCount](#getFaceCount())()` | |
| `int[]` | `[getFaceIndices1](#getFaceIndices1())()` | |
| `int[]` | `[getFaceIndices2](#getFaceIndices2())()` | |
| `int[]` | `[getFaceIndices3](#getFaceIndices3())()` | |
| `short[]` | `[getFaceTextures](#getFaceTextures())()` | |
| `byte[]` | `[getFaceTransparencies](#getFaceTransparencies())()` | |
| `int` | `[getVerticesCount](#getVerticesCount())()` | |
| `float[]` | `[getVerticesX](#getVerticesX())()` | |
| `float[]` | `[getVerticesY](#getVerticesY())()` | |
| `float[]` | `[getVerticesZ](#getVerticesZ())()` | |
| `[T](Mesh.html "type parameter in Mesh")` | `[rotateY180Ccw](#rotateY180Ccw())()` | Rotates this model 180 degrees around the vertical axis. |
| `[T](Mesh.html "type parameter in Mesh")` | `[rotateY270Ccw](#rotateY270Ccw())()` | Rotates this model 270 degrees around the vertical axis. |
| `[T](Mesh.html "type parameter in Mesh")` | `[rotateY90Ccw](#rotateY90Ccw())()` | Rotates this model 90 degrees around the vertical axis. |
| `[T](Mesh.html "type parameter in Mesh")` | `[scale](#scale(int,int,int))​(int x,
int y,
int z)` | Resizes this model by the passed amount (1/128ths). |
| `[T](Mesh.html "type parameter in Mesh")` | `[translate](#translate(int,int,int))​(int x,
int y,
int z)` | Offsets this model by the passed amount (1/128ths of a tile). |

* + ### Method Detail

- #### getVerticesCount

```
int getVerticesCount()
```
- #### getVerticesX

```
float[] getVerticesX()
```
- #### getVerticesY

```
float[] getVerticesY()
```
- #### getVerticesZ

```
float[] getVerticesZ()
```
- #### getFaceCount

```
int getFaceCount()
```
- #### getFaceIndices1

```
int[] getFaceIndices1()
```
- #### getFaceIndices2

```
int[] getFaceIndices2()
```
- #### getFaceIndices3

```
int[] getFaceIndices3()
```
- #### getFaceTransparencies

```
byte[] getFaceTransparencies()
```
- #### getFaceTextures

```
short[] getFaceTextures()
```
- #### rotateY90Ccw

```
[T](Mesh.html "type parameter in Mesh") rotateY90Ccw()
```

Rotates this model 90 degrees around the vertical axis.
[`ModelData.cloneVertices()`](ModelData.html#cloneVertices()) should be called before calling this method
- #### rotateY180Ccw

```
[T](Mesh.html "type parameter in Mesh") rotateY180Ccw()
```

Rotates this model 180 degrees around the vertical axis.
[`ModelData.cloneVertices()`](ModelData.html#cloneVertices()) should be called before calling this method
- #### rotateY270Ccw

```
[T](Mesh.html "type parameter in Mesh") rotateY270Ccw()
```

Rotates this model 270 degrees around the vertical axis.
[`ModelData.cloneVertices()`](ModelData.html#cloneVertices()) should be called before calling this method
- #### translate

```
[T](Mesh.html "type parameter in Mesh") translate​(int x,
int y,
int z)
```

Offsets this model by the passed amount (1/128ths of a tile).
[`ModelData.cloneVertices()`](ModelData.html#cloneVertices()) should be called before calling this method
- #### scale

```
[T](Mesh.html "type parameter in Mesh") scale​(int x,
int y,
int z)
```

Resizes this model by the passed amount (1/128ths).
[`ModelData.cloneVertices()`](ModelData.html#cloneVertices()) should be called before calling this method