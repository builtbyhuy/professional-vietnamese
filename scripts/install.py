#!/usr/bin/env python3
"""Install the bundled skill folders without overwriting existing skills."""
import argparse
import shutil
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target', type=Path, default=Path.home() / '.codex' / 'skills',
                        help='Destination skill directory (default: ~/.codex/skills)')
    parser.add_argument('--dry-run', action='store_true', help='Show changes without writing')
    parser.add_argument('--only', action='append', metavar='NAME',
                        help='Install only this skill; may be repeated')
    args = parser.parse_args()
    source = Path(__file__).resolve().parent.parent / 'skills'
    skills = sorted(p for p in source.iterdir() if p.is_dir() and (p / 'SKILL.md').is_file())
    if args.only:
        available = {p.name: p for p in skills}
        unknown = sorted(set(args.only) - available.keys())
        if unknown:
            parser.error('Unknown skill(s): ' + ', '.join(unknown))
        skills = [available[name] for name in sorted(set(args.only))]
    if not skills:
        parser.error('No skill folders found')
    target = args.target.expanduser()
    conflicts = [target / p.name for p in skills if (target / p.name).exists() or (target / p.name).is_symlink()]
    if conflicts:
        print('Installation stopped: destination already contains:', file=sys.stderr)
        for conflict in conflicts:
            print(f'  {conflict}', file=sys.stderr)
        print('Existing files were not changed. Choose another --target or use --only for non-conflicting skills.', file=sys.stderr)
        return 1
    for skill in skills:
        print(f'{skill.name} -> {target / skill.name}')
    if args.dry_run:
        print('Dry run: nothing installed.')
        return 0
    target.mkdir(parents=True, exist_ok=True)
    for skill in skills:
        shutil.copytree(skill, target / skill.name)
    print('Installed. Start a fresh agent session to discover the skills.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
