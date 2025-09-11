# GameState.State (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/GameState.State.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + java.lang.Enum<[GameState.State](GameState.State.html "enum in org.tribot.script.sdk")>
+ - org.tribot.script.sdk.GameState.State

* All Implemented Interfaces:
`java.io.Serializable`, `java.lang.Comparable<[GameState.State](GameState.State.html "enum in org.tribot.script.sdk")>`

Enclosing class:
[GameState](GameState.html "class in org.tribot.script.sdk")

---

```
public static enum GameState.State
extends java.lang.Enum<[GameState.State](GameState.State.html "enum in org.tribot.script.sdk")>
```

A current state of the game, such as loading, at login screen, or logged in.

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[CONNECTION\_LOST](#CONNECTION_LOST)` | Connection to the server was lost. |
| `[HOPPING](#HOPPING)` | A world hop is taking place. |
| `[LOADING](#LOADING)` | The game is being loaded. |
| `[LOGGED\_IN](#LOGGED_IN)` | The user has successfully logged in. |
| `[LOGGING\_IN](#LOGGING_IN)` | There is a player logging in. |
| `[LOGIN\_SCREEN](#LOGIN_SCREEN)` | The client is at the login screen. |
| `[LOGIN\_SCREEN\_AUTHENTICATOR](#LOGIN_SCREEN_AUTHENTICATOR)` | The client is at the login screen entering authenticator code. |
| `[STARTING](#STARTING)` | The client is starting. |
| `[UNKNOWN](#UNKNOWN)` | Unknown game state. |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [GameState.State](GameState.State.html "enum in org.tribot.script.sdk")` | `[valueOf](#valueOf(java.lang.String))​(java.lang.String name)` | Returns the enum constant of this type with the specified name. |
| `static [GameState.State](GameState.State.html "enum in org.tribot.script.sdk")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
- ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

- #### UNKNOWN

```
public static final [GameState.State](GameState.State.html "enum in org.tribot.script.sdk") UNKNOWN
```

Unknown game state.
- #### STARTING

```
public static final [GameState.State](GameState.State.html "enum in org.tribot.script.sdk") STARTING
```

The client is starting.
- #### LOGIN\_SCREEN

```
public static final [GameState.State](GameState.State.html "enum in org.tribot.script.sdk") LOGIN_SCREEN
```

The client is at the login screen.
- #### LOGIN\_SCREEN\_AUTHENTICATOR

```
public static final [GameState.State](GameState.State.html "enum in org.tribot.script.sdk") LOGIN_SCREEN_AUTHENTICATOR
```

The client is at the login screen entering authenticator code.
- #### LOGGING\_IN

```
public static final [GameState.State](GameState.State.html "enum in org.tribot.script.sdk") LOGGING_IN
```

There is a player logging in.
- #### LOADING

```
public static final [GameState.State](GameState.State.html "enum in org.tribot.script.sdk") LOADING
```

The game is being loaded.
- #### LOGGED\_IN

```
public static final [GameState.State](GameState.State.html "enum in org.tribot.script.sdk") LOGGED_IN
```

The user has successfully logged in.
- #### CONNECTION\_LOST

```
public static final [GameState.State](GameState.State.html "enum in org.tribot.script.sdk") CONNECTION_LOST
```

Connection to the server was lost.
- #### HOPPING

```
public static final [GameState.State](GameState.State.html "enum in org.tribot.script.sdk") HOPPING
```

A world hop is taking place.

+ ### Method Detail

- #### values

```
public static [GameState.State](GameState.State.html "enum in org.tribot.script.sdk")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (GameState.State c : GameState.State.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [GameState.State](GameState.State.html "enum in org.tribot.script.sdk") valueOf​(java.lang.String name)
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