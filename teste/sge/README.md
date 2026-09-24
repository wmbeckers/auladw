# SGE — Biblioteca de Alunos (aluno.h / aluno.c)

## Estrutura

```
include/aluno.h   -> interface pública do módulo (contrato)
src/aluno.c       -> implementação (calcularMedia, calcularSituacao, imprimirAluno)
src/main.c        -> programa cliente, usa apenas aluno.h
Makefile          -> automatiza compilação, empacotamento e linkedição
```

## Como compilar e rodar

```bash
make          # compila em modo normal e gera o executável "escola"
./escola

make DEBUG=1  # recompila com -DDEBUG (ativa mensagens de depuração)
./escola

make run      # compila (se preciso) e já executa
make clean    # remove build/, lib/ e o executável
```

Ao rodar `make`, as pastas `build/` (arquivos-objeto `.o`) e `lib/`
(biblioteca estática `libaluno.a`) são criadas automaticamente — por isso
não fazem parte deste zip.
itório/zip.
