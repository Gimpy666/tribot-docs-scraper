# ScriptRuntimeInfo (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/script/ScriptRuntimeInfo.html

**Package:** Packageorg.tribot.script.sdk.script

---

* java.lang.Object
* + org.tribot.script.sdk.script.ScriptRuntimeInfo

* ---

```
public class ScriptRuntimeInfo
extends java.lang.Object
```

Contains various methods to get script runtime information

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[ScriptRuntimeInfo](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static java.lang.String` | `[getScriptName](#getScriptName())()` | Gets the active script name. |
| `static int` | `[getScriptRepoId](#getScriptRepoId())()` | Gets the active script's repo id |
| `static double` | `[getScriptRepoVersion](#getScriptRepoVersion())()` | Gets the repo version of the active script. |
| `static boolean` | `[isLocalScript](#isLocalScript())()` | Checks if the active script is a local script |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### ScriptRuntimeInfo

```
public ScriptRuntimeInfo()
```

+ ### Method Detail

- #### getScriptName

```
public static java.lang.String getScriptName()
```

Gets the active script name. If this is a repo script, it will be the repo script name. Otherwise, it will be from the manifest.

Returns:
the active script name
- #### getScriptRepoId

```
public static int getScriptRepoId()
```

Gets the active script's repo id

Returns:
the active script's repo id, or -1 if not running from the repo
- #### isLocalScript

```
public static boolean isLocalScript()
```

Checks if the active script is a local script

Returns:
true if the active script is a local script, false otherwise
- #### getScriptRepoVersion

```
public static double getScriptRepoVersion()
```

Gets the repo version of the active script.

Returns:
the repo version of the active script, or -1 if not running from the repo