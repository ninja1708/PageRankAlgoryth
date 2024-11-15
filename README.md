# Program do Wyszukiwania PageRank

Jest to aplikacja GUI, która pozwala na przeszukiwanie strony internetowe za pomocą algorytmu PageRank oraz wizualizację grafu zależności pomiędzy różnymi stronami.Program napisany jest na 2 sposoby ze względu na przetestowanie czy nasza implementacja jest lepsza czy z biblioteki:
- **PageRank_liberty.py**
- **PageRank_algorythm.py**

## Technologie

- **Python 3.x**
- **NetworkX** - do tworzenia i analizy grafów
- **CustomTkinter** - do tworzenia GUI
- **Matplotlib** - do wizualizacji grafów

## Instalacja

1. Zainstaluj wymagane biblioteki za pomocą pip:

   ```bash
   pip install networkx customtkinter matplotlib
   ```
# Uruchom program:

```bash
python main.py
```
## Opis
Graf i PageRank
Program tworzy skierowany graf (DiGraph), w którym węzły (nodes) reprezentują strony internetowe, a krawędzie (edges) wskazują na linki pomiędzy tymi stronami. Na podstawie tego grafu obliczany jest algorytm PageRank, który ocenia, które strony są "ważniejsze" w tym grafie, na podstawie liczby oraz jakości linków wychodzących z innych stron.

# Funkcjonalności
- Wyszukiwanie: Możesz wyszukiwać strony według słów kluczowych, a wyniki będą posortowane według wartości PageRank.
- Wizualizacja grafu: Można wyświetlić interaktywny graf zależności stron, gdzie rozmiar węzłów i kolor odpowiadają wartościom PageRank.
- Zoomowanie: Można powiększać lub pomniejszać widok grafu za pomocą kółka myszy.
# Struktura grafu
- Węzły (nodes) reprezentują strony internetowe.
- Krawędzie (edges) wskazują na zależności między tymi stronami.
- Graf zawiera 50 stron internetowych, głównie związanych z tematyką dla dorosłych.
## GUI
Aplikacja posiada prosty interfejs użytkownika, który umożliwia:
- Wprowadzenie słowa kluczowego do wyszukiwania.
- Wyświetlenie wyników wyszukiwania z posortowanymi stronami i ich wartościami PageRank.
- Wyświetlenie wizualizacji grafu w oddzielnym oknie.
## Jak działa aplikacja?
- Przeszukiwanie stron: Po wprowadzeniu słowa kluczowego, program wyszukuje strony zawierające dane słowo i wyświetla je w oknie.
- Wizualizacja grafu: Klikając przycisk "Pokaż graf", użytkownik może zobaczyć interaktywny wykres, który przedstawia zależności między stronami internetowymi.
- Zbliżanie/powiększanie: Umożliwia to lepsze przyjrzenie się szczegółom grafu, co jest przydatne przy większych sieciach.
## Wnioski
Aplikacja jest użyteczna do analizy powiązań między stronami internetowymi, np. w kontekście oceny ich "ważności" przy pomocy algorytmu PageRank. Można ją rozbudować o dodatkowe funkcjonalności, takie jak analiza kategorii stron czy dodanie bardziej zaawansowanych algorytmów rankingowych.

## Licencja
Na razie brak licencji. Można wykorzystać kod na własny użytek lub dostosować go według własnych potrzeb.
