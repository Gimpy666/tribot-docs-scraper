# Log (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/Log.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.Log

* ---

```
public class Log
extends java.lang.Object
```

Contains methods for logging

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[Log](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);) | Modifier and Type | Method | Description |
| `static void` | `[debug](#debug(java.lang.Object))​(java.lang.Object msg)` | Logs the specified message with the log level debug |
| `static void` | `[error](#error(java.lang.Object))​(java.lang.Object msg)` | Logs the specified message with the log level error |
| `static void` | `[error](#error(java.lang.Object,java.lang.Throwable))​(java.lang.Object msg,
java.lang.Throwable throwable)` | Logs the specified message and throwable with the log level error |
| `static void` | `[info](#info(java.lang.Object))​(java.lang.Object msg)` | Logs the specified message with the log level info |
| `static void` | `[log](#log(java.lang.Object))​(java.lang.Object msg)` | Deprecated.
use an appropriate log level such as [`info(Object)`](#info(java.lang.Object)) or [`debug(Object)`](#debug(java.lang.Object))
|
| `static void` | `[trace](#trace(java.lang.Object))​(java.lang.Object msg)` | Logs the specified message with the log level trace |
| `static void` | `[warn](#warn(java.lang.Object))​(java.lang.Object msg)` | Logs the specified message with the log level warn |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### Log

```
public Log()
```

+ ### Method Detail

- #### log

```
@Deprecated
public static void log​(java.lang.Object msg)
```

Deprecated.
use an appropriate log level such as [`info(Object)`](#info(java.lang.Object)) or [`debug(Object)`](#debug(java.lang.Object))

Prints the message to the client debug

Parameters:
`msg` - the message to print
- #### info

```
public static void info​(java.lang.Object msg)
```

Logs the specified message with the log level info

Parameters:
`msg` - the message to log
- #### debug

```
public static void debug​(java.lang.Object msg)
```

Logs the specified message with the log level debug

Parameters:
`msg` - the message to log
- #### warn

```
public static void warn​(java.lang.Object msg)
```

Logs the specified message with the log level warn

Parameters:
`msg` - the message to log
- #### error

```
public static void error​(java.lang.Object msg)
```

Logs the specified message with the log level error

Parameters:
`msg` - the message to log
- #### error

```
public static void error​(java.lang.Object msg,
java.lang.Throwable throwable)
```

Logs the specified message and throwable with the log level error

Parameters:
`msg` - the message to log
`throwable` - a throwable to log the stack trace
- #### trace

```
public static void trace​(java.lang.Object msg)
```

Logs the specified message with the log level trace

Parameters:
`msg` - the message to log