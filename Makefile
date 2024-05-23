JSON_FILES := $(wildcard schemas/*.json)

LANGUAGES := go python rust typescript

# Targets for each language
.PHONY: all go python rust prepare_dirs clean

all: prepare_dirs go python rust typescript

# Prepare output directories
prepare_dirs:
	@$(foreach dir,$(LANGUAGES),mkdir -p $(dir);)

# Define rules for Go
go: $(patsubst schemas/%.json,go/%.go,$(JSON_FILES))

go/%.go: schemas/%.json
	@echo "Generating Go definition for $< into $@"
	@quicktype -s schema $< -o $@ --lang go

# Define rules for Python
python: $(patsubst schemas/%.json,python/%.py,$(JSON_FILES))

python/%.py: schemas/%.json
	@echo "Generating Python definition for $< into $@"
	@quicktype -s schema $< -o $@ --lang python

# Define rules for Rust
rust: $(patsubst schemas/%.json,rust/%.rs,$(JSON_FILES))

rust/%.rs: schemas/%.json
	@echo "Generating Rust definition for $< into $@"
	@quicktype -s schema $< -o $@ --lang rust

# Clean target to remove generated files
clean:
	@echo "Cleaning up..."
	@rm -rf $(LANGUAGES)
