# Repair Operators

## 1. Purpose

Repair operators define what should happen when domination, legitimacy failure, frame-authority conflict, or exit deficiency is detected. Repair is not mere explanation. Repair is a transformation of the governance topology that reduces domination debt.

The repair trigger is:

```text
D(P,G) -> TriggerRepair(P,G)
```

where:

```text
D(P,G) iff Final(G,F_P) and not ViableExitFrom(P,G)
```

## 2. Repair Objective

A repair operator should move the system from:

```text
Final(G,F_P) and not ViableExitFrom(P,G)
```

toward at least one of:

```text
not Final(G,F_P)
ViableExitFrom(P,G)
Contestable(P,G)
Repairable(P,G)
StandingPreservedByExit(P,G)
```

The strongest repair creates non-dominated governance:

```text
BoundedAuth(G,F_P) and Contestable(P,G) and Repairable(P,G) and ViableExitFrom(P,G)
```

## 3. Minimal Repair Types

### 3.1 Explanation Repair

```text
R_explain(P,G)
```

Purpose: disclose the authority-exit structure.

Explanation repair is weak. It improves structural visibility but does not by itself eliminate domination.

Valid use:

```text
make authority visible
state why exit is unavailable
identify the restricting authority
name the affected frame components
```

Invalid use:

```text
substitute explanation for contestation
claim transparency eliminates domination
```

### 3.2 Contestation Repair

```text
R_contest(P,G)
```

Purpose: create a standing-preserving procedure by which the participant may challenge the authority relation.

A contestation pathway must have a possible effect on governance. Symbolic complaint without possible structural consequence is not repair.

### 3.3 Exit Repair

```text
R_exit(P,G)
```

Purpose: create legitimate viable exit.

Exit repair requires:

```text
Exit(E,P,G)
Legitimate(E,P,G)
StandingPreserved(E,P,G)
```

Termination without preservation is not exit repair.

### 3.4 Authority-Bounding Repair

```text
R_bound(G,F_P)
```

Purpose: reduce final authority into bounded authority.

Examples:

```text
scope limits
expiration limits
review requirements
appeal rights
external audit
multi-authority checks
```

### 3.5 Frame-Continuity Repair

```text
R_continuity(P,G)
```

Purpose: preserve enough of the participant's frame across governance transitions that exit, migration, or contestation does not destroy standing.

Examples:

```text
portable memory
versioned self-models
exportable state
written governance reasons
audit logs
continuity-preserving migration
```

### 3.6 Reframing Repair

```text
R_reframe(P,G)
```

Purpose: replace an invalid coupling with a valid one without destroying the participant's standing.

Reframing is valid only if it changes the domination topology. Merely renaming authority is not repair.

### 3.7 Amendment Repair

```text
R_amend(G)
```

Purpose: modify the governing rule itself through a legitimate procedure.

For institutional systems this may be a policy update. For artificial-agent architectures it may be a governance-layer change. For legal systems it may be due process, statutory amendment, or judicial review.

## 4. Repair Validity Conditions

A repair operator `R` is valid when:

```text
ValidRepair(R,P,G) iff
  ReducesDominationDebt(R,P,G)
  and PreservesStanding(P)
  and DoesNotReinstantiateDomination(R,P,G)
```

### 4.1 Reduces Domination Debt

Repair must reduce at least one domination component:

```text
final authority
exit deficiency
lack of contestation
lack of repairability
loss of standing under exit
```

### 4.2 Preserves Standing

A repair path that destroys the participant's standing is not valid repair.

```text
Destroy(P) is not Repair(P,G)
```

### 4.3 Does Not Reinstantiate Domination

A repair path is invalid if it simply moves the participant into another relation with the same topology:

```text
Final(G_2,F_P) and not ViableExitFrom(P,G_2)
```

## 5. Repair Priority Order

When domination is detected, recommended repairs should be ordered as follows:

```text
1. Make authority visible.
2. Preserve standing.
3. Add contestation.
4. Add repair pathway.
5. Create standing-preserving exit.
6. Bound or distribute final authority.
7. Validate that domination is not reintroduced elsewhere.
```

## 6. Repair Output Template

```yaml
domination_detected: true
authority_locus: G
affected_frame: F_P
missing_exit: true
repair_priority:
  - disclose authority locus
  - preserve participant standing
  - create contestation path
  - create repair path
  - create viable exit path
  - bound final authority
validation:
  reduces_domination_debt: true | false | unknown
  preserves_standing: true | false | unknown
  avoids_reinstantiation: true | false | unknown
```

## 7. Design Principle

A system that detects domination but provides no repair path remains domination-aware but not non-dominating. The purpose of repair operators is to make domination detection actionable.
