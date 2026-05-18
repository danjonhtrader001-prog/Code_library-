# C++ — Fondamentaux

Bases indispensables pour le moteur HFT basse latence.

| Fichier | Sujet |
|---------|--------|
| `01_types_io.cpp` | Types, I/O, `constexpr` |
| `02_pointers_references.cpp` | Pointeurs, références, `const` |
| `03_stl_containers.cpp` | `vector`, `map`, `unordered_map` |
| `04_classes_raii.cpp` | Classes, RAII, règle des cinq |
| `05_templates.cpp` | Templates, génériques |
| `06_smart_pointers.cpp` | `unique_ptr`, `shared_ptr` |

## Compilation

```bash
cd fundamentals
mkdir -p build && cd build
cmake .. && cmake --build .
./01_types_io
```

Nécessite **C++17** et **CMake 3.14+**.
