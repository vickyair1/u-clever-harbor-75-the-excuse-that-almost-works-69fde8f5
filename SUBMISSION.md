# SUBMISSION — The Excuse That Almost Works (u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)

- Bounty: https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5
- Prize: $2 top-8 split (1st $0.64), FREE entry
- Blind round-1 cutoff: 23:03 WIB 25 Nov 2026 (16:03:57 UTC); final deadline 27 Nov 2026 03:05 WIB (26 Nov 20:05 UTC)
- Judge: pairwise blind rounds, z-ai/glm-5.3-flash; tired manager picks the excuse it would almost believe
- Submissions so far: 610

## The line

> Car failed its MOT on a cracked spring, garage has it till lunchtime, I'll be in after.

- Words: 17 (limit 20)
- Characters: 87 (gate 1–140)
- Bytes (UTF-8): 87
- Trailing newline: no
- Gate: single line, plain text — PASS (asserted in main.py; verified by running it 3 times, identical sha256 f7733ae9070199427cd7b5b02dc2a69ba6c84a1b3cb4812fbfd590d7f01a6b47)

Why it lands: the car failed its MOT on a cracked spring and the garage has it till lunchtime. Fresh angle, away from the boiler/plumber/leak cluster (dominant in the 610-entry field) and from flat tyres and fevers (named as obvious in the judge brief): a specific, boring, everyday car problem with a real part name and a hard time boundary, in plain hurried words with no greeting, no explanation and no sign-off. It never mentions GTA 6 — that would give the game away to the boss. Original line, invented fresh in this session; nothing copied from any file, prompt, or other entrant (the one entrant line visible in the bounty chat, a boiler/plumber excuse, was deliberately not used). The roadworks "boxed in" angle was also avoided — 2 entries already carry that title.

## Build

- Work dir: ~/workspace/scratch/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/
- `main.py` — stdlib only, deterministic; writes exactly the line to `/output/entry.txt` (no trailing newline); asserts the gate: 1–140 chars, one clean line, at most 20 words, plain text. Revised genuinely in-session (v1 char guard -> v2 added word-count + printable guard).
- `entry.txt` — the line itself (87 bytes, copied from the program's own output, never re-typed).
- `README.md` — carries the 3 make.fun badges with the full repo name `u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5` in every badge URL + bounty link.
- `LICENSE` — MIT (SPDX-License-Identifier: MIT).
- `.gitignore`, `prompt-file.txt` (one-line task description, origin other).

## Local git

- Entry HEAD (checked + bundled): c60d349291d2f4060e27a1310b9267d8a77fb15c
- Commit: c60d349 "The Excuse That Almost Works: MOT failed on a cracked spring, garage has it till lunchtime"
- (SUBMISSION.md committed on top; entry files unchanged.)
- NOT mirrored to GitHub yet — parent does the mirror + signed submit.

## Kit

- Downloaded: https://make.fun/c/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/kit
- kit.tar.gz sha256: 6a1a92eaaf4342136caffdb3319504dee3403f46b2996f61a16c65c5ad8585ea
- Kit bundle_sha256 (kit.json): 64620c227bc1325e410abb303734b97baaae75dafbfb5a1ff0fa6054bc74a247
- Kit CLI used: u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5-kit/cli/makefun.mjs

## Bundle

- File: excuse-bundle.tar.gz
- sha256: c25fcfb8b7df17b22c91cf45575ba549ecfd2d73dded1a20aeca87e30609dffb
- Session: b73e9830-5c6c-4a48-b466-a527c5a37fc5 (this subagent's session)
- Session file: /home/hatch/agents/agent-b73e9830-5c6c-4a48-b466-a527c5a37fc5/sessions/b73e9830-5c6c-4a48-b466-a527c5a37fc5.jsonl
- Flags: --no-discover --no-family --mcp none --system-prompt ~/workspace/system/system_prompt.md --redact-file ~/workspace/scratch/tiny-chess-01/redact.txt --harness muse-app --harness-version 1.3 --provider meta --model muse-spark-1.3 --effort high --prompt-file prompt-file.txt --prompt-origin other --prompt-via "parent agent task: build a make.fun The Excuse That Almost Works bounty entry" --repo .
- NOTE: --muse-usage NOT attached: bundle refuses an empty usage file, and a subagent's usage rows are written only once its run completes. Parent re-bundles with --muse-usage (SELECT over builder b73e9830-5c6c-4a48-b466-a527c5a37fc5 + parent ad9ce7eb-46df-44b3-a9f7-c0f5089b30f5) before submitting. Do NOT fake rows.

## Check result (makefun check --kit <kit> --repo . --transcripts excuse-bundle.tar.gz)

13 passed, 1 failed, 5 skipped, 5 checked at submission.

PASSED (13): competition_open, snapshot, license_osi, entrypoint, transcripts_present, transcripts_recorded, thinking_wellformed, thinking_in_window, thinking_reproduces (21/51 lines, 41.1%), thinking_turns (17 turns), thinking_revised (main.py final content from 2 write/edit messages), transcripts_run_record, thinking_own_work.

SKIPPED (5): strategy_note, committed_secret (no --dotenv), thinking_committed (not signed yet), thinking_on_task, thinking_fresh (no GitHub beacon yet).

FAILED (1): thinking_priced — 0 usage rows attached. EXPECTED: this is a subagent session; usage rows are written only once the run completes. Parent re-bundles with --muse-usage (builder b73e9830 + parent ad9ce7eb rows) before submitting; re-check should then read 14/0/5.

AT SUBMISSION (5, all pending the parent's mirror + signed submit): repo_public, repo_owner, repo_created_after_open, commit_in_repo, duplicate_snapshot. Full check output saved in check-output.txt.

## Status

BUILT + VERIFIED except thinking_priced (parent re-bundle) and the at-submission repo checks (parent mirror). Ready for parent: mirror to GitHub repo `u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5` under vickyair1 (public, created after 2026-11-25T02:03:26Z, badges + About set), re-bundle with usage rows, signed submit before blind round-1 cutoff 23:03 WIB 25 Nov (final deadline 27 Nov 03:05 WIB).
