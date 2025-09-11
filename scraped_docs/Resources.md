# Resources (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/util/Resources.html

**Package:** Packageorg.tribot.script.sdk.util

---

* java.lang.Object
* + org.tribot.script.sdk.util.Resources

* ---

```
public class Resources
extends java.lang.Object
```

Contains utilities to load script resources

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[Resources.ResourceNotFoundException](Resources.ResourceNotFoundException.html "class in org.tribot.script.sdk.util")` | Exception thrown when a resource is not found |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[Resources](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static byte[]` | `[getBytes](#getBytes(java.lang.String))​(java.lang.String name)` | Gets the bytes of a resource with the specified name |
| `static java.lang.String` | `[getCssPath](#getCssPath(java.lang.String))​(java.lang.String name)` | Gets a string path to a css file to be used with javafx. |
| `static java.awt.image.BufferedImage` | `[getImage](#getImage(java.lang.String))​(java.lang.String name)` | Parses the specified resource with the specified name as an image |
| `static com.google.gson.JsonElement` | `[getJson](#getJson(java.lang.String))​(java.lang.String name)` | Parses the specified resource with the specified name as a json file |
| `static <T> T` | `[getJson](#getJson(java.lang.String,java.lang.Class))​(java.lang.String name,
java.lang.Class<T> type)` | Parses the specified resource with the specified name as a json file with the specified type |
| `static java.util.Properties` | `[getProperties](#getProperties(java.lang.String))​(java.lang.String name)` | Parses the specified resource with the specified name as a properties file |
| `static java.io.InputStream` | `[getStream](#getStream(java.lang.String))​(java.lang.String name)` | Gets an input stream to a resource with the specified name |
| `static java.lang.String` | `[getString](#getString(java.lang.String))​(java.lang.String name)` | Gets the resource with the specified name as a string |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### Resources

```
public Resources()
```

+ ### Method Detail

- #### getStream

```
public static java.io.InputStream getStream​(java.lang.String name)
throws [Resources.ResourceNotFoundException](Resources.ResourceNotFoundException.html "class in org.tribot.script.sdk.util")
```

Gets an input stream to a resource with the specified name

Parameters:
`name` - the resource name
Returns:
an input stream pointing to the resource
Throws:
`[Resources.ResourceNotFoundException](Resources.ResourceNotFoundException.html "class in org.tribot.script.sdk.util")`
- #### getBytes

```
public static byte[] getBytes​(java.lang.String name)
throws [Resources.ResourceNotFoundException](Resources.ResourceNotFoundException.html "class in org.tribot.script.sdk.util")
```

Gets the bytes of a resource with the specified name

Parameters:
`name` - the resource name
Returns:
the resource as a byte array
Throws:
`[Resources.ResourceNotFoundException](Resources.ResourceNotFoundException.html "class in org.tribot.script.sdk.util")`
- #### getString

```
public static java.lang.String getString​(java.lang.String name)
throws [Resources.ResourceNotFoundException](Resources.ResourceNotFoundException.html "class in org.tribot.script.sdk.util")
```

Gets the resource with the specified name as a string

Parameters:
`name` - the resource name
Returns:
the resource as a string
Throws:
`[Resources.ResourceNotFoundException](Resources.ResourceNotFoundException.html "class in org.tribot.script.sdk.util")`
- #### getProperties

```
public static java.util.Properties getProperties​(java.lang.String name)
throws [Resources.ResourceNotFoundException](Resources.ResourceNotFoundException.html "class in org.tribot.script.sdk.util")
```

Parses the specified resource with the specified name as a properties file

Parameters:
`name` - the resource name
Returns:
the resource as a properties object
Throws:
`[Resources.ResourceNotFoundException](Resources.ResourceNotFoundException.html "class in org.tribot.script.sdk.util")`
- #### getJson

```
public static com.google.gson.JsonElement getJson​(java.lang.String name)
throws [Resources.ResourceNotFoundException](Resources.ResourceNotFoundException.html "class in org.tribot.script.sdk.util")
```

Parses the specified resource with the specified name as a json file

Parameters:
`name` - the resource name
Returns:
the resource as a json object
Throws:
`[Resources.ResourceNotFoundException](Resources.ResourceNotFoundException.html "class in org.tribot.script.sdk.util")`
- #### getJson

```
public static <T> T getJson​(java.lang.String name,
java.lang.Class<T> type)
throws [Resources.ResourceNotFoundException](Resources.ResourceNotFoundException.html "class in org.tribot.script.sdk.util")
```

Parses the specified resource with the specified name as a json file with the specified type

Parameters:
`name` - the resource name
Returns:
the resource as the specified type
Throws:
`[Resources.ResourceNotFoundException](Resources.ResourceNotFoundException.html "class in org.tribot.script.sdk.util")`
- #### getImage

```
public static java.awt.image.BufferedImage getImage​(java.lang.String name)
throws [Resources.ResourceNotFoundException](Resources.ResourceNotFoundException.html "class in org.tribot.script.sdk.util")
```

Parses the specified resource with the specified name as an image

Parameters:
`name` - the resource name
Returns:
the resource as an image
Throws:
`[Resources.ResourceNotFoundException](Resources.ResourceNotFoundException.html "class in org.tribot.script.sdk.util")`
- #### getCssPath

```
public static java.lang.String getCssPath​(java.lang.String name)
throws [Resources.ResourceNotFoundException](Resources.ResourceNotFoundException.html "class in org.tribot.script.sdk.util")
```

Gets a string path to a css file to be used with javafx. You can directly use the result of this to add a stylesheet.
Ex. `scene.getStylesheets().add(Resources.getCssPath("my-resource.css"))`

Note the implementation of this copies to a separate temporary file and returns the url due to the way tribot resource loading currently works.

Parameters:
`name` - the resource name
Returns:
the css file resource path
Throws:
`[Resources.ResourceNotFoundException](Resources.ResourceNotFoundException.html "class in org.tribot.script.sdk.util")`