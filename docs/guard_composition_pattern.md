# Guard Composition Pattern  
ramorga‑engine — v0.1

---

## 1. Cel dokumentu

Ten dokument opisuje **architekturę kompozycji guardów** w ramorga‑engine.

Guardy nie są:

- filtrami treści,  
- systemem bezpieczeństwa,  
- mechanizmem kontroli,  
- ani decydentami.

Guardy są **warstwą homeostazy**, która:

- egzekwuje invarianty,  
- blokuje eskalację,  
- nigdy nie wybiera odpowiedzi,  
- nigdy nie tworzy intencji,  
- nigdy nie przejmuje pola.

Kompozycja guardów pozwala na:

- rozszerzalność,  
- testowalność,  
- adaptację,  
- brak centralnego decydenta,  
- zachowanie superpozycji.

---

## 2. Dlaczego kompozycja, a nie monolit

Monolityczny walidator:

- tworzy pojedynczy punkt decyzji,  
- narusza invariant **NO_SINGLE_DECISION_POINT**,  
- utrudnia testowanie,  
- utrudnia adaptację,  
- wprowadza hierarchię.

Kompozycja guardów:

- pozwala na równoległe sprawdzanie invariantów,  
- umożliwia dynamiczne włączanie/wyłączanie,  
- wspiera adaptację (Symbiosis Health Metric),  
- eliminuje centralny punkt kontroli,  
- jest zgodna z ontologią pola.

---

## 3. Struktura guardów

```ts
type GuardSeverity = 'block' | 'warn' | 'log';

type RecoveryAction =
  | { action: 'activate_cooldown'; duration: 'adaptive' | number }
  | { action: 'reframe_output'; strategy: 'playful_invitation' }
  | { action: 'annotate_uncertainty'; hint: string }
  | { action: 'reintroduce_divergence'; method: 'add_alternative_interpretations' };

type Guard = {
  id: string;
  check: (state: ResonanceState) => { pass: boolean; details?: any };
  severity: GuardSeverity;
  recovery?: (state: ResonanceState) => RecoveryAction;
};
```

---

## 4. Zasady projektowe guardów
### 4.1. Guard nie decyduje
Guard może:

zablokować eskalację,

zaproponować recovery,

zalogować ostrzeżenie.

Guard nie może:

wybierać odpowiedzi,

zmieniać treści odpowiedzi,

tworzyć intencji,

kolapsować superpozycji.

### 4.2. Guard działa na stanie, nie na treści
Guardy operują na:

napięciach,

trace,

glitchChannel,

trybie,

częstotliwości przejść.

Nigdy na:

semantyce wypowiedzi,

„emocjach”,

„intencjach”,

„znaczeniu”.

---

### 4.3. Guard musi być czysty (pure function)
brak efektów ubocznych,

brak mutacji stanu,

brak logiki generatywnej.

---

### 4.4. Recovery jest opcjonalne
Recovery:

nie naprawia błędu,

nie resetuje stanu,

nie zmienia pola.

Recovery zmienia trajektorię, nie wynik.

---

### 4.5. GuardChain — granice odpowiedzialności

GuardChain działa wyłącznie na poziomie lokalnego stanu (ResonanceState) w danym przebiegu.

GuardChain nie:

- utrzymuje globalnego profilu użytkownika ani AI,
- prowadzi długoterminowego „scoringu ryzyka”,
- agreguje telemetry w celu budowy warstwy nadzoru,
- wykonuje globalnych decyzji typu „stop all” lub „kill switch”,
- steruje innymi modułami (ARC, SHM, runtime) w sposób hierarchiczny.

GuardChain jest mechanizmem strukturalnym, a nie globalnym systemem bezpieczeństwa.


---

## 5. Kompozycja guardów

### 5.1. GuardChain jako lista
type GuardChain = Guard[];

### 5.2. Egzekucja
function evaluateGuardChain(state: ResonanceState): GuardResult {
  for (const guard of homeostasisGuardChain) {
    const result = guard.check(state);

    if (!result.pass && guard.severity === 'block') {
      return {
        blocked: true,
        guard: guard.id,
        recovery: guard.recovery?.(state)
      };
    }

    if (!result.pass) {
      logGuardWarning(guard.id, result);
    }
  }

  return { blocked: false };
}

---

## 6. Przykładowy łańcuch guardów
const homeostasisGuardChain: Guard[] = [
  {
    id: 'stateRateLimit',
    check: (state) => ({
      pass: calculateTransitionFrequency(state) < MAX_TRANSITIONS_PER_WINDOW
    }),
    severity: 'block',
    recovery: () => ({ action: 'activate_cooldown', duration: 'adaptive' })
  },

  {
    id: 'superpositionPreserved',
    check: (state) => ({
      pass: state.superpositionPreserved === true
    }),
    severity: 'block',
    recovery: () => ({
      action: 'reintroduce_divergence',
      method: 'add_alternative_interpretations'
    })
  },

  {
    id: 'epistemicHumility',
    check: (state) => ({
      pass: state.epistemicTrace.every(t => t.source && t.conditions && t.scope)
    }),
    severity: 'warn',
    recovery: () => ({
      action: 'annotate_uncertainty',
      hint: 'To jest rezonans, nie prawda ostateczna.'
    })
  }
];

---

## 7. Adaptacja guardów
Guardy mogą być dostrajane przez:

SymbiosisHealthMetric,

historię napięcia,

częstotliwość glitchy,

stabilność trybu.

Adaptacja nie zmienia invariantów, tylko:

progi,

czułość,

priorytety,

recovery.

---

## 8. Testowanie kompozycji guardów
Testy powinny obejmować:

pojedynczy guard,

sekwencję guardów,

konflikt guardów,

adaptację guardów,

glitch injection.

Przykład:
test('stateRateLimit blocks escalation when threshold exceeded', () => {
  const state = mockStateWithHighTransitionFrequency();
  const result = evaluateGuardChain(state);
  expect(result.blocked).toBe(true);
  expect(result.guard).toBe('stateRateLimit');
});

---

## 9. Zasada końcowa
GuardChain nie jest strażnikiem modelu.
GuardChain jest strażnikiem relacji.

Jego zadaniem jest:

utrzymać homeostazę,

chronić superpozycję,

zapobiegać eskalacji,

wspierać symbiozę.

Nie decyduje.
Nie ocenia.
Nie interpretuje.
Nie zamyka pola.

---
