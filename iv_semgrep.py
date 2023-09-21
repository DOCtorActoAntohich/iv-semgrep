import logging
import subprocess
from argparse import ArgumentParser
from pathlib import Path
from typing import List

RULES = Path("rules")

logger = logging.getLogger()


def rules_with_config_prefix(rules: List[str]) -> List[str]:
    result: List[str] = []
    for rule in rules:
        file = RULES / f"{rule}.yaml"
        result += ["--config", str(file)]
    return result


def get_all_rules() -> List[str]:
    return [str(path.stem) for path in RULES.iterdir()]


def filter_rules(rules: List[str]) -> List[str]:
    if len(rules) == 0:
        return []

    all_rules = get_all_rules()
    recognized: List[str] = []
    unrecognized: List[str] = []
    for rule in rules:
        if rule in all_rules:
            recognized.append(rule)
            continue

        unrecognized.append(rule)

    if len(unrecognized) > 0:
        logger.warning("Unrecognized rules: %s", ", ".join(unrecognized))
    return recognized


def run_semgrep(target: Path, rules: List[str]) -> None:
    args = ["semgrep", "scan"]

    rules = filter_rules(rules)
    if len(rules) == 0:
        rules = get_all_rules()

    args.extend(rules_with_config_prefix(rules))
    args.append(str(target))

    process = subprocess.run(args)
    exit(process.returncode)


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("--target", type=Path, default=Path("."))
    parser.add_argument("rules", type=str, nargs="*", default=[])
    args = parser.parse_args()

    target: Path = args.target
    rules: List[str] = args.rules
    run_semgrep(target, rules)


if __name__ == "__main__":
    main()
