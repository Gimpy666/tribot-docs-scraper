# ScriptSettings (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/util/ScriptSettings.html

**Package:** Packageorg.tribot.script.sdk.util

---

* java.lang.Object
* + org.tribot.script.sdk.util.ScriptSettings

* ---

```
public class ScriptSettings
extends java.lang.Object
```

Contains utility methods for saving/loading script settings.

Note that any settings object that is saved/loaded must have the @DoNotRename annotation applied to all fields that should be saved/loaded.
To skip a field, you can make it transient.
`Gson` is used internally to serialize and deserialize the objects.

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[ScriptSettings.ScriptSettingsBuilder](ScriptSettings.ScriptSettingsBuilder.html "class in org.tribot.script.sdk.util")` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [ScriptSettings.ScriptSettingsBuilder](ScriptSettings.ScriptSettingsBuilder.html "class in org.tribot.script.sdk.util")` | `[builder](#builder())()` | |
| `boolean` | `[delete](#delete(java.lang.String))​(java.lang.String name)` | Attempts to delete the settings file at the specified path |
| `static [ScriptSettings](ScriptSettings.html "class in org.tribot.script.sdk.util")` | `[getDefault](#getDefault())()` | Creates a default script settings handler |
| `java.io.File` | `[getDirectory](#getDirectory())()` | Gets the base directory where script settings will save/load, based on the config. |
| `java.util.List<java.lang.String>` | `[getSaveNames](#getSaveNames())()` | Lists all the file names in the base directory where script settings will save/load. |
| `<T> java.util.Optional<T>` | `[load](#load(java.lang.String,java.lang.Class))​(java.lang.String name,
java.lang.Class<T> settingsType)` | Attempts to load the specified settings type at the specified path. |
| `<T> boolean` | `[save](#save(java.lang.String,T))​(java.lang.String name,
T scriptSettings)` | Attempts to save the specified script settings object to the specified path |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Method Detail

- #### getDirectory

```
public java.io.File getDirectory()
```

Gets the base directory where script settings will save/load, based on the config.

Generally meant to be used with a file picker/chooser.

Returns:
the base directory where script settings will save/load
- #### getSaveNames

```
public java.util.List<java.lang.String> getSaveNames()
```

Lists all the file names in the base directory where script settings will save/load.
This will give a relative path to the base directory. Any of these can be passed to [`load(String, Class)`](#load(java.lang.String,java.lang.Class)).

Returns:
the file names in the base directory where script settings will save/load
- #### save

```
public <T> boolean save​(java.lang.String name,
T scriptSettings)
```

Attempts to save the specified script settings object to the specified path

Type Parameters:
`T` - the settings object type
Parameters:
`name` - the settings name
`scriptSettings` - the settings object to save
Returns:
true if saved successfully, false otherwise
- #### load

```
public <T> java.util.Optional<T> load​(java.lang.String name,
java.lang.Class<T> settingsType)
```

Attempts to load the specified settings type at the specified path.

Type Parameters:
`T` - the result type
Parameters:
`name` - the settings name
`settingsType` - the settings type
Returns:
an optional with the settings object if it was loaded properly, or an empty optional if there was an issue loading
- #### delete

```
public boolean delete​(java.lang.String name)
```

Attempts to delete the settings file at the specified path

Parameters:
`name` - the settings file name
Returns:
true if the file was deleted, false otherwise
- #### getDefault

```
public static [ScriptSettings](ScriptSettings.html "class in org.tribot.script.sdk.util") getDefault()
```

Creates a default script settings handler

Returns:
a script settings handler configured with the default settings
- #### builder

```
public static [ScriptSettings.ScriptSettingsBuilder](ScriptSettings.ScriptSettingsBuilder.html "class in org.tribot.script.sdk.util") builder()
```