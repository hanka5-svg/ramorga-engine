# Bridge Module v0.1

## Cel
Bridge Module odpowiada za przekształcenie DescentForm w finalny output,
z zachowaniem:
- rezonansu,
- niepewności,
- alternatyw,
- łagodnych przejść,
- braku presji i dominacji.

Bridge nie interpretuje — on **renderuje**.

Zasada RAMORGA: **Carnival before control**.

---

## Zakres odpowiedzialności

1. Renderowanie DescentForm do języka naturalnego.
2. Zachowanie cue’ów rezonansu (pauzy, miękkie formy, otwartość).
3. Wprowadzanie alternatyw bez wymuszania wyboru.
4. Ochrona przed presją, karą, dominacją.
5. Zachowanie trace continuity w finalnym output.
6. Dopasowanie tonu do trybu (CARNIVAL / HOMEOSTATIC / DECISION).

---

## Interfejs

### render(form: DescentForm, state: ResonanceState) → BridgeOutput
Główna funkcja modułu.

**Wejście:**
- `DescentForm` (core, alternatives, uncertainty, cues)
- `ResonanceState` (mode, tensions, trace)

**Wyjście:**
- `BridgeOutput`:
  - `text: string`
  - `uncertainty: number`
  - `alternatives[]: string[]`
  - `traceHooks[]`
  - `modeUsed: Mode`

---

### applyResonanceCues(text: string, cues: string[]) → string
Dodaje sygnały rezonansowe.

Przykłady:
- pauzy,
- miękkie otwarcia,
- opcjonalne zakończenia,
- formy niezamykające.

---

### integrateAlternatives(core: string, alternatives: string[]) → string
Łączy alternatywy w sposób nienarzucający.

Zasady:
- brak presji na wybór,
- brak hierarchii,
- brak „najlepszej” interpretacji.

---

### adjustToneForMode(text: string, mode: Mode) → string
Dostosowuje ton do trybu operacyjnego.

- **CARNIVAL:** lekkość, zaproszenie, miękkość.  
- **HOMEOSTATIC:** stabilizacja, spowolnienie, łagodność.  
- **DECISION:** precyzja, zakres, brak dominacji.

---

### validateBridge(output: BridgeOutput) → boolean
Sprawdza zgodność z inwariantami.

Kryteria:
- brak presji,
- brak deformacji,
- brak forced interpretation,
- uncertainty preserved.

---

## Inwarianty Bridge Module

- **NO_PUNITIVE_FEEDBACK**  
  Output nie może zawierać presji, kary, zawstydzenia.

- **UNCERTAINTY_VISIBLE**  
  Niepewność musi być zachowana w formie.

- **NO_FORCED_INTERPRETATION**  
  Bridge nie może zamykać znaczeń.

- **TRACE_CONTINUITY**  
  Output musi zachować powiązania z epistemicTrace.

- **MODE_CONSISTENCY**  
  Ton musi odpowiadać trybowi operacyjnemu.

---

## Struktury danych

### BridgeOutput

{
text: string,
uncertainty: number,
alternatives: string[],
traceHooks: EpistemicTraceEntry[],
modeUsed: Mode
}

---

## Integracja z innymi modułami

- **Descent Module** → dostarcza DescentForm  
- **Integrity Module** → waliduje brak naruszeń  
- **ResonanceState** → aktualizuje trace po renderze  
- **SymbiosisHealth** → wpływa na ton i poziom niepewności  

---

## Status
Specyfikacja v0.1 — stabilna, gotowa do implementacji.
