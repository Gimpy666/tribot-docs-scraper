# RuntimeTypeAdapterFactory (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/util/serialization/RuntimeTypeAdapterFactory.html

**Package:** Packageorg.tribot.script.sdk.util.serialization

**Description:** Without additional type information, the serialized JSON is ambiguous. Is
 the bottom shape in this drawing a rectangle or a diamond?{
     "bottomShape": {
       "width": 10,
       "height": 5,
   ...

---

* java.lang.Object
* + org.tribot.script.sdk.util.serialization.RuntimeTypeAdapterFactory<T>

* All Implemented Interfaces:
`com.google.gson.TypeAdapterFactory`

---

```
public final class RuntimeTypeAdapterFactory<T>
extends java.lang.Object
implements com.google.gson.TypeAdapterFactory
```

Adapts values whose runtime type may differ from their declaration type. This
is necessary when a field's type is not the same type that GSON should create
when deserializing that field. For example, consider these types:

```

abstract class Shape {
int x;
int y;
}
class Circle extends Shape {
int radius;
}
class Rectangle extends Shape {
int width;
int height;
}
class Diamond extends Shape {
int width;
int height;
}
class Drawing {
Shape bottomShape;
Shape topShape;
}

```

Without additional type information, the serialized JSON is ambiguous. Is
the bottom shape in this drawing a rectangle or a diamond?
```

{
"bottomShape": {
"width": 10,
"height": 5,
"x": 0,
"y": 0
},
"topShape": {
"radius": 2,
"x": 4,
"y": 1
}
}
```

This class addresses this problem by adding type information to the
serialized JSON and honoring that type information when the JSON is
deserialized:
```

{
"bottomShape": {
"type": "Diamond",
"width": 10,
"height": 5,
"x": 0,
"y": 0
},
"topShape": {
"type": "Circle",
"radius": 2,
"x": 4,
"y": 1
}
}
```

Both the type field name (`"type"`) and the type labels (`"Rectangle"`) are configurable.

### Registering Types

Create a `RuntimeTypeAdapterFactory` by passing the base type and type field
name to the [`of(java.lang.Class<T>, java.lang.String, boolean)`](#of(java.lang.Class,java.lang.String,boolean)) factory method. If you don't supply an explicit type
field name, `"type"` will be used.
```

RuntimeTypeAdapterFactory<Shape> shapeAdapterFactory
= RuntimeTypeAdapterFactory.of(Shape.class, "type");

```

Next register all of your subtypes. Every subtype must be explicitly
registered. This protects your application from injection attacks. If you
don't supply an explicit type label, the type's simple name will be used.

```

shapeAdapterFactory.registerSubtype(Rectangle.class, "Rectangle");
shapeAdapterFactory.registerSubtype(Circle.class, "Circle");
shapeAdapterFactory.registerSubtype(Diamond.class, "Diamond");

```

Finally, register the type adapter factory in your application's GSON builder:

```

Gson gson = new GsonBuilder()
.registerTypeAdapterFactory(shapeAdapterFactory)
.create();

```

Like `GsonBuilder`, this API supports chaining:
```

RuntimeTypeAdapterFactory<Shape> shapeAdapterFactory = RuntimeTypeAdapterFactory.of(Shape.class)
.registerSubtype(Rectangle.class)
.registerSubtype(Circle.class)
.registerSubtype(Diamond.class);

```

### Serialization and deserialization

In order to serialize and deserialize a polymorphic object,
you must specify the base type explicitly.

```

Diamond diamond = new Diamond();
String json = gson.toJson(diamond, Shape.class);

```

And then:

```

Shape shape = gson.fromJson(json, Shape.class);

```

* + ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `<R> com.google.gson.TypeAdapter<R>` | `[create](#create(com.google.gson.Gson,com.google.gson.reflect.TypeToken))​(com.google.gson.Gson gson,
com.google.gson.reflect.TypeToken<R> type)` | |
| `static <T> [RuntimeTypeAdapterFactory](RuntimeTypeAdapterFactory.html "class in org.tribot.script.sdk.util.serialization")<T>` | `[of](#of(java.lang.Class))​(java.lang.Class<T> baseType)` | Creates a new runtime type adapter for `baseType` using `"type"` as
the type field name. |
| `static <T> [RuntimeTypeAdapterFactory](RuntimeTypeAdapterFactory.html "class in org.tribot.script.sdk.util.serialization")<T>` | `[of](#of(java.lang.Class,java.lang.String))​(java.lang.Class<T> baseType,
java.lang.String typeFieldName)` | Creates a new runtime type adapter using for `baseType` using `typeFieldName` as the type field name. |
| `static <T> [RuntimeTypeAdapterFactory](RuntimeTypeAdapterFactory.html "class in org.tribot.script.sdk.util.serialization")<T>` | `[of](#of(java.lang.Class,java.lang.String,boolean))​(java.lang.Class<T> baseType,
java.lang.String typeFieldName,
boolean maintainType)` | Creates a new runtime type adapter using for `baseType` using `typeFieldName` as the type field name. |
| `[RuntimeTypeAdapterFactory](RuntimeTypeAdapterFactory.html "class in org.tribot.script.sdk.util.serialization")<[T](RuntimeTypeAdapterFactory.html "type parameter in RuntimeTypeAdapterFactory")>` | `[registerSubtype](#registerSubtype(java.lang.Class))​(java.lang.Class<? extends [T](RuntimeTypeAdapterFactory.html "type parameter in RuntimeTypeAdapterFactory")> type)` | Registers `type` identified by its `simple
name`. |
| `[RuntimeTypeAdapterFactory](RuntimeTypeAdapterFactory.html "class in org.tribot.script.sdk.util.serialization")<[T](RuntimeTypeAdapterFactory.html "type parameter in RuntimeTypeAdapterFactory")>` | `[registerSubtype](#registerSubtype(java.lang.Class,java.lang.String))​(java.lang.Class<? extends [T](RuntimeTypeAdapterFactory.html "type parameter in RuntimeTypeAdapterFactory")> type,
java.lang.String label)` | Registers `type` identified by `label`. |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Method Detail

- #### of

```
public static <T> [RuntimeTypeAdapterFactory](RuntimeTypeAdapterFactory.html "class in org.tribot.script.sdk.util.serialization")<T> of​(java.lang.Class<T> baseType,
java.lang.String typeFieldName,
boolean maintainType)
```

Creates a new runtime type adapter using for `baseType` using `typeFieldName` as the type field name. Type field names are case sensitive.
`maintainType` flag decide if the type will be stored in pojo or not.
- #### of

```
public static <T> [RuntimeTypeAdapterFactory](RuntimeTypeAdapterFactory.html "class in org.tribot.script.sdk.util.serialization")<T> of​(java.lang.Class<T> baseType,
java.lang.String typeFieldName)
```

Creates a new runtime type adapter using for `baseType` using `typeFieldName` as the type field name. Type field names are case sensitive.
- #### of

```
public static <T> [RuntimeTypeAdapterFactory](RuntimeTypeAdapterFactory.html "class in org.tribot.script.sdk.util.serialization")<T> of​(java.lang.Class<T> baseType)
```

Creates a new runtime type adapter for `baseType` using `"type"` as
the type field name.
- #### registerSubtype

```
public [RuntimeTypeAdapterFactory](RuntimeTypeAdapterFactory.html "class in org.tribot.script.sdk.util.serialization")<[T](RuntimeTypeAdapterFactory.html "type parameter in RuntimeTypeAdapterFactory")> registerSubtype​(java.lang.Class<? extends [T](RuntimeTypeAdapterFactory.html "type parameter in RuntimeTypeAdapterFactory")> type,
java.lang.String label)
```

Registers `type` identified by `label`. Labels are case
sensitive.

Throws:
`java.lang.IllegalArgumentException` - if either `type` or `label`
have already been registered on this type adapter.
- #### registerSubtype

```
public [RuntimeTypeAdapterFactory](RuntimeTypeAdapterFactory.html "class in org.tribot.script.sdk.util.serialization")<[T](RuntimeTypeAdapterFactory.html "type parameter in RuntimeTypeAdapterFactory")> registerSubtype​(java.lang.Class<? extends [T](RuntimeTypeAdapterFactory.html "type parameter in RuntimeTypeAdapterFactory")> type)
```

Registers `type` identified by its `simple
name`. Labels are case sensitive.

Throws:
`java.lang.IllegalArgumentException` - if either `type` or its simple name
have already been registered on this type adapter.
- #### create

```
public <R> com.google.gson.TypeAdapter<R> create​(com.google.gson.Gson gson,
com.google.gson.reflect.TypeToken<R> type)
```

Specified by:
`create` in interface `com.google.gson.TypeAdapterFactory`