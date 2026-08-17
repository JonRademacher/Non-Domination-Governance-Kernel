# Counterexample: False Frame Attribution

## Claim Being Tested

The kernel must not classify domination when the alleged participant frame has not been structurally established.

## Scenario

An observer attributes a frame to an object or process that does not exhibit sufficient interpretive structure, transformation capacity, or boundary recognition. The object may be affected by authority or constraint, but it is not shown to possess a structural frame in the kernel's sense.

Examples may include:

```text
a passive file in storage
a simple inert object
a static record with no interpretive or transformational capacity
a process whose state is entirely externally overwritten without internal structure
```

## Kernel Assessment

The preliminary evaluability condition fails:

```text
HasFrame(P)=0
```

Therefore domination classification should return:

```text
classification = unevaluable
```

not:

```text
D(P,G)=1
```

## Why Domination Is Not Established

The domination predicate requires a frame:

```text
D(P,G) ⇔ Final(G,F_P) ∧ ¬ViableExitFrom(P,G)
```

If `F_P` is not established, the predicate lacks its object. Authority over an object is not automatically authority over a frame.

## Misclassification Risk

The risk is anthropomorphic or structural over-attribution. If the kernel classifies every controlled object as dominated, it becomes useless.

## Lesson

```text
Frame first. Domination second.
```

No domination classification should be made until a structural frame is established.
