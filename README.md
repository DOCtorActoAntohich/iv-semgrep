# IV Semgrep

A dead simple and silly wrapper around [`semgrep`](https://github.com/returntocorp/semgrep).
Fun stuff.

We wanted to immortalize some of the written development policies,
so we needed to reuse some custom rules, preferably without copying them every time.

Thus, this repository provides a reusable `pre-commit` hook.

## How to setup a hook

Add something like this to your `.pre-commit-config.yaml`

```yaml
  - repo: https://github.com/DOCtorActoAntohich/iv-semgrep
    rev: v0.1.0
    hooks:
      - id: iv_semgrep
        entry: iv_semgrep
        args: ["--target", "."]
```

By default, this tool checks against all of the rules.

If you specify specific rules in `args`, it will only check what's listed.
You can see the list of rules in `rules` folder.

To add them, write their exact filenames, without the extension. For example:

```yaml
args: ["--target", ".", "else-block", "raw-open-call"]
```

## `.semgrepignore`

`.semgrepignore` file works as usual - files and directories listed there will not be examined.
Put this file in the target directory.

Example `.semprepignore`:

```dockerfile
# Common large paths
node_modules/
build/
dist/
vendor/
.env/
.venv/
.tox/
*.min.js
.npm/
.yarn/

# Common test paths
# test/
# tests/
*_test.go
```

## Testing and writing more rules

Go for `make test` to make tests run.

For a test, all you need is a `rules/some-rule.yaml` with the rule definition,
and `tests/some-rule.py` with code to test against.
The code doesn't have to make sense though, as `semgrep` only checks specific patterns.
File stems (names, not formats) have to match exactly.

~~Also yeah, a Python file name format is against the Python style guide,
but we have to accept it because otherwise tests won't run lol.~~

To test a rule, put a `# ruleid: some-rule` right before the block of code you want to detect.
Tests fail if the marked block isn't detected, or if something else is found.
