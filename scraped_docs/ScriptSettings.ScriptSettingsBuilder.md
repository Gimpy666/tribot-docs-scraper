# ScriptSettings.ScriptSettingsBuilder (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/util/ScriptSettings.ScriptSettingsBuilder.html

**Package:** Packageorg.tribot.script.sdk.util

---

* java.lang.Object
* + org.tribot.script.sdk.util.ScriptSettings.ScriptSettingsBuilder

* Enclosing class:
[ScriptSettings](ScriptSettings.html "class in org.tribot.script.sdk.util")

---

```
public static class ScriptSettings.ScriptSettingsBuilder
extends java.lang.Object
```

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `[ScriptSettings.ScriptSettingsBuilder](ScriptSettings.ScriptSettingsBuilder.html "class in org.tribot.script.sdk.util")` | `[basePath](#basePath(java.lang.String))​(@NonNull java.lang.String basePath)` | The base directory to store the files in. |
| `[ScriptSettings](ScriptSettings.html "class in org.tribot.script.sdk.util")` | `[build](#build())()` | |
| `[ScriptSettings.ScriptSettingsBuilder](ScriptSettings.ScriptSettingsBuilder.html "class in org.tribot.script.sdk.util")` | `[gson](#gson(com.google.gson.Gson))​(@NonNull com.google.gson.Gson gson)` | The gson instance to use for serializing/deserializing the settings object. |
| `java.lang.String` | `[toString](#toString())()` | |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

* + ### Method Detail

- #### gson

```
public [ScriptSettings.ScriptSettingsBuilder](ScriptSettings.ScriptSettingsBuilder.html "class in org.tribot.script.sdk.util") gson​(@NonNull
@NonNull com.google.gson.Gson gson)
```

The gson instance to use for serializing/deserializing the settings object. Defaults to a plain Gson instance with pretty printing.

Returns:
`this`.
- #### basePath

```
public [ScriptSettings.ScriptSettingsBuilder](ScriptSettings.ScriptSettingsBuilder.html "class in org.tribot.script.sdk.util") basePath​(@NonNull
@NonNull java.lang.String basePath)
```

The base directory to store the files in. Defaults to the tribot directory/script-name

Returns:
`this`.
- #### build

```
public [ScriptSettings](ScriptSettings.html "class in org.tribot.script.sdk.util") build()
```
- #### toString

```
public java.lang.String toString()
```

Overrides:
`toString` in class `java.lang.Object`