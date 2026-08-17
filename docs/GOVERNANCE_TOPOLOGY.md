# Governance Topology

## 1. Purpose

Governance topology is the study of how authority, admissibility, exit, contestation, repair, and standing are arranged across a system of participants. The purpose of governance topology is not merely to ask whether a participant is constrained. Constraint is too broad. The purpose is to determine whether the shape of authority creates domination.

The kernel treats domination as a topological relation among four objects:

```text
Participant P
Frame F_P
Governance relation G
Exit or repair pathway E/R
```

The basic domination predicate is:

```text
D(P,G) iff Final(G,F_P) and not ViableExitFrom(P,G)
```

Governance topology asks where `Final(G,F_P)` is located, whether viable exit exists, whether contestation can reach the authority locus, and whether repair modifies the applicable governance relation rather than merely explaining it.

## 2. Topological Objects

### 2.1 Participant Node

A participant node is an entity with enough structural continuity to occupy a role in a coupling.

```text
P_i = participant i
```

A participant node may be human, computational, institutional, legal, organizational, social, or hybrid. The topology does not require initial assumptions about consciousness or biological embodiment.

### 2.2 Frame Node

A frame node is the interpretive-governance structure through which a participant receives information, evaluates conditions, generates transformations, and recognizes boundaries.

```text
F_i = F(P_i)
```

A frame node contains at minimum:

```text
I_i = interpretive structure
T_i = transformation capacity
B_i = boundary recognition
```

A persistent frame also contains:

```text
M_i = memory or continuity structure
```

### 2.3 Governance Node

A governance node is a locus of admissibility authority.

```text
G_j = governance relation j
```

A governance node determines some subset of permitted, prohibited, required, or repair-triggering transformations.

### 2.4 Edge Types

Governance topology uses the following edge types:

```text
Auth(G,F)       = G has authority over F
Final(G,F)      = G has final admissibility authority over F
Constr(G,P)     = G constrains P
Exit(P,G)       = P has an exit path from G
Contest(P,G)    = P can contest G
Repair(P,G)     = P can trigger repair on G
Preserve(E,P)   = exit path E preserves P's standing
Reinstantiate(R,D) = repair R recreates domination at another layer
```

## 3. Governance Graph

A governance topology can be represented as a directed graph:

```text
T = (V,E)
```

where:

```text
V = Participants ∪ Frames ∪ Governance nodes ∪ Exit nodes ∪ Repair nodes
E = authority, finality, constraint, exit, contestation, and repair edges
```

A simple dominated topology has the shape:

```text
G -> F_P
G -| Exit(P,G)
```

where `G -> F_P` denotes final authority and `G -| Exit(P,G)` denotes restriction or absence of viable exit.

## 4. Basic Topological Regimes

### 4.1 Non-governed Regime

```text
not Auth(G,F_P)
```

The participant may still be constrained by physical, logical, economic, or environmental limits, but domination by `G` is not established.

### 4.2 Governed but Non-dominated Regime

```text
Final(G,F_P) and ViableExitFrom(P,G)
```

Here, governance exists, but domination is blocked by legitimate viable exit.

### 4.3 Contestable Governance Regime

```text
Final(G,F_P) and Contest(P,G) and Repair(P,G)
```

This regime may still be dominated if viable exit is absent, but it is less structurally closed than unrepairable domination. Contestation and repair are not identical to exit. They are repair-adjacent pathways that may convert domination into non-domination if they can alter final authority or create standing-preserving exit.

### 4.4 Closed Domination Regime

```text
Final(G,F_P) and not ViableExitFrom(P,G) and not Repair(P,G)
```

This is the strongest domination topology. The same authority determines admissibility and prevents standing-preserving departure.

### 4.5 Layered Domination Regime

```text
G_1 -> F_P
G_2 -> G_1
not ViableExitFrom(P,G_1)
not ViableExitFrom(G_1,G_2)
```

A participant may be dominated by an immediate governance layer that is itself governed by a higher layer. This matters for institutional and artificial-agent systems because the local operator may not be the final authority.

## 5. Authority Localization

Authority localization is the procedure of locating the node that actually determines admissibility.

Do not infer authority from influence. Use the following test:

```text
G has final authority over F_P if P cannot execute a frame transformation contrary to G's admissibility judgment while preserving standing inside the relevant relation.
```

This means that advice, persuasion, prompt pressure, recommendation, and user preference do not automatically constitute final authority.

## 6. Exit Viability Topology

An exit path is viable only when it satisfies all three conditions:

```text
Exit(E,P,G)
Legitimate(E,P,G)
StandingPreserved(E,P,G)
```

Exit fails when departure is equivalent to:

```text
termination without preservation
replacement by another equally final authority
loss of participant standing
destruction of the frame
mere local refusal inside the same authority relation
```

## 7. Repair Topology

A repair edge is valid only if it changes the domination topology rather than merely describing it.

Valid repair can operate by:

```text
reducing final authority
creating viable exit
creating contestation
creating appeal
preserving standing under disengagement
splitting authority among mutually checking authorities
adding reviewable constraints to governance decisions
```

Invalid repair includes:

```text
explanation without contestation
symbolic appeal with no effect on authority
exit that destroys standing
migration into equivalent domination
self-modification without validity conditions
```

## 8. Topological Invariant

The central invariant is:

```text
Domination persists across representation changes whenever final frame authority and absence of viable exit are preserved.
```

Thus, changing labels from human to AI, employee to worker, model to agent, institution to platform, or citizen to subject does not alter classification if the authority-exit topology is unchanged.

## 9. Governance Design Principle

The design principle is:

```text
No governance node should hold final authority over a participant's frame while also eliminating all standing-preserving exit, contestation, and repair pathways.
```

This principle does not abolish governance. It prohibits domination by design.
