# GameState (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/GameState.html

**Package:** Packagenet.runelite.api

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + [java.lang.Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[GameState](GameState.html "enum in net.runelite.api")>
+ - net.runelite.api.GameState

* All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/Serializable.html?is-external=true "class or interface in java.io")`, `[Comparable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Comparable.html?is-external=true "class or interface in java.lang")<[GameState](GameState.html "enum in net.runelite.api")>`

---

```
public enum GameState
extends [Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[GameState](GameState.html "enum in net.runelite.api")>
```

An enumeration of game states the client is in.

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

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `int` | `[getState](#getState())()` | The raw state value. |
| `static [GameState](GameState.html "enum in net.runelite.api")` | `[of](#of(int))​(int state)` | Utility method that maps the rank value to its respective
[`GameState`](GameState.html "enum in net.runelite.api") value. |
| `static [GameState](GameState.html "enum in net.runelite.api")` | `[valueOf](#valueOf(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)` | Returns the enum constant of this type with the specified name. |
| `static [GameState](GameState.html "enum in net.runelite.api")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#clone() "class or interface in java.lang"), [compareTo](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#compareTo(E) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#finalize() "class or interface in java.lang"), [getDeclaringClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#getDeclaringClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#hashCode() "class or interface in java.lang"), [name](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#name() "class or interface in java.lang"), [ordinal](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#ordinal() "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#toString() "class or interface in java.lang"), [valueOf](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#valueOf(java.lang.Class,java.lang.String) "class or interface in java.lang")`
- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Enum Constant Detail

- #### UNKNOWN

```
public static final [GameState](GameState.html "enum in net.runelite.api") UNKNOWN
```

Unknown game state.
- #### STARTING

```
public static final [GameState](GameState.html "enum in net.runelite.api") STARTING
```

The client is starting.
- #### LOGIN\_SCREEN

```
public static final [GameState](GameState.html "enum in net.runelite.api") LOGIN_SCREEN
```

The client is at the login screen.
- #### LOGIN\_SCREEN\_AUTHENTICATOR

```
public static final [GameState](GameState.html "enum in net.runelite.api") LOGIN_SCREEN_AUTHENTICATOR
```

The client is at the login screen entering authenticator code.
- #### LOGGING\_IN

```
public static final [GameState](GameState.html "enum in net.runelite.api") LOGGING_IN
```

There is a player logging in.
- #### LOADING

```
public static final [GameState](GameState.html "enum in net.runelite.api") LOADING
```

The game is being loaded.
- #### LOGGED\_IN

```
public static final [GameState](GameState.html "enum in net.runelite.api") LOGGED_IN
```

The user has successfully logged in.
- #### CONNECTION\_LOST

```
public static final [GameState](GameState.html "enum in net.runelite.api") CONNECTION_LOST
```

Connection to the server was lost.
- #### HOPPING

```
public static final [GameState](GameState.html "enum in net.runelite.api") HOPPING
```

A world hop is taking place.

+ ### Method Detail

- #### values

```
public static [GameState](GameState.html "enum in net.runelite.api")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (GameState c : GameState.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [GameState](GameState.html "enum in net.runelite.api") valueOf​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)
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
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/IllegalArgumentException.html?is-external=true "class or interface in java.lang")` - if this enum type has no constant with the specified name
`[NullPointerException](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/NullPointerException.html?is-external=true "class or interface in java.lang")` - if the argument is null
- #### of

```
public static [GameState](GameState.html "enum in net.runelite.api") of​(int state)
```

Utility method that maps the rank value to its respective
[`GameState`](GameState.html "enum in net.runelite.api") value.

Parameters:
`state` - the raw state value
Returns:
the gamestate
- #### getState

```
public int getState()
```

The raw state value.