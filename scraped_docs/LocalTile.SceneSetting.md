# LocalTile.SceneSetting (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/types/LocalTile.SceneSetting.html

**Package:** Packageorg.tribot.script.sdk.types

---

* java.lang.Object
* + java.lang.Enum<[LocalTile.SceneSetting](LocalTile.SceneSetting.html "enum in org.tribot.script.sdk.types")>
+ - org.tribot.script.sdk.types.LocalTile.SceneSetting

* All Implemented Interfaces:
`java.io.Serializable`, `java.lang.Comparable<[LocalTile.SceneSetting](LocalTile.SceneSetting.html "enum in org.tribot.script.sdk.types")>`

Enclosing class:
[LocalTile](LocalTile.html "class in org.tribot.script.sdk.types")

---

```
public static enum LocalTile.SceneSetting
extends java.lang.Enum<[LocalTile.SceneSetting](LocalTile.SceneSetting.html "enum in org.tribot.script.sdk.types")>
```

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[BRIDGE](#BRIDGE)` | |
| `[UNDER\_ROOF](#UNDER_ROOF)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [LocalTile.SceneSetting](LocalTile.SceneSetting.html "enum in org.tribot.script.sdk.types")` | `[valueOf](#valueOf(java.lang.String))​(java.lang.String name)` | Returns the enum constant of this type with the specified name. |
| `static [LocalTile.SceneSetting](LocalTile.SceneSetting.html "enum in org.tribot.script.sdk.types")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
- ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

- #### BRIDGE

```
public static final [LocalTile.SceneSetting](LocalTile.SceneSetting.html "enum in org.tribot.script.sdk.types") BRIDGE
```
- #### UNDER\_ROOF

```
public static final [LocalTile.SceneSetting](LocalTile.SceneSetting.html "enum in org.tribot.script.sdk.types") UNDER_ROOF
```

+ ### Method Detail

- #### values

```
public static [LocalTile.SceneSetting](LocalTile.SceneSetting.html "enum in org.tribot.script.sdk.types")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (LocalTile.SceneSetting c : LocalTile.SceneSetting.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [LocalTile.SceneSetting](LocalTile.SceneSetting.html "enum in org.tribot.script.sdk.types") valueOf​(java.lang.String name)
```

Returns the enum constant of this type with the specified name.
The string must match *exactly* an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

Parameters:
`name` - the name of the enum constant to be returned.
Returns:
the enum constant with the specified name
Throws:
`java.lang.IllegalArgumentException` - if this enum type has no constant with the specified name
`java.lang.NullPointerException` - if the argument is null