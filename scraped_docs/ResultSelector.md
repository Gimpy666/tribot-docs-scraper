# ResultSelector (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/util/ResultSelector.html

**Package:** Packageorg.tribot.script.sdk.util

---

* Type Parameters:
`T` - the type of the result to extract

All Superinterfaces:
`java.util.stream.Collector<T,​java.util.List<T>,​java.util.Optional<T>>`

---

```
public interface ResultSelector<T>
extends java.util.stream.Collector<T,​java.util.List<T>,​java.util.Optional<T>>
```

Represents an interface that extracts a result from a list. Meant to be used as a collection operation on a stream.

* + ### Nested Class Summary

- ### Nested classes/interfaces inherited from interface java.util.stream.Collector

`java.util.stream.Collector.Characteristics`

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) [Default Methods](javascript:show(16);) | Modifier and Type | Method | Description |
| `default java.util.function.BiConsumer<java.util.List<[T](ResultSelector.html "type parameter in ResultSelector")>,​[T](ResultSelector.html "type parameter in ResultSelector")>` | `[accumulator](#accumulator())()` | |
| `default java.util.Set<java.util.stream.Collector.Characteristics>` | `[characteristics](#characteristics())()` | |
| `default java.util.function.BinaryOperator<java.util.List<[T](ResultSelector.html "type parameter in ResultSelector")>>` | `[combiner](#combiner())()` | |
| `default java.util.function.Function<java.util.List<[T](ResultSelector.html "type parameter in ResultSelector")>,​java.util.Optional<[T](ResultSelector.html "type parameter in ResultSelector")>>` | `[finisher](#finisher())()` | |
| `java.util.Optional<[T](ResultSelector.html "type parameter in ResultSelector")>` | `[select](#select(java.util.List))​(java.util.List<[T](ResultSelector.html "type parameter in ResultSelector")> results)` | Extracts a result from the list. |
| `default java.util.function.Supplier<java.util.List<[T](ResultSelector.html "type parameter in ResultSelector")>>` | `[supplier](#supplier())()` | |

* + ### Method Detail

- #### select

```
java.util.Optional<[T](ResultSelector.html "type parameter in ResultSelector")> select​(java.util.List<[T](ResultSelector.html "type parameter in ResultSelector")> results)
```

Extracts a result from the list.

The logic behind the extraction algorithm is specific to the result selector implementation.

Parameters:
`results` - the list of results
Returns:
an extracted result based
- #### supplier

```
default java.util.function.Supplier<java.util.List<[T](ResultSelector.html "type parameter in ResultSelector")>> supplier()
```

Specified by:
`supplier` in interface `java.util.stream.Collector<[T](ResultSelector.html "type parameter in ResultSelector"),​java.util.List<[T](ResultSelector.html "type parameter in ResultSelector")>,​java.util.Optional<[T](ResultSelector.html "type parameter in ResultSelector")>>`
- #### accumulator

```
default java.util.function.BiConsumer<java.util.List<[T](ResultSelector.html "type parameter in ResultSelector")>,​[T](ResultSelector.html "type parameter in ResultSelector")> accumulator()
```

Specified by:
`accumulator` in interface `java.util.stream.Collector<[T](ResultSelector.html "type parameter in ResultSelector"),​java.util.List<[T](ResultSelector.html "type parameter in ResultSelector")>,​java.util.Optional<[T](ResultSelector.html "type parameter in ResultSelector")>>`
- #### combiner

```
default java.util.function.BinaryOperator<java.util.List<[T](ResultSelector.html "type parameter in ResultSelector")>> combiner()
```

Specified by:
`combiner` in interface `java.util.stream.Collector<[T](ResultSelector.html "type parameter in ResultSelector"),​java.util.List<[T](ResultSelector.html "type parameter in ResultSelector")>,​java.util.Optional<[T](ResultSelector.html "type parameter in ResultSelector")>>`
- #### finisher

```
default java.util.function.Function<java.util.List<[T](ResultSelector.html "type parameter in ResultSelector")>,​java.util.Optional<[T](ResultSelector.html "type parameter in ResultSelector")>> finisher()
```

Specified by:
`finisher` in interface `java.util.stream.Collector<[T](ResultSelector.html "type parameter in ResultSelector"),​java.util.List<[T](ResultSelector.html "type parameter in ResultSelector")>,​java.util.Optional<[T](ResultSelector.html "type parameter in ResultSelector")>>`
- #### characteristics

```
default java.util.Set<java.util.stream.Collector.Characteristics> characteristics()
```

Specified by:
`characteristics` in interface `java.util.stream.Collector<[T](ResultSelector.html "type parameter in ResultSelector"),​java.util.List<[T](ResultSelector.html "type parameter in ResultSelector")>,​java.util.Optional<[T](ResultSelector.html "type parameter in ResultSelector")>>`