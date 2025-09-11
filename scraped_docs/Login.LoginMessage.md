# Login.LoginMessage (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/Login.LoginMessage.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + java.lang.Enum<[Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk")>
+ - org.tribot.script.sdk.Login.LoginMessage

* All Implemented Interfaces:
`java.io.Serializable`, `java.lang.Comparable<[Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk")>`

Enclosing class:
[Login](Login.html "class in org.tribot.script.sdk")

---

```
public static enum Login.LoginMessage
extends java.lang.Enum<[Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk")>
```

Represents a mesage that can be displayed when trying to log in, such as already logged in

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[ALREADY\_LOGGED\_IN](#ALREADY_LOGGED_IN)` | |
| `[AUTHENTICATOR](#AUTHENTICATOR)` | |
| `[AUTHENTICATOR\_ALREADY\_LOGGED\_IN](#AUTHENTICATOR_ALREADY_LOGGED_IN)` | |
| `[AUTHENTICATOR\_ERROR\_CONNECTING](#AUTHENTICATOR_ERROR_CONNECTING)` | |
| `[AUTHENTICATOR\_INVALID\_SKILL\_TOTAL](#AUTHENTICATOR_INVALID_SKILL_TOTAL)` | |
| `[AUTHENTICATOR\_LOGIN\_LIMITED\_EXCEEDED](#AUTHENTICATOR_LOGIN_LIMITED_EXCEEDED)` | |
| `[AUTHENTICATOR\_MEM\_WORLD](#AUTHENTICATOR_MEM_WORLD)` | |
| `[AUTHENTICATOR\_NO\_REPLY](#AUTHENTICATOR_NO_REPLY)` | |
| `[AUTHENTICATOR\_SERVER\_OFFLINE](#AUTHENTICATOR_SERVER_OFFLINE)` | |
| `[AUTHENTICATOR\_STANDING\_IN\_MEMBERS](#AUTHENTICATOR_STANDING_IN_MEMBERS)` | |
| `[AUTHENTICATOR\_TIMED\_OUT](#AUTHENTICATOR_TIMED_OUT)` | |
| `[AUTHENTICATOR\_TOO\_MANY\_ATTEMPTS](#AUTHENTICATOR_TOO_MANY_ATTEMPTS)` | |
| `[AUTHENTICATOR\_WORLD\_FULL](#AUTHENTICATOR_WORLD_FULL)` | |
| `[BANNED](#BANNED)` | |
| `[BETA\_WORLD](#BETA_WORLD)` | |
| `[CONNECTING](#CONNECTING)` | |
| `[DISCONNECTED](#DISCONNECTED)` | |
| `[ENTER](#ENTER)` | |
| `[ERROR\_CONNECTING](#ERROR_CONNECTING)` | |
| `[INVALID](#INVALID)` | |
| `[INVALID\_SKILL\_TOTAL](#INVALID_SKILL_TOTAL)` | |
| `[LOCKED](#LOCKED)` | |
| `[LOGIN\_LIMIT\_EXCEEDED](#LOGIN_LIMIT_EXCEEDED)` | |
| `[MEM\_WORLD](#MEM_WORLD)` | |
| `[NEW\_USER](#NEW_USER)` | |
| `[NO\_REPLY](#NO_REPLY)` | |
| `[NOT\_MEMBER](#NOT_MEMBER)` | |
| `[PVP\_WORLD](#PVP_WORLD)` | |
| `[SERVER\_OFFLINE](#SERVER_OFFLINE)` | |
| `[STANDING\_IN\_MEMBERS](#STANDING_IN_MEMBERS)` | |
| `[TIMED\_OUT](#TIMED_OUT)` | |
| `[TOO\_MANY\_ATTEMPTS](#TOO_MANY_ATTEMPTS)` | |
| `[UPDATE\_IN\_PROGRESS](#UPDATE_IN_PROGRESS)` | |
| `[UPDATED](#UPDATED)` | |
| `[WORLD\_FULL](#WORLD_FULL)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `boolean` | `[isAuthenticatorMessage](#isAuthenticatorMessage())()` | |
| `static [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk")` | `[valueOf](#valueOf(java.lang.String))​(java.lang.String name)` | Returns the enum constant of this type with the specified name. |
| `static [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
- ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

- #### ALREADY\_LOGGED\_IN

```
public static final [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk") ALREADY_LOGGED_IN
```
- #### AUTHENTICATOR

```
public static final [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk") AUTHENTICATOR
```
- #### AUTHENTICATOR\_ALREADY\_LOGGED\_IN

```
public static final [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk") AUTHENTICATOR_ALREADY_LOGGED_IN
```
- #### AUTHENTICATOR\_ERROR\_CONNECTING

```
public static final [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk") AUTHENTICATOR_ERROR_CONNECTING
```
- #### AUTHENTICATOR\_INVALID\_SKILL\_TOTAL

```
public static final [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk") AUTHENTICATOR_INVALID_SKILL_TOTAL
```
- #### AUTHENTICATOR\_LOGIN\_LIMITED\_EXCEEDED

```
public static final [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk") AUTHENTICATOR_LOGIN_LIMITED_EXCEEDED
```
- #### AUTHENTICATOR\_MEM\_WORLD

```
public static final [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk") AUTHENTICATOR_MEM_WORLD
```
- #### AUTHENTICATOR\_NO\_REPLY

```
public static final [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk") AUTHENTICATOR_NO_REPLY
```
- #### AUTHENTICATOR\_SERVER\_OFFLINE

```
public static final [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk") AUTHENTICATOR_SERVER_OFFLINE
```
- #### AUTHENTICATOR\_STANDING\_IN\_MEMBERS

```
public static final [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk") AUTHENTICATOR_STANDING_IN_MEMBERS
```
- #### AUTHENTICATOR\_TIMED\_OUT

```
public static final [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk") AUTHENTICATOR_TIMED_OUT
```
- #### AUTHENTICATOR\_TOO\_MANY\_ATTEMPTS

```
public static final [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk") AUTHENTICATOR_TOO_MANY_ATTEMPTS
```
- #### AUTHENTICATOR\_WORLD\_FULL

```
public static final [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk") AUTHENTICATOR_WORLD_FULL
```
- #### BANNED

```
public static final [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk") BANNED
```
- #### BETA\_WORLD

```
public static final [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk") BETA_WORLD
```
- #### CONNECTING

```
public static final [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk") CONNECTING
```
- #### DISCONNECTED

```
public static final [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk") DISCONNECTED
```
- #### ENTER

```
public static final [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk") ENTER
```
- #### ERROR\_CONNECTING

```
public static final [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk") ERROR_CONNECTING
```
- #### INVALID

```
public static final [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk") INVALID
```
- #### INVALID\_SKILL\_TOTAL

```
public static final [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk") INVALID_SKILL_TOTAL
```
- #### LOCKED

```
public static final [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk") LOCKED
```
- #### LOGIN\_LIMIT\_EXCEEDED

```
public static final [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk") LOGIN_LIMIT_EXCEEDED
```
- #### MEM\_WORLD

```
public static final [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk") MEM_WORLD
```
- #### NEW\_USER

```
public static final [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk") NEW_USER
```
- #### NOT\_MEMBER

```
public static final [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk") NOT_MEMBER
```
- #### NO\_REPLY

```
public static final [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk") NO_REPLY
```
- #### PVP\_WORLD

```
public static final [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk") PVP_WORLD
```
- #### SERVER\_OFFLINE

```
public static final [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk") SERVER_OFFLINE
```
- #### STANDING\_IN\_MEMBERS

```
public static final [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk") STANDING_IN_MEMBERS
```
- #### TIMED\_OUT

```
public static final [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk") TIMED_OUT
```
- #### TOO\_MANY\_ATTEMPTS

```
public static final [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk") TOO_MANY_ATTEMPTS
```
- #### UPDATED

```
public static final [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk") UPDATED
```
- #### UPDATE\_IN\_PROGRESS

```
public static final [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk") UPDATE_IN_PROGRESS
```
- #### WORLD\_FULL

```
public static final [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk") WORLD_FULL
```

+ ### Method Detail

- #### values

```
public static [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (Login.LoginMessage c : Login.LoginMessage.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk") valueOf​(java.lang.String name)
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
- #### isAuthenticatorMessage

```
public boolean isAuthenticatorMessage()
```