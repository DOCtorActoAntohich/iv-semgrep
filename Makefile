.PHONY: default
default:
	@echo Choose target


.PHONY: test
test:
	semgrep --test --quiet --config rules tests