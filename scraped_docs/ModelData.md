# ModelData (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/ModelData.html

**Package:** Packagenet.runelite.api

---

* All Superinterfaces:
`[Mesh](Mesh.html "interface in net.runelite.api")<[ModelData](ModelData.html "interface in net.runelite.api")>`, `[Node](Node.html "interface in net.runelite.api")`, `[Renderable](Renderable.html "interface in net.runelite.api")`

---

```
public interface ModelData
extends [Mesh](Mesh.html "interface in net.runelite.api")<[ModelData](ModelData.html "interface in net.runelite.api")>, [Renderable](Renderable.html "interface in net.runelite.api")
```

An unlit model

* + ### Field Summary

Fields | Modifier and Type | Field | Description |
| `static int` | `[DEFAULT\_AMBIENT](#DEFAULT_AMBIENT)` | |
| `static int` | `[DEFAULT\_CONTRAST](#DEFAULT_CONTRAST)` | |
| `static int` | `[DEFAULT\_X](#DEFAULT_X)` | |
| `static int` | `[DEFAULT\_Y](#DEFAULT_Y)` | |
| `static int` | `[DEFAULT\_Z](#DEFAULT_Z)` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `[ModelData](ModelData.html "interface in net.runelite.api")` | `[cloneColors](#cloneColors())()` | Clones [`getFaceColors()`](#getFaceColors()) so they can be safely mutated |
| `[ModelData](ModelData.html "interface in net.runelite.api")` | `[cloneTextures](#cloneTextures())()` | Clones [`Mesh.getFaceTextures()`](Mesh.html#getFaceTextures()) so they can be safely mutated |
| `[ModelData](ModelData.html "interface in net.runelite.api")` | `[cloneTransparencies](#cloneTransparencies())()` | Clones [`Mesh.getFaceTransparencies()`](Mesh.html#getFaceTransparencies()) so they can be safely mutated |
| `[ModelData](ModelData.html "interface in net.runelite.api")` | `[cloneTransparencies](#cloneTransparencies(boolean))​(boolean force)` | Clones [`Mesh.getFaceTransparencies()`](Mesh.html#getFaceTransparencies()) so they can be safely mutated |
| `[ModelData](ModelData.html "interface in net.runelite.api")` | `[cloneVertices](#cloneVertices())()` | Clones [`Mesh.getVerticesX()`](Mesh.html#getVerticesX()), [`Mesh.getVerticesY()`](Mesh.html#getVerticesY()), and [`Mesh.getVerticesZ()`](Mesh.html#getVerticesZ()) so
they can be safely mutated |
| `short[]` | `[getFaceColors](#getFaceColors())()` | Gets colors as Jagex HSL |
| `[Model](Model.html "interface in net.runelite.api")` | `[light](#light())()` | Lights a model with default values |
| `[Model](Model.html "interface in net.runelite.api")` | `[light](#light(int,int,int,int,int))​(int ambient,
int contrast,
int x,
int y,
int z)` | Lights a model. |
| `[ModelData](ModelData.html "interface in net.runelite.api")` | `[recolor](#recolor(short,short))​(short colorToReplace,
short colorToReplaceWith)` | Applies a recolor using Jagex's HSL format. |
| `[ModelData](ModelData.html "interface in net.runelite.api")` | `[retexture](#retexture(short,short))​(short find,
short replace)` | Applies a retexture, changing texture ids. |
| `[ModelData](ModelData.html "interface in net.runelite.api")` | `[shallowCopy](#shallowCopy())()` | Shallow-copies a model. |

- ### Methods inherited from interface net.runelite.api.[Mesh](Mesh.html "interface in net.runelite.api")

`[getFaceCount](Mesh.html#getFaceCount()), [getFaceIndices1](Mesh.html#getFaceIndices1()), [getFaceIndices2](Mesh.html#getFaceIndices2()), [getFaceIndices3](Mesh.html#getFaceIndices3()), [getFaceTextures](Mesh.html#getFaceTextures()), [getFaceTransparencies](Mesh.html#getFaceTransparencies()), [getVerticesCount](Mesh.html#getVerticesCount()), [getVerticesX](Mesh.html#getVerticesX()), [getVerticesY](Mesh.html#getVerticesY()), [getVerticesZ](Mesh.html#getVerticesZ()), [rotateY180Ccw](Mesh.html#rotateY180Ccw()), [rotateY270Ccw](Mesh.html#rotateY270Ccw()), [rotateY90Ccw](Mesh.html#rotateY90Ccw()), [scale](Mesh.html#scale(int,int,int)), [translate](Mesh.html#translate(int,int,int))`
- ### Methods inherited from interface net.runelite.api.[Node](Node.html "interface in net.runelite.api")

`[getHash](Node.html#getHash()), [getNext](Node.html#getNext()), [getPrevious](Node.html#getPrevious())`
- ### Methods inherited from interface net.runelite.api.[Renderable](Renderable.html "interface in net.runelite.api")

`[getAnimationHeightOffset](Renderable.html#getAnimationHeightOffset()), [getModel](Renderable.html#getModel()), [getModelHeight](Renderable.html#getModelHeight()), [setModelHeight](Renderable.html#setModelHeight(int))`

* + ### Field Detail

- #### DEFAULT\_AMBIENT

```
static final int DEFAULT_AMBIENT
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ModelData.DEFAULT_AMBIENT)
- #### DEFAULT\_CONTRAST

```
static final int DEFAULT_CONTRAST
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ModelData.DEFAULT_CONTRAST)
- #### DEFAULT\_X

```
static final int DEFAULT_X
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ModelData.DEFAULT_X)
- #### DEFAULT\_Y

```
static final int DEFAULT_Y
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ModelData.DEFAULT_Y)
- #### DEFAULT\_Z

```
static final int DEFAULT_Z
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ModelData.DEFAULT_Z)

+ ### Method Detail

- #### getFaceColors

```
short[] getFaceColors()
```

Gets colors as Jagex HSL

See Also:
[`JagexColor`](JagexColor.html "class in net.runelite.api")
- #### light

```
[Model](Model.html "interface in net.runelite.api") light​(int ambient,
int contrast,
int x,
int y,
int z)
```

Lights a model.

The produced model shares verticies, face transparencies, face indicies, and textures with
the underlying ModelData. If any of these may be mutated the corresponding `cloneX`
method should be called before `light`ing
- #### light

```
[Model](Model.html "interface in net.runelite.api") light()
```

Lights a model with default values

See Also:
[`light(int, int, int, int, int)`](#light(int,int,int,int,int))
- #### recolor

```
[ModelData](ModelData.html "interface in net.runelite.api") recolor​(short colorToReplace,
short colorToReplaceWith)
```

Applies a recolor using Jagex's HSL format. You should call [`cloneColors()`](#cloneColors()) ()} before calling
this method
- #### retexture

```
[ModelData](ModelData.html "interface in net.runelite.api") retexture​(short find,
short replace)
```

Applies a retexture, changing texture ids. You should call [`cloneTextures()`](#cloneTextures()) before calling
this method
- #### shallowCopy

```
[ModelData](ModelData.html "interface in net.runelite.api") shallowCopy()
```

Shallow-copies a model. Does not copy any arrays, which are still shared with this object.
- #### cloneVertices

```
[ModelData](ModelData.html "interface in net.runelite.api") cloneVertices()
```

Clones [`Mesh.getVerticesX()`](Mesh.html#getVerticesX()), [`Mesh.getVerticesY()`](Mesh.html#getVerticesY()), and [`Mesh.getVerticesZ()`](Mesh.html#getVerticesZ()) so
they can be safely mutated
- #### cloneColors

```
[ModelData](ModelData.html "interface in net.runelite.api") cloneColors()
```

Clones [`getFaceColors()`](#getFaceColors()) so they can be safely mutated
- #### cloneTextures

```
[ModelData](ModelData.html "interface in net.runelite.api") cloneTextures()
```

Clones [`Mesh.getFaceTextures()`](Mesh.html#getFaceTextures()) so they can be safely mutated
- #### cloneTransparencies

```
[ModelData](ModelData.html "interface in net.runelite.api") cloneTransparencies()
```

Clones [`Mesh.getFaceTransparencies()`](Mesh.html#getFaceTransparencies()) so they can be safely mutated
- #### cloneTransparencies

```
[ModelData](ModelData.html "interface in net.runelite.api") cloneTransparencies​(boolean force)
```

Clones [`Mesh.getFaceTransparencies()`](Mesh.html#getFaceTransparencies()) so they can be safely mutated

Parameters:
`force` - Ensure [`Mesh.getFaceTransparencies()`](Mesh.html#getFaceTransparencies()) is non null