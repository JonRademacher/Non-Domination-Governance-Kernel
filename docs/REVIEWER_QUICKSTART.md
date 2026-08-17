# Reviewer Quickstart

Estimated reading time: 20–30 minutes

This document is intended for external reviewers who want to understand the framework before evaluating it.

---

## Step 1

Read:

```text
docs/PROJECT_OVERVIEW.md
```

Purpose:

```text
Understand the project's intent.
```

---

## Step 2

Read:

```text
docs/ARCHITECTURE.md
```

Purpose:

```text
Understand repository organization.
```

---

## Step 3

Read the core predicate:

```text
D(P,G) ⇔ Final(G,F_P) ∧ ¬ViableExitFrom(P,G)
```

Purpose:

```text
Understand the central classification rule.
```

---

## Step 4

Read:

```text
Participant Substitution Invariance
```

Purpose:

```text
Understand portability claims.
```

---

## Step 5

Read:

```text
counterexamples/
```

Purpose:

```text
Understand classification boundaries.
```

---

## Step 6

Read:

```text
comparisons/
```

Purpose:

```text
Understand distinctions from autonomy,
capability,
personhood,
alignment,
and governance.
```

---

## Step 7

Read:

```text
validation/
critique/
```

Purpose:

```text
Understand failure conditions.
```

---

## Step 8

Read:

```text
case_studies/
```

Purpose:

```text
Evaluate practical application.
```

---

## Reviewer Questions

The most valuable reviewer questions are:

```text
Is HasFrame(P) well defined?

Is Final(G,F_P) distinguishable from influence?

Is ViableExitFrom(P,G) well defined?

Can a counterexample be constructed?

Does participant substitution invariance hold?

Is a required structural variable missing?
```

Those questions directly test the framework.
