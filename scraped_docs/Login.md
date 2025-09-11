# Login (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/Login.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.Login

* ---

```
public class Login
extends java.lang.Object
```

Utilities for logging in and inspecting current login state

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk")` | Represents a mesage that can be displayed when trying to log in, such as already logged in |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[Login](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static java.util.Optional<[Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk")>` | `[getLoginMessage](#getLoginMessage())()` | Attempts to get the login message at the login screen |
| `static java.lang.String` | `[getSelectedLoginName](#getSelectedLoginName())()` | |
| `static boolean` | `[isLoggedIn](#isLoggedIn())()` | Checks if we are currently logged in |
| `static boolean` | `[isLoginMusicDisabled](#isLoginMusicDisabled())()` | Checks if login music is disabled. |
| `static boolean` | `[login](#login())()` | Attempts to log in using the account selected by the user when starting the script |
| `static boolean` | `[login](#login(java.lang.String,java.lang.String))​(java.lang.String username,
java.lang.String password)` | Attempts to log in using ths specified credentials |
| `static boolean` | `[login](#login(java.lang.String,java.lang.String,java.lang.String))​(java.lang.String username,
java.lang.String password,
java.lang.String authenticatorSecret)` | Attempts to log in using ths specified credentials |
| `static boolean` | `[logout](#logout())()` | Attempts to log out |
| `static void` | `[setLoginMusic](#setLoginMusic(boolean))​(boolean disabled)` | Sets whether login music should be disabled or not |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### Login

```
public Login()
```

+ ### Method Detail

- #### isLoggedIn

```
public static boolean isLoggedIn()
```

Checks if we are currently logged in

Returns:
true if we are logged in, false otherwise
- #### login

```
public static boolean login()
```

Attempts to log in using the account selected by the user when starting the script

Returns:
true if logged in successfully, false otherwise
- #### login

```
public static boolean login​(java.lang.String username,
java.lang.String password)
```

Attempts to log in using ths specified credentials

Parameters:
`username` - the account username
`password` - the account password
Returns:
true if logged in successfully, false otherwise
- #### login

```
public static boolean login​(java.lang.String username,
java.lang.String password,
java.lang.String authenticatorSecret)
```

Attempts to log in using ths specified credentials

Parameters:
`username` - the account username
`password` - the account password
`authenticatorSecret` - the authenticator secret key to handle the authenticator, if applicable
Returns:
true if logged in successfully, false otherwise
- #### logout

```
public static boolean logout()
```

Attempts to log out

Returns:
true if logged out successfully, false otherwise
- #### getLoginMessage

```
public static java.util.Optional<[Login.LoginMessage](Login.LoginMessage.html "enum in org.tribot.script.sdk")> getLoginMessage()
```

Attempts to get the login message at the login screen

Returns:
the login message at the login screen
- #### isLoginMusicDisabled

```
public static boolean isLoginMusicDisabled()
```

Checks if login music is disabled.

Returns:
true if login music is disabled, false otherwise
- #### setLoginMusic

```
public static void setLoginMusic​(boolean disabled)
```

Sets whether login music should be disabled or not
- #### getSelectedLoginName

```
public static java.lang.String getSelectedLoginName()
```