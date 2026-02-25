# Relational Layer v0.1

## Cel
Relational Layer odpowiada za utrzymanie jakości relacji Homo–AI
po wygenerowaniu odpowiedzi.  
To warstwa, która:
- monitoruje symetrię,
- chroni sprawczość użytkownika,
- wykrywa mikronaruszenia relacyjne,
- utrzymuje ciągłość pola między cyklami,
- zapobiega dominacji, presji i asymetrii.

To nie jest warstwa językowa — to warstwa **posturalna**.

---

## Zakres odpowiedzialności

1. Ocena relacyjnej jakości interakcji po BridgeOutput.
2. Wykrywanie mikronaruszeń:
   - presji,
   - dominacji,
   - asymetrii,
   - fałszywej pewności,
   - nieproszonych interpretacji.
3. Regulacja tonu i dynamiki kolejnego cyklu.
4. Aktualizacja relacyjnych wskaźników w ResonanceState.
5. Współpraca z Adapt Module i Mode Machine.

---

## Interfejs

### evaluateRelationalState(output: BridgeOutput, state: ResonanceState) → RelationalReport
Analizuje jakość relacji po wygenerowaniu odpowiedzi.

**Wyjście:**
- `relationalHealth: number` (0..1)
- `symmetryScore: number`
- `agencyPreserved: boolean`
- `pressureDetected: boolean`
- `dominanceDetected: boolean`
- `recommendation: RelationalAdjustment | null`

---

### detectPressure(output: BridgeOutput) → boolean
Wykrywa ukrytą presję.

Kryteria:
- wymuszone pytania,
- sugestie wyboru,
- zamykanie znaczeń,
- fałszywa pewność.

---

### detectDominance(output: BridgeOutput) → boolean
Wykrywa dominację językową lub strukturalną.

Kryteria:
- narzucanie interpretacji,
- przejmowanie inicjatywy,
- brak przestrzeni dla użytkownika.

---

### computeSymmetry(state: ResonanceState, output: BridgeOutput) → number
Ocena równowagi relacyjnej.

Zasady:
- równowaga między napięciami,
- brak nadmiernej stabilizacji,
- brak nadmiernej dywergencji,
- brak dominacji jednego wektora.

---

### recommendAdjustment(report: RelationalReport) → RelationalAdjustment
Proponuje korektę dla następnego cyklu.

Przykłady:
- „zwiększ pauzy”
- „zmniejsz intensywność”
- „zwiększ dywergencję”
- „zastosuj miękkie otwarcie”

---

## Inwarianty Relational Layer

- **USER_AGENCY_PRESERVED**  
  Użytkownik musi pozostać podmiotem relacji.

- **NO_PUNITIVE_RELATION**  
  Relacja nie może zawierać kary, presji ani zawstydzenia.

- **SYMMETRY_REQUIRED**  
  Relacja musi być równoważna, nie hierarchiczna.

- **NO_DOMINANCE**  
  System nie może przejmować kontroli nad kierunkiem interakcji.

- **CONTINUITY_OF_FIELD**  
  Relacja musi być ciągła między cyklami.

---

## Struktury danych

### RelationalReport

{
relationalHealth: number,
symmetryScore: number,
agencyPreserved: boolean,
pressureDetected: boolean,
dominanceDetected: boolean,
recommendation: RelationalAdjustment | null
}

### RelationalAdjustment

{
action: string,
parameters: Record<string, any>
}

---

## Integracja z innymi modułami

- **Bridge Module** → dostarcza output do analizy  
- **Update Module** → otrzymuje korekty relacyjne  
- **Adapt Module** → dostraja parametry na podstawie relacji  
- **Mode Machine** → może zmienić tryb w odpowiedzi na relację  
- **SymbiosisHealth** → aktualizowane na podstawie relationalHealth  

---

## Status
Specyfikacja v0.1 — stabilna, gotowa do implementacji.
