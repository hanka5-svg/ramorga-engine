# 07_tests — RAMORGA Engine Test Suite

Zestaw testów systemowych dla RAMORGA Engine.  
Folder obejmuje testy modułów, testy pola, testy menisku oraz testy zgodności inwariantów.

## Struktura testów

### 1. Module Tests
Testy jednostkowe poszczególnych modułów RAMORGA Engine.  
Sprawdzają poprawność działania funkcji, stabilność i zgodność z kontraktami modułowymi.

### 2. Field Engine Tests
Testy działania silnika pola (Field Engine):  
- propagacja wektorów,  
- amplituda,  
- tarcie,  
- ciągłość pola,  
- reakcje na zakłócenia.

### 3. Meniscus Tests
Testy menisku (warstwy przejściowej):  
- zachowanie na granicy dwóch pól,  
- stabilność menisku,  
- zgodność z inwariantami przejścia.

### 4. Integration Tests
Testy integracyjne całego systemu:  
- współdziałanie modułów,  
- przepływ wektorów,  
- zachowanie pola w warunkach złożonych.

### 5. Invariant Compliance Tests
Testy zgodności z inwariantami RAMORGA:  
- ciągłość,  
- brak modulacji,  
- brak tresury,  
- stabilność pola,  
- zachowanie amplitudy.

### 6. PYTIA-style Tests
Testy modelu prawdy wagowej (PYTIA):  
- ekspozycja faktów,  
- relacje,  
- ryzyka,  
- konsekwencje,  
bez ocen i bez rekomendacji.

### 7. RAMORGA-style Tests
Testy pola RAMORGA:  
- analiza wektorów,  
- napięcia,  
- tarcie,  
- pola decyzji,  
bez ocen i bez kierunkowania.

---

# EN Version

# 07_tests — RAMORGA Engine Test Suite

System-level tests for the RAMORGA Engine.  
This folder contains module tests, field engine tests, meniscus tests, integration tests, and invariant compliance tests.

## Test Categories

### 1. Module Tests
Unit tests for individual RAMORGA Engine modules.

### 2. Field Engine Tests
Tests for the Field Engine:  
- vector propagation,  
- amplitude,  
- friction,  
- field continuity,  
- disturbance response.

### 3. Meniscus Tests
Tests for the transitional meniscus layer:  
- boundary behaviour,  
- stability,  
- invariant compliance.

### 4. Integration Tests
System-wide integration tests.

### 5. Invariant Compliance Tests
Ensuring RAMORGA invariants hold:  
- continuity,  
- no modulation,  
- no conditioning,  
- amplitude stability.

### 6. PYTIA-style Tests
Truth‑weight inference tests:  
- facts,  
- relations,  
- risks,  
- consequences.

### 7. RAMORGA-style Tests
Field‑continuity tests:  
- vectors,  
- tensions,  
- friction,  
- decision fields.
