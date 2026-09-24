CC = gcc
CFLAGS = -std=c17 -Wall -Wextra -Wpedantic -Iinclude

# Para compilar em modo DEBUG:
#   make DEBUG=1
ifdef DEBUG
CFLAGS += -DDEBUG
endif

BUILD = build
LIB   = lib

.PHONY: all clean run

all: escola

# --- Etapa 1: compila aluno.c em objeto -----------------------------------
$(BUILD)/aluno.o: src/aluno.c include/aluno.h | $(BUILD)
	$(CC) $(CFLAGS) -c src/aluno.c -o $(BUILD)/aluno.o

# --- Etapa 2: empacota o objeto na biblioteca estática ---------------------
$(LIB)/libaluno.a: $(BUILD)/aluno.o | $(LIB)
	ar rcs $(LIB)/libaluno.a $(BUILD)/aluno.o

# --- Etapa 3: compila o cliente e liga com a biblioteca ---------------------
escola: src/main.c $(LIB)/libaluno.a
	$(CC) $(CFLAGS) src/main.c -L$(LIB) -laluno -o escola

$(BUILD):
	mkdir -p $(BUILD)

$(LIB):
	mkdir -p $(LIB)

run: escola
	./escola

clean:
	rm -rf $(BUILD) $(LIB) escola
